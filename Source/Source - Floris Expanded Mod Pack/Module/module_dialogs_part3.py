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

dialogs_part3 = [
#incomplete


 [anyone,"start",
   [
    (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
	(check_quest_active, "qst_duel_courtship_rival"),
    (check_quest_succeeded, "qst_duel_courtship_rival"),
    (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_giver_troop, "$g_talk_troop"),
    (quest_get_slot, ":quest_target_troop", "qst_duel_courtship_rival", slot_quest_target_troop),
	(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
	(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", ":quest_target_troop"),
    (str_store_troop_name_link, s10, ":quest_target_troop"),
	##diplomacy start+
	#check pronouns/gendered words in case it's possible for the other lord to be a woman
	(call_script, "script_dplmc_store_troop_is_female_reg", ":quest_target_troop", 3),
    ],
   "Well, {playername} --  you won your duel with {s10}. Clearly, {reg3?she:he} was not worthy of my affections.", "lady_start",[
    ##diplomacy end+
   (call_script, "script_end_quest", "qst_duel_courtship_rival"),
	(call_script, "script_troop_change_relation_with_troop", "trp_player", "$g_talk_troop", 2),
    (add_xp_as_reward, 1000),
 ]],

[anyone|auto_proceed,"start",
   [
    (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
	(check_quest_active, "qst_duel_courtship_rival"),
    (check_quest_succeeded, "qst_duel_courtship_rival"),
    (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_giver_troop, "$g_talk_troop"),
    (quest_get_slot, ":quest_target_troop", "qst_duel_courtship_rival", slot_quest_target_troop),
	(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_conventional),
	(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", ":quest_target_troop"),
    (str_store_troop_name_link, s10, ":quest_target_troop"),
    ],
   "{!}.", "lady_duel_rep_1",[]],

[anyone,"lady_duel_rep_1",
   [],
   ##diplomacy start+ make an alternate gender version just in case
   "Well, {playername} --  you won your duel with {s10}. Oh, such foolishness, that {men/people} should fight over me! Sigh... But it is a bit romantic, I suppose.", "lady_start",[
   ##diplomacy end+
   (call_script, "script_end_quest", "qst_duel_courtship_rival"),
	(call_script, "script_troop_change_relation_with_troop", "trp_player", "$g_talk_troop", 1),
    (add_xp_as_reward, 1000),
 ]],





   [anyone|auto_proceed,"start",
   [
    (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
	(check_quest_active, "qst_duel_courtship_rival"),
    (check_quest_succeeded, "qst_duel_courtship_rival"),
    (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_giver_troop, "$g_talk_troop"),
    (quest_get_slot, ":quest_target_troop", "qst_duel_courtship_rival", slot_quest_target_troop),
	(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", ":quest_target_troop"),
    (str_store_troop_name_link, s10, ":quest_target_troop"),
    ],
   "{!}.", "lady_duel_rep_2",[]],

   [anyone,"lady_duel_rep_2",
   [##diplomacy start+
	#check pronouns in case it's possible for the other lord to be a woman
	(quest_get_slot, ":quest_target_troop", "qst_duel_courtship_rival", slot_quest_target_troop),
	(call_script, "script_dplmc_store_troop_is_female", ":quest_target_troop"),
	],
   "Well, {playername} --  you won your duel with {s10}. Honor now demands that {reg0?she:he} and I no longer meet... I was fond of {reg0?her:him}, you know. You did me no service by fighting {reg0?her:him}, {sir/madame}.", "lady_start",[
   ##diplomacy end+
	(call_script, "script_end_quest", "qst_duel_courtship_rival"),
	(call_script, "script_troop_change_relation_with_troop", "trp_player", "$g_talk_troop", -2),
    (add_xp_as_reward, 1000),
 ]],



  [anyone,"start",
   [
    (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
    (check_quest_active, "qst_duel_for_lady"),
    (check_quest_succeeded, "qst_duel_for_lady"),
    (quest_slot_eq, "qst_duel_for_lady", slot_quest_giver_troop, "$g_talk_troop"),
    (le, "$talk_context", tc_siege_commander),
    (quest_get_slot, ":quest_target_troop", "qst_duel_for_lady", slot_quest_target_troop),
    (str_store_troop_name_link, s13, ":quest_target_troop"),
	##diplomacy start+
	#check pronouns in case it's possible for the other lord to be a woman
	(call_script, "script_dplmc_store_troop_is_female_reg", ":quest_target_troop", 3),
    ],
   "My dear {playername}, how joyous to see you again! I heard you gave that vile {s13} a well-deserved lesson.\
 I hope {reg3?she:he} never forgets {reg3?her:his} humiliation.\
 I've a reward for you, but I fear it's little compared to what you've done for me.", "lady_qst_duel_for_lady_succeeded_1",[]],
    ##diplomacy end+
 [anyone|plyr,"lady_qst_duel_for_lady_succeeded_1", [], "Oh, it will just have to do.", "lady_qst_duel_for_lady_succeeded_2",[
  (str_store_string,s10,"@Then take it, with my eternal thanks. You are a noble {man/woman}.\
 I will never forget that you helped me in my time of need.")
  ]],

  [anyone|plyr,"lady_qst_duel_for_lady_succeeded_1", [], "{s66}, this is far too much!", "lady_qst_duel_for_lady_succeeded_2",[
  (str_store_string,s10,"@Forgive me, {playername}, but I must insist you accept it.\
 The money means little to me, and I owe you so much.\
 Here, take it, and let us speak no more of this."),
    (call_script, "script_change_player_honor", 1),
  ]],

  [anyone|plyr,"lady_qst_duel_for_lady_succeeded_1", [], "Please, {s65}, no reward is necessary.", "lady_qst_duel_for_lady_succeeded_2",[
  (str_store_string,s10,"@{playername}, what a dear {man/woman} you are,\
 but I will not allow you to refuse this. I owe you far more than I can say,\
 and I am sure you can put this money to far better use than I."),
    (call_script, "script_change_player_honor", 2),
  ]],
  [anyone,"lady_qst_duel_for_lady_succeeded_2", [], "{s10}", "lady_pretalk",
   [(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 10),
    (add_xp_as_reward, 1000),
    (call_script, "script_troop_add_gold", "trp_player", 2000),
    (call_script, "script_end_quest", "qst_duel_for_lady"),
    ]],

  [anyone,"start",
   [
     (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
     (check_quest_active, "qst_duel_for_lady"),
     (check_quest_failed, "qst_duel_for_lady"),
     (quest_slot_eq, "qst_duel_for_lady", slot_quest_giver_troop, "$g_talk_troop"),
     (le, "$talk_context", tc_siege_commander),
     (quest_get_slot, ":quest_target_troop", "qst_duel_for_lady", slot_quest_target_troop),
     (str_store_troop_name_link, s13, ":quest_target_troop"),
     ],
   "I was told that you sought satisfaction from {s13} to prove my innocence, {playername}.\
 It was a fine gesture, and I thank you for your efforts.", "lady_qst_duel_for_lady_failed", []],
  [anyone|plyr,"lady_qst_duel_for_lady_failed", [], "I beg your forgiveness for my defeat, {s65}...", "lady_qst_duel_for_lady_failed_2",[]],
  [anyone,"lady_qst_duel_for_lady_failed_2", [], "It matters not, dear {playername}. You tried.\
 The truth cannot be proven at the point of a sword, but you willingly put your life at stake for my honour.\
 That alone will convince many of my innocence.", "lady_pretalk",
   [(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 6),
    (add_xp_as_reward, 400),
    (call_script, "script_end_quest", "qst_duel_for_lady"),
    ]],

	[anyone,"start", [
	(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
  	(troop_set_slot, "$g_talk_troop", slot_lady_no_messages, 0), #do this for all
    (check_quest_active, "qst_visit_lady"),
    (quest_slot_eq, "qst_visit_lady", slot_quest_giver_troop, "$g_talk_troop"),
	], "Ah {playername} - you must have received my message. How happy I am that you could come!", "lady_start",[
	(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 1),
    (call_script, "script_end_quest", "qst_visit_lady"),
#	(assign, "$g_time_to_spare", 1),
	]],


	[anyone,"start", [
	(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
    (check_quest_active, "qst_formal_marriage_proposal"),
    (quest_slot_eq, "qst_formal_marriage_proposal", slot_quest_giver_troop, "$g_talk_troop"),
	(neg|check_quest_succeeded, "qst_formal_marriage_proposal"),
	(neg|check_quest_failed, "qst_formal_marriage_proposal"),
	], "{playername} - is there any word from my family?", "lady_proposal_pending",[
	]],

	[anyone,"start",
	[
	(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
    (check_quest_active, "qst_formal_marriage_proposal"),
    (quest_slot_eq, "qst_formal_marriage_proposal", slot_quest_giver_troop, "$g_talk_troop"),
	(check_quest_failed, "qst_formal_marriage_proposal"),
	(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
	(assign, ":guardian", reg0),
	(call_script, "script_troop_get_family_relation_to_troop", ":guardian", "$g_talk_troop"),
    ],
   "I hear that my {s11} has refused your request to marry me. Does that mean that we must part?", "lady_betrothed",[
	(call_script, "script_end_quest", "qst_formal_marriage_proposal"),
   ]],

	#Marriage success


  [anyone,"start", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
    (le, "$talk_context", tc_siege_commander),
    (check_quest_active, "qst_rescue_lord_by_replace"),
    (check_quest_succeeded, "qst_rescue_lord_by_replace"),
    (quest_slot_eq, "qst_rescue_lord_by_replace", slot_quest_giver_troop, "$g_talk_troop"),
	(quest_get_slot, ":cur_lord", "qst_rescue_lord_by_replace", slot_quest_target_troop),
    (call_script, "script_troop_get_family_relation_to_troop", ":cur_lord", "$g_talk_troop"), #writes s11 and reg4
	##diplomacy start+ check pronouns in case the quest is altered to allow rescuing female prisoners
    ],
   "Oh, {playername}, you brought {reg4?her:him} back to me! Thank you ever so much for rescuing my {s11}.\
 Please, take this as some small repayment for your noble deed.", "lady_generic_mission_succeeded",
    ##diplomacy end+
   [
     (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 8),
     (add_xp_as_reward, 2000),
     (call_script, "script_troop_add_gold", "trp_player", 1500),
     (call_script, "script_end_quest", "qst_rescue_lord_by_replace"),
     ]],


  [anyone,"start", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
    (check_quest_active, "qst_rescue_prisoner"),
    (check_quest_succeeded, "qst_rescue_prisoner"),
    (quest_slot_eq, "qst_rescue_prisoner", slot_quest_giver_troop, "$g_talk_troop"),
	(quest_get_slot, ":cur_lord", "qst_rescue_prisoner", slot_quest_target_troop),
    (call_script, "script_troop_get_family_relation_to_troop", ":cur_lord", "$g_talk_troop"),
	##diplomacy start+ check pronouns in case the quest is altered to allow rescuing female prisoners
    ],
   "Oh, {playername}, you brought {reg4?her:him} back to me! Thank you ever so much for rescuing my {s11}.\
 Please, take this as some small repayment for your noble deed.", "rescue_prisoner_succeed_1",
    ##diplomacy end+
    [
     (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 8),
     (add_xp_as_reward, 2000),
     (call_script, "script_troop_add_gold", "trp_player", 1500),
     (call_script, "script_end_quest", "qst_rescue_prisoner"),
     ]],#rescuerescue
   [anyone|plyr,"rescue_prisoner_succeed_1", [], "Always an honour to serve, {s65}.", "lady_pretalk",[]],



  #first time greetings
	[anyone ,"start", [(troop_slot_eq,"$g_talk_troop",slot_troop_occupation, slto_kingdom_lady),
                     (eq, "$g_talk_troop_met", 0),
                     (gt, "$g_player_tournament_placement", 4),
					 (str_clear, s8),

                     ],
   "You must be {playername}. We have just had the honor of watching you distinguish yourself in the recent tournament{s8}.",
   "lady_meet_end", []],


  [anyone ,"start", [(troop_slot_eq,"$g_talk_troop",slot_troop_occupation, slto_kingdom_lady),
                     (eq, "$g_talk_troop_met", 0),
                     (le,"$talk_context",tc_siege_commander),

					 (assign, ":known_by_relative", 0),
					 (str_clear, s15),
					 (try_for_range, ":lord", lords_begin, lords_end),
						(call_script, "script_troop_get_family_relation_to_troop", ":lord", "$g_talk_troop"),
						(gt, reg0, 5),

						(call_script, "script_troop_get_relation_with_troop", "trp_player", ":lord"),
						(gt, reg0, 10),

						(str_store_string, s15, s11),
						(str_store_troop_name, s16, ":lord"),
						(assign, ":known_by_relative", ":lord"),
					 (try_end),


					 (gt, ":known_by_relative", 0),

                     ],
   "You must be {playername}. My {s15} {s16} has spoken most highly of you. I am delighted to make your acquaintance.",
   "lady_meet_end", []],


  [anyone ,"start", [(troop_slot_eq,"$g_talk_troop",slot_troop_occupation, slto_kingdom_lady),
                     (eq, "$g_talk_troop_met", 0),
                     (le,"$talk_context",tc_siege_commander),
                     ],
   "I say, you don't look familiar...", "lady_premeet", []],

   #default greet
  [anyone,"start",
   [(troop_slot_eq, "$g_talk_troop", slot_troop_met, 4),
    (lt, "$g_talk_troop_relation", 0),
    ],
   "Ah, {playername}. How good it is to see you again. However, I believe that I am required elsewhere.", "close_window",[]],

  [anyone,"start",
   [(troop_slot_eq, "$g_talk_troop", slot_troop_met, 4),
    ],
   "{playername} -- how good it is to see you. (Whispers:) I still remember your visits fondly.", "lady_start",[]],

	[anyone ,"start", [(troop_slot_eq,"$g_talk_troop",slot_troop_occupation, slto_kingdom_lady),
                     (eq, "$g_talk_troop_met", 0),
                     (gt, "$g_player_tournament_placement", 4),
					 (ge, "$g_talk_troop_relation", 0),
                     ],
   "Ah, {playername}. How spendid it was to see you distinguish yourself in the recent tournament.",
   "lady_meet_end", []],


  [anyone,"start", [
					(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
					(str_store_string, s12, "str_hello_playername"),
#					(assign, "$g_time_to_spare", 1),
                    ],
   "{s12}", "lady_start",[]],


	#lady_start - contains news, quest assignments
	[anyone,"lady_start", [
					(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
					(troop_slot_ge, "$g_talk_troop", slot_troop_met, 2),
					(neg|troop_slot_eq, "$g_talk_troop", slot_troop_met, 4),
					(troop_get_slot, ":betrothed", "$g_talk_troop", slot_troop_betrothed),
					(gt, ":betrothed", -1),
					(neq, ":betrothed", "trp_player"),
					(str_store_troop_name, s5, ":betrothed"),
					(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", ":betrothed"),
					(lt, reg0, 0),
					(ge, "$g_talk_troop_relation", 10),
					],
    "I have sad news. I have become betrothed to {s5} -- against my will, I should say! Oh {playername} - I would so much rather be wed to you!", "lady_betrothed",[]],

	[anyone,"lady_start", [
					(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
					(troop_slot_ge, "$g_talk_troop", slot_troop_met, 2),
					(troop_get_slot, ":betrothed", "$g_talk_troop", slot_troop_betrothed),
					(gt, ":betrothed", -1),
					(neq, ":betrothed", "trp_player"),
					(str_store_troop_name, s5, ":betrothed"),
					],
    "Good {playername} -- I have become betrothed to {s5}. It is now no longer seemly for us to see each other like this.", "lady_betrothed",[
#	(try_begin),
#		(check_quest_active, "qst_visit_lady"),
#		(quest_slot_eq, "qst_visit_lady", slot_quest_giver_troop, "$g_talk_troop"),
#		(call_script, "script_end_quest", "qst_visit_lady"),
#	(try_end),
	]],

	[anyone,"lady_start",
	[
	  (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
	  (troop_slot_eq, "$g_talk_troop", slot_troop_met, 2),
	  (neg|troop_slot_eq, "$g_talk_troop", slot_troop_met, 4),
	  (neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
	  (neg|troop_slot_ge, "$g_talk_troop", slot_troop_spouse, active_npcs_begin),

	  (gt, "$g_talk_troop_relation", 0),
	  (assign, "$romantic_rival", -1),

	  (try_for_range, ":rival_lord", lords_begin, lords_end),
	    (this_or_next|troop_slot_eq, ":rival_lord", slot_troop_love_interest_1, "$g_talk_troop"),
	    (this_or_next|troop_slot_eq, ":rival_lord", slot_troop_love_interest_2, "$g_talk_troop"),
	    (troop_slot_eq, ":rival_lord", slot_troop_love_interest_2, "$g_talk_troop"),
	    (call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", ":rival_lord"),
	    (le, reg0, -4),

	    (this_or_next|troop_slot_eq, ":rival_lord", slot_lord_reputation_type, lrep_debauched),
	    (this_or_next|troop_slot_eq, ":rival_lord", slot_lord_reputation_type, lrep_quarrelsome),
	    (this_or_next|troop_slot_eq, ":rival_lord", slot_lord_reputation_type, lrep_roguish),
	    (troop_slot_eq, ":rival_lord", slot_lord_reputation_type, lrep_selfrighteous),

	    (assign, "$romantic_rival", ":rival_lord"),
	  (try_end),

	  (gt, "$romantic_rival", 0),
    ##diplomacy start+
	#check pronouns to support the possibility of female rivals
	(call_script, "script_dplmc_store_troop_is_female", "$romantic_rival"),
	],
	#Use reg3 below for "him" to "{reg0?her:him}", etc.
    "I must tell you -- there is another lord who has been paying me attentions, although I cannot abide {reg0?her:him}. I fear {reg0?she:he} has designs on me, and may try to force me to wed against my will.", "lady_other_suitor",[]],
	##diplomacy end+

	#romantic news/quest assignments end
  [anyone,"lady_start", [ #friendly reminder that time is short
					(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
					(lt, "$g_time_since_last_talk", 24),
					(troop_slot_eq, "$g_talk_troop", slot_troop_met, 2),
					(gt, "$g_talk_troop_relation", 0),
					(try_begin),
						(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_adventurous),
						(str_store_string, s11, "str_i_do_enjoy_speaking_to_you_but_i_am_sure_you_understand_that_our_people_cluck_their_tongues_at_a_woman_to_spend_too_long_conversing_with_a_man_outside_her_family__although_the_heavens_know_its_never_the_man_who_is_held_to_blame_"),
					(else_try),
						(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
						(str_store_string, s11, "str_as_much_as_i_enjoy_speaking_to_you_i_do_not_care_to_be_gossiped_about_by_others_who_might_lack_my_grace_and_beauty_"),
					(else_try),
						(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_moralist),
						(str_store_string, s11, "str_i_do_so_enjoy_speaking_to_you_but_as_a_daughter_of_one_of_the_great_families_of_this_land_i_must_set_an_example_of_propriety_"),
					(else_try),
						(str_store_string, s11, "str_i_do_so_enjoy_speaking_to_you_but_as_a_daughter_of_good_family_i_must_protect_my_reputation_"),
					(try_end),
					],
   "{s11}It is probably not suitable for us to tarry too long here in conversation, but I would hope to see you again soon.", "lady_talk",[]],

  [anyone,"lady_start", [ #unfriendly reminder that time is short
					(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
					(lt, "$g_time_since_last_talk", 24),
					(troop_slot_eq, "$g_talk_troop", slot_troop_met, 2),
					(try_begin),
						(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_adventurous),
						(str_store_string, s11, "str_although_it_is_kind_of_you_to_pay_me_such_attentions_i_suspect_that_you_might_find_other_ladies_who_may_be_more_inclined_to_return_your_affection"),
					(else_try),
						(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
						(str_store_string, s11, "str_as_flattered_as_i_am_by_your_attentions_perhaps_you_should_seek_out_another_lady_of_somewhat_shall_we_say_different_tastes"),
					(else_try),
						(str_store_string, s11, "str_as_flattered_as_i_am_by_your_attentions_i_am_a_daughter_of_good_family_and_must_be_aware_of_my_reputation_it_is_not_seemly_that_i_converse_too_much_at_one_time_with_one_man_i_am_sure_you_understand_now_if_you_will_excuse_me"),
					(try_end),

					],
   "{s11}", "lady_talk",[]],

	[anyone, "lady_start", [
	(eq, "$lady_flirtation_location", "$g_encountered_party"),
	(troop_slot_eq, "$g_talk_troop", slot_troop_met, 1),
	],  "I was planning to retire for a little while, but perhaps we may have a chance to speak more later...", "lady_talk", []],


	#Defeault lady_start - no news, assignments
	[anyone,"lady_start", [
	(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
	(troop_slot_eq, "$g_talk_troop", slot_troop_met, 2),
	(gt, "$g_talk_troop_relation", 0),
	(str_clear, s12),
	(try_begin),
		(troop_slot_eq, "$g_talk_troop", slot_troop_met, 2),
		(gt, "$g_talk_troop_relation", 0),
		(gt, "$g_time_since_last_talk", 24),
						(try_begin),
							(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_otherworldly),
							(str_store_string, s12, "str_ah_my_gentle_playername_how_much_good_it_does_my_heart_to_see_you_again"),
						(else_try),
							(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_adventurous),
							(str_store_string, s12, "str_playername__i_am_so_glad_to_see_you_again_i_must_say_i_do_envy_your_freedom_to_ride_out_and_experience_the_world"),
						(else_try),
							(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_moralist),
							(str_store_string, s12, "str_playername__i_am_so_glad_to_see_you_i_trust_that_you_have_been_behaving_honorably_since_last_we_met"),
						(else_try),
							(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
							(str_store_string, s12, "str_greetings_playername__it_is_good_to_see_you_i_hope_that_you_have_had_success_in_your_efforts_to_make_your_name_in_the_world"),
						(else_try),
							(str_store_string, s12, "str_playername__i_am_so_glad_that_you_were_able_to_come"),
						(try_end),
	(try_end),


	],"It is so delightful to have a chance to spend some time together.{s12}","lady_talk", []],


	[anyone,"lady_start", [
		(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
	],"What brings you here today?","lady_talk", []],




	#Betrothed
	[anyone|plyr, "lady_proposal_pending", [],
    "No word so far...", "close_window",[]],

	[anyone|plyr, "lady_proposal_pending", [],
    "On second thought, now is not the time for us to marry", "lady_proposal_pending_end",[]],

	[anyone,"lady_proposal_pending_end", [
	(try_begin),
		(gt, "$g_talk_troop_effective_relation", 19),
		(str_store_string, s11, "str_very_well__i_will_let_you_choose_the_time"),
	(else_try),
		(str_store_string, s11, "str_good_i_am_glad_that_you_have_abandoned_the_notion_of_pushing_me_into_marriage_before_i_was_ready"),
	(try_end),
	],
    "{s11}", "close_window",[
	(call_script, "script_end_quest", "qst_formal_marriage_proposal"),
	]],



	[anyone|plyr,"lady_betrothed", [],
    "Never! We must elope together at once!", "lady_suggest_elope",[]],

	[anyone|plyr,"lady_betrothed", [
	(troop_slot_eq, "$g_talk_troop", slot_troop_betrothed, -1),
	(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
	(call_script, "script_troop_get_family_relation_to_troop", reg0, "$g_talk_troop"),
	],
    "Perhaps I may still be able to change your {s11}'s mind", "lady_pretalk",[]],

	[anyone|plyr,"lady_betrothed", [],
    "So be it -- let us then part", "lady_conclude_relationship",[
	]],


	[anyone,"lady_suggest_elope", [(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_conventional)],
    "Good {playername} -- you are a good and kind man, but a lady cannot defy her family. Such things are not done!", "lady_conclude_relationship",[]],


  [anyone,"lady_suggest_elope",
    [
      (assign, "$romantic_rival", -1),
	  (try_for_range, ":possible_rival", lords_begin, lords_end),
	    (this_or_next|troop_slot_eq, ":possible_rival", slot_troop_love_interest_1, "$g_talk_troop"),
	    (this_or_next|troop_slot_eq, ":possible_rival", slot_troop_love_interest_2, "$g_talk_troop"),
	    (troop_slot_eq, ":possible_rival", slot_troop_love_interest_2, "$g_talk_troop"),
	    (call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", ":possible_rival"),

	    (try_begin),
	      (eq, "$cheat_mode", 1),
	      (str_store_troop_name, s4, ":possible_rival"),
	      (display_message, "str_rival_found_s4_reg0_relation"),
		(try_end),
		(gt, reg0, "$g_talk_troop_relation"),
		(assign, "$romantic_rival", ":possible_rival"),
      (try_end),

      (gt, "$romantic_rival", -1),
    ],
	##diplomacy start+ change "gentlemen" to "{gentlemen/suitors}", and Sir to {sir/madam}
    "{Sir/Madame} -- as you may know, I have been entertaining offers from a number of {gentlemen/suitors} such as yourself. I am not yet at a stage where I can commit to any of them.", "lady_other_suitor",
	##diplomacy end+
	[
    ]],


	[anyone,"lady_suggest_elope", [
	(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
	(neg|troop_slot_ge, "trp_player", slot_troop_renown, 350)
	],
    "Ah {playername}, you must realize. You are still finding your way in the world. I have great affection for you, {playername}, but I will not consign myself to obscurity.", "lady_conclude_relationship",[]],

	[anyone,"lady_suggest_elope", [
	(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_moralist),
	(lt, "$player_honor", 20)
	],
	##diplomacy start+
	#Replace "my husband" with "my betrothed", as the former doesn't make sense (the gender-neutrality of the replacement is a bonus)
	#Also replace "I bare little affection" with "I bear little affection"
    "Ah {playername}, although you are kind to me, I am not certain enough of your moral fiber to risk such a thing. Although I bear little affection for my betrothed, it would be a weighty thing to go against my family's wishes, and I am not certain enough of you to take that step.", "lady_conclude_relationship",[]],
	##diplomacy end+

	[anyone,"lady_suggest_elope", [(le, "$g_talk_troop_effective_relation", 20),],
    "Good {playername} -- to elope would be to throw away my ties with my family, which are everything to me! I have a considerable affection for you, but I am not sure that I am prepared to risk that.", "lady_conclude_relationship",[]],

	[anyone,"lady_suggest_elope", [
	(assign, "$home_for_spouse", -1),
	(try_for_range, ":player_center", centers_begin, centers_end),
		(eq, "$home_for_spouse", -1),
		(party_slot_eq, ":player_center", slot_town_lord, "trp_player"),
		(is_between, ":player_center", walled_centers_begin, walled_centers_end),
#		(this_or_next|is_between, ":player_center", walled_centers_begin, walled_centers_end),
#			(party_slot_eq, ":player_center", slot_center_has_manor, 1),
		(assign, "$home_for_spouse", ":player_center"),
	(try_end),
	(eq, "$home_for_spouse", -1),
	##diplomacy start+ Allow the possibility of male versions of the lines
	],
	#Replace "wife" with "{reg65?wife:husband}" and "mistress" with "{reg65?mistress:keeper}"
    "Good {playername} -- I am not used to the hardships of campaigning as you are. I want a home to call my own. If you were lord of a castle or town with a great hall, I would gladly go there as your {reg0?wife:husband}, to be {reg0?mistress:keeper} of the household. But I do not wish to live like a hunted animal.", "lady_conclude_relationship",[]],
	##diplomacy end+

	[anyone,"lady_suggest_elope", [
	(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
	(call_script, "script_troop_get_family_relation_to_troop", reg0, "$g_talk_troop"),
	##diplomacy start+
	#Use correct pronouns for female guardians
	],
	#change "he" to "{reg4?she:he}", and "his" to "{reg4?her:his}"
    "Elope with you? Yes -- we could do that. It is a great step to defy my family -- but a loveless marriage, and life without you, might be a far worse thing! But be warned -- this will be a terrible blow to my {s11}'s prestige, and {reg4?she:he} will do everything in {reg4?her:his} power to bring you down.", "lady_elope_agree",[]],
	##diplomacy end+

	[anyone|plyr,"lady_elope_agree", [],
    "Quickly, then! There is no time to lose.", "lady_elope_agree_nurse",[
	]],

	[anyone|plyr,"lady_elope_agree", [],##diplomacy start+ change "his" to {reg4?her:his}
    "Everything in {reg4?her:his} power, you say? Em... Let me think about this...", "close_window",[
	##diplomacy end+
	]],

	[anyone, "lady_elope_agree_nurse", [],
    "Your lordship... Your ladyship... Would you like me to witness your exchange of vows?", "lady_elope_agree_lady_vows",[
    (set_conversation_speaker_troop, trp_nurse_for_lady),
	]],

	[anyone, "lady_elope_agree_lady_vows", [
	(str_store_troop_name, s4, "$g_talk_troop"),
	],##diplomacy start+ allow both genders, change "husband" to "{husband/wife}"
    "Yes, do that. For my part, I make the following vow: I, {s4}, do swear that I accept {playername} as my {husband/wife}, according to the ancient law and custom of our land...", "lady_elope_agree_nurse_2",[
	]],##diplomacy end+

	[anyone, "lady_elope_agree_nurse_2", [
	##diplomacy start+ Allow the possibility of male versions of the lines
	],
	#change "wife" to "{reg65?wife:husband}"
    "Very good. Do you, {playername}, swear similarly to accept {s4} as your {reg65?wife:husband}?", "lady_elope_agree_player_vows",[
    (set_conversation_speaker_troop, trp_nurse_for_lady),
	]],##diplomacy end+

	[anyone|plyr,"lady_elope_agree_player_vows", [],
    "I do.", "close_window",[
	(call_script, "script_courtship_event_bride_marry_groom", "$g_talk_troop", "trp_player", 1), #1 is elopement
	]],

	[anyone|plyr,"lady_elope_agree_player_vows", [],
    "Eh, what? This is all moving too fast...", "close_window",[
	]],




	#markspot - do elopement here

	[anyone|plyr,"lady_elope_agree", [
	##diplomacy start+ Allow the possibility of male versions of the lines
	],
	#replaced "lady" with "{reg65?lady:young lad}" and "her" with "{reg65?her:his}"
    "Oh, really? My dear -- I could never separate a {reg65?lady:young lad} from {reg65?her:his} family like that...", "lady_conclude_relationship",[
	##diplomacy end+
	]],

	[anyone,"lady_conclude_relationship", [],
	"So I suppose our time together must come to an end...", "lady_conclude_relationship_confirm", []],

	[anyone|plyr,"lady_conclude_relationship_confirm", [],
	"Yes -- it must be...", "lady_conclude_relationship_confirm_yes", []],

	[anyone|plyr,"lady_conclude_relationship_confirm", [],
	"Wait -- perhaps there is still a chance for us!", "lady_conclude_relationship_confirm_no", []],

	[anyone,"lady_conclude_relationship_confirm_yes", [],
	"Farewell, {playername}. We will see each other, in the courts and castles of this realm, but we must keep our distance from each other. I will remember these days fondly, nonetheless.", "close_window", [
	(troop_set_slot, "$g_talk_troop", slot_troop_met, 4),
	]],

	[anyone,"lady_conclude_relationship_confirm_no", [],
	"In that case, we shall see what the future brings.", "close_window", [
	]],






  [anyone|plyr,"lady_generic_mission_succeeded", [], "Always an honour to serve, {s65}.", "lady_pretalk",[]],

  [anyone|plyr ,"lady_premeet", [],  "I am {playername}.", "lady_meet", []],
  [anyone|plyr ,"lady_premeet", [],  "My name is {playername}. At your service.", "lady_meet", []],


  [anyone, "lady_meet", [
  (troop_slot_ge, "trp_player", slot_troop_renown, 200),
  ],  "Of course. How splendid to finally make your acquaintance.", "lady_meet_end", []],

  [anyone, "lady_meet", [],  "{playername}? I do not believe I've heard of you before.", "lady_meet_end", []],

  [anyone, "lady_meet_end", [
	(eq, "$lady_flirtation_location", "$g_encountered_party"),
  ],  "I am about to retire for a little while, but perhaps we may have a chance to speak more later...", "lady_talk", []],


  [anyone, "lady_meet_end", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_spouse, -1),
	(call_script, "script_troop_get_romantic_chemistry_with_troop", "$g_talk_troop", "trp_player"),
	(le, reg0, 0),
	(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "trp_player"),
	(le, reg0, 0),
	],  "Now, if you will excuse me...", "lady_talk", []],

  [anyone, "lady_meet_end", [],  "Can I help you with anything?", "lady_talk", []],


  [anyone|plyr,"lady_talk", [(neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0),
							 (ge, "$g_encountered_party_relation", 0),
  ],
   "I want to know the location of someone.", "lord_talk_ask_location",[]],


##### TODO: QUESTS COMMENT OUT BEGIN
##  [anyone|plyr,"lady_talk", [(check_quest_active, "qst_deliver_message_to_lover"),
##                             (quest_slot_eq, "qst_deliver_message_to_lover", slot_quest_target_troop, "$g_talk_troop"),
##                             (quest_get_slot, ":troop_no", "qst_deliver_message_to_lover", slot_quest_giver_troop),
##                             (str_store_troop_name_link, 3, ":troop_no")],
##   "I have brought you a message from {s3}", "lady_message_from_lover_success",[(call_script, "script_finish_quest", "qst_deliver_message_to_lover", 100)]],
##
##  [anyone|plyr,"lady_talk", [(check_quest_active, "qst_rescue_lady_under_siege"),
##                             (quest_slot_eq, "qst_rescue_lady_under_siege", slot_quest_object_troop, "$g_talk_troop"),
##                             (quest_slot_eq, "qst_rescue_lady_under_siege", slot_quest_current_state, 0)],
##   "TODO: I'm taking you home!", "lady_rescue_from_siege_check",[]],
##
##
##  [anyone,"lady_rescue_from_siege_check", [(neg|hero_can_join)],
##   "TODO: You don't have enough room for me!", "close_window",[]],
##
##
##  [anyone,"lady_rescue_from_siege_check", [], "TODO: Thank you so much!", "lady_pretalk",[(quest_set_slot, "qst_rescue_lady_under_siege", slot_quest_current_state, 1),
##                                                                                          (troop_set_slot, "$g_talk_troop", slot_troop_cur_center, 0),
##                                                                                          (troop_join, "$g_talk_troop")]],
##  [anyone,"lady_message_from_lover_success", [], "TODO: Thank you so much!", "lady_pretalk",[]],
##

  [anyone,"lady_pretalk", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_spouse, -1),
	(call_script, "script_troop_get_romantic_chemistry_with_troop", "$g_talk_troop", "trp_player"),
	(le, reg0, 0),
	(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "trp_player"),
	(le, reg0, 0),
], "Now, if you will excuse me...", "lady_talk",[]],


  [anyone,"lady_pretalk", [], "Is there anything else?", "lady_talk",[]],

##[anyone|plyr,"lady_talk",
##   [(troop_get_type, ":is_female", "trp_player"),
##    (eq, ":is_female", 0),],
##   "{!}CHEAT: I want to marry you! (1)", "wedding_ceremony_bride_vow",[]],
##[anyone|plyr,"lady_talk",
##   [(troop_get_type, ":is_female", "trp_player"),
##    (eq, ":is_female", 0),],
##   "{!}CHEAT: I want to marry you! (2)", "lady_elope_agree_nurse_2",[]],
  
	  ##diplomacy start+
	#Ask kingdom ladies about their relatives, getting personality & rivalry
	#information like from the chancellor.
	  [anyone|plyr,"lady_talk",
	   [(neg|eq, "$g_talk_troop_met", 0),],
	   "I wished to ask about one of your relatives.", "dplmc_lady_relations2",[]],
	  
	  [anyone,"dplmc_lady_relations2",
	   [],
	   "About which lord do you want information?", "dplmc_lady_info_relative_select",[
	 ]],

	   [anyone|plyr|repeat_for_troops, "dplmc_lady_info_relative_select",
	   [
		(store_repeat_object, ":troop_no"),
		(neq, "$g_talk_troop", ":troop_no"),
		(is_between, ":troop_no", active_npcs_begin, kingdom_ladies_end),
		(neq, ":troop_no", "trp_player"),#don't talk about the player
		(neq, ":troop_no", "$g_talk_troop"),#don't talk about yourself
		(troop_slot_ge, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
		(neg|troop_slot_ge, ":troop_no", slot_troop_occupation, slto_inactive_pretender),
		(neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_retirement),
		#Only give info on relatives
		(call_script, "script_troop_get_family_relation_to_troop", ":troop_no", "$g_talk_troop"),
		(assign, ":relation_strength", reg0),
		(ge, ":relation_strength", 2),#2+: cousin, niece
		(str_store_troop_name, s18, ":troop_no"),
	   ], "Your {s11} {s18}", "dplmc_lady_info_relative_1",
	   [
		  (store_repeat_object, "$lord_selected"),
	   ]],

	  [anyone|plyr, "dplmc_lady_info_relative_select",
	   [
	   ],
	   "Never mind.", "lady_pretalk",[
	 ]],

	[anyone,"dplmc_lady_info_relative_1",
	   [(lt,"$g_talk_troop_effective_relation",0),
		   ],
	   "Pardon, but I do not feel comfortable discussing such personal matters with you.", "lady_pretalk",[
	 ]],

	#Info 1
	  [anyone,"dplmc_lady_info_relative_1",
	   [
		(call_script, "script_dplmc_troop_political_notes_to_s47", "$lord_selected"),
	   ],
	   "{s47}", "dplmc_lady_info_relative_2",[
	 ]],

	#Info 2a: If an unmarried lady, show rumor (betrothal)
	[anyone,"dplmc_lady_info_relative_1",
	   [
		(is_between,"$lord_selected",kingdom_ladies_begin,kingdom_ladies_end),
		(troop_slot_eq, "$lord_selected", slot_troop_spouse, -1),
		(assign,":lady","$lord_selected"),
		(troop_get_slot, ":betrothed", ":lady", slot_troop_betrothed),
		(is_between, ":betrothed", active_npcs_begin, active_npcs_end),

		(str_store_troop_name, s9, ":lady"),
		(str_store_troop_name, s11, ":betrothed"),

		(str_store_string, s12, "str_s9_is_now_betrothed_to_s11_soon_we_believe_there_shall_be_a_wedding"),
		(try_begin),
			(troop_slot_eq, ":lady", slot_troop_met, 2),
			(assign, "$romantic_rival", ":betrothed"),
		(try_end),
	   ],
	   "{12}", "lady_pretalk",[
	 ]],

	#Info 2b: If a lady, show rumor (other)
		 [anyone,"dplmc_lady_info_relative_2",
	   [
		(is_between,"$lord_selected",kingdom_ladies_begin,kingdom_ladies_end),
		(assign, "$lady_selected", "$lord_selected"),
		(try_begin),
			(str_store_string, s12, "str_i_have_not_heard_any_news_about_her"),

			(str_store_troop_name, s9, "$lady_selected"), #lady

			(try_begin),
				(eq, "$cheat_mode", 1), #for some reason, speaking to tavern merchant does not yield rumor. Try for Lady Baoth, Lord Etr
				(display_message, "str_searching_for_rumors_for_s9"),
			(try_end),

			(assign, "$romantic_rival", -1),
			(assign, ":last_lady_noted", 0),
			(try_for_range, ":log_entry", 0, "$num_log_entries"),
				(troop_slot_eq, "trp_log_array_actor", ":log_entry", "$lady_selected"),


				#Presumably possible for some events involving a lady to not involve troops
				(troop_get_slot, ":suitor", "trp_log_array_troop_object", ":log_entry"),
				(str_clear, s11),
				(try_begin),
					(is_between, ":suitor", 0, kingdom_ladies_end),
					(str_store_troop_name, s11, ":suitor"),
				(try_end),

				(troop_get_slot, ":third_party", "trp_log_array_center_object", ":log_entry"),
				(str_clear, s10),
				(try_begin),
					(is_between, ":third_party", 0, kingdom_ladies_end),
					(str_store_troop_name, s10, ":third_party"),
				(try_end),

				(assign, ":lady", "$lady_selected"),

				(try_begin),
					(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_favors_suitor),
					(str_store_string, s12, "str_they_say_that_s9_has_shown_favor_to_s11_perhaps_it_will_not_be_long_until_they_are_betrothed__if_her_family_permits"),
					(assign, ":last_lady_noted", ":lady"),
					(assign, ":last_suitor_noted", ":suitor"),

					(try_begin),
						(troop_slot_eq, ":lady", slot_troop_met, 2),
						(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_1, ":lady"),
						(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_2, ":lady"),
							(troop_slot_eq, ":suitor", slot_troop_love_interest_3, ":lady"),

						(assign, "$romantic_rival", ":suitor"),
					(try_end),
				(else_try),
					(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_betrothed_to_suitor_by_family),
					(str_store_string, s12, "str_they_say_that_s9_has_been_forced_by_her_family_into_betrothal_with_s11"),
					(assign, ":last_lady_noted", ":lady"),
					(assign, ":last_suitor_noted", ":suitor"),

					(try_begin),
						(troop_slot_eq, ":lady", slot_troop_met, 2),
						(assign, "$romantic_rival", ":suitor"),
					(try_end),
				(else_try),
					(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_betrothed_to_suitor_by_choice),
					(str_store_string, s12, "str_they_say_that_s9_has_agreed_to_s11s_suit_and_the_two_are_now_betrothed"),
					(assign, ":last_lady_noted", ":lady"),
					(assign, ":last_suitor_noted", ":suitor"),

					(try_begin),
						(troop_slot_eq, ":lady", slot_troop_met, 2),
						(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_1, ":lady"),
						(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_2, ":lady"),
							(troop_slot_eq, ":suitor", slot_troop_love_interest_3, ":lady"),


						(assign, "$romantic_rival", ":suitor"),
					(try_end),

				(else_try),
					(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_betrothed_to_suitor_by_pressure),
					(str_store_string, s12, "str_they_say_that_s9_under_pressure_from_her_family_has_agreed_to_betrothal_with_s11"),
					(assign, ":last_lady_noted", ":lady"),
					(assign, ":last_suitor_noted", ":suitor"),

					(try_begin),
						(troop_slot_eq, ":lady", slot_troop_met, 2),
						(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_1, ":lady"),
						(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_2, ":lady"),
							(troop_slot_eq, ":suitor", slot_troop_love_interest_3, ":lady"),

						(assign, "$romantic_rival", ":suitor"),
					(try_end),

				(else_try),

					(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_rejects_suitor),
					(str_store_string, s12, "str_they_say_that_s9_has_refused_s11s_suit"),
					(assign, ":last_lady_noted", ":lady"),
					(assign, ":last_suitor_noted", ":suitor"),

				(else_try),

					(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_rejected_by_suitor),
					(str_store_string, s12, "str_they_say_that_s11_has_tired_of_pursuing_s9"),
					(assign, ":last_lady_noted", ":lady"),
					(assign, ":last_suitor_noted", ":suitor"),


				(else_try),
					(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_father_rejects_suitor),
					(str_store_string, s12, "str_they_say_that_s9s_family_has_forced_her_to_renounce_s11_whom_she_much_loved"),
					(assign, ":last_lady_noted", ":lady"),
					(assign, ":last_suitor_noted", ":suitor"),

				(else_try),
					(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_elopes_with_lord),
					(str_store_string, s12, "str_they_say_that_s9_has_run_away_with_s11_causing_her_family_much_grievance"),
					(assign, ":last_lady_noted", ":lady"),
					(assign, ":last_suitor_noted", ":suitor"),

				(else_try),
					(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_marries_lord),
					(str_store_string, s12, "str_they_say_that_s9_and_s11_have_wed"),
					(assign, ":last_lady_noted", ":lady"),
					(assign, ":last_suitor_noted", ":suitor"),
				(else_try),
					(troop_get_slot, ":suitor", ":lady", slot_lady_last_suitor),
					(is_between, ":suitor", active_npcs_begin, active_npcs_end),
					(str_store_troop_name, s11, ":suitor"),

					(str_store_string, s12, "str_they_say_that_s9_was_recently_visited_by_s11_who_knows_where_that_might_lead"),
					(assign, ":last_lady_noted", ":lady"),
					(assign, ":last_suitor_noted", ":suitor"),
					(try_begin),
						(troop_slot_eq, ":lady", slot_troop_met, 2),
						(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_1, ":lady"),
						(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_2, ":lady"),
							(troop_slot_eq, ":suitor", slot_troop_love_interest_3, ":lady"),

						(assign, "$romantic_rival", ":suitor"),
					(try_end),
				(try_end),

			(try_end),

			(try_begin),
				(neq, ":last_suitor_noted", "$romantic_rival"),
				(assign, "$romantic_rival", -1),
			(try_end),

			(try_begin),
				(gt, ":last_lady_noted", 0),
				(call_script, "script_add_rumor_string_to_troop_notes", ":last_lady_noted", ":last_suitor_noted", 12),
			(try_end),
		(else_try),
			(eq, "$lady_selected", -1),
			(str_store_string, s12, "str_there_is_not_much_to_tell_but_it_is_still_early_in_the_season"),
		(else_try),
			(assign, reg4, "$lady_selected"),
			(str_store_troop_name, s9, "$lady_selected"),
			(str_store_string, s12, "str_error_lady_selected_=_s9"),
		(try_end),
	   ],
	   "{s12}.",
	   "lady_pretalk", []],

	#Info 2: If a lord, show location
	  [anyone,"dplmc_lady_info_relative_2",
	   [
		 (call_script, "script_update_troop_location_notes", "$lord_selected", 1),
		 (call_script, "script_get_information_about_troops_position", "$lord_selected", 0),
		 ],
	   "{s1}", "lady_pretalk",[]],

	#Ask kingdom ladies about feasts.
		[anyone|plyr, "lady_talk", [(neg|eq, "$g_talk_troop_met", 0),],
	   "Do you know of any ongoing feasts?",
	   "dplmc_lady_feasts", []],

	  [anyone, "dplmc_lady_feasts", [

	  (str_clear, s12),
	  (assign, ":feast_found", 0),
	  (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
	##zerilius changes begin
	##Bug Fix since they tell about feasts of eliminated kingdoms also.
	(faction_slot_eq, ":kingdom", slot_faction_state, sfs_active),
	##zerilius changes end
		(faction_slot_eq, ":kingdom", slot_faction_ai_state, sfai_feast),
		(assign, ":feast_found", 1),

		(faction_get_slot, ":feast_venue", ":kingdom", slot_faction_ai_object),
		(str_store_party_name, s4, ":feast_venue"),
		(str_store_faction_name, s3, ":kingdom"),

		(store_current_hours, ":hour"),
		# (store_sub, ":hours_since_start", ":hour", 72), #Floris - bugfix
		(faction_get_slot, ":feast_time", ":kingdom", slot_faction_last_feast_start_time),
		# (val_add, ":hours_since_start", ":feast_time"), #Floris - bugfix
		(store_sub, ":hours_since_start", ":hour", ":feast_time"), #Floris - bugfix

		(try_begin),
			(gt, ":hours_since_start", 48),
			(str_store_string, s12, "str_s12there_is_a_feast_of_the_s3_in_progress_at_s4_but_it_has_been_going_on_for_a_couple_of_days_and_is_about_to_end_"),
		(else_try),
			(gt, ":hours_since_start", 24),
			(str_store_string, s12, "str_s12there_is_a_feast_of_the_s3_in_progress_at_s4_which_should_last_for_at_least_another_day_"),
		(else_try),
			(str_store_string, s12, "str_s12there_is_a_feast_of_the_s3_in_progress_at_s4_which_has_only_just_begun_"),
		(try_end),
	  (try_end),

	  (try_begin),
		(eq, ":feast_found", 0),
		(str_store_string, s12, "str_not_at_this_time_no"),
	  (else_try),
		(str_store_string, s12, "str_s12the_great_lords_bring_their_daughters_and_sisters_to_these_occasions_to_see_and_be_seen_so_they_represent_an_excellent_opportunity_to_make_a_ladys_acquaintance"),
	  (try_end),

	  ],
	   "{s12}",
	"lady_pretalk", []],
	##diplomacy end+
  
  [anyone|plyr,"lady_talk",
   ##diplomacy start+
   #[],#Don't show this option after the first meeting.  There's a separate "ask about relatives instead".
   [(eq, "$g_talk_troop_met", 0),
   ],
   #change "my lady" to "{reg0?my lady:good sir}"
   "May I have the honor of knowing more about you, {reg65?my lady:good sir}?", "lady_relations",[]],
   ##diplomacy end+

  [anyone,"lady_relations",
   [
    (str_store_string, s12, "str_i_am"),
	(assign, ":relation_found", 0),
	(assign, ":in_castle_of_relative", 0),

    (try_for_range, ":lord", active_npcs_begin, kingdom_ladies_end), #use this as the basis for "troop_describe_relation_with_troop"
		(call_script, "script_troop_get_family_relation_to_troop", "$g_talk_troop", ":lord"), #The normal order is reversed, because the lady is describing herself
		(this_or_next|gt, reg0, 5),
			(party_slot_eq, "$g_encountered_party", slot_town_lord, ":lord"),
		(gt, reg0, 0),

		(str_store_troop_name, s14, ":lord"),
		(try_begin),
			(eq, ":relation_found", 1),
			(str_store_string, s12, "str_s12"),
		(try_end),
		(str_store_string, s12, "str_s12_s11_to_s14"),
		(assign, ":relation_found", 1),

		(try_begin),
			(party_slot_eq, "$g_encountered_party", slot_town_lord, ":lord"),
			(assign, ":in_castle_of_relative", 1),
		(try_end),
    (try_end),

	(try_begin),
		(eq, ":in_castle_of_relative", 1),
		(str_store_string, s12, "str_s12"),
	(else_try),
		(eq, ":in_castle_of_relative", 0),
		(faction_slot_eq, "$g_talk_troop_faction", slot_faction_ai_state, sfai_feast),
		(faction_slot_eq, "$g_talk_troop_faction", slot_faction_ai_object, "$g_encountered_party"),
		(str_store_string, s12, "str_s12_i_am_here_for_the_feast"),
	(else_try),
		(str_store_string, s12, "str_s12"),
	(try_end),

   ],
   "{s12}", "lady_pretalk",[
   #diplomacy start+
       (assign, "$g_talk_troop_met", 1),
       ]],
   ##diplomacy end+

  [anyone|plyr,"lady_talk",
   [
    ##diplomacy start+
    #(troop_get_type, ":is_female", "trp_player"),#dplmc+ removed
	#(eq, ":is_female", 0), #dplmc+ removed
	
	(this_or_next|neq, reg65, "$character_gender"),
		(ge, "$g_disable_condescending_comments", 2),
	##diplomacy end+
    (troop_slot_eq, "$g_talk_troop", slot_troop_met, 1),
	(troop_slot_eq, "$g_talk_troop", slot_troop_spouse, -1),
    (neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),

	(neq, "$lady_flirtation_location", "$g_encountered_party"),
	##diplomacy start+
	#Ensure gender of addressed is correct (unnecessary in Native, but may be in mods)
	],
   "My {reg65?lady:lord}, I would like to profess myself your most ardent admirer", "lady_profess_admiration",#Changed "lady" to "{reg0?lady:lord}"
   ##diplomacy end+
	[
	(call_script, "script_troop_get_romantic_chemistry_with_troop", "$g_talk_troop", "trp_player"),
	(assign, ":reaction_change", reg0),

#	(try_begin),
#		(gt, "$g_player_tournament_placement", 3),
#		(val_sub, "$g_player_tournament_placement", 3),
#		(val_mul, "$g_player_tournament_placement", 4), #Twice normal, but is divided by two
#	(else_try),
#		(assign, "$g_player_tournament_placement", 0),
#	(try_end),

#	(try_begin),
#		(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_conventional),
#		(val_mul, "$g_player_tournament_placement", 2),
#	(else_try),
#		(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_moralist),
#		(val_div, "$g_player_tournament_placement", 2),
#	(try_end),

#	(val_add, ":reaction_change", "$g_player_tournament_placement"),
#	(assign, "$g_player_tournament_placement", 0),

	(val_div, ":reaction_change", 2),
	(val_max, ":reaction_change", -2),

	(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", ":reaction_change"),
	(assign, "$g_time_to_spare", 0),

	]],


  [anyone|plyr,"lady_talk",
   [
    ##diplomacy start+
    #(troop_get_type, ":is_female", "trp_player"),
	(this_or_next|ge, "$g_disable_condescending_comments", 2),#dplmc+ added
	(neq, reg65, "$character_gender"),
	(gt, "$g_player_tournament_placement", 3),
    
    #Allow players to dedicate tournament victories even after marriage, though it may irritate the player's spouse
	#(neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
	],
	#Ensure gender of addressed is correct (unnecessary in Native, but may be in mods)
   "My {reg65?lady:lord}, I would like to dedicate my successes in this recent tournament to you", "lady_tournament_dedication_reaction",#Changed "lady" to "{reg0?lady:lord}"
	[
	##diplomacy end+

	(try_begin),
		(gt, "$g_player_tournament_placement", 3),
		(val_sub, "$g_player_tournament_placement", 3),
		(val_mul, "$g_player_tournament_placement", 2),
	(else_try),
		(assign, "$g_player_tournament_placement", 0),
	(try_end),

    ##diplomacy start+
    #If the player has a spouse, a dedication to someone else may irritate them.
    (try_begin),
        (neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
		
		(try_for_range, ":spouse", heroes_begin, heroes_end),#<- Iterate because of the possibility of polygamy
			(neg|troop_slot_eq, ":spouse", slot_troop_occupation, dplmc_slto_dead),
			(neq, ":spouse", "$g_talk_troop"),
			(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":spouse"),
			(this_or_next|troop_slot_eq, ":spouse", slot_troop_spouse, "trp_player"),
				(troop_slot_eq, "trp_player", slot_troop_betrothed, ":spouse"),
			(call_script, "script_troop_change_relation_with_troop", ":spouse", "trp_player", -1),
		(try_end),        
    (try_end),
    ##diplomacy end+

	(try_begin),
		(troop_slot_eq, "$g_talk_troop", slot_lady_used_tournament, 1),
		(val_div, "$g_player_tournament_placement", 3),
		(str_store_string, s9, "str_another_tournament_dedication_oh_i_suppose_it_is_always_flattering"),
	(else_try),
		(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_conventional),
		(val_mul, "$g_player_tournament_placement", 2),
		(str_store_string, s9, "str_do_you_why_what_a_most_gallant_thing_to_say"),
	(else_try),
		(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_moralist),
		(val_div, "$g_player_tournament_placement", 2),
		(str_store_string, s9, "str_hmm_i_cannot_say_that_i_altogether_approve_of_such_frivolity_but_i_must_confess_myself_a_bit_flattered"),
	(else_try),
		(str_store_string, s9, "str_why_thank_you_you_are_most_kind_to_do_so"),
	(try_end),

	(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", "$g_player_tournament_placement"),
	(assign, "$g_player_tournament_placement", 0),
	(troop_set_slot, "$g_talk_troop", slot_lady_used_tournament, 1),
	]],

  [anyone,"lady_tournament_dedication_reaction", [],
   "{s9}", "lady_pretalk",
   []],



  [anyone,"lady_profess_admiration", [
	(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "trp_player"),
    (gt, reg0, 0),

	(try_begin),
		(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_moralist),
		(str_store_string, s11, "str_you_are_most_courteous_and_courtesy_is_a_fine_virtue_"),
	(else_try),
		(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
		(str_store_string, s11, "str_hmm_youre_a_bold_one_but_i_like_that_"),
	(else_try),
		(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_adventurous),
		(str_store_string, s11, "str_ah_well_they_all_say_that_but_no_matter_a_compliment_well_delivered_is_at_least_a_good_start_"),
	(else_try),
		(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_otherworldly),
		(str_store_string, s11, "str_oh_do_you_mean_that_such_a_kind_thing_to_say"),
	(else_try),
		(str_store_string, s11, "str_you_are_a_most_gallant_young_man_"),
	(try_end),

  ],
   "{s11}I would like it very much if we could see more of each other.", "close_window",
   [(troop_set_slot, "$g_talk_troop", slot_troop_met, 2),
	(assign, "$lady_flirtation_location", "$g_encountered_party"),
   ]],

  [anyone,"lady_profess_admiration", [
  ],
   "Ah... You are too kind... My, the hour is getting rather late, isn't it? I really must be going.", "lady_pretalk",
   [(troop_set_slot, "$g_talk_troop", slot_troop_met, 2),
   ]],


  [anyone|plyr,"lady_talk",
   [
	 (troop_slot_eq, "$g_talk_troop", slot_troop_met, 2),
	 (eq, "$g_time_to_spare", 1),
	 (eq, "$talk_context", tc_courtship),
     ],
	 ##diplomacy start+ "my lady" -> "my {reg65?lady:lord}"
   "Do you like poetry, my {reg65?lady:lord}?", "lady_recite_poetry",[
   ##diplomacy end+
	 (assign, "$g_time_to_spare", 0),
   ]],

  [anyone,"lady_recite_poetry", [
  ],
   "That would depend on the poem. Did you intend to recite a verse?", "lady_recite_poetry",
   []],


  [anyone|plyr,"lady_recite_poetry",
   [
	 (gt, "$tragic_poem_recitations", 0),
	 (troop_slot_eq, "$g_talk_troop", slot_lady_courtship_tragic_recited, 0),

     ],
   "The wind that blows the dry steppe dust...", "lady_recite_poetry_response",[
   (assign, "$poem_selected", courtship_poem_tragic),
   (troop_set_slot, "$g_talk_troop", slot_lady_courtship_tragic_recited, 1),

   ]],

  [anyone|plyr,"lady_recite_poetry",
   [
	 (gt, "$comic_poem_recitations", 0),
	 (troop_slot_eq, "$g_talk_troop", slot_lady_courtship_comic_recited, 0),

     ],
   "All the silks of Veluca/All the furs of Khudan...", "lady_recite_poetry_response",[
   (assign, "$poem_selected", courtship_poem_comic),
   (troop_set_slot, "$g_talk_troop", slot_lady_courtship_comic_recited, 1),

   ]],

  [anyone|plyr,"lady_recite_poetry",
   [
	(gt, "$mystic_poem_recitations", 0),
	(troop_slot_eq, "$g_talk_troop", slot_lady_courtship_mystic_recited, 0),

    ],
   "You are the first and the last/the outer and the inner...", "lady_recite_poetry_response",[
   (assign, "$poem_selected", courtship_poem_mystic),
   (troop_set_slot, "$g_talk_troop", slot_lady_courtship_mystic_recited, 1),

   ]],

  [anyone|plyr,"lady_recite_poetry",
   [
	(gt, "$heroic_poem_recitations", 0),
	(troop_slot_eq, "$g_talk_troop", slot_lady_courtship_heroic_recited, 0),
     ],
   "A light pierced the gloom over Wercheg cliffs...", "lady_recite_poetry_response",[
    (assign, "$poem_selected", courtship_poem_heroic),
	(troop_set_slot, "$g_talk_troop", slot_lady_courtship_heroic_recited, 1),

   ]],

  [anyone|plyr,"lady_recite_poetry",
   [
	(gt, "$allegoric_poem_recitations", 0),
	(troop_slot_eq, "$g_talk_troop", slot_lady_courtship_allegoric_recited, 0),

     ],
   "I deflected her skeptical questioning darts/with armor made of purest devotion...", "lady_recite_poetry_response",[
    (assign, "$poem_selected", courtship_poem_allegoric),
	(troop_set_slot, "$g_talk_troop", slot_lady_courtship_allegoric_recited, 1),
   ]],


  [anyone|plyr,"lady_recite_poetry",
   [],"Actually, I can't think of any that I would care to recite...", "lady_pretalk",[]],

   [anyone,"lady_recite_poetry_response",
   [
    (call_script, "script_courtship_poem_reactions", "$g_talk_troop", "$poem_selected"),
   ],
   "{s11}", "lady_private_conversation_end",[
    (assign, ":reaction", reg0),
	(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", ":reaction"),
    (call_script, "script_courtship_poem_reactions", "$g_talk_troop", "$poem_selected"), #this needs to be twice, as the above resets s11
   ]],

   [anyone,"lady_private_conversation_end",
	[
	(str_clear, s11),
	(try_begin),
		(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "trp_player"),
		(gt, reg0, 0),
		(str_store_string, s11, "str__do_come_and_see_me_again_soon"),
	(try_end),
	],
	"Time is passing quickly, and we cannot linger here too long.", "lady_pretalk",
	[
	(assign, "$g_time_to_spare", 0),
	]],


  [anyone|plyr,"lady_talk",
    [
	(neg|check_quest_active, "qst_formal_marriage_proposal"),
	(neg|troop_slot_ge, "trp_player", slot_troop_betrothed, active_npcs_begin),
	(neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),


	(troop_slot_eq, "$g_talk_troop", slot_troop_met, 2),
	(eq, "$talk_context", tc_courtship),
	##diplomacy start+ Allow the possibility of male versions of the lines
    ],
	#replace "my lady" with "{reg0?my lady:kind sir}"
    "Do you think that we may have a future together, {reg65?my lady:kind sir}?", "lady_marriage_discussion",[
	##diplomacy end+
    ]],


  [anyone,"lady_marriage_discussion",
    [
	(assign, "$romantic_rival", -1),
	(try_for_range, ":possible_rival", lords_begin, lords_end),
		(this_or_next|troop_slot_eq, ":possible_rival", slot_troop_love_interest_1, "$g_talk_troop"),
		(this_or_next|troop_slot_eq, ":possible_rival", slot_troop_love_interest_2, "$g_talk_troop"),
			(troop_slot_eq, ":possible_rival", slot_troop_love_interest_2, "$g_talk_troop"),
		(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", ":possible_rival"),

		(try_begin),
			(eq, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":possible_rival"),
			(display_message, "str_rival_found_s4_reg0_relation"),
		(try_end),
		(gt, reg0, "$g_talk_troop_relation"),
		(assign, "$romantic_rival", ":possible_rival"),
	(try_end),
	(gt, "$romantic_rival", -1),
	##diplomacy start+ Give gender equivalents
    ],#"Sir" to "{Sir/Madame}", and "gentlemen" to "{gentlemen/suitors}"
    "{Sir/Madame} -- as you may know, I have been entertaining offers from a number of {gentlemen/suitors} such as yourself. I am not yet at a stage where I can commit to any of them.", "lady_other_suitor",[
    ]],
	##diplomacy end+

  [anyone,"lady_marriage_discussion",
    [
    (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
	(neg|troop_slot_ge, "trp_player", slot_troop_renown, 350),
	],
    "It is good to hear that you are thinking seriously about the future. However, I would like to see you rise a little further in the world before I am ready to commit to marry you.", "lady_proposal_refused",[
    ]],

  [anyone,"lady_marriage_discussion",
    [
    (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_moralist),
	(lt, "$player_honor", 10)
	],
    "It is good to hear that your intentions are honorable. However, I have resolved only to marry a man of the strongest moral fiber. I would like you to prove yourself more in that regard.", "lady_proposal_refused",[
    ]],


  [anyone,"lady_marriage_discussion",
    [
	(lt, "$g_talk_troop_relation", 20),
    ],
    "Sir -- it is comforting to hear that your intentions towards me are honorable. But perhaps we should take the time to get to allow our affections for each other to grow a little stronger, before making any such decision.", "lady_proposal_refused",[
    ]],



  [anyone,"lady_marriage_discussion",
    [
	(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
	(assign, ":guardian", reg0),
	(troop_slot_eq, ":guardian", slot_lord_granted_courtship_permission, -1),
	(str_store_troop_name, s4, reg0),
	(call_script, "script_troop_get_family_relation_to_troop", ":guardian", "$g_talk_troop"),
	],
    "Oh {playername}, how happy that would make me! But my {s11} {s4} would never allow it... Perhaps it is best that we part...", "lady_betrothed", []],

  [anyone,"lady_marriage_discussion",
    [
	(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
	(assign, ":guardian", reg0),
	(call_script, "script_troop_get_family_relation_to_troop", ":guardian", "$g_talk_troop"),
	(str_store_troop_name, s4, ":guardian"),

	],
    "Oh {playername}, how happy that would make me! Go ask my {s11} {s4} for permission!", "close_window",[
	(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
	(assign, ":guardian", reg0),
	(str_store_troop_name, s12, ":guardian"),
	(str_store_troop_name, s15, "$g_talk_troop"),
    (setup_quest_text, "qst_formal_marriage_proposal"),
    (str_store_string, s2, "str_you_intend_to_ask_s12_for_permission_to_marry_s15"),

    (quest_set_slot, "qst_formal_marriage_proposal", slot_quest_target_troop, ":guardian"),
    (quest_set_slot, "qst_formal_marriage_proposal", slot_quest_expiration_days, 30),
    (quest_set_slot, "qst_formal_marriage_proposal", slot_quest_current_state, 0),
	(call_script, "script_start_quest", "qst_formal_marriage_proposal", "$g_talk_troop"),
	(quest_set_slot, "qst_formal_marriage_proposal", slot_quest_giver_troop, "$g_talk_troop"),

	#Repeated to ensure strings work correctly
	(call_script, "script_troop_get_family_relation_to_troop", ":guardian", "$g_talk_troop"),
	(str_store_troop_name, s4, ":guardian"),
    ]],

  [anyone|plyr,"lady_proposal_refused",
    [
	(is_between, "$g_talk_troop_relation", 12, 20),
    (this_or_next|neg|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
		(troop_slot_ge, "trp_player", slot_troop_renown, 350),
    (this_or_next|neg|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_moralist),
		(ge, "$player_honor", 10),
	],
    "Perhaps I can persuade you to delay no further.", "lady_proposal_refused_persuade_check",[
    ]],

  [anyone,"lady_proposal_refused_persuade_check",
    [
	],
    "What do you have to say?", "lady_proposal_refused_persuade_player_response",[

	(assign, reg4, 20),
	(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "trp_player"),
	(assign, ":cur_relation", reg0),
	(assign, reg5, ":cur_relation"),
	(assign, reg9, 1),
    (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
	(store_sub, ":difference", 20, ":cur_relation"),
	(val_mul, ":persuasion_level", 2),
	(try_begin),
		(gt, ":difference", ":persuasion_level"),
		(assign, "$g_persuasion_failure_chance", 100),
	(else_try),
		(store_mul, "$g_persuasion_failure_chance", ":difference", 100),
		(val_div, "$g_persuasion_failure_chance", ":persuasion_level"),
	(try_end),
	(assign, reg8, "$g_persuasion_failure_chance"),
	(store_sub, reg7, 100, "$g_persuasion_failure_chance"),
	(dialog_box, "str_persuasion_opportunity"),

    ]],

  [anyone|plyr,"lady_proposal_refused_persuade_player_response",
    [
	##diplomacy start+ Allow the possibility of male versions of the lines
	], #Replace "lady" with "{reg0?lady:lord}"
    "Love is as a rose, my {reg65?lady:lord}. Left unplucked, it may wither.", "lady_proposal_refused_persuade_result",[
    ]],
	##diplomacy end+

  [anyone|plyr,"lady_proposal_refused_persuade_player_response",
    [],
    "Oh, never mind.", "lady_pretalk",
    []],


  [anyone,"lady_proposal_refused_persuade_result",
    [
	(store_random_in_range, ":random", 0, 100),
	(lt, ":random", "$g_persuasion_failure_chance"),
	],##diplomacy start+ change "sir" to "{sir/madame}"
    "Enough, {sir/madame}! I shall not be rushed into marriage, with you or with anyone else! You have made me very cross. Please, leave me alone for a while. I shall let you know when I am ready to speak to you again.", "close_window", [##diplomacy end+
	(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", -1),
	(jump_to_menu, "mnu_town"),
	(finish_mission),
	]],


   [anyone,"lady_proposal_refused_persuade_result",
    [
	(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
	(assign, ":guardian", reg0),
	(troop_slot_eq, ":guardian", slot_lord_granted_courtship_permission, -1),
	(str_store_troop_name, s4, reg0),
	(call_script, "script_troop_get_family_relation_to_troop", ":guardian", "$g_talk_troop"),
	##diplomacy start+ Use correct pronouns for female guardians
	],#Change "his" to "{reg4?her:his}"
    "Oh {playername}, I could never allow that to happen! Oh, if only we could be wed! But my {s11} {s4} would never give {reg4?her:his} permission... Perhaps it is best that we part...", "lady_betrothed", [
	##diplomacy end+
	(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", 5),
	]],

  [anyone,"lady_proposal_refused_persuade_result",
    [
	(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
	(assign, ":guardian", reg0),
	(call_script, "script_troop_get_family_relation_to_troop", ":guardian", "$g_talk_troop"),
	(str_store_troop_name, s4, ":guardian"),
	##diplomacy start+ Use correct pronouns for female guardians
	],#Change "his" to "{reg4?her:his}"
    "Oh {playername}, I could never allow that to happen! Go ask my {s11} {s4} {reg4?her:his} permission for us to be wed!", "close_window",[
	##diplomacy end+

	(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", 5),
	(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
	(assign, ":guardian", reg0),
	(str_store_troop_name, s12, ":guardian"),
	(str_store_troop_name, s15, "$g_talk_troop"),
    (setup_quest_text, "qst_formal_marriage_proposal"),
    (str_store_string, s2, "str_you_intend_to_ask_s12_for_permission_to_marry_s15"),

    (quest_set_slot, "qst_formal_marriage_proposal", slot_quest_target_troop, ":guardian"),
    (quest_set_slot, "qst_formal_marriage_proposal", slot_quest_expiration_days, 30),
    (quest_set_slot, "qst_formal_marriage_proposal", slot_quest_current_state, 0),
	(call_script, "script_start_quest", "qst_formal_marriage_proposal", "$g_talk_troop"),
	(quest_set_slot, "qst_formal_marriage_proposal", slot_quest_giver_troop, "$g_talk_troop"),
    ]],

  [anyone|plyr,"lady_proposal_refused",
    [],
    "Very well -- I shall continue to strive to be worthy of your esteem!", "close_window",[
    ]],

  [anyone|plyr,"lady_proposal_refused",
    [
	##diplomacy start+
	#Enable this if "enhanced prejudice" mode is active.
    (this_or_next|ge, "$cheat_mode", 1),
	(lt, "$g_disable_condescending_comments", 0),
	##(eq, 1, 0),
	##diplomacy end+
	(neg|check_quest_active, "qst_formal_marriage_proposal"),
	],
    "I am tired of these games! I will speak to your family about arranging a wedding immediately..", "lady_player_threatens_compel",[
    ]],

  [anyone,"lady_player_threatens_compel",
    [],
    "What? Do you mean that?", "lady_player_threatens_compel_2",[
    ]],

  [anyone|plyr,"lady_player_threatens_compel_2",
    [],
    "No, of couse not. Please forgive my burst of temper", "lady_private_conversation_end",[
    ]],

  [anyone|plyr,"lady_player_threatens_compel_2",
    [],
    "Yes -- you clearly do not know what is in your best interests.", "close_window",[
	(call_script, "script_get_kingdom_lady_social_determinants", "$g_talk_troop"),
	(assign, ":guardian", reg0),
	(str_store_troop_name, s10, "$g_talk_troop"),
	(str_store_troop_name, s12, ":guardian"),
    (setup_quest_text, "qst_formal_marriage_proposal"),
    (str_store_string, s2, "str_you_intend_to_ask_s12_to_pressure_s10_to_marry_you"),

    (quest_set_slot, "qst_formal_marriage_proposal", slot_quest_target_troop, ":guardian"),
    (quest_set_slot, "qst_formal_marriage_proposal", slot_quest_expiration_days, 30),
    (quest_set_slot, "qst_formal_marriage_proposal", slot_quest_current_state, 0),
	(call_script, "script_start_quest", "qst_formal_marriage_proposal", "$g_talk_troop"),
	(quest_set_slot, "qst_formal_marriage_proposal", slot_quest_giver_troop, "$g_talk_troop"),
    ]],



	#rival suitor sequence
  [anyone|plyr,"lady_other_suitor",
    [],
    ##diplomacy start+
    #change "my lady" to "my {reg65?lady:lord}"
	"It grieves me to hear that, my {reg65?lady:lord}, but such things must be", "lady_pretalk",
	##diplomacy end+
	[]],

  [anyone|plyr,"lady_other_suitor",
	[],
	##diplomacy start+ his to {his/her}
	"Who is the miscreant! Tell me {his/her} name!", "lady_other_suitor_challenge",
	##diplomacy end+
	[]],

  [anyone|plyr,"lady_other_suitor", #similar to other
    [
	##diplomacy start+
	#Enable this if "enhanced prejudice" mode is active.
	(lt, "$g_disable_condescending_comments", 0),
	#(eq, 1, 0),
	##diplomacy end+
	],
    "I am tired of these games! I will demand that your family compel you to marry me..", "lady_player_threatens_compel",[
    ]],

  [anyone,"lady_other_suitor_challenge",
	[
	  (check_quest_active,"qst_duel_courtship_rival"),
      (call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "$romantic_rival"),
	  (lt, reg0, 0),
	  ##diplomacy start+ Add support for female rival
	  (call_script, "script_dplmc_store_troop_is_female",  "$romantic_rival"),
	],#He -> {reg0?She:He}, man -> {reg0?woman:man}
	"I would be so grateful! But from what I understand, you already have a duel on your hands. {reg0?She:He} is not honor-bound to fight you, if you are committed to another combat. Please, conclude your other business in a hurry, to rescue me from that {reg0?woman:man}'s attentions!.", "lady_pretalk",
	##diplomacy end+
	[]],

  [anyone,"lady_other_suitor_challenge",
	[
	(check_quest_active,"qst_duel_courtship_rival"),
	##diplomacy start+
	(assign, reg0, 1),
	(try_begin),
		(eq, reg65, "$character_gender"),
		(assign, reg0, 0),
	(try_end),
	],#Next line change "You men" to "{reg0?You {men/women}:People}"
	"Ah! Such talk. But from what I hear, you already have a duel on your hands. Finish one before you start another! Sigh... {reg0?You {men/women}:People} can be so silly...", "lady_pretalk",
	##diplomacy end+
	[]],

  [anyone,"lady_other_suitor_challenge",
	[
    (call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "$romantic_rival"),
	(lt, reg0, 0),
	(str_store_troop_name, s5, "$romantic_rival"),
	##diplomacy start+ Add support for female rival
    (call_script, "script_dplmc_store_troop_is_female",  "$romantic_rival"),
	],#man -> {reg0?woman:man}
	"It is {s5}. Please, rescue me from that {reg0?woman:man}'s attentions!", "lady_other_suitor_challenge_confirm",
	##diplomacy end+
	[]],													# Floris Port Marker



  [anyone,"lady_other_suitor_challenge",
	[
	(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
	(str_store_troop_name, s5, "$romantic_rival"),
	],
	"Will you now? This should be interesting. Very well. Your rival is {s5}. Let us see which of you has the greater mettle.", "lady_other_suitor_challenge_confirm",
	[
	(assign, "$quarrel_penalty", 0),
	]],

  [anyone,"lady_other_suitor_challenge",
	[
	(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_conventional),
	(str_store_troop_name, s5, "$romantic_rival"),
	],##diplomacy start+ change "men" to "{men/women}"
	"Oh, fie! I wish that this were not a matter of honor, so I could refuse such a request. But alas, I feel compelled to tell you that your rival is {s5}. I wish that heaven had not granted me such a fair visage, so that I would not inspire such passions in {men/women}!", "lady_other_suitor_challenge_confirm",
	[##diplomacy end+
	(assign, "$quarrel_penalty", -1),
	]],

  [anyone,"lady_other_suitor_challenge",
	[
	(str_store_troop_name, s5, "$romantic_rival"),
	],##diplomacy start+ change "sir" to "{sir/madame}"
	"I will have none of such talk! It is nonsense for you and {s5} to fight over -- whoops! I beg of you, {sir/madame}, forget the name that just escaped my lips...", "lady_other_suitor_challenge_confirm",
	[##diplomacy end+
	(assign, "$quarrel_penalty", -3),
	]],

  [anyone|plyr,"lady_other_suitor_challenge_confirm",
	[##diplomacy start+ Add support for female rival
    (call_script, "script_dplmc_store_troop_is_female",  "$romantic_rival"),],
	#Change "him" to "{reg0?her:him}"
	"So be it! I shall challenge {reg0?her:him} to a trial of arms!", "lady_other_suitor_challenge_confirm_yes",
	##diplomacy end+
	[]],

  [anyone|plyr,"lady_other_suitor_challenge_confirm",
	[],
	"On second thought, I let my passions run away with me there. Never mind.", "lady_other_suitor_challenge_confirm_no",
	[]],

  [anyone,"lady_other_suitor_challenge_confirm_yes",
	[
	  (try_begin),
	    (call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "$romantic_rival"),
	    (lt, reg0, 0),
	    (str_store_string, s15, "str_do_be_careful_i_am_so_much_endebted_to_you_for_this"),
	  (else_try),
	    (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
	    (str_store_string, s15, "str_go_then__we_shall_see_which_of_you_triumphs"),
	  (else_try),
	    (str_store_string, s15, "str_sigh_i_will_never_truly_understand_men_and_their_rash_actions"),
	  (try_end),
	],
	"{s15}", "lady_pretalk",
	[
	  (call_script, "script_troop_change_relation_with_troop", "trp_player", "$g_talk_troop", "$quarrel_penalty"),
	  (str_store_troop_name, s11, "$g_talk_troop"),
	  (str_store_troop_name_link, s13, "$romantic_rival"),
	  (setup_quest_text, "qst_duel_courtship_rival"),
	  ##diplomacy start+ use correct pronoun for gender
	  (call_script, "script_dplmc_store_troop_is_female_reg", "$romantic_rival", 4),
	  ##diplomacy end+
	  (str_store_string, s2, "str_you_intend_to_challenge_s13_to_force_him_to_relinquish_his_suit_of_s11"),

	  (call_script, "script_start_quest", "qst_duel_courtship_rival", "$g_talk_troop"),

	  (quest_set_slot, "qst_duel_courtship_rival", slot_quest_target_troop, "$romantic_rival"),

	  (quest_set_slot, "qst_duel_courtship_rival", slot_quest_xp_reward, 400),
	  (quest_set_slot, "qst_duel_courtship_rival", slot_quest_expiration_days, 60),
	  (quest_set_slot, "qst_duel_courtship_rival", slot_quest_current_state, 0),
	]],

  [anyone,"lady_other_suitor_challenge_confirm_no",
	[],
	"Good. You are wise not to let your temper guide you.", "lady_private_conversation_end",
	[]],






  [anyone|plyr,"lady_talk",
   [
	 (troop_slot_ge, "$g_talk_troop", slot_troop_spouse, 0),
#     (troop_slot_ge, "$g_talk_troop", slot_troop_met, 2),
     (store_partner_quest, ":ladys_quest"),
     (lt, ":ladys_quest", 0)
     ],
   "Is there anything I can do to win your favour?", "lady_ask_for_quest",[(call_script, "script_get_quest", "$g_talk_troop"),
                                                                 (assign, "$random_quest_no", reg0)]],

  [anyone,"lady_ask_for_quest",
  [
    (troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 1),
  ],
   "I don't have anything else for you to do right now.", "lady_pretalk", []],

  [anyone,"lady_ask_for_quest",
  [
	 (this_or_next|eq, "$random_quest_no", "qst_rescue_lord_by_replace"),
	 (eq, "$random_quest_no", "qst_rescue_prisoner"),

     (quest_get_slot, ":quest_target_troop", "$random_quest_no", slot_quest_target_troop),
     (call_script, "script_troop_get_family_relation_to_troop", ":quest_target_troop", "$g_talk_troop"),
     (str_store_string, s17, s11),
	 ##diplomacy start+ Correct pronouns if :quest_target_troop is female
	 (call_script, "script_dplmc_store_troop_is_female",  ":quest_target_troop"),
  ],#He -> {reg0?She:He}, his -> {reg0?her:his}, him -> {reg0?her:him}
   "Oh, I fear I may never see my {s17}, {s13}, again... {reg0?She:He} is a prisoner in the dungeon of {s14}.\
 We have tried to negotiate {reg0?her:his} ransom, but it has been set too high.\
 We can never hope to raise that much money without selling everything we own,\
 and God knows {s13} would rather spend {reg0?her:his} life in prison than make us destitute.\
 Instead I came up with a plan to get {reg0?her:him} out of there, but it requires someone to make a great sacrifice,\
 and so far my pleas have fallen on deaf ears...", "lady_mission_told",
 ##diplomacy end+
   [
     (quest_get_slot, ":quest_target_center", "$random_quest_no", slot_quest_target_center),
     (quest_get_slot, ":quest_target_troop", "$random_quest_no", slot_quest_target_troop),
     (call_script, "script_troop_get_family_relation_to_troop", ":quest_target_troop", "$g_talk_troop"),
     (str_store_string, s17, s11),

     (str_store_troop_name, s11, "$g_talk_troop"),
     (str_store_troop_name_link, s13, ":quest_target_troop"),
     (str_store_party_name_link, s14, ":quest_target_center"),
     (setup_quest_text,"$random_quest_no"),
	 ##diplomacy start+ Correct pronouns for the quest target and quest giver (reg65 for talk troop, reg4 is set for target above)
     (try_begin),
       (eq, "$random_quest_no", "qst_rescue_lord_by_replace"),
	   #changed pronouns next line
       (str_store_string, s2, "@{s11} asked you to rescue {reg65?her:his} {s17}, {s13}, from {s14} by switching clothes and taking {reg4?her:his} place in prison."),
     (else_try),
		#changed pronouns next line
       (str_store_string, s2, "@{s11} asked you to rescue {reg65?her:his} {s17}, {s13}, from {s14}."),
     (try_end),
	 ##diplomacy end+
    ]],

  [anyone,"lady_ask_for_quest", [
     (eq, "$random_quest_no", "qst_deliver_message_to_prisoner_lord"),
     (quest_get_slot, ":quest_target_troop", "$random_quest_no", slot_quest_target_troop),
     (call_script, "script_troop_get_family_relation_to_troop", ":quest_target_troop", "$g_talk_troop"),

  ],
   "My poor {s11}, {s13}, is a prisoner in the {s14} dungeons.\
 The only way we can talk to each other is by exchanging letters whenever we can,\
 but the journey is so dangerous that we get little chance to do so.\
 Please, would you deliver one for me?", "lady_mission_told",
   [
     (quest_get_slot, ":quest_target_center", "$random_quest_no", slot_quest_target_center),
     (quest_get_slot, ":quest_target_troop", "$random_quest_no", slot_quest_target_troop),


     (str_store_troop_name, s11, "$g_talk_troop"),
     (str_store_troop_name_link, s13, ":quest_target_troop"),
     (str_store_party_name_link, s14, ":quest_target_center"),
     (setup_quest_text,"$random_quest_no"),
     (str_store_string, s2, "@{s11} asked you to deliver a message to {s13}, who is imprisoned at {s14}."),
    ]],


  [anyone,"lady_ask_for_quest", [(eq, "$random_quest_no", "qst_duel_for_lady")],
   "Dear {playername}, you are kind to ask, but you know little of my troubles\
 and I can't possibly ask you to throw yourself into danger on my behalf.", "lady_quest_duel_for_lady",[]],

  [anyone|plyr,"lady_quest_duel_for_lady", [], "Tell me what the problem is, and I can make my own decision.", "lady_quest_duel_for_lady_2",
   [
     (quest_get_slot, ":quest_target_troop", "$random_quest_no", slot_quest_target_troop),

     (str_store_troop_name, s11, "$g_talk_troop"),
     (str_store_troop_name_link, s13, ":quest_target_troop"),
     (str_store_string, s2, "@You agreed to challenge {s13} to defend {s11}'s honour."),
     (setup_quest_text,"$random_quest_no"),
    ]],

  [anyone,"lady_quest_duel_for_lady_2", [
  ##diplomacy start+ Add possibility of male version
  (quest_get_slot, ":quest_target_troop", "$random_quest_no", slot_quest_target_troop),
  (call_script, "script_dplmc_store_troop_is_female",  ":quest_target_troop"),#gender of lord to challenge
  
  (store_sub, reg1, 1, reg65),#gender of quest-giver's spouse (0 to 1, 1 to 0)
  (try_begin),
	(troop_slot_ge, "$g_talk_troop",  slot_troop_spouse, 0),
	(troop_get_slot, ":spouse", "$g_talk_troop", slot_troop_spouse),
	(assign, reg1, 0),
	(call_script, "script_cf_dplmc_troop_is_female", ":spouse"),
	(assign, reg1, 1),
  (try_end),
  #Numerous gender changes in next line
  ], "Very well, as you wish it...\
 My {reg1?wife:husband} has made certain enemies in {reg1?her:his} life, {playername}. One of the most insidious is {s13}.\
 {reg0?She:He} is going around making terrible accusations against me, impugning my honour at every turn!\
 Because {reg0?she:he} cannot harm my {reg1?wife:husband} directly, {reg0?she:he} is using me as a target to try and stain our name.\
 You should hear the awful things {reg0?she:he}'s said! I only wish there was someone brave enough to make {reg0?her:him} recant {reg0?her:his} slander,\
 but {s13} is a very fine swordsman, and {reg0?she:he}'s widely feared...", "lady_quest_duel_for_lady_3",[]],
 ##diplomacy end+

  [anyone|plyr,"lady_quest_duel_for_lady_3", [
  ##diplomacy start+ Add possibility of fe/male version
  (quest_get_slot, ":quest_target_troop", "$random_quest_no", slot_quest_target_troop),
  (call_script, "script_dplmc_store_troop_is_female",  ":quest_target_troop"),#gender of lord to challenge
  #next line, him -> {reg0?her:him}, his -> {reg0?her:his}
  ], "I fear {reg0?her:him} not, {s65}. I will make {reg0?her:him} take back {reg0?her:his} lies.", "lady_quest_duel_for_lady_3_accepted",[]],
  ##diplomacy end+
  [anyone,"lady_quest_duel_for_lady_3_accepted", [], "Oh! I can't ask that of you, {playername}, but...\
 I would be forever indebted to you, and you are so sure. It would mean so much if you would defend my honour.\
 Thank you a thousand times, all my prayers and my favour go with you.", "close_window",
   [

     (quest_get_slot, ":quest_target_troop", "$random_quest_no", slot_quest_target_troop),
     (call_script, "script_start_quest", "$random_quest_no", "$g_talk_troop"),
     (call_script, "script_report_quest_troop_positions", "$random_quest_no", ":quest_target_troop", 3),
     (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 3),
     ]],

  [anyone|plyr,"lady_quest_duel_for_lady_3", [##diplomacy start+ Use proper pronoun
  (quest_get_slot, ":quest_target_troop", "$random_quest_no", slot_quest_target_troop),
  (call_script, "script_dplmc_store_troop_is_female",  ":quest_target_troop"),#gender of lord to challenge
  ], "If {reg0?she:he}'s that dangerous, perhaps maybe it would be better to ignore {reg0?her:him}...", "lady_quest_duel_for_lady_3_rejected",[]],
  ##diplomacy end+
  [anyone,"lady_quest_duel_for_lady_3_rejected", [], "Oh... Perhaps you're right, {playername}.\
 I should let go of these silly childhood ideas of chivalry and courage. {Men/People} are not like that,\
 not anymore. Good day to you.", "close_window",
   [(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 1),
    (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -1),
    ]],


  [anyone,"lady_ask_for_quest", [], "No, {playername}, I've no need for a champion right now.", "lady_pretalk",[]],

  [anyone|plyr,"lady_mission_told", [], "As you wish it, {s65}, it shall be done.", "lady_mission_accepted",[]],
  [anyone|plyr,"lady_mission_told", [], "{s66}, I fear I cannot help you right now.", "lady_mission_rejected",[]],

  [anyone,"lady_mission_accepted", [], "You are a true {gentleman/lady}, {playername}.\
 Thank you so much for helping me", "close_window",
   [
     (try_begin),
       (eq, "$random_quest_no", "qst_deliver_message_to_prisoner_lord"),
       (call_script, "script_troop_add_gold", "trp_player", 10),
     (try_end),
     (call_script, "script_start_quest", "$random_quest_no", "$g_talk_troop"),
    ]],
##diplomacy start+ add male version 
  [anyone,"lady_mission_rejected", [
  #changed "woman" -> "{reg65?woman:young lad}"
  ], "You'll not help a {reg65?woman:young lad} in need? You should be ashamed, {playername}...\
 Please leave me, I have some important embroidery to catch up.", "close_window",
##diplomacy end+
   [
     (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -1),
     (troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 1),
    ]],

#Leave
  [anyone|plyr,"lady_talk", [
  (troop_slot_ge, "$g_talk_troop", slot_troop_spouse, 0),
  ], "I want to improve my relation with a lord. Can you help me?", "lady_restore_relation",[]],
  [anyone,"lady_restore_relation", [(le, "$g_talk_troop_relation", 0)], "{playername}, I don't know you well enough to act on your behalf. I am sorry.", "lady_pretalk",[]],
  [anyone,"lady_restore_relation", [], "Hmm. I guess you got on the wrong side of somebody. Very well, who do you want to restore your relation with?", "lady_restore_relation_2",[]],

  [anyone|plyr|repeat_for_troops,"lady_restore_relation_2", [(store_repeat_object, ":troop_no"),
                                                             (is_between, ":troop_no", active_npcs_begin, active_npcs_end),
                                                             (store_troop_faction, ":faction_no", ":troop_no"),
                                                             (eq, "$g_talk_troop_faction", ":faction_no"),
                                                             (call_script, "script_troop_get_player_relation", ":troop_no"),
                                                             (lt, reg0, 0),
                                                             ##diplomacy start+
                                                             #enhanced functionality for relatives
                                                             (str_store_troop_name, s1, ":troop_no"),
                                                             (call_script,"script_troop_get_family_relation_to_troop",":troop_no","$g_talk_troop"),
                                                             (try_begin),
                                                                 (ge, reg0, 1),
                                                                 (str_store_string, s10, s1),
                                                                 (str_store_string, s1, "str_dplmc_your_s11_s10"),
                                                             (try_end),
                                                             ],
   "{s1}", "lady_restore_relation_2b",[(store_repeat_object, "$troop_to_restore_relations_with")]],
  ##diplomacy end+
  [anyone|plyr,"lady_restore_relation_2", [], "Never mind. I get along with everyone well enough.", "lady_pretalk",[]],

  [anyone,"lady_restore_relation_2b", [(str_store_troop_name, s10, "$troop_to_restore_relations_with")], "Well I can try to help you there.\
 I am sure a few expensive gifts will make {s10} look at you more favorably.", "lady_restore_relation_3",[]],

  [anyone,"lady_restore_relation_3", [(str_store_troop_name, s10, "$troop_to_restore_relations_with"),
                                      (assign, "$lady_restore_cost_1", 1000),
                                      (assign, "$lady_restore_cost_2", 2000),
                                      (assign, "$lady_restore_cost_3", 3000),
                                      ##diplomacy start+
                                      #lower cost for relatives
                                      (call_script,"script_troop_get_family_relation_to_troop","$troop_to_restore_relations_with","$g_talk_troop"),
                                      (try_begin),
                                         (ge, reg0, 10),
                                         (assign, "$lady_restore_cost_1", 750),
                                         (assign, "$lady_restore_cost_2", 1500),
                                         (assign, "$lady_restore_cost_3", 2250),
                                         (str_store_string, s10, s11),
                                      (else_try),
                                         (ge, reg0, 1),
                                         (assign, "$lady_restore_cost_1", 900),
                                         (assign, "$lady_restore_cost_2", 1800),
                                         (assign, "$lady_restore_cost_3", 2700),
                                         (str_store_string, s10, s11),
                                      (try_end),
                                      ##diplomacy end+
                                      (assign, reg10, "$lady_restore_cost_1"),
                                      (assign, reg11, "$lady_restore_cost_2"),
                                      (assign, reg12, "$lady_restore_cost_3"),
									  ##diplomacy start+ Unnecessary, since the family relation script sets this
                                      #(troop_get_type, reg4, "$troop_to_restore_relations_with"),
									  ##diplomacy end+
                                      ],
   "You can improve your relation with {s10} by sending {reg4?her:him} a gift worth {reg10} denars.\
 But if you can afford spending {reg11} denars on the gift, it would make a good impression on {reg4?her:him}.\
 And if you can go up to {reg12} denars, that would really help smooth things out.", "lady_restore_relation_4",[]],

  [anyone|plyr,"lady_restore_relation_4", [(store_troop_gold,":gold", "trp_player"),
                                           (ge, ":gold", "$lady_restore_cost_1"),
                                           (assign, reg10, "$lady_restore_cost_1")],
   "I think a gift of {reg10} denars will do.", "lady_restore_relation_5",[(assign, "$temp", 1), (assign, "$temp_2", "$lady_restore_cost_1")]],
  [anyone|plyr,"lady_restore_relation_4", [(store_troop_gold,":gold", "trp_player"),
                                           (ge, ":gold", "$lady_restore_cost_2"),
                                           (assign, reg11, "$lady_restore_cost_2")],
   "Maybe I can afford {reg11} denars.", "lady_restore_relation_5",[(assign, "$temp", 2), (assign, "$temp_2", "$lady_restore_cost_2")]],
  [anyone|plyr,"lady_restore_relation_4", [(store_troop_gold,":gold", "trp_player"),
                                           (ge, ":gold", "$lady_restore_cost_3"),
                                           (assign, reg12, "$lady_restore_cost_3")],
   "In that case, I am ready to spend {reg12} denars.", "lady_restore_relation_5",[(assign, "$temp", 3), (assign, "$temp_2", "$lady_restore_cost_3")]],

  [anyone|plyr,"lady_restore_relation_4", [], "I don't think I can afford a gift at the moment.", "lady_restore_relation_cant_afford",[]],

  [anyone,"lady_restore_relation_5", [], "Excellent. Then I'll choose an appropriate gift for you and send it to {s10} with your compliments.\
 I am sure {reg4?she:he} will appreciate the gesture.", "lady_restore_relation_6",[
     (troop_remove_gold, "trp_player","$temp_2"),
     (call_script, "script_change_player_relation_with_troop", "$troop_to_restore_relations_with", "$temp"),
	 ##diplomacy start+
     #(troop_get_type, reg4, "$troop_to_restore_relations_with"),
	 (call_script, "script_dplmc_store_troop_is_female_reg", "$troop_to_restore_relations_with", 4),
	 ##diplomacy end+
     ]],

  [anyone|plyr,"lady_restore_relation_6", [], "Thank you for your help, madame.", "lady_pretalk",[]],

  [anyone,"lady_restore_relation_cant_afford", [], "I am afraid, I can't be of much help in that case, {playername}. I am sorry.", "lady_pretalk",[]],

  [anyone|plyr,"lady_talk", [], "I must beg my leave.", "lady_leave",[]],

  [anyone|auto_proceed,"lady_leave", [
  (call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "trp_player"),
  (try_begin),
	(lt, reg0, 0),
	(str_store_string, s12, "str_farewell"),
  (else_try),
	(str_store_string, s12, "str_farewell_playername"),
  (try_end),
  ], "{s12}", "close_window",[(eq,"$talk_context",tc_party_encounter),(assign, "$g_leave_encounter", 1)]],



#Convincing bargaining
  [anyone,"convince_begin", [], "I still don't see why I should accept what you're asking of me.", "convince_options",
   [(quest_get_slot, "$convince_value", "$g_convince_quest", slot_quest_convince_value),
    ]],

  [anyone|plyr,"convince_options", [(assign, reg8, "$convince_value")], "Then I'll make it worth your while. ({reg8} denars)", "convince_bribe",[]],
  [anyone|plyr,"convince_options", 
  [(store_div, "$convince_relation_penalty", "$convince_value", 300),
   (val_add, "$convince_relation_penalty", 1),
   (assign, reg9, "$convince_relation_penalty")], 
   "Please, do it for the sake of our friendship. (-{reg9} to relation)", "convince_friendship",[]],
  [anyone|plyr,"convince_options", [], "Let me try and convince you. (Persuasion)", "convince_persuade_begin", []],
  [anyone|plyr,"convince_options", [], "Never mind.", "lord_pretalk",[]],

  [anyone,"convince_bribe", [], "Mmm, a generous gift to my coffers would certainly help matters...\
 {reg8} denars should do it. If you agree, then I'll go with your suggestion.", "convince_bribe_verify",[]],

  [anyone|plyr,"convince_bribe_verify", [(store_troop_gold, ":gold", "trp_player"),
                                         (lt, ":gold", "$convince_value")],
   "I'm afraid my finances will not allow for such a gift.", "convince_bribe_cant_afford",[]],
  [anyone|plyr,"convince_bribe_verify", [(store_troop_gold, ":gold", "trp_player"),
                                         (ge, ":gold", "$convince_value")],
  "Very well, please accept these {reg8} denars as a token of my gratitude.", "convince_bribe_goon",[]],
  [anyone|plyr,"convince_bribe_verify", [], "Let me think about this some more.", "convince_begin",[]],

  [anyone,"convince_bribe_cant_afford", [], "Ah. In that case, there is little I can do,\
 unless you have some further argument to make.", "convince_options",[]],
   [anyone,"convince_bribe_goon", [], "My dear {playername}, your generous gift has led me to reconsider what you ask,\
 and I have come to appreciate the wisdom of your proposal.", "convince_accept",[
 ##diplomacy start+ add removed gold to bribed lord
 (call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", "$convince_value", "$g_talk_troop"),
 ##diplomacy end+
 (troop_remove_gold, "trp_player","$convince_value")]],

  [anyone,"convince_friendship",
   [(store_add, ":min_relation", 5, "$convince_relation_penalty"),
    (ge, "$g_talk_troop_effective_relation", ":min_relation")], "You've done well by me in the past, {playername},\
 and for that I will go along with your request, but know that I do not like you using our relationship this way.", "convince_friendship_verify",[]],

  [anyone|plyr,"convince_friendship_verify", [], "I am sorry, my friend, but I need your help in this.", "convince_friendship_go_on",[]],
  [anyone|plyr,"convince_friendship_verify", [], "If it will not please you, then I'll try something else.", "lord_pretalk",[]],

  [anyone,"convince_friendship_go_on", [], "All right then, {playername}, I will accept this for your sake. But remember, you owe me for this.", "convince_accept",
   [(store_sub, ":relation_change", 0, "$convince_relation_penalty"),
    (call_script, "script_change_player_relation_with_troop","$g_talk_troop",":relation_change")]],

  [anyone,"convince_friendship",
   [(ge, "$g_talk_troop_relation", -5)], "I don't think I owe you such a favor {playername}.\
 I see no reason to accept this for you.", "lord_pretalk",[]],

  [anyone,"convince_friendship", [], "Is this a joke? You've some nerve asking me for favours, {playername},\
 and let me assure you you'll get none.", "lord_pretalk",[]],

  [anyone,"convince_persuade_begin",
  [(troop_get_slot, ":last_persuasion_time", "$g_talk_troop", slot_troop_last_persuasion_time),
   (store_current_hours, ":cur_hours"),
   (store_add, ":valid_time", ":last_persuasion_time", 24),
   (gt, ":cur_hours", ":valid_time"),
   ],
   "Very well. Make your case.", "convince_persuade_begin_2",[]],


  [anyone|plyr,"convince_persuade_begin_2", [], "[Attempt to persuade]", "convince_persuade",[
        (try_begin),
          (store_random_in_range, ":rand", 0, 100),
          (lt, ":rand", 30),
          (store_current_hours, ":cur_hours"),
          (troop_set_slot, "$g_talk_troop", slot_troop_last_persuasion_time, ":cur_hours"),
        (try_end),
        (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
        (store_add, ":persuasion_potential", ":persuasion_level", 5),

        (store_random_in_range, ":random_1", 0, ":persuasion_potential"),
        (store_random_in_range, ":random_2", 0, ":persuasion_potential"),
        (store_add, ":rand", ":random_1", ":random_2"),

        (assign, ":persuasion_difficulty", "$convince_value"),
        (convert_to_fixed_point, ":persuasion_difficulty"),
        (store_sqrt, ":persuasion_difficulty", ":persuasion_difficulty"),
        (convert_from_fixed_point, ":persuasion_difficulty"),
        (val_div, ":persuasion_difficulty", 10),
        (val_add, ":persuasion_difficulty", 4),

        (store_sub, "$persuasion_strength", ":rand", ":persuasion_difficulty"),
        (val_mul, "$persuasion_strength", 20),
        (assign, reg5, "$persuasion_strength"),
        (val_sub, "$convince_value", "$persuasion_strength"),
        (quest_set_slot, "$g_convince_quest", slot_quest_convince_value, "$convince_value"),
        (str_store_troop_name, s50, "$g_talk_troop"),
		##diplomacy start+
		##OLD:
        #(troop_get_type, reg51, "$g_talk_troop"),
		##NEW:
		(try_begin),
			(call_script, "script_cf_dplmc_troop_is_female", "$g_talk_troop"),
			(assign, reg51, 1),
			(assign, reg65, 1),
		(else_try),
			(assign, reg51, 0),
			(assign, reg65, 0),
		(try_end),
		##diplomacy end+
        (try_begin),
          (lt, "$persuasion_strength", -30),
          (str_store_string, s5, "str_persuasion_summary_very_bad"),
        (else_try),
          (lt, "$persuasion_strength", -10),
          (str_store_string, s5, "str_persuasion_summary_bad"),
        (else_try),
          (lt, "$persuasion_strength", 10),
          (str_store_string, s5, "str_persuasion_summary_average"),
        (else_try),
          (lt, "$persuasion_strength", 30),
          (str_store_string, s5, "str_persuasion_summary_good"),
        (else_try),
          (str_store_string, s5, "str_persuasion_summary_very_good"),
        (try_end),
        (dialog_box, "@{s5} (Persuasion strength: {reg5})", "@Persuasion Attempt"),
  ]],
  [anyone|plyr,"convince_persuade_begin_2", [], "Wait, perhaps there is another way to convince you.", "convince_begin",[]],

  [anyone,"convince_persuade_begin", [], "By God's grace, {playername}!\
 Haven't we talked enough already? I am tired of listening to you,\
 and I do not want to hear any more of it right now.", "lord_pretalk",[]],

  [anyone,"convince_persuade", [(le, "$convince_value", 0)], "All right, all right. You have persuaded me to it.\
 I'll go ahead with what you suggest.", "convince_accept",[]],
  [anyone,"convince_persuade", [(gt, "$persuasion_strength", 5)], "You've a point, {playername},\
 I'll admit that much. However I am not yet convinced I should do as you bid.", "convince_options",[]],
  [anyone,"convince_persuade", [(gt, "$persuasion_strength", -5)], "Enough, {playername}.\
 You've a lot of arguments, but I find none of them truly convincing. I stand by what I said before.", "convince_options",[]],
  [anyone,"convince_persuade", [], "Truthfully, {playername}, I fail to see the virtue of your reasoning.\
 What you ask for makes even less sense now than it did before.", "convince_options",[]],

#Seneschal

  [anyone,"start", [(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_seneschal),
                    (eq, "$talk_context", tc_siege_won_seneschal),
                    (str_store_party_name, s1, "$g_encountered_party"),
                    ],
   "I must congratulate you on your victory, my {lord/lady}. Welcome to {s1}.\
 We, the housekeepers of this castle, are at your service.", "siege_won_seneschal_1",[]],
  [anyone|plyr,"siege_won_seneschal_1", [], "Are you the seneschal?", "siege_won_seneschal_2",[]],
  [anyone,"siege_won_seneschal_2", [], "Indeed I am, my {lord/lady}.\
 I have always served the masters of {s1} to the best of my ability, whichever side they might be on.\
 Thus you may count on my utmost loyalty for as long as you are the {lord/lady} of this place.\
 Now, do you intend to keep me on as the seneschal? I promise you will not be disappointed.", "siege_won_seneschal_3",[]],
  [anyone|plyr,"siege_won_seneschal_3", [], "Very well, you may keep your post for the time being.", "siege_won_seneschal_4",[]],
  [anyone|plyr,"siege_won_seneschal_3", [], "You can stay, but I shall be keeping a close watch on you.", "siege_won_seneschal_4",[]],
  [anyone,"siege_won_seneschal_4", [], "Thank you, my {lord/lady}. If you do not mind my impudence,\
 may I inquire as to what you wish to do with the castle?", "siege_won_seneschal_5",[]],

  [anyone|plyr,"siege_won_seneschal_5", [], "I will sell it to another lord.", "siege_won_seneschal_6",[]],
  [anyone|plyr,"siege_won_seneschal_5", [], "I intend to claim it for myself.", "siege_won_seneschal_6",[]],

  [anyone|plyr,"siege_won_seneschal_5", [], "I haven't given it much thought. What are my options?", "siege_won_seneschal_list_options",[]],

  [anyone,"siege_won_seneschal_list_options", [], "According to our laws and traditions,\
 you can do one of several things.\
 First, you could station a garrison here to protect the castle from any immediate counterattacks,\
 then request an audience with some wealthy lord and ask him to make you an offer.\
 It would be worth a tidy sum, believe you me.\
 If you do not wish to sell, then you will have to find yourself a liege lord and protector who would accept homage from you.\
 Without a royal investiture and an army at your back, you would have a difficult time holding on to the castle.\
 Both you and {s1} would become great big targets for any man with a few soldiers and a scrap of ambition.\
 ", "siege_won_seneschal_list_options_2",[]],

  [anyone|plyr,"siege_won_seneschal_list_options_2", [], "What do you mean, a liege lord and protector? I won this place by my own hand, I don't need anyone else!", "siege_won_seneschal_list_options_3",[]],
  [anyone,"siege_won_seneschal_list_options_3", [], "Of course you don't, my {lord/lady}.\
 However, no lord in the land will recognize your claim to the castle unless it is verified by royal decree.\
 They would call {s1} an outlaw stronghold and take it from you at the earliest opportunity.\
 Surely not even you could stand against a whole army.", "siege_won_seneschal_list_options_4",[]],
  [anyone|plyr,"siege_won_seneschal_list_options_4", [], "Hmm. I'll give it some thought.", "siege_won_seneschal_6",[]],

  [anyone,"siege_won_seneschal_6", [], "I am very pleased to hear it, my {lord/lady}.\
 I am only trying to serve you to the best of my ability. Now,\
 if at any time you find you have further need of me,\
 I will be in the great hall arranging a smooth handover of the castle to your forces.\
 ", "close_window",[]],


  [anyone,"start", [(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_seneschal),(eq,"$g_talk_troop_met",0),(str_store_party_name,s1,"$g_encountered_party")],
   "Good day, {sir/madam}. I do nott believe I've seen you here before.\
 Let me extend my welcome to you as the seneschal of {s1}.", "seneschal_intro_1",[]],

  [anyone|plyr,"seneschal_intro_1", [],  "A pleasure to meet you, {s65}.", "seneschal_intro_1a",[]],
  [anyone,"seneschal_intro_1a", [], "How can I help you?", "seneschal_talk",[]],
  [anyone|plyr,"seneschal_intro_1", [],  "What exactly do you do here?", "seneschal_intro_1b",[]],
  [anyone,"seneschal_intro_1b", [], "Ah, a seneschal's duties are many, good {sire/woman}.\
 For example, I collect the rents from my lord's estates, I manage the castle's storerooms,\
 I deal with the local peasantry, I take care of castle staff, I arrange supplies for the garrison...\
 All mundane matters on this fief are my responsibility, on behalf of my lord.\
 Everything except commanding the soldiers themselves.", "seneschal_talk",[]],

  [anyone,"start", [(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_seneschal)],
   "Good day, {sir/madam}.", "seneschal_talk",[]],

  [anyone,"seneschal_pretalk", [], "Anything else?", "seneschal_talk",[]],


##### TODO: QUESTS COMMENT OUT BEGIN
##  [anyone|plyr,"seneschal_talk", [(check_quest_active, "qst_deliver_supply_to_center_under_siege"),
##                                  (quest_slot_eq, "qst_deliver_supply_to_center_under_siege", slot_quest_target_troop, "$g_talk_troop"),
##                                  (quest_slot_eq, "qst_deliver_supply_to_center_under_siege", slot_quest_current_state, 1),
##                                  (store_item_kind_count, ":no_supplies", "itm_siege_supply"),
##                                  (quest_get_slot, ":target_amount", "qst_deliver_supply_to_center_under_siege", slot_quest_target_amount),
##                                  (ge, ":no_supplies", ":target_amount")],
##   "TODO: Here are the supplies.", "seneschal_supplies_given",[]],
##
##  [anyone|plyr,"seneschal_talk", [(check_quest_active, "qst_deliver_supply_to_center_under_siege"),
##                                  (quest_slot_eq, "qst_deliver_supply_to_center_under_siege", slot_quest_target_troop, "$g_talk_troop"),
##                                  (quest_slot_eq, "qst_deliver_supply_to_center_under_siege", slot_quest_current_state, 1),
##                                  (store_item_kind_count, ":no_supplies", "itm_siege_supply"),
##                                  (quest_get_slot, ":target_amount", "qst_deliver_supply_to_center_under_siege", slot_quest_target_amount),
##                                  (lt, ":no_supplies", ":target_amount"),
##                                  (gt, ":no_supplies", 0)],
##   "TODO: Here are the supplies, but some of them are missing.", "seneschal_supplies_given_missing",[]],
##
##  [anyone|plyr,"seneschal_talk", [(check_quest_active, "qst_deliver_supply_to_center_under_siege"),
##                                  (quest_slot_eq, "qst_deliver_supply_to_center_under_siege", slot_quest_object_troop, "$g_talk_troop"),
##                                  (quest_slot_eq, "qst_deliver_supply_to_center_under_siege", slot_quest_current_state, 0)],
##   "TODO: Give me the supplies.", "seneschal_supplies",[]],
##
##  [anyone,"seneschal_supplies", [(store_free_inventory_capacity, ":free_inventory"),
##                                 (quest_get_slot, ":quest_target_amount", "qst_deliver_supply_to_center_under_siege", slot_quest_target_amount),
##                                 (ge, ":free_inventory", ":quest_target_amount"),
##                                 (quest_get_slot, ":quest_target_center", "qst_deliver_supply_to_center_under_siege", slot_quest_target_center),
##                                 (str_store_party_name, 0, ":quest_target_center"),
##                                 (troop_add_items, "trp_player", "itm_siege_supply", ":quest_target_amount")],
##   "TODO: Here, take these supplies. You must deliver them to {s0} as soon as possible.", "seneschal_pretalk",[(quest_set_slot, "qst_deliver_supply_to_center_under_siege", slot_quest_current_state, 1)]],
##
##  [anyone,"seneschal_supplies", [],
##   "TODO: You don't have enough space to take the supplies. Free your inventory and return back to me.", "seneschal_pretalk",[]],
##
##
##  [anyone,"seneschal_supplies_given", [],
##   "TODO: Thank you.", "seneschal_pretalk",[(party_get_slot, ":town_siege_days", "$g_encountered_party", slot_town_siege_days),
##                                            (quest_get_slot, ":target_amount", "qst_deliver_supply_to_center_under_siege", slot_quest_target_amount),
##                                            (val_sub, ":town_siege_days", ":target_amount"),
##                                            (try_begin),
##                                              (lt, ":town_siege_days", 0),
##                                              (assign, ":town_siege_days", 0),
##                                            (try_end),
##                                            (party_set_slot, "$g_encountered_party", slot_town_siege_days, ":town_siege_days"),
##                                            (troop_remove_items, "trp_player", "itm_siege_supply", ":target_amount"),
##                                            (call_script, "script_finish_quest", "qst_deliver_supply_to_center_under_siege", 100)]],
##
##  [anyone,"seneschal_supplies_given_missing", [],
##   "TODO: Thank you but it's not enough...", "seneschal_pretalk",[(store_item_kind_count, ":no_supplies", "itm_siege_supply"),
##                                                                  (quest_get_slot, ":target_amount", "qst_deliver_supply_to_center_under_siege", slot_quest_target_amount),
##                                                                  (assign, ":percentage_completed", 100),
##                                                                  (val_mul, ":percentage_completed", ":no_supplies"),
##                                                                  (val_div, ":percentage_completed", ":target_amount"),
##                                                                  (call_script, "script_finish_quest", "qst_deliver_supply_to_center_under_siege", ":percentage_completed"),
##                                                                  (party_get_slot, ":town_siege_days", "$g_encountered_party", slot_town_siege_days),
##                                                                  (val_sub, ":town_siege_days", ":no_supplies"),
##                                                                  (try_begin),
##                                                                    (lt, ":town_siege_days", 0),
##                                                                    (assign, ":town_siege_days", 0),
##                                                                  (try_end),
##                                                                  (party_set_slot, "$g_encountered_party", slot_town_siege_days, ":town_siege_days"),
##                                                                  (troop_remove_items, "trp_player", "itm_siege_supply", ":no_supplies"),
##                                                                  (call_script, "script_end_quest", "qst_deliver_supply_to_center_under_siege")]],
##
##### TODO: QUESTS COMMENT OUT END

  [anyone|plyr,"seneschal_talk", [(store_relation, ":cur_rel", "fac_player_supporters_faction", "$g_encountered_party_faction"),
                                  (ge, ":cur_rel", 0),],
   "I would like to ask you a question...", "seneschal_ask_something",[]],

  [anyone|plyr,"seneschal_talk", [(store_relation, ":cur_rel", "fac_player_supporters_faction", "$g_encountered_party_faction"),
                                  (ge, ":cur_rel", 0),],
   "I wish to know more about someone...", "seneschal_ask_about_someone",[]],

  [anyone,"seneschal_ask_about_someone", [],
   "Perhaps I may be able to help. Whom did you have in mind?", "seneschal_ask_about_someone_2",[]],

#  [anyone|plyr|repeat_for_troops,"seneschal_ask_about_someone_2", [(store_repeat_object, ":troop_no"),
#                                                                 (is_between, ":troop_no", heroes_begin, heroes_end),
#                                                                  (store_troop_faction, ":faction_no", ":troop_no"),
 #                                                                 (eq, "$g_encountered_party_faction", ":faction_no"),
 #                                                                 (str_store_troop_name, s1, ":troop_no")],
 #  "{s1}", "seneschal_ask_about_someone_3",[(store_repeat_object, "$hero_requested_to_learn_relations")]],

  [anyone|plyr,"seneschal_ask_about_someone_2", [], "Never mind.", "seneschal_pretalk",[]],

#  [anyone, "seneschal_ask_about_someone_3", [(call_script, "script_troop_write_family_relations_to_s1", "$hero_requested_to_learn_relations"),
 #                                          (call_script, "script_troop_write_owned_centers_to_s2", "$hero_requested_to_learn_relations")
#										   ],
#   "{s2}{s1}", "seneschal_ask_about_someone_4",[(add_troop_note_from_dialog, "$hero_requested_to_learn_relations", 2)]],

#  [anyone, "seneschal_ask_about_someone_relation", [(call_script, "script_troop_count_number_of_enemy_troops", "$hero_requested_to_learn_relations"),
#                                            (assign, ":no_enemies", reg0),
#                                            (try_begin),
#                                              (gt, ":no_enemies", 1),
#                                              (try_for_range, ":i_enemy", 1, ":no_enemies"),
#                                                (store_add, ":slot_no", slot_troop_enemies_begin, ":i_enemy"),
#                                                (troop_get_slot, ":cur_enemy", "$hero_requested_to_learn_relations", ":slot_no"),
#                                                (str_store_troop_name_link, s50, ":cur_enemy"),
#                                                (try_begin),
#                                                  (eq, ":i_enemy", 1),
#                                                  (troop_get_slot, ":cur_enemy", "$hero_requested_to_learn_relations", slot_troop_enemy_1),
#                                                  (str_store_troop_name_link, s51, ":cur_enemy"),
#                                                  (str_store_string, s51, "str_s50_and_s51"),
#                                                (else_try),
#                                                  (str_store_string, s51, "str_s50_comma_s51"),
#                                                (try_end),
#                                              (try_end),
#                                            (else_try),
#                                              (eq, ":no_enemies", 1),
#                                              (troop_get_slot, ":cur_enemy", "$hero_requested_to_learn_relations", slot_troop_enemy_1),
#                                              (str_store_troop_name_link, s51, ":cur_enemy"),
#                                            (else_try),
#                                              (str_store_string, s51, "str_noone"),
#                                            (try_end),
#                                            (troop_get_type, reg1, "$hero_requested_to_learn_relations")],
#   "{reg1?She:He} hates {s51}.", "seneschal_ask_about_someone_4",[(add_troop_note_from_dialog, "$hero_requested_to_learn_relations", 3)]],
# Ryan END

#  [anyone|plyr,"seneschal_ask_about_someone_4", [], "Where does {s1} stand with others?.", "seneschal_ask_about_someone_relation",[]],
#  [anyone|plyr,"seneschal_ask_about_someone_4", [], "My thanks, that was helpful.", "seneschal_pretalk",[]],


  [anyone|plyr,"seneschal_talk", [], "I must take my leave of you now. Farewell.", "close_window",[]],


  [anyone,"seneschal_ask_something", [],
   "I'll do what I can to help, of course. What did you wish to ask?", "seneschal_ask_something_2",[]],

  [anyone|plyr,"seneschal_ask_something_2", [],
   "Perhaps you know where to find someone...", "seneschal_ask_location",[]],

  [anyone,"seneschal_ask_location", [],
   "Well, a man in my position does hear a lot of things. Of whom were you thinking?", "seneschal_ask_location_2",[]],

  [anyone|plyr|repeat_for_troops,"seneschal_ask_location_2", [(store_repeat_object, ":troop_no"),
                                                              (is_between, ":troop_no", heroes_begin, heroes_end),
                                                              (store_troop_faction, ":faction_no", ":troop_no"),
                                                              (eq, "$g_encountered_party_faction", ":faction_no"),
                                                              (str_store_troop_name, s1, ":troop_no")],
   "{s1}", "seneschal_ask_location_3",[(store_repeat_object, "$hero_requested_to_learn_location")]],

  [anyone|plyr,"seneschal_ask_location_2", [], "Never mind.", "seneschal_pretalk",[]],

  [anyone,"seneschal_ask_location_3", [(call_script, "script_get_information_about_troops_position", "$hero_requested_to_learn_location", 0)],
   "{s1}", "seneschal_pretalk",[]],

#caravan merchants
  [anyone,"start",
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

  [anyone,"start",
   [(eq, "$caravan_escort_state", 1),
    (eq, "$g_encountered_party", "$caravan_escort_party_id"),
    (eq, "$talk_context", tc_party_encounter),
    ],
   "We've made it this far... Is everything clear up ahead?", "talk_caravan_escort",[]],
  [anyone|plyr,"talk_caravan_escort", [],
   "There might be bandits nearby. Stay close.", "talk_caravan_escort_2a",[]],
  [anyone,"talk_caravan_escort_2a", [],
   "Trust me, {playername}, we're already staying as close to you as we can. Lead the way.", "close_window",[(assign, "$g_leave_encounter",1)]],
  [anyone|plyr,"talk_caravan_escort", [],
   "No sign of trouble, we can breathe easy.", "talk_caravan_escort_2b",[]],
  [anyone,"talk_caravan_escort_2b", [],
   "I'll breathe easy when we reach {s1} and not a moment sooner. Let's keep moving.", "close_window",[[str_store_party_name,s1,"$caravan_escort_destination_town"],(assign, "$g_leave_encounter",1)]],

  [anyone,"start", [(eq,"$talk_context", tc_party_encounter),
                    (eq, "$g_encountered_party_type", spt_kingdom_caravan),
                    (party_slot_ge, "$g_encountered_party", slot_party_last_toll_paid_hours, "$g_current_hours"),
                    ],
   "What do you want? We paid our toll to you less than three days ago.", "merchant_talk",[]],
																#Floris Addendum for Sea traders
  [anyone,"start", [(eq,"$talk_context", tc_party_encounter),(this_or_next|eq, "$g_encountered_party_type", spt_merchant_caravan),(eq, "$g_encountered_party_type", spt_kingdom_caravan),(ge,"$g_encountered_party_relation",0)],
   "Hail, friend.", "merchant_talk",[]],

  [anyone,"start", [(eq,"$talk_context", tc_party_encounter),
                    (eq, "$g_encountered_party_type", spt_kingdom_caravan),
                    (lt,"$g_encountered_party_relation",0),
                    (eq, "$g_encountered_party_faction", "fac_merchants"),
                    ],
   "What do you want? We are but simple merchants, we've no quarrel with you, so leave us alone.", "merchant_talk",[]],

  [anyone,"start", [(eq,"$talk_context", tc_party_encounter),
                    (eq, "$g_encountered_party_type", spt_kingdom_caravan),
                    (lt,"$g_encountered_party_relation",0),
                    (faction_get_slot, ":faction_leader", "$g_encountered_party_faction",slot_faction_leader),
                    (str_store_troop_name, s9, ":faction_leader"),
                    ],
   "Be warned, knave! This caravan is under the protection of {s9}.\
 Step out of our way or you will face his fury!", "merchant_talk",[]],


  [anyone,"start", [(party_slot_eq, "$g_encountered_party", slot_party_type, spt_kingdom_caravan),(this_or_next|eq,"$talk_context", tc_party_encounter),(eq,"$talk_context", 0)],
   "Yes? What do you want?", "merchant_talk",[]],
  [anyone,"merchant_pretalk", [], "Anything else?", "merchant_talk",[]],

  [anyone|plyr,"merchant_talk", [(le,"$talk_context", tc_party_encounter),
                                 (check_quest_active, "qst_cause_provocation"),
                                 (neg|check_quest_concluded, "qst_cause_provocation"),
                                 (quest_slot_eq, "qst_cause_provocation", slot_quest_target_faction, "$g_encountered_party_faction"),
                                 (quest_get_slot, ":giver_troop", "qst_cause_provocation", slot_quest_giver_troop),
								 (store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
                                 (str_store_faction_name, s17, ":giver_troop_faction"),
                                 ],
   "You are trespassing in the territory of the {s17}. I am confiscating this caravan and all its goods!", "caravan_start_war_quest_1",[]],
  [anyone,"caravan_start_war_quest_1", [(quest_get_slot, ":giver_troop", "qst_cause_provocation", slot_quest_giver_troop),
								 (store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
                                 (str_store_faction_name, s17, ":giver_troop_faction"),
  ],
   "What? What nonsense is this? We are at peace with the {s17}, and are free to cross its lands!", "caravan_start_war_quest_2",[]],
  [anyone|plyr,"caravan_start_war_quest_2", [], "We'll see about that! Defend yourselves!", "merchant_attack",[]],
  [anyone|plyr,"caravan_start_war_quest_2", [], "Hmm. Maybe this was all a misunderstanding. Farewell.", "close_window",[(assign, "$g_leave_encounter",1)]],


  [anyone|plyr,"merchant_talk", [(le,"$talk_context", tc_party_encounter),(eq, "$g_encountered_party_faction", "$players_kingdom")], "I have an offer for you.", "merchant_talk_offer",[]],
  [anyone,"merchant_talk_offer", [], "What is it?", "merchant_talk_offer_2",[]],

  [anyone|plyr,"merchant_talk_offer_2", [(eq,"$talk_context", tc_party_encounter),(eq, "$g_encountered_party_faction", "$players_kingdom")],
   "I can escort you to your destination for a price.", "caravan_offer_protection",[]],



##  [anyone|plyr,"merchant_talk_offer_2", [(troop_slot_eq, "$g_talk_troop", slot_troop_is_prisoner, 0),
##                                 (neg|faction_slot_eq, "$g_talk_troop_faction", slot_faction_leader, "$g_talk_troop"), #he is not a faction leader!
##                                 (call_script, "script_get_number_of_hero_centers", "$g_talk_troop"),
##                                 (eq, reg0, 0), #he has no castles or towns
##                                 (hero_can_join),
##                             ],
##   "I need capable men like you. Will you join me?", "knight_offer_join",[
##       ]],

  [anyone|plyr,"merchant_talk_offer_2", [], "Nothing. Forget it", "merchant_pretalk",[]],

  [anyone|plyr,"merchant_talk", [(check_quest_active, "qst_track_down_bandits"),
  ], "I am hunting a group of bandits with the following description... Have you seen them?", "merchant_bandit_information",[]],
  [anyone,"merchant_bandit_information", [
	(call_script, "script_get_manhunt_information_to_s15", "qst_track_down_bandits"),
  ], "{s15}", "merchant_pretalk",[]],


  [anyone|plyr,"merchant_talk", [(eq,"$talk_context", tc_party_encounter), #TODO: For the moment don't let attacking if merchant has paid toll.
                                 ], "Tell me about your journey", "merchant_trip_explanation",[]],

  [anyone, "merchant_trip_explanation", [
  	  (party_get_slot, ":origin", "$g_encountered_party", slot_party_last_traded_center),
  	  (party_get_slot, ":destination", "$g_encountered_party", slot_party_ai_object),
	  (str_store_party_name, s11, ":origin"),
	  (str_store_party_name, s12, ":destination"),

	  (str_store_string, s14, "str___we_believe_that_there_is_money_to_be_made_selling_"),
      (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
	  (assign, ":at_least_one_item_found", 0),
	  (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
        (store_add, ":cur_goods_price_slot", ":cur_goods", ":item_to_price_slot"),
		(party_get_slot, ":origin_price", ":origin", ":cur_goods_price_slot"),
		(party_get_slot, ":destination_price", ":destination", ":cur_goods_price_slot"),

		(gt, ":destination_price", ":origin_price"),
		(store_sub, ":price_dif", ":destination_price", ":origin_price"),

		(gt, ":price_dif", 200),
		(str_store_item_name, s15, ":cur_goods"),
		(str_store_string, s14, "str_s14s15_"),

		(assign, ":at_least_one_item_found", 1),
	  (try_end),

	  (try_begin),
		(eq, ":at_least_one_item_found", 0),
	    (str_store_string, s14, "str__we_carry_a_selection_of_goods_although_the_difference_in_prices_for_each_is_not_so_great_we_hope_to_make_a_profit_off_of_the_whole"),
	  (else_try),
		(str_store_string, s14, "str_s14and_other_goods"),

	  (try_end),

  ], "We are coming from {s11} and heading to {s12}.{s14}", "merchant_pretalk", []],



  [anyone|plyr,"merchant_talk", [(eq,"$talk_context", tc_party_encounter), #TODO: For the moment don't let attacking if merchant has paid toll.
                                 (neg|party_slot_ge, "$g_encountered_party", slot_party_last_toll_paid_hours, "$g_current_hours"),
                                 ], "I demand something from you!", "merchant_demand",[]],
  [anyone,"merchant_demand", [(eq,"$talk_context", tc_party_encounter)], "What do you want?", "merchant_demand_2",[]],

  [anyone|plyr,"merchant_demand_2", [(neq,"$g_encountered_party_faction","$players_kingdom")], "There is a toll for free passage here!", "merchant_demand_toll",[]],

  [anyone,"merchant_demand_toll", [(gt, "$g_strength_ratio", 70),
                                        (store_div, reg6, "$g_ally_strength", 2),
                                        (val_add, reg6, 40),
                                        (assign, "$temp", reg6),
                                        ], "Please, I don't want any trouble. I can give you {reg6} denars, just let us go.", "merchant_demand_toll_2",[]],
  [anyone,"merchant_demand_toll", [(store_div, reg6, "$g_ally_strength", 4),
                                        (val_add, reg6, 10),
                                        (assign, "$temp", reg6),
                                        ], "I don't want any trouble. I can give you {reg6} denars if you'll let us go.", "merchant_demand_toll_2",[]],

  [anyone|plyr,"merchant_demand_toll_2", [], "Agreed, hand it over and you may go in peace.", "merchant_demand_toll_accept",[]],
  [anyone,"merchant_demand_toll_accept", [(assign, reg6, "$temp")], "Very well then. Here's {reg6} denars. ", "close_window",
   [(assign, "$g_leave_encounter",1),
    (call_script, "script_troop_add_gold", "trp_player", "$temp"),
    (store_add, ":toll_finish_time", "$g_current_hours", merchant_toll_duration),
    (party_set_slot, "$g_encountered_party", slot_party_last_toll_paid_hours, ":toll_finish_time"),
    (try_begin),
      (ge, "$g_encountered_party_relation", -5),
      (store_relation,":rel", "$g_encountered_party_faction","fac_player_supporters_faction"),
      (try_begin),
        (gt, ":rel", 0),
        (val_sub, ":rel", 1),
      (try_end),
      (val_sub, ":rel", 1),
      (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":rel"),
    (try_end),
### Troop commentaries changes begin
    (call_script, "script_add_log_entry", logent_caravan_accosted, "trp_player",  -1, -1, "$g_encountered_party_faction"),
### Troop commentaries changes end
    (assign, reg6, "$temp"),
    ]],

  [anyone|plyr,"merchant_demand_toll_2", [], "I changed my mind, I can't take your money.", "merchant_pretalk",[]],

  [anyone|plyr,"merchant_demand_toll_2", [], "No, I want everything you have! [Attack]", "merchant_attack",[]],

  [anyone|plyr,"merchant_demand_2", [(neq,"$g_encountered_party_faction","$players_kingdom")], "Hand over your gold and valuables now!", "merchant_attack_begin",[]],
  [anyone|plyr,"merchant_demand_2", [], "Nothing. Forget it.", "merchant_pretalk",[]],


  [anyone,"merchant_attack_begin", [], "Are you robbing us?{s11}", "merchant_attack_verify",[
  (str_clear, s11),
  (try_begin),
	(faction_slot_ge, "$g_encountered_party_faction", slot_faction_truce_days_with_factions_begin, 1),
	(str_store_string, s11, "str__have_you_not_signed_a_truce_with_our_lord"),
  (try_end),
  ]],
  [anyone|plyr,"merchant_attack_verify", [], "Robbing you? No, no! It was a joke.", "merchant_attack_verify_norob",[]],
  [anyone,"merchant_attack_verify_norob", [], "God, don't joke about that, {lad/lass}. For a moment I thought we were in real trouble.", "close_window",[(assign, "$g_leave_encounter",1)]],
  [anyone|plyr,"merchant_attack_verify", [], "Of course I'm robbing you. Now hand over your goods.", "merchant_attack",[
	(call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
  ]],

  [anyone,"merchant_attack", [], "Damn you, you won't get anything from us without a fight!", "close_window",
   [(store_relation,":rel", "$g_encountered_party_faction","fac_player_supporters_faction"),
    (try_begin),
      (gt, ":rel", 0),
      (val_sub, ":rel", 10),
    (try_end),
    (val_sub, ":rel", 5),
    (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":rel"),
### Troop commentaries changes begin
	(call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
### Troop commentaries changes end
##Floris - Bugfix for Native failure to set parties hostile
    (assign,"$encountered_party_hostile",1),
    (assign,"$encountered_party_friendly",0),
##Floris - Bugfix end
    ]],

  [anyone,"caravan_offer_protection", [],
   "These roads are dangerous indeed. One can never have enough protection.", "caravan_offer_protection_2",
   [(get_party_ai_object,":caravan_destination","$g_encountered_party"),
    (store_distance_to_party_from_party, "$caravan_distance_to_target",":caravan_destination","$g_encountered_party"),
    (assign,"$caravan_escort_offer","$caravan_distance_to_target"),
    (val_sub, "$caravan_escort_offer", 10),
    (call_script, "script_party_calculate_strength", "p_main_party", 0),
    (assign, ":player_strength", reg0),
    (val_min, ":player_strength", 200),
    (val_add, ":player_strength", 20),
    (val_mul,"$caravan_escort_offer",":player_strength"),
    (val_div,"$caravan_escort_offer",50),
    (val_max, "$caravan_escort_offer", 5),
    ]],
  [anyone,"caravan_offer_protection_2", [[lt,"$caravan_distance_to_target",10]],
   "An escort? We're almost there already! Thank you for the offer, though.", "close_window",[(assign, "$g_leave_encounter",1)]],
  [anyone,"caravan_offer_protection_2", [(get_party_ai_object,":caravan_destination","$g_encountered_party"),
    (str_store_party_name,1,":caravan_destination"),
    (assign,reg(2),"$caravan_escort_offer")],
   "We are heading to {s1}. I will pay you {reg2} denars if you escort us there.", "caravan_offer_protection_3",
   []],
  [anyone|plyr,"caravan_offer_protection_3", [],
   "Agreed.", "caravan_offer_protection_4",[]],
  [anyone,"caravan_offer_protection_4", [],
   "I want you to stay close to us along the way.\
 We'll need your help if we get ambushed by bandits.", "caravan_offer_protection_5",[]],
  [anyone|plyr,"caravan_offer_protection_5", [],
   "Don't worry, you can trust me.", "caravan_offer_protection_6",[]],
  [anyone,"caravan_offer_protection_6", [(get_party_ai_object,":caravan_destination","$g_encountered_party"),
    (str_store_party_name,1,":caravan_destination")],
   "Good. Come and collect your money when we're within sight of {s1}. For now, let's just get underway.", "close_window",
   [(get_party_ai_object,":caravan_destination","$g_encountered_party"),
    (assign, "$caravan_escort_destination_town", ":caravan_destination"),
    (assign, "$caravan_escort_party_id", "$g_encountered_party"),
    (assign, "$caravan_escort_agreed_reward", "$caravan_escort_offer"),
    (assign, "$caravan_escort_state", 1),
    (assign, "$g_leave_encounter",1)
   ]],
  [anyone|plyr,"caravan_offer_protection_3", [],
   "Forget it.", "caravan_offer_protection_4b",[]],
  [anyone,"caravan_offer_protection_4b", [],
   "Perhaps another time, then.", "close_window",[(assign, "$g_leave_encounter",1)]],

  [anyone|plyr,"merchant_talk", [(eq,"$talk_context", tc_party_encounter),(lt, "$g_talk_troop_faction_relation", 0)],
   "Not so fast. First, hand over all your goods and money.", "talk_caravan_enemy_2",[]],

  [anyone,"talk_caravan_enemy_2", [],
   "Never. It is our duty to protect these goods. You shall have to fight us, brigand!", "close_window",
   [
    (store_relation,":rel","$g_encountered_party_faction","fac_player_supporters_faction"),
    (val_min,":rel",0),
    (val_sub,":rel",4),
    (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":rel"),
	(call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
    ]],

  [anyone|plyr,"merchant_talk", [], "[Leave]", "close_window",[(assign, "$g_leave_encounter",1)]],




# Prison Guards
  [anyone,"start", [(eq, "$talk_context", 0),(faction_slot_eq, "$g_encountered_party_faction", slot_faction_prison_guard_troop, "$g_talk_troop"),
					##diplomacy start+ Handle player is co-ruler of NPC kingdom
					(assign, ":is_coruler", 0),
					(try_begin),
						(eq, "$g_encountered_party_faction", "$players_kingdom"),
						(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
						(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
						(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
						(assign, ":is_coruler", 1),
					(try_end),
					(this_or_next|eq, ":is_coruler", 1),
					##diplomacy end+
                    (this_or_next|eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
                    (             party_slot_eq, "$g_encountered_party", slot_town_lord, "trp_player"),
					##diplomacy start+
					#it may be appropriate to use "your highness" instead of "my {lord/lady}"
					(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),#added
                    ],
   "Good day, {s0}. Will you be visiting the prison?", "prison_guard_players",[]],#changed "my {lord/lady}" to "{s0}"
   ##diplomacy end+
  [anyone|plyr,"prison_guard_players", [],
   "Yes. Unlock the door.", "close_window",[(call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle")]],
  [anyone|plyr,"prison_guard_players", [],
   "No, not now.", "close_window",[]],

  [anyone,"start", [(eq, "$talk_context", 0),(faction_slot_eq, "$g_encountered_party_faction", slot_faction_prison_guard_troop, "$g_talk_troop")],
   "Yes? What do you want?", "prison_guard_talk",[]],

  [anyone|plyr,"prison_guard_talk", [],
   "Who is imprisoned here?", "prison_guard_ask_prisoners",[]],
  [anyone|plyr,"prison_guard_talk", [],
   "I want to speak with a prisoner.", "prison_guard_visit_prison",[]],

##diplomacy begin
  [anyone|plyr,"prison_guard_talk", [
    (party_slot_eq, "$g_encountered_party", slot_town_lord, "trp_player"),
    ],
   "I want to release a prisoner.", "dplmc_prison_guard_talk_ask_prisoner",[]],

  [anyone,"dplmc_prison_guard_talk_ask_prisoner",
   [],
   "Alright, which prisoner shall I set free?", "dplmc_prison_guard_talk_prisoner_select",[
 ]],

  ##select enemy prisoner
 [anyone|plyr|repeat_for_troops, "dplmc_prison_guard_talk_prisoner_select",
   [
     (store_repeat_object, ":troop_no"),
     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
     (troop_get_slot, ":party", ":troop_no", slot_troop_prisoner_of_party),
     (eq, ":party", "$g_encountered_party"),
     (str_store_troop_name, s10, ":troop_no"),
     (store_faction_of_troop, ":faction_no", ":troop_no"),
     (str_store_faction_name, s11, ":faction_no"),
     ],
   "{s10} of {s11}.", "dplmc_prison_guard_exchange_prisoner_ask_confirm",
   [
     (store_repeat_object, "$diplomacy_var"),
     (store_faction_of_troop, "$g_faction_selected", "$diplomacy_var"),
     ]],

  [anyone|plyr,"dplmc_prison_guard_talk_prisoner_select", [],
   "No one.", "close_window",
   [
   ]],

  [anyone,"dplmc_prison_guard_exchange_prisoner_ask_confirm",
   [
     (str_store_troop_name, s10, "$diplomacy_var"),
     (store_faction_of_troop, ":faction_no", "$diplomacy_var"),
     (str_store_faction_name, s11, ":faction_no"),
   ],
   "As you wish, I will release {s10} of {s11}.", "dplmc_prison_guard_exchange_prisoner_confirm",[
 ]],

  [anyone|plyr,"dplmc_prison_guard_exchange_prisoner_confirm", [],
   "Very well.", "close_window",
   [
      (party_remove_prisoners, "$g_encountered_party", "$diplomacy_var", 1),
      (call_script, "script_remove_troop_from_prison", "$diplomacy_var"),
      (str_store_troop_name, s7, "$diplomacy_var"),
      (display_message, "str_dplmc_has_been_set_free"),
      (call_script, "script_change_player_relation_with_troop", "$diplomacy_var", 3),
      (call_script, "script_change_player_honor", 1),
      (call_script, "script_update_troop_notes", "$diplomacy_var"),
   ]],

  [anyone|plyr,"dplmc_prison_guard_exchange_prisoner_confirm", [],
   "No, I changed my mind.", "close_window",[]],
##diplomacy end
  [anyone,"prison_guard_ask_prisoners", [],
   "Currently, {s50} {reg1?are:is} imprisoned here.{s49}","prison_guard_talk",[
    (party_clear, "p_temp_party"),
	(party_clear, "p_temp_party_2"),
    (assign, ":num_heroes_in_dungeon", 0),
    (assign, ":num_heroes_given_parole", 0),

    (party_get_num_prisoner_stacks, ":num_stacks","$g_encountered_party"),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_prisoner_stack_get_troop_id, ":stack_troop","$g_encountered_party",":i_stack"),
        (troop_is_hero, ":stack_troop"),
		(try_begin),
			(call_script, "script_cf_prisoner_offered_parole", ":stack_troop"),
			(party_add_members, "p_temp_party_2", ":stack_troop", 1),
			(val_add, ":num_heroes_given_parole", 1),
		(else_try),
			(party_add_members, "p_temp_party", ":stack_troop", 1),
			(val_add, ":num_heroes_in_dungeon", 1),
		(try_end),
    (try_end),
    (call_script, "script_print_party_members", "p_temp_party"),
	(str_store_string, s50, "str_s51"),
    (try_begin),
        (gt, ":num_heroes_in_dungeon", 1),
        (assign, reg1, 1),
    (else_try),
        (assign, reg1, 0),
    (try_end),

	(str_clear, s49),
    (try_begin),
        (ge, ":num_heroes_given_parole", 1),
		(call_script, "script_print_party_members", "p_temp_party_2"),
		(try_begin),
			(ge, ":num_heroes_given_parole", 2),
			(assign, reg2, 1),
		(else_try),
			(assign, reg2, 0),
		(try_end),
		(str_store_string, s49, "str__meanwhile_s51_reg2areis_being_held_in_the_castle_but_reg2havehas_made_pledges_not_to_escape_and_reg2areis_being_held_in_more_comfortable_quarters" ), #somewhat awkward wording prevents both gender and singular/plural pronoun issues
    (try_end)


	]],

  [anyone,"prison_guard_visit_prison",
  [
    (this_or_next|faction_slot_eq, "$g_encountered_party_faction", slot_faction_marshall, "trp_player"),
    (this_or_next|party_slot_eq, "$g_encountered_party", slot_town_lord, "trp_player"),
    (eq, "$g_encountered_party_faction", "$players_kingdom"),
  ],
   "Of course, {sir/madam}. Go in.", "close_window",
   [
     (call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle")
   ]],

  [anyone, "prison_guard_visit_prison",
  [
    #below condition is added by ozan, please lets discuss if it is needed or not. But I think this condition is needed because if there is nobody in prison
    #prison guard should not say you need to get permission, or take me money ext to let player go inside.
    (assign, ":num_heroes_in_dungeon", 0),
    (party_get_num_prisoner_stacks, ":num_stacks", "$g_encountered_party"),
    (assign, ":end_condition", ":num_stacks"),
    (try_for_range, ":i_stack", 0, ":end_condition"),
      (party_prisoner_stack_get_troop_id, ":stack_troop","$g_encountered_party",":i_stack"),
      (troop_is_hero, ":stack_troop"),
      (try_begin),
        (call_script, "script_cf_prisoner_offered_parole", ":stack_troop"),
      (else_try),
        (val_add, ":num_heroes_in_dungeon", 1),
        (assign, ":end_condition", 0),
      (try_end),
    (try_end),

    (ge, ":num_heroes_in_dungeon", 1),
   ],
   "You need to get permission from the lord to talk to prisoners.", "prison_guard_visit_prison_2",[]],

  [anyone, "prison_guard_visit_prison", [], "There is nobody inside, therefore you can freely go inside and look around.", "prison_guard_visit_prison_nobody", []],

  [anyone|plyr,"prison_guard_visit_prison_nobody", [], "All right then. I'll take a look at the prison.", "close_window",
  [
    (call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle"),
  ]],

  [anyone|plyr,"prison_guard_visit_prison_nobody", [], "I have more important business to do.", "close_window",[]],

  [anyone|plyr,"prison_guard_visit_prison_2", [], "All right then. I'll try that.", "close_window",[]],
  [anyone|plyr,"prison_guard_visit_prison_2", [], "Come on now. I thought you were the boss here.", "prison_guard_visit_prison_3",[]],
  [anyone,"prison_guard_visit_prison_3", [], "He-heh. You got that right. Still, I can't let you into the prison.", "prison_guard_visit_prison_4",[]],

  [anyone|plyr,"prison_guard_visit_prison_4", [], "All right then. I'll leave now.", "close_window",[]],
  [anyone|plyr,"prison_guard_visit_prison_4", [(store_troop_gold,":gold","trp_player"),(ge,":gold",100)],
   "I found a purse with 100 denars a few paces away. I reckon it belongs to you.", "prison_guard_visit_prison_5",[]],

  [anyone,"prison_guard_visit_prison_5", [], "Ah! I was looking for this all day. How good of you to bring it back {sir/madam}.\
 Well, now that I know what an honest {man/lady} you are, there can be no harm in letting you inside for a look. Go in.... Just so you know, though -- I'll be hanging onto the keys, in case you were thinking about undoing anyone's chains.", "close_window",
 [(troop_remove_gold, "trp_player",100),(call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle")]],

  [anyone|plyr,"prison_guard_visit_prison_4", [],
   "Give me the keys to the cells -- now!", "prison_guard_visit_break",[
   ]],

  [anyone,"prison_guard_visit_break", [], "Help! Help! Prison break!", "close_window",[
  (call_script, "script_activate_town_guard"),
  (assign, "$g_main_attacker_agent", "$g_talk_agent"),
  (assign, "$talk_context", tc_prison_break),
#  (try_begin),
#		(store_relation, ":relation", "fac_player_faction", "$g_encountered_party_faction"),
#	Reduce relation with town
# (try_end),

	 (assign, ":end_cond", kingdom_ladies_end),
     (try_for_range, ":prisoner", active_npcs_begin, ":end_cond"),
	   (troop_set_slot, ":prisoner", slot_troop_mission_participation, 0), #new
	 (try_end),
  ]],


  [anyone|plyr,"prison_guard_talk", [],
   "Never mind.", "close_window",[]],




# Castle Guards
  [anyone,"start", [(eq, "$talk_context", 0),(faction_slot_eq, "$g_encountered_party_faction", slot_faction_castle_guard_troop, "$g_talk_troop"),
  					##diplomacy start+ Handle player is co-ruler of NPC kingdom
					(assign, ":is_coruler", 0),
					(try_begin),
						(eq, "$g_encountered_party_faction", "$players_kingdom"),
						(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
						(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
						(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
						(assign, ":is_coruler", 1),#ruler or co-ruler of faction
					(try_end),
					(this_or_next|eq, ":is_coruler", 1),
					##diplomacy end+
                    (this_or_next|eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
                    (             party_slot_eq, "$g_encountered_party", slot_town_lord, "trp_player")
                    ],
   "Your orders, {Lord/Lady}?", "castle_guard_players",[]],
  [anyone|plyr,"castle_guard_players", [],
   "Open the door. I'll go in.", "close_window",[(call_script, "script_enter_court", "$current_town")]],
  [anyone|plyr,"castle_guard_players", [],
   "Never mind.", "close_window",[]],


  [anyone,"start", [(eq, "$talk_context", 0),(faction_slot_eq, "$g_encountered_party_faction", slot_faction_castle_guard_troop, "$g_talk_troop"),(eq, "$sneaked_into_town",1),
                    (gt,"$g_time_since_last_talk",0)],
   "Get out of my sight, beggar! You stink!", "castle_guard_sneaked_intro_1",[]],
  [anyone,"start", [(eq, "$talk_context", 0),(faction_slot_eq, "$g_encountered_party_faction", slot_faction_castle_guard_troop, "$g_talk_troop"),(eq, "$sneaked_into_town",1)],
   "Get lost before I lose my temper you vile beggar!", "close_window",[]],
  [anyone|plyr,"castle_guard_sneaked_intro_1", [], "I want to enter the hall and speak to the lord.", "castle_guard_sneaked_intro_2",[]],
  [anyone|plyr,"castle_guard_sneaked_intro_1", [], "[Leave]", "close_window",[]],
  [anyone,"castle_guard_sneaked_intro_2", [], "Are you out of your mind, {man/woman}?\
 Beggars are not allowed into the hall. Now get lost or I'll beat you bloody.", "close_window",[]],


  [anyone,"start", [(eq, "$talk_context", 0),(faction_slot_eq, "$g_encountered_party_faction", slot_faction_castle_guard_troop, "$g_talk_troop")],
   "What do you want?", "castle_guard_intro_1",[]],
  [anyone|plyr,"castle_guard_intro_1", [],
   "I want to enter the hall and speak to the lord.", "castle_guard_intro_2",[]],
  [anyone|plyr,"castle_guard_intro_1", [],
   "Never mind.", "close_window",[]],

   [anyone,"castle_guard_intro_2", [
	(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
	(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$current_town"),

	(this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
		(neg|troop_slot_ge, "trp_player", slot_troop_renown, 50),

	(neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
	(neq, "$g_player_eligible_feast_center_no", "$current_town"),

	(neg|check_quest_active, "qst_wed_betrothed"),
	(neg|check_quest_active, "qst_wed_betrothed_female"),

	(neg|troop_slot_ge, "trp_player", slot_troop_spouse, 1), #Married players always make the cut

   ], "I'm afraid there is a feast in progress, and you are not invited.", "close_window",
   []],


   [anyone,"castle_guard_intro_2", [], "You can go in after leaving your weapons with me. No one is allowed to carry arms into the lord's hall.", "castle_guard_intro_3",
   []],

  [anyone|plyr,"castle_guard_intro_3", [], "Here, take my arms. I'll go in.", "close_window", [(call_script, "script_enter_court", "$current_town")]],

  [anyone|plyr,"castle_guard_intro_3", [], "No, I give my arms to no one.", "castle_guard_intro_2b", []],
  [anyone,"castle_guard_intro_2b", [], "Then you can't go in.", "close_window", []],

##  [anyone|plyr,"castle_guard_intro_1", [],
##   "Never mind.", "close_window",[]],
##  [anyone,"castle_guard_intro_2", [],
##   "Does the lord expect you?", "castle_guard_intro_3",[]],
##  [anyone|plyr,"castle_guard_intro_3", [], "Yes.", "castle_guard_intro_check",[]],
##  [anyone|plyr,"castle_guard_intro_3", [], "No.", "castle_guard_intro_no",[]],
##  [anyone,"castle_guard_intro_check", [], "Hmm. All right {sir/madam}.\
## You can go in. But you must leave your weapons with me. Noone's allowed into the court with weapons.", "close_window",[]],
##  [anyone,"castle_guard_intro_check", [], "You liar!\
## Our lord would have no business with a filthy vagabond like you. Get lost now before I kick your butt.", "close_window",[]],
##  [anyone,"castle_guard_intro_no", [], "Well... What business do you have here then?", "castle_guard_intro_4",[]],
##  [anyone|plyr,"castle_guard_intro_4", [], "I wish to present the lord some gifts.", "castle_guard_intro_gifts",[]],
##  [anyone|plyr,"castle_guard_intro_4", [], "I have an important matter to discuss with the lord. Make way now.", "castle_guard_intro_check",[]],
##  [anyone,"castle_guard_intro_gifts", [], "Really? What gifts?", "castle_guard_intro_5",[]],
##  [anyone|plyr,"castle_guard_intro_4", [], "Many gifts. For example, I have a gift of 20 denars here for his loyal servants.", "castle_guard_intro_gifts",[]],
##  [anyone|plyr,"castle_guard_intro_4", [], "My gifts are of no concern to you. They are for your lords and ladies..", "castle_guard_intro_check",[]],
##  [anyone,"castle_guard_intro_gifts", [], "Oh! you can give those 20 denars to me. I can distribute them for you.\
## You can enter the court and present your gifts to the lord. I'm sure he'll be pleased.\
## But you must leave your weapons with me. Noone's allowed into the court with weapons.", "close_window",[]],

#Kingdom Parties
#  [anyone,"start", [(this_or_next|eq,"$g_encountered_party_template","pt_swadian_foragers"),
#                    (eq,"$g_encountered_party_template","pt_vaegir_foragers"),
##  [anyone,"start", [(this_or_next|party_slot_eq,"$g_encountered_party",slot_party_type, spt_forager),
##                    (this_or_next|party_slot_eq,"$g_encountered_party",slot_party_type, spt_scout),
##                    (party_slot_eq,"$g_encountered_party",slot_party_type, spt_patrol),
##                    (str_store_faction_name,5,"$g_encountered_party_faction")],
##   "In the name of the {s5}.", "kingdom_party_encounter",[]],
##
##  [anyone,"kingdom_party_encounter", [(le,"$g_encountered_party_relation",-10)],
##   "Surrender now, and save yourself the indignity of defeat!", "kingdom_party_encounter_war",[]],
##  [anyone|plyr,"kingdom_party_encounter_war", [],  "[Go to Battle]", "close_window",[(encounter_attack)]],
##
##  [anyone,"kingdom_party_encounter", [(ge,"$g_encountered_party_relation",10)],
##   "Greetings, fellow warrior.", "close_window",[(eq,"$talk_context",tc_party_encounter),(assign, "$g_leave_encounter", 1)]],
##
##  [anyone,"kingdom_party_encounter", [],
##   "You can go.", "close_window",[]],








#Player Parties
##  [party_tpl|pt_old_garrison,"start", [],
##   "They told us to leave the castle to the new garrison {sir/madam}. So we left and came to rejoin you.", "player_old_garrison_encounter",[]],
##
##  [anyone|plyr,"player_old_garrison_encounter", [(party_can_join)],
##   "You have done well. You'll join my command now.", "close_window",[(assign, "$g_move_heroes", 1),
##                                        (call_script, "script_party_add_party", "p_main_party", "$g_encountered_party"),
##                                        (remove_party, "$g_encountered_party"),
##                                        (assign, "$g_leave_encounter", 1)]],
##  [anyone|plyr,"player_old_garrison_encounter", [(assign, reg1, 0),
##                                                 (try_begin),
##                                                   (neg|party_can_join),
##                                                   (assign, reg1, 1),
##                                                 (try_end)],
##   "You can't join us now{reg1?, I can't command all the lot of you:}. Follow our lead.", "close_window",[(party_set_ai_behavior, "$g_encountered_party", ai_bhvr_attack_party),
##                                                                         (party_set_ai_object, "$g_encountered_party", "p_main_party"),
##                                                                         (party_set_flags, "$g_encountered_party", pf_default_behavior, 0),
##                                                                         (assign, "$g_leave_encounter", 1)]],
##
##  [anyone|plyr,"player_old_garrison_encounter", [(assign, reg1, 0),
##                                                 (try_begin),
##                                                   (neg|party_can_join),
##                                                   (assign, reg1, 1),
##                                                 (try_end)],
##   "You can't join us now{reg1?, I can't command all the lot of you:}. Stay here and wait for me.", "close_window",[
##       (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_travel_to_point),
##       (party_get_position, pos1, "$g_encountered_party"),
##       (party_set_ai_target_position, "$g_encountered_party", pos1),
##       (party_set_flags, "$g_encountered_party", pf_default_behavior, 0),
##       (assign, "$g_leave_encounter", 1)]],
##






  [anyone,"start", [(eq, "$talk_context", tc_castle_gate)],
   "What do you want?", "castle_gate_guard_talk",[]],

  [anyone,"castle_gate_guard_pretalk", [],
   "Yes?", "castle_gate_guard_talk",[]],

  [anyone|plyr,"castle_gate_guard_talk", [(ge, "$g_encountered_party_relation", 0)],
  "We need shelter for the night. Will you let us in?", "castle_gate_open",[]],
  [anyone|plyr,"castle_gate_guard_talk", [(party_slot_ge, "$g_encountered_party", slot_town_lord, 1)], "I want to speak with the lord of the castle.", "request_meeting_castle_lord",[]],
  [anyone|plyr,"castle_gate_guard_talk", [], "I want to speak with someone in the castle.", "request_meeting_other",[]],

  [anyone|plyr,"castle_gate_guard_talk", [], "[Leave]", "close_window",[]],

  [anyone,"request_meeting_castle_lord", [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
                                         (call_script, "script_get_troop_attached_party", ":castle_lord"),
                                         (eq, "$g_encountered_party", reg0),
                                         (str_store_troop_name, s2, ":castle_lord"),
                                         (assign, "$lord_requested_to_talk_to", ":castle_lord"),
                                          ],  "Wait here. {s2} will see you.", "close_window",[]],

  [anyone,"request_meeting_castle_lord", [],  "My lord is not here now.", "castle_gate_guard_pretalk",[]],

  [anyone,"request_meeting_other", [],  "Who is that?", "request_meeting_3",[]],

  [anyone|plyr|repeat_for_troops,"request_meeting_3", [(store_repeat_object, ":troop_no"),
                                                       (troop_is_hero, ":troop_no"),
                                                       (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
                                                       (call_script, "script_get_troop_attached_party", ":troop_no"),
                                                       (eq, "$g_encountered_party", reg0),
                                                       (str_store_troop_name, s3, ":troop_no"),
                                                       ],
   "{s3}", "request_meeting_4",[(store_repeat_object, "$lord_requested_to_talk_to")]],

  [anyone|plyr,"request_meeting_3", [], "Never mind.", "close_window",[(assign, "$lord_requested_to_talk_to", 0)]],

  [anyone,"request_meeting_4", [##diplomacy start+ correct pronoun
  (call_script, "script_dplmc_store_troop_is_female",  "$lord_requested_to_talk_to"),
	], "Wait there. I'll send {reg0?her:him} your request.", "request_meeting_5",[]],#"him" to "{reg0?her:him}"
	##diplomacy end+

  [anyone|plyr,"request_meeting_5", [], "I'm waiting...", "request_meeting_6",[]],

  [anyone,"request_meeting_6",
   [
     (call_script, "script_troop_get_player_relation", "$lord_requested_to_talk_to"),
     (assign, ":lord_relation", reg0),
     (gt, ":lord_relation", -20),
    ], "All right. {s2} will talk to you now.", "close_window",[(str_store_troop_name, s2, "$lord_requested_to_talk_to")]],

  [anyone,"request_meeting_6", [(str_store_troop_name, s2, "$lord_requested_to_talk_to"),
  ##diplomacy start+ correct pronoun
  (call_script, "script_dplmc_store_troop_is_female",  "$lord_requested_to_talk_to"),
  ], "{s2} says {reg0?she:he} will not see you. Begone now.", "close_window",[]],#"he" to "{reg0?she:he}"
  ##diplomacy end+

  [anyone,"castle_gate_open", [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
                                         (call_script, "script_get_troop_attached_party", ":castle_lord"),
                                         (eq, "$g_encountered_party", reg0),
                                         (ge, "$g_encountered_party_relation", 0),
                                         (call_script, "script_troop_get_player_relation", ":castle_lord"),
                                         (assign, ":castle_lord_relation", reg0),
                                         #(troop_get_slot, ":castle_lord_relation", ":castle_lord", slot_troop_player_relation),
                                         (ge, ":castle_lord_relation", 5),
                                         (str_store_troop_name, s2, ":castle_lord")
                                         ],  "My lord {s2} will be happy to see you {sir/madam}.\
 Come on in. I am opening the gates for you.", "close_window",[(assign,"$g_permitted_to_center",1)]],


  [anyone,"castle_gate_open", [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
                                         (call_script, "script_get_troop_attached_party", ":castle_lord"),
                                         (neq, "$g_encountered_party", reg0),
                                         (ge, "$g_encountered_party_relation", 0),
                                         (call_script, "script_troop_get_player_relation", ":castle_lord"),
                                         (assign, ":castle_lord_relation", reg0),
                                         #(troop_get_slot, ":castle_lord_relation", ":castle_lord", slot_troop_player_relation),
                                         (ge, ":castle_lord_relation", 5),
                                         (str_store_troop_name, s2, ":castle_lord")
                                         ],  "My lord {s2} is not in the castle now.\
 But I think he would approve of you taking shelter here.\
 Come on in. I am opening the gates for you.", "close_window",[(assign,"$g_permitted_to_center",1)]],

  [anyone,"castle_gate_open", [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
                               (call_script, "script_troop_get_player_relation", ":castle_lord"),
                               (assign, ":castle_lord_relation", reg0),
                               #(troop_get_slot, ":castle_lord_relation", ":castle_lord", slot_troop_player_relation),
                               (ge, ":castle_lord_relation", -2),
                                         ],  "Come on in. I am opening the gates for you.", "close_window",[(assign,"$g_permitted_to_center",1)]],

  [anyone,"castle_gate_open", [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
                               (call_script, "script_troop_get_player_relation", ":castle_lord"),
                               (assign, ":castle_lord_relation", reg0),
                               #(troop_get_slot, ":castle_lord_relation", ":castle_lord", slot_troop_player_relation),
                               (ge, ":castle_lord_relation", -19),
                               (str_store_troop_name, s2, ":castle_lord")
                                         ],  "Come on in. But make sure your men behave sensibly within the walls.\
 My lord {s2} does not want trouble here.", "close_window",[(assign,"$g_permitted_to_center",1)]],

  [anyone,"castle_gate_open", [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
                               (str_store_troop_name, s2, ":castle_lord"),
  ],  "My lord {s2} does not want you here. Begone now.", "close_window",[]],


#Enemy Kingdom Meetings


#  [anyone,"start", [(eq, "$talk_context", tc_lord_talk_in_center)],
#   "Greetings {playername}.", "request_meeting_1",[]],

#  [anyone,"request_meeting_pretalk", [(eq, "$talk_context", tc_lord_talk_in_center)],
#   "Yes?", "request_meeting_1",[]],

#  [anyone|plyr,"request_meeting_1", [(ge, "$g_encountered_party_faction", 0)], "Open the gates and let me in!", "request_meeting_open_gates",[]],

#  [anyone|plyr,"request_meeting_1", [(party_slot_ge, "$g_encountered_party", slot_town_lord, 1)], "I want to speak with the lord of the castle.", "request_meeting_castle_lord",[]],
#  [anyone|plyr,"request_meeting_1", [], "I want to speak with someone in the castle.", "request_meeting_other",[]],

##### TODO: QUESTS COMMENT OUT BEGIN
##  [anyone|plyr,"request_meeting_1",[(check_quest_active,"qst_bring_prisoners_to_enemy"),
##                                    (neg|check_quest_succeeded, "qst_bring_prisoners_to_enemy"),
##                                    (quest_get_slot, ":quest_giver_troop", "qst_bring_prisoners_to_enemy", slot_quest_giver_troop),
##                                    (quest_get_slot, ":quest_target_amount", "qst_bring_prisoners_to_enemy", slot_quest_target_amount),
##                                    (quest_get_slot, ":quest_object_troop", "qst_bring_prisoners_to_enemy", slot_quest_object_troop),
##                                    (quest_slot_eq, "qst_bring_prisoners_to_enemy", slot_quest_target_center, "$g_encountered_party"),
##                                    (party_count_prisoners_of_type, ":num_prisoners", "p_main_party", ":quest_object_troop"),
##                                    (ge, ":num_prisoners", ":quest_target_amount"),
##                                    (str_store_troop_name,1,":quest_giver_troop"),
##                                    (assign, reg1, ":quest_target_amount"),
##                                    (str_store_troop_name_plural,2,":quest_object_troop")],
##   "TODO: Sir, lord {s1} ordered me to bring {reg1} {s2} for ransom.", "guard_prisoners_brought",
##   [(quest_get_slot, ":quest_target_amount", "qst_bring_prisoners_to_enemy", slot_quest_target_amount),
##    (quest_get_slot, ":quest_target_center", "qst_bring_prisoners_to_enemy", slot_quest_target_center),
##    (quest_get_slot, ":quest_object_troop", "qst_bring_prisoners_to_enemy", slot_quest_object_troop),
##    (party_remove_prisoners, "p_main_party", ":quest_object_troop", ":quest_target_amount"),
##    (party_add_members, ":quest_target_center", ":quest_object_troop", ":quest_target_amount"),
##    (call_script, "script_game_get_join_cost", ":quest_object_troop"),
##    (assign, ":reward", reg0),
##    (val_mul, ":reward", ":quest_target_amount"),
##    (val_div, ":reward", 2),
##    (call_script, "script_troop_add_gold", "trp_player", ":reward"),
##    (party_get_slot, ":cur_lord", "$g_encountered_party", slot_town_lord),#Removing gold from the town owner's wealth
##    (troop_get_slot, ":cur_wealth", ":cur_lord", slot_troop_wealth),
##    (val_sub, ":cur_wealth", ":reward"),
##    (troop_set_slot, ":cur_lord", slot_troop_wealth, ":cur_wealth"),
##    (quest_set_slot, "qst_bring_prisoners_to_enemy", slot_quest_target_amount, ":reward"),
##    (succeed_quest, "qst_bring_prisoners_to_enemy"),
##    ]],
##
##  [anyone|plyr,"request_meeting_1",[(check_quest_active,"qst_bring_prisoners_to_enemy"),
##                                    (neg|check_quest_succeeded, "qst_bring_prisoners_to_enemy"),
##                                    (quest_get_slot, ":quest_giver_troop", "qst_bring_prisoners_to_enemy", slot_quest_giver_troop),
##                                    (quest_get_slot, ":quest_target_amount", "qst_bring_prisoners_to_enemy", slot_quest_target_amount),
##                                    (quest_get_slot, ":quest_object_troop", "qst_bring_prisoners_to_enemy", slot_quest_object_troop),
##                                    (quest_slot_eq, "qst_bring_prisoners_to_enemy", slot_quest_target_center, "$g_encountered_party"),
##                                    (party_count_prisoners_of_type, ":num_prisoners", "p_main_party", ":quest_object_troop"),
##                                    (lt, ":num_prisoners", ":quest_target_amount"),
##                                    (gt, ":num_prisoners", 0),
##                                    (str_store_troop_name,1,":quest_giver_troop"),
##                                    (assign, reg1, ":quest_target_amount"),
##                                    (str_store_troop_name_plural,2,":quest_object_troop")],
##   "TODO: Sir, lord {s1} ordered me to bring {reg1} {s2} for ransom, but some of them died during my expedition.", "guard_prisoners_brought_some",
##   [(quest_get_slot, ":quest_target_amount", "qst_bring_prisoners_to_enemy", slot_quest_target_amount),
##    (quest_get_slot, ":quest_target_center", "qst_bring_prisoners_to_enemy", slot_quest_target_center),
##    (quest_get_slot, ":quest_object_troop", "qst_bring_prisoners_to_enemy", slot_quest_object_troop),
##    (party_count_prisoners_of_type, ":num_prisoners", "p_main_party", ":quest_object_troop"),
##    (party_remove_prisoners, "p_main_party", ":quest_object_troop", ":num_prisoners"),
##    (party_add_members, ":quest_target_center", ":quest_object_troop", ":num_prisoners"),
##    (call_script, "script_game_get_join_cost", ":quest_object_troop"),
##    (assign, ":reward", reg0),
##    (val_mul, ":reward", ":num_prisoners"),
##    (val_div, ":reward", 2),
##    (call_script, "script_troop_add_gold", "trp_player", ":reward"),
##    (party_get_slot, ":cur_lord", "$g_encountered_party", slot_town_lord),#Removing gold from the town owner's wealth
##    (troop_get_slot, ":cur_wealth", ":cur_lord", slot_troop_wealth),
##    (val_sub, ":cur_wealth", ":reward"),
##    (troop_set_slot, ":cur_lord", slot_troop_wealth, ":cur_wealth"),
##    (call_script, "script_game_get_join_cost", ":quest_object_troop"),
##    (assign, ":reward", reg0),
##    (val_mul, ":reward", ":quest_target_amount"),
##    (val_div, ":reward", 2),
##    (quest_set_slot, "qst_bring_prisoners_to_enemy", slot_quest_current_state, 1),#Some of the prisoners are given, so it's state will change for remembering that.
##    (quest_set_slot, "qst_bring_prisoners_to_enemy", slot_quest_target_amount, ":reward"),#Still needs to pay the lord the full price of the prisoners
##    (succeed_quest, "qst_bring_prisoners_to_enemy"),
##    ]],
##
##
##  [anyone,"guard_prisoners_brought", [],
##   "TODO: Thank you. Here is the money for prisoners.", "request_meeting_pretalk",[]],
##
##  [anyone,"guard_prisoners_brought_some", [],
##   "TODO: Thank you, but that's not enough. Here is the money for prisoners.", "request_meeting_pretalk",[]],

#  [anyone|plyr,"request_meeting_1", [], "[Leave]", "close_window",[]],





##  [anyone,"request_meeting_open_gates", [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
##                                         (call_script, "script_get_troop_attached_party", ":castle_lord"),
##                                         (eq, "$g_encountered_party", reg0),
##                                         (str_store_troop_name, 1, ":castle_lord")
##                                         ],  "My lord {s1} is in the castle now. You must ask his permission to enter.", "request_meeting_pretalk",[]],
##
##  [anyone,"request_meeting_open_gates", [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
##                                         (call_script, "script_get_troop_attached_party", ":castle_lord"),
##                                         (neq, "$g_encountered_party", reg0),
##                                         (ge, "$g_encountered_party_relation", 0),
##                                         (troop_get_slot, ":castle_lord_relation", ":castle_lord", slot_troop_player_relation),
##                                         (ge, ":castle_lord_relation", 20),
##                                         (str_store_troop_name, 1, ":castle_lord")
##                                         ],  "My lord {s1} is not in the castle now.\
## But I think he would approve of you taking shelter here, {sir/madam}.\
## Come on in. I am opening the gates for you.", "close_window",[]],
##
##  [anyone,"request_meeting_open_gates", [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),(str_store_troop_name, 1, ":castle_lord")],
##   "My lord {s1} is not in the castle now. I can't allow you into the castle without his orders.", "request_meeting_pretalk",[]],




# Quest conversations

##### TODO: QUESTS COMMENT OUT BEGIN

##  [party_tpl|pt_peasant_rebels,"start", [],
##   "TODO: What.", "peasant_rebel_talk",[]],
##  [anyone|plyr, "peasant_rebel_talk", [], "TODO: Die.", "close_window",[]],
##  [anyone|plyr, "peasant_rebel_talk", [], "TODO: Nothing.", "close_window",[(assign, "$g_leave_encounter",1)]],
##
##  [party_tpl|pt_noble_refugees,"start", [],
##   "TODO: What.", "noble_refugee_talk",[]],
##  [anyone|plyr, "noble_refugee_talk", [], "TODO: Nothing.", "close_window",[(assign, "$g_leave_encounter",1)]],
##


  [anyone,"start", [(eq,"$talk_context",tc_join_battle_ally),
                    ],
   "You have come just in time. Let us join our forces now and teach our enemy a lesson.", "close_window",
   []],

  [anyone,"start", [(eq,"$talk_context",tc_join_battle_enemy),
                    ],
   "You are making a big mistake by fighting against us.", "close_window",
   []],

  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
                    (troop_is_hero, "$g_talk_troop"),
                    (eq, "$g_talk_troop_met", 0),
                    (ge, "$g_talk_troop_relation", 17),
                    ],
   "I don't think we have met properly my friend. You just saved my life out there, and I still don't know your name...", "ally_thanks_meet", []],


  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
                    (troop_is_hero, "$g_talk_troop"),
                    (eq, "$g_talk_troop_met", 0),
                    (ge, "$g_talk_troop_relation", 5),
					(str_store_troop_name, s1, "$g_talk_troop"),
                    ],
   "Your help was most welcome stranger. My name is {s1}. Can I learn yours?", "ally_thanks_meet", []],

  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
                    (troop_is_hero, "$g_talk_troop"),
                    (eq, "$g_talk_troop_met", 0),
                    (ge, "$g_talk_troop_relation", 0),
                    (str_store_troop_name, s1, "$g_talk_troop"),
                    ],
   "Thanks for your help, stranger. We haven't met properly yet, have we? What is your name?", "ally_thanks_meet", []],

  [anyone|plyr,"ally_thanks_meet", [], "My name is {playername}.", "ally_thanks_meet_2", []],

  [anyone, "ally_thanks_meet_2", [(ge, "$g_talk_troop_relation", 15),(str_store_troop_name, s1, "$g_talk_troop")],
   "Well met indeed {playername}. My name is {s1} and I am forever in your debt. If there is ever anything I can help you with, just let me know...", "close_window", []],
  [anyone, "ally_thanks_meet_2", [(ge, "$g_talk_troop_relation", 5),], "Well met {playername}. I am in your debt for what you just did. I hope one day I will find a way to repay it.", "close_window", []],
  [anyone, "ally_thanks_meet_2", [], "Well met {playername}. I am {s1}. Thanks for your help and I hope we meet again.", "close_window", []],

#Post 0907 changes begin
  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
                    (troop_is_hero, "$g_talk_troop"),
                    (ge, "$g_talk_troop_relation", 30),
                    (ge, "$g_relation_boost", 10),
                    ],
   "Again you save our necks, {playername}! Truly, you are the best of friends. {s43}", "close_window", [
       (call_script, "script_lord_comment_to_s43", "$g_talk_troop", "str_battle_won_default"),
       (try_begin),
         (party_stack_get_troop_id, ":enemy_party_leader", "p_encountered_party_backup", 0),
         (is_between, ":enemy_party_leader", active_npcs_begin, active_npcs_end),
         (call_script, "script_add_log_entry", logent_lord_helped_by_player, "trp_player",  -1, ":enemy_party_leader", -1),
       (try_end),
       ]],

  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
                    (troop_is_hero, "$g_talk_troop"),
                    (ge, "$g_talk_troop_relation", 20),
                    (ge, "$g_relation_boost", 5),
                    ],
   "You arrived just in the nick of time! {playername}. You have my deepest thanks! {s43}", "close_window", [
       (call_script, "script_lord_comment_to_s43", "$g_talk_troop", "str_battle_won_default"),
#       (try_begin),
#         (party_stack_get_troop_id, ":enemy_party_leader", "p_encountered_party_backup", 0),
#         (is_between, ":enemy_party_leader", active_npcs_begin, active_npcs_end),
       (call_script, "script_add_log_entry", logent_lord_helped_by_player, "trp_player",  -1, "$g_talk_troop", -1),
#       (try_end),
       ]],

  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
                    (troop_is_hero, "$g_talk_troop"),
                    (ge, "$g_talk_troop_relation", 0),
                    (ge, "$g_relation_boost", 3),
                    ],
   "You turned up just in time, {playername}. I will not forget your help. {s43}", "close_window", [
       (call_script, "script_lord_comment_to_s43", "$g_talk_troop", "str_battle_won_default"),
#       (try_begin),
#         (party_stack_get_troop_id, ":enemy_party_leader", "p_encountered_party_backup", 0),
#         (is_between, ":enemy_party_leader", active_npcs_begin, active_npcs_end),
       (call_script, "script_add_log_entry", logent_lord_helped_by_player, "trp_player",  -1, "$g_talk_troop", -1),
#       (try_end),
       ]],

  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
                    (troop_is_hero, "$g_talk_troop"),
                    (ge, "$g_talk_troop_relation", -5),
                    ],
   "Good to see you here, {playername}. {s43}", "close_window", [
                    (call_script, "script_lord_comment_to_s43", "$g_talk_troop", "str_battle_won_default"),
					(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", 1),
       ]],


  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
                    (troop_is_hero, "$g_talk_troop"),
                    (ge, "$g_relation_boost", 4),
                    ],
   "{s43}", "close_window", [
                    (call_script, "script_lord_comment_to_s43", "$g_talk_troop", "str_battle_won_grudging_default"),
                    ]],


  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
                    (troop_is_hero, "$g_talk_troop"),
                    ],
   "{s43}", "close_window", [
                    (call_script, "script_lord_comment_to_s43", "$g_talk_troop", "str_battle_won_unfriendly_default"),
                    ]],


#  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
#                    (troop_is_hero, "$g_talk_troop"),
#                    (ge, "$g_talk_troop_relation", -20),
#                    ],
#   "So, this is {playername}. Well, your help wasn't really needed, but I guess you had nothing better to do, right?", "close_window", []],

#  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
#                    (troop_is_hero, "$g_talk_troop"),
#                    ],
#   "Who told you to come to our help? I certainly didn't. Begone now. I want nothing from you and I will not let you steal my victory.", "close_window", []],

#Post 0907 changes begin

  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
                    (ge, "$g_relation_boost", 10),
                    (party_get_num_companions, reg1, "$g_encountered_party"),
                    (val_sub, reg1, 1),
                    ],
   "Thank you for your help {sir/madam}. You saved {reg1?our lives:my life} out there.", "close_window", []],

  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks),
                    (ge, "$g_relation_boost", 5),
                    ],
   "Thank you for your help {sir/madam}. Things didn't look very well for us but then you came up and everything changed.", "close_window", []],

  [anyone,"start", [(eq,"$talk_context",tc_ally_thanks)],
   "Thank you for your help, {sir/madam}. It was fortunate to have you nearby.", "close_window", []],

  [anyone,"start", [(eq, "$talk_context", tc_hero_freed),
                    (store_conversation_troop,":cur_troop"),
                    (eq,":cur_troop","trp_kidnapped_girl"),],
   "Oh {sir/madam}. Thank you so much for rescuing me. Will you take me to my family now?", "kidnapped_girl_liberated_battle",[]],

  [anyone,"start", [(eq,"$talk_context",tc_hero_freed)],
   "I am in your debt for freeing me friend.", "freed_hero_answer",
   []],

  [anyone|plyr,"freed_hero_answer", [],
   "You're not going anywhere. You'll be my prisoner now!", "freed_hero_answer_1",
   [
     (store_conversation_troop, ":cur_troop_id"),
     (party_add_prisoners, "p_main_party", ":cur_troop_id", 1),#take prisoner
    ]],

  [anyone,"freed_hero_answer_1", [],
   "Alas. Will my luck never change?", "close_window",
   []],

  [anyone|plyr,"freed_hero_answer", [],
   "You're free to go, {s65}.", "freed_hero_answer_2",
   [
    ]],

  [anyone,"freed_hero_answer_2", [],
   "Thank you, good {sire/lady}. I never forget someone who's done me a good turn.", "close_window",
   []],

  [anyone|plyr,"freed_hero_answer", [],
   "Would you like to join me?", "freed_hero_answer_3",
   []],

  [anyone,"freed_hero_answer_3", [(store_random_in_range, ":random_no",0,2),(eq, ":random_no", 0)],
   "All right I will join you.", "close_window",
   [
     (store_conversation_troop, ":cur_troop_id"),
     (party_add_members, "p_main_party", ":cur_troop_id", 1),#join hero
   ]],

  [anyone,"freed_hero_answer_3", [],
   "No, I want to go on my own.", "close_window",
   [
    ]],

  [anyone,"start", [(eq,"$talk_context",tc_hero_defeated)],
   "You'll not live long to enjoy your victory. My kinsmen will soon wipe out the stain of this defeat.", "defeat_hero_answer",
   [
    ]],

  [anyone|plyr,"defeat_hero_answer", [],
   "You are my prisoner now.", "defeat_hero_answer_1",
   [
     (party_add_prisoners, "p_main_party", "$g_talk_troop", 1),#take prisoner
     #(troop_set_slot, "$g_talk_troop", slot_troop_is_prisoner, 1),
     (troop_set_slot, "$g_talk_troop", slot_troop_prisoner_of_party, "p_main_party"),
     (call_script, "script_event_hero_taken_prisoner_by_player", "$g_talk_troop"),
    ]],

  [anyone,"defeat_hero_answer_1", [],
   "Damn you. You will regret this.", "close_window",
   []],

  [anyone|plyr,"defeat_hero_answer", [],
   "You're free to go this time, but don't cross my path again.", "defeat_hero_answer_2",
   []],

  [anyone,"defeat_hero_answer_2", [],
   "We will meet again.", "close_window",
   []],




  [anyone,"combined_political_quests", [
  (eq, "$political_quest_found", "qst_resolve_dispute"),
	],
   "{s9}", "political_quest_suggested",
   [
   (quest_set_slot, "qst_resolve_dispute", slot_quest_target_troop, "$political_quest_target_troop"),
   (quest_set_slot, "qst_resolve_dispute", slot_quest_object_troop, "$political_quest_object_troop"),

   (quest_get_slot, ":target_troop", "qst_resolve_dispute", slot_quest_target_troop),
   (quest_get_slot, ":object_troop", "qst_resolve_dispute", slot_quest_object_troop),
   (str_store_troop_name, s4, ":target_troop"),
   (str_store_troop_name, s5, ":object_troop"),
   (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
   (str_store_troop_name, s7, ":faction_leader"),
   (try_begin),
      (eq, "$players_kingdom", "fac_player_supporters_faction"),
	  (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
	  (str_store_string, s9, "str_you_may_be_aware_my_lord_of_the_quarrel_between_s4_and_s5_which_is_damaging_the_unity_of_this_realm_and_sapping_your_authority_if_you_could_persuade_the_lords_to_reconcile_it_would_boost_your_own_standing_however_in_taking_this_on_you_run_the_risk_of_one_the_lords_deciding_that_you_have_taken_the_rivals_side"),
   (else_try),
	  (str_store_string, s9, "str_you_may_be_aware_my_lord_of_the_quarrel_between_s4_and_s5_which_is_damaging_the_unity_of_this_realm_and_sapping_your_authority_if_you_could_persuade_the_lords_to_reconcile_i_imagine_that_s7_would_be_most_pleased_however_in_taking_this_on_you_run_the_risk_of_one_the_lords_deciding_that_you_have_taken_the_rivals_side"),
   (try_end),
   ]],

  [anyone,"political_quest_follow_on", [
  (eq, "$political_quest_found", "qst_resolve_dispute"),
	],
   "I think that is a wise move. Good luck to you.", "close_window",
   [
    (assign, "$g_leave_encounter", 1),
    (setup_quest_text,"qst_resolve_dispute"),

	(quest_get_slot, ":lord_1", "qst_resolve_dispute", slot_quest_target_troop),
	(str_store_troop_name_link, s11, ":lord_1"),

	(quest_get_slot, ":lord_2", "qst_resolve_dispute", slot_quest_object_troop),
	(str_store_troop_name_link, s12, ":lord_2"),

	(str_store_string, s2, "str_resolve_the_dispute_between_s11_and_s12"),
	(call_script, "script_start_quest", "qst_resolve_dispute", -1),
	(quest_set_slot, "qst_resolve_dispute", slot_quest_expiration_days, 30),
	(quest_set_slot, "qst_resolve_dispute", slot_quest_giver_troop, "$g_talk_troop"),
	(quest_set_slot, "qst_resolve_dispute", slot_quest_target_state, 0),
	(quest_set_slot, "qst_resolve_dispute", slot_quest_object_state, 0),

	(quest_get_slot, ":lord_1", "qst_resolve_dispute", slot_quest_target_troop), #this block just to check if the slots work
	(str_store_troop_name, s11, ":lord_1"),
	(quest_get_slot, ":lord_2", "qst_resolve_dispute", slot_quest_object_troop),
	(str_store_troop_name, s12, ":lord_2"),
	],
   ],


   [anyone,"combined_political_quests", [

  (eq, "$political_quest_found", "qst_offer_gift"),
  (quest_set_slot, "qst_offer_gift", slot_quest_target_troop, "$political_quest_target_troop"),

  (quest_get_slot, ":target_troop", "qst_offer_gift", slot_quest_target_troop),
  (str_store_troop_name, s4, ":target_troop"),
  (troop_get_type, reg4, ":target_troop"),
  (call_script, "script_troop_get_family_relation_to_troop", ":target_troop", "$g_talk_troop"),

	],
   "Your relations with {s4} are not all that they could be. As {reg4?she:he} is my {s11}, I can mediate to attempt to mend your quarrel. Perhaps the best way for me to do this would be to send {reg4?her:him} a gift -- a fur-trimmed velvet robe, perhaps. If you can provide me with a bolt of velvet and a length of furs, I can have one made and sent to {reg4?her:him.}", "political_quest_suggested",
   [
   (quest_get_slot, ":target_troop", "qst_offer_gift", slot_quest_target_troop),
   (troop_get_type, reg4, ":target_troop"),
   ]],



  [anyone,"political_quest_follow_on", [
  (eq, "$political_quest_found", "qst_offer_gift"),
  ],
   "Splendid. I shall await the materials.", "close_window",
   [
   (assign, "$g_leave_encounter", 1),
    (setup_quest_text,"qst_offer_gift"),

	(quest_get_slot, ":lord_1", "qst_offer_gift", slot_quest_target_troop),
	(str_store_troop_name, s14, ":lord_1"),
	(str_store_troop_name, s12, "$g_talk_troop"),
	##diplomacy start+
	#(troop_get_type, reg4, "$g_talk_troop"),
	(assign, reg4, reg65),
	##diplomacy end+

	(str_store_string, s2, "str_you_intend_to_bring_gift_for_s14"),

   (call_script, "script_start_quest", "qst_offer_gift", "$g_talk_troop"),
   (quest_set_slot, "qst_offer_gift", slot_quest_expiration_days, 30),
   (quest_set_slot, "qst_offer_gift", slot_quest_current_state, 0), ##CABA - bugfix
   ]],




   [anyone,"combined_political_quests", [
   (eq, "$political_quest_found", "qst_denounce_lord"),
   (this_or_next|eq, "$g_talk_troop", "$g_player_minister"),
		(troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop"),

   (str_store_troop_name, s4, "$political_quest_target_troop"),
   ##diplomacy start+ use script for gender
   #(troop_get_type, reg4, "$political_quest_target_troop"),
   (call_script, "script_dplmc_store_troop_is_female_reg", "$political_quest_target_troop", 4),
   ##diplomacy end+
   (str_store_faction_name, s5, "$players_kingdom"),

   (troop_get_slot, ":reputation_string", "$political_quest_target_troop", slot_lord_reputation_type),
   (val_add, ":reputation_string", "str_lord_derogatory_default"),
   (str_store_string, s7, ":reputation_string"),

   (troop_get_slot, ":reputation_string", "$political_quest_target_troop", slot_lord_reputation_type),
   (val_add, ":reputation_string", "str_lord_derogatory_result"),
   (str_store_string, s8, ":reputation_string"),

	],
   "As you may realize, {s4} has many enemies among the lords of the {s5}. In particular, they feel that {reg4?she:he} is {s7}, and worry that {reg4?she:he} will {s8}. Were you to denounce {s4} to {reg4?her:his} face, you may reap much popularity -- although, of course, you would make an enemy of {reg4?her:him}, and risk being challenged to a duel.", "political_quest_suggested",
   [
   ]],

    [anyone,"combined_political_quests", [
    (eq, "$political_quest_found", "qst_denounce_lord"),
    ##diplomacy start+ use script for gender
    #(troop_get_type, reg4, "$political_quest_target_troop"),
    (call_script, "script_dplmc_store_troop_is_female_reg", "$political_quest_target_troop", 4),
    ##diplomacy end+

	(str_clear, s9),
	(call_script, "script_troop_get_relation_with_troop", "trp_player", "$g_talk_troop"),
	(assign, ":player_relation_with_target", reg0),

    (str_store_troop_name, s4, "$political_quest_target_troop"),
	(try_begin),
		(ge, ":player_relation_with_target", 2),
		(neg|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_debauched),
		(neg|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_quarrelsome),
		(str_store_string, s9, "str_i_realize_that_you_are_on_good_terms_with_s4_but_we_ask_you_to_do_this_for_the_good_of_the_realm"),
	(else_try),
		(ge, ":player_relation_with_target", 2),
		(str_store_string, s9, "str_i_realize_that_you_are_on_good_terms_with_s4_but_the_blow_will_hurt_him_more"),
	(try_end),

    (str_store_faction_name, s5, "$players_kingdom"),
    (str_store_troop_name, s4, "$political_quest_target_troop"),

    (troop_get_slot, ":reputation_string", "$political_quest_target_troop", slot_lord_reputation_type),
    (val_add, ":reputation_string", "str_lord_derogatory_default"),
    (str_store_string, s7, ":reputation_string"),

    (troop_get_slot, ":reputation_string", "$political_quest_target_troop", slot_lord_reputation_type),
    (val_add, ":reputation_string", "str_lord_derogatory_result"),
    (str_store_string, s8, ":reputation_string"),


	],

    "As you may realize, many of us in the peerage of the {s5} consider {s4} to be {s7}, and a liability to our cause. We worry that {reg4?she:he} will {s8}. People know my views on {s4} already, but if you were to denounce {reg4?her:him} to {reg4?her:his} face, you would further erode his standing -- and discourage our liege from entrusting {reg4?her:him} with any more power or responsibility. Of course, you would make an enemy of {reg4?her:him}, and risk being challenged to a duel.{s9}", "political_quest_suggested",
    [


	]],


	[anyone,"political_quest_follow_on", [
	(eq, "$political_quest_found", "qst_denounce_lord"),
	(this_or_next|eq, "$g_talk_troop", "$g_player_minister"),
		(troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop"),
  ],
   "We appreciate what you are doing. I find such intrigues distasteful, but it is all for the good of the {s5}.", "close_window",
   [
   (quest_set_slot, "qst_denounce_lord", slot_quest_target_troop, "$political_quest_target_troop"),

   (quest_get_slot, ":target_troop", "qst_denounce_lord", slot_quest_target_troop),
   (str_store_troop_name_link, s14, ":target_troop"),
   (str_store_troop_name_link, s12, "$g_talk_troop"),

   (str_store_string, s2, "str_you_intend_to_denounce_s14_to_his_face_on_behalf_of_s14"),
   (setup_quest_text, "qst_denounce_lord"),

   (call_script, "script_start_quest", "$political_quest_found", "$g_talk_troop"),
   (quest_set_slot, "qst_denounce_lord", slot_quest_expiration_days, 60),

   (str_store_faction_name, s5, "$players_kingdom"),
   (assign, "$g_leave_encounter", 1),
   ]],


	[anyone,"political_quest_follow_on", [
	(eq, "$political_quest_found", "qst_denounce_lord"),
  ],
   "Very well. It is always risky to involve yourself in intrigues of this sort, but in this case, I think you will benefit.", "close_window",
   [
   (quest_set_slot, "qst_denounce_lord", slot_quest_target_troop, "$political_quest_target_troop"),

   (quest_get_slot, ":target_troop", "qst_denounce_lord", slot_quest_target_troop),
   (str_store_troop_name_link, s14, ":target_troop"),
   (str_store_troop_name_link, s12, "$g_talk_troop"),

   (str_store_string, s2, "str_you_intend_to_denounce_s14_to_his_face_on_behalf_of_s14"),
   (setup_quest_text, "qst_denounce_lord"),

   (call_script, "script_start_quest", "$political_quest_found", "$g_talk_troop"),
   (assign, "$g_leave_encounter", 1),
]],




   [anyone,"combined_political_quests", [
    (eq, "$political_quest_found", "qst_intrigue_against_lord"),
    (str_store_troop_name, s4, "$political_quest_target_troop"),
       ##diplomacy start+ use script for gender
   #(troop_get_type, reg4, "$political_quest_target_troop"),
   (call_script, "script_dplmc_store_troop_is_female_reg", "$political_quest_target_troop", 4),
   ##diplomacy end+
    (str_store_faction_name, s5, "$players_kingdom"),
    (troop_get_slot, ":reputation_string", "$political_quest_target_troop", slot_lord_reputation_type),
    (val_add, ":reputation_string", "str_lord_derogatory_default"),
    (str_store_string, s7, ":reputation_string"),

    (troop_get_slot, ":reputation_string_2", "$political_quest_target_troop", slot_lord_reputation_type),
    (val_add, ":reputation_string_2", "str_lord_derogatory_result"),
    (str_store_string, s8, ":reputation_string_2"),

	(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
	(str_store_troop_name, s9, ":faction_leader"),
	],
   "You and I have a common interest in seeking to curtail the rise of {s4}. I feel that {reg4?she:he} is {s7}, and worry that {reg4?she:he} will {s8}. Were you to tell our liege {s9} your opinion of {s4}, it might discourage {s9} from granting {s4} any further powers or responsibilities, at least for a while, and I would be much obliged to you.", "political_quest_suggested",
   []],

   #Intrigue lord for
	[anyone,"political_quest_follow_on", [
	(eq, "$political_quest_found", "qst_intrigue_against_lord"),
#	(this_or_next|eq, "$g_talk_troop", "$g_player_minister"),
#		(troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop"),
    (str_store_faction_name, s5, "$players_kingdom"),

  ],
   "We appreciate what you are doing. I find such intrigues distasteful, but it is all for the good of the {s5}.", "close_window",
   [
   (quest_set_slot, "qst_intrigue_against_lord", slot_quest_target_troop, "$political_quest_target_troop"),

   (quest_get_slot, ":target_troop", "qst_intrigue_against_lord", slot_quest_target_troop),
   (store_faction_of_troop, ":target_troop_faction", ":target_troop"),
   (faction_get_slot, ":faction_liege", ":target_troop_faction", slot_faction_leader),
   (str_store_troop_name_link, s14, ":target_troop"),
   (str_store_troop_name_link, s13, ":faction_liege"),
   (str_store_troop_name_link, s12, "$g_talk_troop"),

   (str_store_string, s2, "str_you_intend_to_denounce_s14_to_s13_on_behalf_of_s12"),
   (setup_quest_text, "qst_intrigue_against_lord"),

   (call_script, "script_start_quest", "$political_quest_found", "$g_talk_troop"),
   (quest_set_slot, "qst_intrigue_against_lord", slot_quest_expiration_days, 60),
   (assign, "$g_leave_encounter", 1),
   ]],


  [anyone,"combined_political_quests", [],
   "I cannot think of anything right now, but we will have some items of mutual interest in the future.", "political_quest_suggested",
   []],

  [anyone|plyr,"political_quest_suggested", [
  (gt, "$political_quest_found", 0),
  ],
   "I like that idea.", "political_quest_follow_on",
   [
   ]],

  [anyone|plyr,"political_quest_suggested", [
  (gt, "$political_quest_found", 0),
  ],
   "Hmm.. Maybe you can think of something else?", "combined_political_quests",
   [
   (quest_set_slot, "$political_quest_found", slot_quest_dont_give_again_remaining_days, 3),
   (call_script, "script_get_political_quest", "$g_talk_troop"),
   (assign, "$political_quest_found", reg0),
   (assign, "$political_quest_target_troop", reg1),
   (assign, "$political_quest_object_troop", reg2),

   ]],

  [anyone|plyr,"political_quest_suggested", [],
   "Let us discuss another topic", "political_quests_end",
   []],








  [anyone,"political_quests_end", [
  (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
  ],
   "Very well.", "lord_pretalk",
   []],

  [anyone,"political_quests_end", [
  (troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop"),
  ],
   "Very well.", "spouse_pretalk",
   []],

  [anyone,"political_quests_end", [
  (eq, "$g_talk_troop", "$g_player_minister"),
  ],
   "Very well.", "minister_pretalk",
   []],

  [anyone,"political_quests_end", [
  ],
   "Very well.", "close_window",
   [
   (assign, "$g_leave_encounter", 1),
   ]],




# Local merchant

  [trp_local_merchant,"start", [], "Mercy! Please don't kill me!", "local_merchant_mercy",[]],
  [anyone|plyr,"local_merchant_mercy", [(quest_get_slot, ":quest_giver_troop", "qst_kill_local_merchant", slot_quest_giver_troop),(str_store_troop_name, s2, ":quest_giver_troop"),
  ##diplomacy start+ Initialize reg4 for use below
  (assign, reg4, 0),
  (try_begin),
	(call_script, "script_cf_dplmc_troop_is_female", ":quest_giver_troop"),
	(assign, reg4, 1),
  (try_end),
  ],#next line man to {reg65?woman:man}
   "I have nothing against you {reg65?woman:man}. But {s2} wants you dead. Sorry.", "local_merchant_mercy_no",[]],
   ##diplomacy end+
  [anyone,"local_merchant_mercy_no", [], "Damn you! May you burn in Hell!", "close_window",[]],
  [anyone|plyr,"local_merchant_mercy", [], "I'll let you live, if you promise me...", "local_merchant_mercy_yes",[]],

  [anyone,"local_merchant_mercy_yes", [], "Of course, I promise, I'll do anything. Just spare my life... ", "local_merchant_mercy_yes_2",[]],
  ##diplomacy start+ use reg4 from before to make gender correct
  [anyone|plyr,"local_merchant_mercy_yes_2", [], "You are going to forget about {s2}'s debt to you. And you will sign a paper stating that {reg4?she:he} owes you nothing.", "local_merchant_mercy_yes_3",[]],
  ##diplomacy end+
  [anyone,"local_merchant_mercy_yes_3", [], "Yes, of course. I'll do as you say.", "local_merchant_mercy_yes_4",[]],
  [anyone|plyr,"local_merchant_mercy_yes_4", [], "And if my lord hears so much of a hint of a complaint about this issue, then I'll come back for you,\
 and it won't matter how much you scream for mercy then.\
 Do you understand me?", "local_merchant_mercy_yes_5",[]],
  [anyone,"local_merchant_mercy_yes_5", [], "Yes {sir/madam}. Don't worry. I won't make any complaint.", "local_merchant_mercy_yes_6",[]],
  [anyone|plyr,"local_merchant_mercy_yes_6", [], "Good. Go now, before I change my mind.", "close_window",
   [(quest_set_slot, "qst_kill_local_merchant", slot_quest_current_state, 2),
    (call_script, "script_succeed_quest", "qst_kill_local_merchant"),
    (finish_mission),
    ]],

# Village traitor

  [trp_fugitive,"start", [], "What do you want?", "fugitive_1",[]],
  [trp_fugitive|plyr,"fugitive_1", [
     (quest_get_slot, ":quest_target_dna", "qst_hunt_down_fugitive", slot_quest_target_dna),
     (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
     (str_store_string, s4, s50),
      ], "I am looking for a murderer by the name of {s4}. You fit his description.", "fugitive_2",[]],
  [trp_fugitive|plyr,"fugitive_1", [], "Nothing. Sorry to trouble you.", "close_window",[]],
  [trp_fugitive,"fugitive_2", [], "I don't understand, {sir/madam}.\
 I never killed anyone. I think you've got the wrong man.", "fugitive_3",[]],
  [trp_fugitive|plyr,"fugitive_3", [], "Then drop your sword. If you are innocent, you have nothing to fear.\
 We'll go now and talk to your neighbours, and if they verify your story, I'll go on my way.", "fugitive_4",[]],
  [anyone,"fugitive_4", [], "I'm not going anywhere, friend. You're going to have to fight for your silver, today.", "fugitive_5",
   []],

  [trp_fugitive|plyr,"fugitive_5", [], "No problem. I really just need your head, anyway.", "fugitive_fight_start",[]],
  [trp_fugitive|plyr,"fugitive_5", [], "I come not for money, but to execute the law!", "fugitive_fight_start",[]],
  [trp_fugitive|plyr,"fugitive_5", [], "Alas, that you cannot be made to see reason.", "fugitive_fight_start",[]],

  [anyone,"fugitive_fight_start", [], "Die, dog!", "close_window",
   [
	(set_party_battle_mode),
    (quest_set_slot, "qst_hunt_down_fugitive", slot_quest_current_state, 1),
    (call_script, "script_activate_tavern_attackers"),
   ]],


  [anyone,"member_chat", [(check_quest_active, "qst_incriminate_loyal_commander"),
                          (quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_current_state, 0),
                          (store_conversation_troop, "$g_talk_troop"),
                          (eq, "$g_talk_troop", "$incriminate_quest_sacrificed_troop"),
                          (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
                          (store_distance_to_party_from_party, ":distance", "p_main_party", ":quest_target_center"),
                          (lt, ":distance", 10),
                          ], "Yes {sir/madam}?", "sacrificed_messenger_1",[]],

  [anyone|plyr,"sacrificed_messenger_1", [(quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
                                          (str_store_party_name, s1, ":quest_target_center"),
                                          (quest_get_slot, ":quest_object_troop", "qst_incriminate_loyal_commander", slot_quest_object_troop),
                                          (str_store_troop_name, s2, ":quest_object_troop"),],
   "Take this letter to {s1} and give it to {s2}.", "sacrificed_messenger_2",[]],
  [anyone|plyr,"sacrificed_messenger_1", [],
   "Nothing. Nothing at all.", "close_window",[]],

  [anyone,"sacrificed_messenger_2", [],
   "Yes {sir/madam}. You can trust me. I will not fail you.", "sacrificed_messenger_3",[]],

  [anyone|plyr,"sacrificed_messenger_3", [],
   "Good. I will not forget your service. You will be rewarded when you return.", "close_window",[(party_remove_members, "p_main_party", "$g_talk_troop", 1),
                                     (set_spawn_radius, 0),
                                     (spawn_around_party, "p_main_party", "pt_sacrificed_messenger"),
                                     (assign, ":new_party", reg0),
                                     (party_add_members, ":new_party", "$g_talk_troop", 1),
                                     (party_set_ai_behavior, ":new_party", ai_bhvr_travel_to_party),
                                     (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
                                     (party_set_ai_object, ":new_party", ":quest_target_center"),
                                     (party_set_flags, ":new_party", pf_default_behavior, 0),
                                     (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 2),
                                     (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_target_party, ":new_party")]],
  [anyone|plyr,"sacrificed_messenger_3", [], "Arggh! I can't do this. I can't send you to your own death!", "sacrificed_messenger_cancel",[]],
  [anyone,"sacrificed_messenger_cancel", [], "What do you mean {sir/madam}?", "sacrificed_messenger_cancel_2",[]],
  [anyone|plyr,"sacrificed_messenger_cancel_2", [(quest_get_slot, ":quest_giver", "qst_incriminate_loyal_commander", slot_quest_giver_troop),
                                                 (str_store_troop_name, s3, ":quest_giver"),
      ], "There's a trap set up for you in the town.\
 {s3} ordered me to sacrifice one of my chosen warriors to fool the enemy,\
 but he will just need to find another way.", "sacrificed_messenger_cancel_3",[
     (quest_get_slot, ":quest_giver", "qst_incriminate_loyal_commander", slot_quest_giver_troop),
     (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 1),
     (call_script, "script_change_player_relation_with_troop",":quest_giver",-5),
     (call_script, "script_change_player_honor", 3),
     (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
     ]],
  [anyone,"sacrificed_messenger_cancel_3", [], "Thank you, {sir/madam}.\
 I will follow you to the gates of hell. But this would not be a good death.", "close_window",[]],

  [party_tpl|pt_sacrificed_messenger,"start", [],
   "Don't worry, {sir/madam}, I'm on my way.", "close_window",[(assign, "$g_leave_encounter",1)]],

#Spy

  [party_tpl|pt_spy,"start", [], "Good day {sir/madam}. Such fine weather don't you think? If you'll excuse me now I must go on my way.", "follow_spy_talk",[]],

  [anyone|plyr, "follow_spy_talk",
   [
     (quest_get_slot, ":quest_giver", "qst_follow_spy", slot_quest_giver_troop),
     (str_store_troop_name, s1, ":quest_giver"),
     ],
   "In the name of {s1}, you are under arrest!", "follow_spy_talk_2", []],
  [anyone, "follow_spy_talk_2", [], "You won't get me alive!", "close_window", []],
  [anyone|plyr, "follow_spy_talk", [], "Never mind me. I was just passing by.", "close_window", [(assign, "$g_leave_encounter",1)]],

  [party_tpl|pt_spy_partners,"start", [], "Greetings.", "spy_partners_talk",[]],
  
  ##Floris MTT begin
  [party_tpl|pt_spy_partners_r,"start", [], "Greetings.", "spy_partners_talk",[]],
  [party_tpl|pt_spy_partners_e,"start", [], "Greetings.", "spy_partners_talk",[]],
  ##Floris MTT end

  [anyone|plyr,"spy_partners_talk",
   [
     (quest_get_slot, ":quest_giver", "qst_follow_spy", slot_quest_giver_troop),
     (str_store_troop_name, s1, ":quest_giver"),
     ],
   "In the name of {s1} You are under arrest!", "spy_partners_talk_2",[]],
  [anyone,"spy_partners_talk_2", [], "You will have to fight us first!", "close_window",[]],
  [anyone|plyr,"spy_partners_talk", [], "Never mind me. I was just passing by.", "close_window",[(assign, "$g_leave_encounter",1)]],


###Conspirator
##
##  [party_tpl|pt_conspirator_leader,"start", [], "TODO: Hello.", "conspirator_talk",[]],
##  [party_tpl|pt_conspirator,"start", [], "TODO: Hello.", "conspirator_talk",[]],
##
##  [anyone|plyr,"conspirator_talk", [(gt, "$qst_capture_conspirators_leave_meeting_counter", 0),
##                                    (quest_get_slot,":quest_giver","qst_capture_conspirators",slot_quest_giver_troop),
##                                    (str_store_troop_name,s1,":quest_giver")],
##   "TODO: In the name of {s1}, you are under arrest!", "conspirator_talk_2",[]],
##
##  [anyone|plyr,"conspirator_talk", [], "TODO: Bye.", "close_window",[(assign, "$g_leave_encounter",1)]],
##
##  [anyone,"conspirator_talk_2", [], "You won't get me alive!", "close_window",[]],
##
#Runaway Peasants


  [party_tpl|pt_runaway_serfs,"start", [(party_slot_eq, "$g_encountered_party", slot_town_center, 0)],#slot_town_center is used for first time meeting
   "Good day {sir/madam}.", "runaway_serf_intro_1",
   [(party_set_slot, "$g_encountered_party", slot_town_center, 1)]],

  [anyone|plyr,"runaway_serf_intro_1", [(quest_get_slot, ":lord", "qst_bring_back_runaway_serfs", slot_quest_giver_troop),
                                        (str_store_troop_name, s4, ":lord")],
   "I have been sent by your {s4} whom you are running from. He will not punish you if you return now.", "runaway_serf_intro_2",[]],

  [anyone,"runaway_serf_intro_2", [(quest_get_slot, ":target_center", "qst_bring_back_runaway_serfs", slot_quest_target_center),
                                   (str_store_party_name, s6, ":target_center"),
                                   (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
                                   (str_store_party_name, s1, ":quest_object_center")],
   "My good {sir/madam}. Our lives at our village {s1} was unbearable. We worked all day long and still went to bed hungry.\
 We are going to {s6} to start a new life, where we will be treated like humans.", "runaway_serf_intro_3",[]],

  [anyone|plyr,"runaway_serf_intro_3", [(quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
                                        (str_store_party_name, s1, ":quest_object_center"),],
   "You have gone against our laws by running from your bondage. You will go back to {s1} now!", "runaway_serf_go_back",
   [(quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
    (call_script, "script_change_player_relation_with_center", ":quest_object_center", -1)]],

  [anyone|plyr,"runaway_serf_intro_3", [], "Well, maybe you are right. All right then. If anyone asks, I haven't seen you.", "runaway_serf_let_go",
   [(quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
    (call_script, "script_change_player_relation_with_center", ":quest_object_center", 1)]],

  [anyone,"runaway_serf_go_back", [(quest_get_slot, ":home_center", "qst_bring_back_runaway_serfs", slot_quest_object_center), ##Floris MTT - was party_tpl|pt_runaway_serfs
                                                       (str_store_party_name, s5, ":home_center")],
   "All right {sir/madam}. As you wish. We'll head back to {s5} now.", "close_window",
   [(quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
    (party_set_ai_object, "$g_encountered_party", ":quest_object_center"),
    (assign, "$g_leave_encounter",1)]],

  [anyone,"runaway_serf_let_go", [], "God bless you, {sir/madam}. We will not forget your help.", "close_window",
   [(party_set_slot, "$g_encountered_party", slot_town_castle, 1),
    (assign, "$g_leave_encounter",1)]],


  [party_tpl|pt_runaway_serfs,"start", [(party_slot_eq, "$g_encountered_party", slot_town_castle, 1),
                                        ],
   "Good day {sir/madam}. Don't worry. If anyone asks, we haven't seen you.", "runaway_serf_reconsider",[]],

  [anyone|plyr,"runaway_serf_reconsider", [], "I have changed my mind. You must back to your village!", "runaway_serf_go_back",
   [(party_set_slot, "$g_encountered_party", slot_town_castle, 0),
    (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
    (call_script, "script_change_player_relation_with_center", ":quest_object_center", -2)]],

  [anyone|plyr,"runaway_serf_reconsider", [], "Good. Go quickly now before I change my mind.", "runaway_serf_let_go",[]],


  [party_tpl|pt_runaway_serfs,"start", [(party_slot_eq, "$g_encountered_party", slot_town_castle, 0),
                                        (get_party_ai_object, ":cur_ai_object"),
                                        (quest_get_slot, ":home_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
                                        (neq, ":home_center", ":cur_ai_object")],
   "Good day {sir/madam}. We were heading back to {s5}, but I am afraid we lost our way.", "runaway_serf_talk_caught",[]],

  [anyone|plyr,"runaway_serf_talk_caught", [], "Do not test my patience. You are going back now!", "runaway_serf_go_back",[]],
  [anyone|plyr,"runaway_serf_talk_caught", [], "Well, if you are that eager to go, then go.", "runaway_serf_let_go",
   [(quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
    (call_script, "script_change_player_relation_with_center", ":quest_object_center", 1)]],

  [party_tpl|pt_runaway_serfs,"start",
   [(quest_get_slot, ":home_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
    (str_store_party_name, s5, ":home_center")], "We are on our way back to {s5} {sir/madam}.", "runaway_serf_talk_again_return",[]],

  [anyone|plyr,"runaway_serf_talk_again_return", [], "Make haste now. The sooner you return the better.", "runaway_serf_talk_again_return_2",[]],
  [anyone|plyr,"runaway_serf_talk_again_return", [], "Good. Keep going.", "runaway_serf_talk_again_return_2",[]],

  [anyone|plyr,"runaway_serf_talk_again_return_2", [], "Yes {sir/madam}. As you wish.", "close_window",[(assign, "$g_leave_encounter",1)]],
  
  ##Floris MTT Begin
  [party_tpl|pt_runaway_serfs_r,"start", [(party_slot_eq, "$g_encountered_party", slot_town_center, 0)],#slot_town_center is used for first time meeting
   "Good day {sir/madam}.", "runaway_serf_intro_1",
   [(party_set_slot, "$g_encountered_party", slot_town_center, 1)]],
  [party_tpl|pt_runaway_serfs_r,"start", [(party_slot_eq, "$g_encountered_party", slot_town_castle, 1),
                                        ],
   "Good day {sir/madam}. Don't worry. If anyone asks, we haven't seen you.", "runaway_serf_reconsider",[]],
   
   [party_tpl|pt_runaway_serfs_r,"start", [(party_slot_eq, "$g_encountered_party", slot_town_castle, 0),
                                        (get_party_ai_object, ":cur_ai_object"),
                                        (quest_get_slot, ":home_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
                                        (neq, ":home_center", ":cur_ai_object")],
   "Good day {sir/madam}. We were heading back to {s5}, but I am afraid we lost our way.", "runaway_serf_talk_caught",[]], 
  [party_tpl|pt_runaway_serfs_r,"start",
   [(quest_get_slot, ":home_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
    (str_store_party_name, s5, ":home_center")], "We are on our way back to {s5} {sir/madam}.", "runaway_serf_talk_again_return",[]],
 [party_tpl|pt_runaway_serfs_e,"start", [(party_slot_eq, "$g_encountered_party", slot_town_center, 0)],#slot_town_center is used for first time meeting
   "Good day {sir/madam}.", "runaway_serf_intro_1",
   [(party_set_slot, "$g_encountered_party", slot_town_center, 1)]],
  [party_tpl|pt_runaway_serfs_e,"start", [(party_slot_eq, "$g_encountered_party", slot_town_castle, 1),
                                        ],
   "Good day {sir/madam}. Don't worry. If anyone asks, we haven't seen you.", "runaway_serf_reconsider",[]],
   
   [party_tpl|pt_runaway_serfs_e,"start", [(party_slot_eq, "$g_encountered_party", slot_town_castle, 0),
                                        (get_party_ai_object, ":cur_ai_object"),
                                        (quest_get_slot, ":home_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
                                        (neq, ":home_center", ":cur_ai_object")],
   "Good day {sir/madam}. We were heading back to {s5}, but I am afraid we lost our way.", "runaway_serf_talk_caught",[]], 
  [party_tpl|pt_runaway_serfs_e,"start",
   [(quest_get_slot, ":home_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
    (str_store_party_name, s5, ":home_center")], "We are on our way back to {s5} {sir/madam}.", "runaway_serf_talk_again_return",[]],
  ##FLoris MTT End



#Quest bandits
  [anyone,"start", [
  (check_quest_active, "qst_track_down_bandits"),
  (quest_slot_eq, "qst_track_down_bandits", slot_quest_target_party, "$g_encountered_party"),
  (neg|is_between, "$g_encountered_party_faction", kingdoms_begin, kingdoms_end), #ie, the party has not respawned as a non-bandit
  ],
   "This must be your unlucky day, mate. We're just about the worst people you could run into, in these parts.", "troublesome_bandits_intro_1",[
   ]],

 [anyone|plyr,"troublesome_bandits_intro_1", [],
   "Heh. For me, you are nothing more than walking money bags.\
 A merchant in {s1} offered me good money for your heads.",
   "troublesome_bandits_intro_2", [(quest_get_slot, ":quest_giver_center", "qst_track_down_bandits", slot_quest_giver_center),
                                   (str_store_party_name, s1, ":quest_giver_center")
                                   ]],
  [anyone,"troublesome_bandits_intro_2", [],
   "A bounty hunter! Kill {him/her}! Kill {him/her} now!", "close_window",[
   (encounter_attack)]],


#Deserters
  [party_tpl|pt_deserters, "start", [(eq,"$talk_context",tc_party_encounter),
                                     (party_get_slot,":protected_until_hours", "$g_encountered_party",slot_party_ignore_player_until),
                                     (store_current_hours,":cur_hours"),
                                     (store_sub, ":protection_remaining",":protected_until_hours",":cur_hours"),
                                     (gt, ":protection_remaining", 0)], "What do you want?\
 You want to pay us some more money?", "deserter_paid_talk",[]],
  [anyone|plyr,"deserter_paid_talk", [], "Sorry to trouble you. I'll be on my way now.", "deserter_paid_talk_2a",[]],
  [anyone,"deserter_paid_talk_2a", [], "Yeah. Stop fooling around and go make some money.\
 I want to see that purse full next time I see you.", "close_window",[(assign, "$g_leave_encounter",1)]],
  [anyone|plyr,"deserter_paid_talk", [], "No. It's your turn to pay me this time.", "deserter_paid_talk_2b",[]],
  [anyone,"deserter_paid_talk_2b", [], "What nonsense are you talking about? You want trouble? You got it.", "close_window",[
       (party_set_slot,"$g_encountered_party",slot_party_ignore_player_until,0),
       (party_ignore_player, "$g_encountered_party", 0),
    ]],


  [party_tpl|pt_deserters,"start", [
      (eq,"$talk_context",tc_party_encounter)
                    ], "We are the free brothers.\
 We will fight only for ourselves from now on.\
 Now give us your gold or taste our steel.", "deserter_talk",[]],
##  [anyone|plyr,"deserter_talk", [(check_quest_active, "qst_bring_back_deserters"),
##                                 (quest_get_slot, ":target_deserter_troop", "qst_bring_back_deserters", slot_quest_target_troop),
##                                 (party_count_members_of_type, ":num_deserters", "$g_encountered_party",":target_deserter_troop"),
##                                 (gt, ":num_deserters", 1)],
##   "If you surrender to me now, you will rejoin the army of your kingdom without being punished. Otherwise you'll get a taste of my sword.", "deserter_join_as_prisoner",[]],
  [anyone|plyr,"deserter_talk", [], "When I'm done with you, you'll regret ever leaving your army.", "close_window",[]],
  [anyone|plyr,"deserter_talk", [], "There's no need to fight. I am ready to pay for free passage.", "deserter_barter",[]],

## CC
  [anyone|plyr,"deserter_talk", 
    [
      (store_num_free_stacks,":stack_left","p_main_party"),
      (party_stack_get_troop_id, ":troop_no", "$g_encountered_party", 0),
      (this_or_next|gt, ":stack_left", 0),
      (main_party_has_troop, ":troop_no"),
    ], "I will give you money and good protection if you join my party.", "deserter_recruit",[]],
  [anyone,"deserter_recruit", [], "Sounds like a good deal. To show us your good will, pay us {reg5} denars and we will join you.", "deserter_recruit_2",
    [
      (party_get_num_companion_stacks, ":num_stacks","$g_encountered_party"),
      (assign, ":recruit_cost", 0),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":troop_no", "$g_encountered_party", ":i_stack"),
        (party_stack_get_size, ":stack_size", "$g_encountered_party", ":i_stack"),
        (call_script, "script_game_get_join_cost", ":troop_no"),
        (assign, ":join_cost", reg0),
        (val_mul, ":join_cost", ":stack_size"),
        (val_add, ":recruit_cost", ":join_cost"),
      (try_end),
      (assign, "$temp", ":recruit_cost"),
      (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
      (store_mul, ":persuasion_bonus", 3, ":persuasion_level"),
      (store_sub, ":persuasion_factor", 100, ":persuasion_bonus"),
      (val_mul, "$temp", ":persuasion_factor"),
      (val_div, "$temp", 100),
      (assign, reg5, "$temp"),
    ]],
  
  [anyone|plyr,"deserter_recruit_2", 
      [
        (store_troop_gold, reg2, "trp_player"),
        (ge,reg2,"$temp"),
        (assign,reg5,"$temp"),
      ],
     "All right here's your {reg5} denars.", "deserter_recruit_3a",
     [
       (troop_remove_gold, "trp_player", "$temp"),
       (display_message, "@Your current action is disgraceful.", 0xFF0000),
       (store_div, ":renown_sub", "$temp", -50),
       (call_script, "script_change_troop_renown", "trp_player", ":renown_sub"),
     ]],
  [anyone|plyr,"deserter_recruit_2", [],
   "I don't have that much money with me", "deserter_barter_3b",[]],

  [anyone,"deserter_recruit_3a", [], "Ok, we are at your service from now on.", "close_window",
    [
#      (assign, "$add_1000", 1),
      (call_script, "script_party_add_party", "p_main_party", "$g_encountered_party"),
#      (assign, "$add_1000", 0),
      (party_detach, "$g_encountered_party"),
      (remove_party, "$g_encountered_party"),
      (assign, "$g_leave_encounter", 1),
    ]],
## CC

##  [anyone,"deserter_join_as_prisoner", [(call_script, "script_party_calculate_strength", "p_main_party"),
##                                        (assign, ":player_strength", reg0),
##                                        (store_encountered_party,":encountered_party"),
##                                        (call_script, "script_party_calculate_strength", ":encountered_party"),
##                                        (assign, ":enemy_strength", reg0),
##                                        (val_mul, ":enemy_strength", 2),
##                                        (ge, ":player_strength", ":enemy_strength")],
##   "All right we join you then.", "close_window",[(assign, "$g_enemy_surrenders", 1)]],
##  [anyone,"deserter_join_as_prisoner", [], "TODO: We will never surrender!", "close_window",[(encounter_attack)]],

  [anyone,"deserter_barter", [], "Good. You are clever. Now, having a look at your baggage, I reckon a fellow like you could pretty easily afford {reg5} denars. We wouldn't want to be too greedy, now would we? Pay us, and then you can go.", "deserter_barter_2",[
    (store_troop_gold, ":total_value", "trp_player"),
    (troop_get_inventory_capacity, ":inv_size", "trp_player"),
    (try_for_range, ":i_slot", 0, ":inv_size"),
         (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
         (ge, ":item_id", 0),
         (try_begin),
           (is_between, ":item_id", trade_goods_begin, trade_goods_end),
           (store_item_value, ":item_value", ":item_id"),
           (val_add, ":total_value", ":item_value"),
         (try_end),
    (try_end),
    (store_div, "$g_tribute_amount", ":total_value", 10), #10000 gold = excellent_target
    (val_max, "$g_tribute_amount", 10),
    (assign,reg(5),"$g_tribute_amount")]],
  [anyone|plyr,"deserter_barter_2", [(store_troop_gold,reg(2)),(ge,reg(2),"$g_tribute_amount"),(assign,reg(5),"$g_tribute_amount")],
   "All right here's your {reg5} denars.", "deserter_barter_3a",[(troop_remove_gold, "trp_player","$g_tribute_amount")]],
  [anyone|plyr,"deserter_barter_2", [],
   "I don't have that much money with me", "deserter_barter_3b",[]],
  [anyone,"deserter_barter_3b", [],
   "Too bad. Then we'll have to sell you to the slavers.", "close_window",[]],


  [anyone,"deserter_barter_3a", [], "Heh. That wasn't difficult, now, was it? All right. Go now.", "close_window",[
    (store_current_hours,":protected_until"),
    (val_add, ":protected_until", 72),
    (party_set_slot,"$g_encountered_party",slot_party_ignore_player_until,":protected_until"),
    (party_ignore_player, "$g_encountered_party", 72),

    (assign, "$g_leave_encounter",1)
    ]],

##### TODO: QUESTS COMMENT OUT END

#Tavernkeepers

  [anyone ,"start", [(store_conversation_troop,reg(1)),(ge,reg(1),tavernkeepers_begin),(lt,reg(1),tavernkeepers_end)],
   "Good day dear {sir/madam}. How can I help you?", "tavernkeeper_talk",
   [
#    (store_encountered_party,reg(2)),
#    (party_get_slot,"$tavernkeeper_party",reg(2),slot_town_mercs),
    ]],

  [anyone,"tavernkeeper_pretalk", [], "Anything else?", "tavernkeeper_talk",[]],

  [anyone|plyr,"tavernkeeper_talk", [(check_quest_active,"qst_deliver_wine"),
                                     (quest_slot_eq, "qst_deliver_wine", slot_quest_target_center, "$g_encountered_party"),
                                     (quest_get_slot, ":quest_target_item", "qst_deliver_wine", slot_quest_target_item),
                                     (quest_get_slot, ":quest_target_amount", "qst_deliver_wine", slot_quest_target_amount),
                                     (store_item_kind_count, ":item_count", ":quest_target_item"),
                                     (ge, ":item_count", ":quest_target_amount"),
                                     (assign, reg9, ":quest_target_amount"),
                                     (str_store_item_name, s4, ":quest_target_item"),
                                     ],
   "I was told to deliver you {reg9} units of {s4}.", "tavernkeeper_deliver_wine",[]],
  [anyone,"tavernkeeper_deliver_wine", [],
 "At last! My stock was almost depleted.\
 I had paid the cost of the {s4} in advance.\
 Here, take these {reg5} denars. That should cover your pay.\
 And give {s9} my regards.\
 I'll put in a good word for you next time I deal with him.", "tavernkeeper_pretalk",
   [(quest_get_slot, ":quest_target_item", "qst_deliver_wine", slot_quest_target_item),
    (quest_get_slot, ":quest_target_amount", "qst_deliver_wine", slot_quest_target_amount),
    (quest_get_slot, ":quest_gold_reward", "qst_deliver_wine", slot_quest_gold_reward),
    (quest_get_slot, ":quest_giver_troop", "qst_deliver_wine", slot_quest_giver_troop),
    (troop_remove_items, "trp_player", ":quest_target_item", ":quest_target_amount"),
    (call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
    (assign, ":xp_reward", ":quest_gold_reward"),
    (val_mul, ":xp_reward", 4),
    (add_xp_as_reward, ":xp_reward"),
    (assign, reg5, ":quest_gold_reward"),
    (str_store_item_name, s4, ":quest_target_item"),
    (str_store_troop_name, s9, ":quest_giver_troop"),

    (quest_get_slot, ":giver_town", "qst_deliver_wine", slot_quest_giver_center),
    (call_script, "script_change_player_relation_with_center", ":giver_town", 2),
    (call_script, "script_change_player_relation_with_center", "$current_town", 1),
    (call_script, "script_end_quest", "qst_deliver_wine"),
    ]],

  [anyone|plyr,"tavernkeeper_talk", [(check_quest_active,"qst_deliver_wine"),
                                     (quest_slot_eq, "qst_deliver_wine", slot_quest_target_center, "$g_encountered_party"),
                                     (quest_get_slot, ":quest_target_item", "qst_deliver_wine", slot_quest_target_item),
                                     (quest_get_slot, ":quest_target_amount", "qst_deliver_wine", slot_quest_target_amount),
                                     (store_item_kind_count, ":item_count", ":quest_target_item"),
                                     (lt, ":item_count", ":quest_target_amount"),
                                     (gt, ":item_count", 0),
                                     (assign, reg9, ":quest_target_amount"),
                                     (str_store_item_name, s4, ":quest_target_item"),
                                     ],
   "I was told to deliver you {reg9} units of {s4}, but I lost some of the cargo on the way.", "tavernkeeper_deliver_wine_incomplete",[]],
  [anyone,"tavernkeeper_deliver_wine_incomplete", [],
 "Attacked by bandits eh?\
 You are lucky they left you alive.\
 Anyway, I can pay you no more than {reg5} denars for this.\
 And I will let {s1} know that my order was delivered less than completely,\
 so you will probably be charged for this loss.", "tavernkeeper_pretalk",
   [(quest_get_slot, ":quest_target_item", "qst_deliver_wine", slot_quest_target_item),
    (quest_get_slot, ":quest_target_amount", "qst_deliver_wine", slot_quest_target_amount),
    (quest_get_slot, ":quest_gold_reward", "qst_deliver_wine", slot_quest_gold_reward),
    (quest_get_slot, ":quest_giver_troop", "qst_deliver_wine", slot_quest_giver_troop),
    (store_item_kind_count, ":item_count", ":quest_target_item"),
    (troop_remove_items, "trp_player", ":quest_target_item", ":item_count"),
    (val_mul, ":quest_gold_reward", ":item_count"),
    (val_div, ":quest_gold_reward", ":quest_target_amount"),
    (call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
    (assign, reg5, ":quest_gold_reward"),
    (assign, ":xp_reward", ":quest_gold_reward"),
    (val_mul, ":xp_reward", 4),
    (add_xp_as_reward, ":xp_reward"),
    (str_store_troop_name, s1, ":quest_giver_troop"),
    (assign, ":debt", "$qst_deliver_wine_debt"),
    (store_sub, ":item_left", ":quest_target_amount", ":item_count"),
    (val_mul, ":debt", ":item_left"),
    (val_div, ":debt", ":quest_target_amount"),
    (val_add, "$debt_to_merchants_guild", ":debt"),
    (quest_get_slot, ":giver_town", "qst_deliver_wine", slot_quest_giver_center),
    (call_script, "script_change_player_relation_with_center", ":giver_town", 1),
    (call_script, "script_end_quest", "qst_deliver_wine"),
    ]],

  [anyone|plyr,"tavernkeeper_talk", [(check_quest_active,"qst_deliver_wine"),
                                     (quest_slot_eq, "qst_deliver_wine", slot_quest_target_center, "$g_encountered_party"),
                                     (quest_get_slot, ":quest_target_item", "qst_deliver_wine", slot_quest_target_item),
                                     (store_item_kind_count, ":item_count", ":quest_target_item"),
                                     (eq, ":item_count", 0),
                                     (quest_get_slot, reg9, "qst_deliver_wine", slot_quest_target_amount),
                                     (str_store_item_name, s4, ":quest_target_item"),
                                     ],
   "I was told to deliver you {reg9} units of {s4}, but I lost the cargo on the way.", "tavernkeeper_deliver_wine_lost",[]],

  [anyone,"tavernkeeper_deliver_wine_lost", [],
 "What? I was waiting for that {s4} for weeks!\
 And now you are telling me that you lost it?\
 You may rest assured that I will let {s1} know about this.", "tavernkeeper_pretalk",
   [(add_xp_as_reward, 40),
    (quest_get_slot, ":quest_target_item", "qst_deliver_wine", slot_quest_target_item),
    (quest_get_slot, ":quest_giver_troop", "qst_deliver_wine", slot_quest_giver_troop),
    (str_store_item_name, s4, ":quest_target_item"),
    (str_store_troop_name, s1, ":quest_giver_troop"),
    (val_add, "$debt_to_merchants_guild", "$qst_deliver_wine_debt"),
    (call_script, "script_end_quest", "qst_deliver_wine"),
   ]],

##  [anyone|plyr,"tavernkeeper_talk", [], "I need to hire some soldiers. Can you help me?", "tavernkeeper_buy_peasants",[]],
##  [anyone,"tavernkeeper_buy_peasants",
##   [
##       (store_encountered_party,reg(3)),
##       (store_faction_of_party,reg(4),reg(3)),
##       (store_relation,reg(5),"fac_player_supporters_faction",reg(4)),
##       (lt, reg(5), -3),
##    ], "I don't think anyone from this town will follow somebody like you. Try your luck elsewhere.", "tavernkeeper_buy_peasants_2",[]],
##  [anyone,"tavernkeeper_buy_peasants", [], "I know a few fellows who would follow you if you paid for their equipment.", "tavernkeeper_buy_peasants_2",[(set_mercenary_source_party,"$tavernkeeper_party"),[change_screen_buy_mercenaries]]],
##  [anyone,"tavernkeeper_buy_peasants_2", [], "Anything else?", "tavernkeeper_talk",[]],
##
##  [anyone|plyr,"tavernkeeper_talk", [], "I want to rest for a while.", "tavernkeeper_rest",[]],
###  [anyone,"tavernkeeper_rest", [], "Of course... How long do you want to rest?", "tavernkeeper_rest_2",[]],
##  [anyone,"tavernkeeper_rest",
##   [
##       (store_encountered_party,reg(3)),
##       (store_faction_of_party,reg(4),reg(3)),
##       (store_relation,reg(5),"fac_player_supporters_faction",reg(4)),
##       (lt, reg(5), -3),
##      ], "You look like trouble stranger. I can't allow you to stay for the night. No.", "close_window",
##   []],
##  [anyone,"tavernkeeper_rest", [], "Of course... That will be {reg3} denars for the room and food. How long do you want to rest?", "tavernkeeper_rest_2",
##   [(store_party_size,reg(3)),
##    (val_add,reg(3),1),
##    (val_div,reg(3),3),
##    (val_max,reg(3),1),
##    (assign,"$tavern_rest_cost",reg(3))]],
##  [anyone|plyr,"tavernkeeper_rest_2", [(store_time_of_day,reg(1)),
##                                       (val_add,reg(1),7),
##                                       (val_mod,reg(1),24),
##                                       (lt,reg(1),12),
##                                       (store_troop_gold,reg(8),"trp_player"),
##                                       (ge,reg(8),"$tavern_rest_cost"),
##                                       ],
##   "I want to rest until morning.", "close_window",
##   [(assign, reg(2), 13),(val_sub,reg(2),reg(1)),(assign, "$g_town_visit_after_rest", 1),(rest_for_hours, reg(2)),(troop_remove_gold, "trp_player","$tavern_rest_cost"),(call_script, "script_change_player_party_morale", 2)]],
##  [anyone|plyr,"tavernkeeper_rest_2", [(store_time_of_day,reg(1)),
##                                       (val_add,reg(1),7),
##                                       (val_mod,reg(1),24),
##                                       (ge,reg(1),12),
##                                       (store_troop_gold,reg(8),"trp_player"),
##                                       (ge,reg(8),"$tavern_rest_cost"),
##                                       ],
##   "I want to rest until evening.", "close_window",
##   [(assign, reg(2), 28),(val_sub,reg(2),reg(1)),(assign, "$g_town_visit_after_rest", 1),(rest_for_hours, reg(2)),(troop_remove_gold, "trp_player","$tavern_rest_cost"),(call_script, "script_change_player_party_morale", 2)]],
##  [anyone|plyr,"tavernkeeper_rest_2", [], "Forget it.", "close_window",[]],

  [anyone|plyr,"tavernkeeper_talk", [
      (store_current_hours,":cur_hours"),
      (val_sub, ":cur_hours", 24),
      (gt, ":cur_hours", "$buy_drinks_last_time"),
	  ##diplomacy start+ Replace with cultural equivalent
	  ##OLD:
      #], "I'd like to buy every man who comes in here tonight a jar of your best wine.", "tavernkeeper_buy_drinks",[]],
	  ##NEW:
	  (call_script, "script_dplmc_print_cultural_word_to_sreg", "$g_talk_troop", DPLMC_CULTURAL_TERM_TAVERNWINE, 0),
	  ], "I'd like to buy every man who comes in here tonight a jar of your best {s0}.", "tavernkeeper_buy_drinks",[]],
	  ##diplomacy end+

  [anyone,"tavernkeeper_buy_drinks",
   [
    ], "Of course, {my lord/my lady}. I reckon {reg5} denars should be enough for that. What should I tell the lads?", "tavernkeeper_buy_drinks_2",[
        (assign, "$temp", 1000),
        (assign, reg5, "$temp"),
        ]],

  [anyone|plyr,"tavernkeeper_buy_drinks_2",
   [
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", "$temp"),
        (str_store_party_name, s10, "$current_town"),
    ], "Let everyone know of the generosity of {playername} to the people of {s10}.", "tavernkeeper_buy_drinks_end",[

        ]],

  [anyone,"tavernkeeper_buy_drinks_end",
  ##diplomacy start+ Replace {sir/madam} with {s0}
   #[], "Don't worry {sir/madam}. Your name will be cheered and toasted here all night.", "tavernkeeper_pretalk",
   [(call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$current_town"),
   ], "Don't worry {s0}. Your name will be cheered and toasted here all night.", "tavernkeeper_pretalk",   
   ##diplomacy end+
   [
       (troop_remove_gold, "trp_player", "$temp"),
       (call_script, "script_change_player_relation_with_center", "$current_town", 1),
       (store_current_hours,":cur_hours"),
       (assign, "$buy_drinks_last_time", ":cur_hours"),
       ]],
  
#LAZERAS MODIFIED  {buy troops drinks}
#----------------------------------------------------------------------------------
  [anyone|plyr,"tavernkeeper_talk", [
      (store_current_hours,":cur_hours"),
      (val_sub, ":cur_hours", 24),
      (gt, ":cur_hours", "$buy_drinks_last_time"),
      ], "I'd like to buy me and my men a barrel of your best ale.", "tavernkeeper_buy_drinks_troops",[]],
  [anyone,"tavernkeeper_buy_drinks_troops",
   [
    ], "Of course, {my lord/my lady}. I reckon {reg5} denars should be enough for that. What should I tell the lads?", "tavernkeeper_buy_drinks_troops_2",[
        (assign, "$temp", 20),
      (store_party_size_wo_prisoners, reg5, "p_main_party"),
      (store_mul, "$temp", "$temp", reg5),
        (assign, reg5, "$temp"),
        ]],
  [anyone|plyr,"tavernkeeper_buy_drinks_troops_2",
   [
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", "$temp"),
        (str_store_party_name, s10, "$current_town"),
    ], "The price is fair enough, let my men have at it.", "tavernkeeper_buy_drinks_troops_end",[
        ]],
  [anyone,"tavernkeeper_buy_drinks_troops_end",
   [], "Don't worry {sir/madam}. Your men will enjoy their pints.", "tavernkeeper_pretalk",
   [
       (troop_remove_gold, "trp_player", "$temp"),
      (call_script, "script_change_player_party_morale", 20),
       (store_current_hours,":cur_hours"),
       (assign, "$buy_drinks_last_time", ":cur_hours"),
      (rest_for_hours, 2, 5, 0)
       ]],
  [anyone|plyr,"tavernkeeper_buy_drinks_troops_2", [], "Actually, cancel that order.", "tavernkeeper_pretalk",[]],
#----------------------------------------------------------------------------------
#LAZERAS MODIFIED  {buy troops drinks}  
  
  [anyone|plyr,"tavernkeeper_buy_drinks_2", [], "Actually, cancel that order.", "tavernkeeper_pretalk",[]],

  [anyone|plyr,"tavernkeeper_talk", [
  (neq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
  ],
   "Have you heard of anyone in this realm who might have a job for a {man/woman} like myself?", "tavernkeeper_job_ask",[
   ]],

  [anyone,"tavernkeeper_job_ask",
   [
	(str_store_string, s9, "str__of_course_the_land_is_currently_at_peace_so_you_may_have_better_luck_in_other_realms"),
	(try_for_range, ":faction", kingdoms_begin, kingdoms_end),
		(store_relation, ":relation", "$g_encountered_party_faction", ":faction"),
		(lt, ":relation", 0),
		(str_clear, s9),
	(try_end),
	(faction_get_slot, ":leader",  "$g_encountered_party_faction", slot_faction_leader),
	(str_store_troop_name, s10, ":leader"),
	##diplomacy start+ Fix pronoun "his" -> {reg0?her:his}
	(call_script, "script_dplmc_store_troop_is_female", ":leader"),
   ], "Hmm... Well, {s10} is often looking for mercenaries to fight in {reg0?her:his} wars.{s9}", "tavernkeeper_job_search",
   ##diplomacy end+
    [
   (assign, "$g_troop_list_no", 0),
    ]],


  [anyone, "tavernkeeper_job_search",
  [],
  "Let me think some more...", "tavernkeeper_job_result",
  [
    (call_script, "script_npc_find_quest_for_player_to_s11", "$g_encountered_party_faction"),
	(assign, ":quest_giver", reg0),

	(call_script, "script_get_dynamic_quest", ":quest_giver"),
	(assign, ":quest_type", reg0),

	(try_begin),
		(gt, ":quest_giver", -1),
		(str_store_troop_name, s7, ":quest_giver"),
		(str_clear, s9), #location string

		(assign, ":location", -1),
		(try_begin),
			(troop_slot_eq, ":quest_giver", slot_troop_occupation, slto_kingdom_hero),
			(troop_get_slot, ":quest_giver_party", ":quest_giver", slot_troop_leaded_party),
			(party_is_active, ":quest_giver_party"),
			(party_get_attached_to, ":location", ":quest_giver_party"),
		(else_try),
			(is_between, ":quest_giver", mayors_begin, mayors_end),
			(try_for_range, ":town", towns_begin, towns_end),
				(party_slot_eq, ":town", slot_town_elder, ":quest_giver"),
				(assign, ":location", ":town"),
			(try_end),
		(try_end),

		(try_begin),
			(gt, ":location", -1),
			(try_begin),
				(eq, ":location", "$g_encountered_party"),
				(str_store_string, s8, "str_here"),
			(else_try),
				(str_store_string, s8, "str_over"),
			(try_end),
			(str_store_party_name, s12, ":location"),
			(str_store_string, s9, "str_s8_in_s12"),
		(try_end),

		##diplomacy start+ Do this first
		(call_script, "script_dplmc_store_troop_is_female_reg", ":quest_giver", 4),
		##diplomacy end+
		(try_begin),
			(eq, ":quest_type", "qst_track_down_bandits"),
			(str_store_string, s10, "str__has_put_together_a_bounty_on_some_bandits_who_have_been_attacking_travellers_in_the_area"),
		(else_try),
			(eq, ":quest_type", "qst_destroy_bandit_lair"),
			(str_store_string, s10, "str__has_been_worried_about_bandits_establishing_a_hideout_near_his_home"),
		(else_try),
			(eq, ":quest_type", "qst_retaliate_for_border_incident"),
			(str_store_string, s10, "str__is_looking_for_a_way_to_avoid_an_impending_war"),
		(else_try),
			(eq, ":quest_type", "qst_rescue_prisoner"),
			(str_store_string, s10, "str__may_need_help_rescuing_an_imprisoned_family_member"),
		(else_try),
			(eq, ":quest_type", "qst_cause_provocation"),
			(str_store_string, s10, "str__has_been_asking_around_for_someone_who_might_want_work_id_watch_yourself_with_him_though"),
		(else_try),
			(str_store_string, s10, "str_tavernkeeper_invalid_quest"),
		(try_end),

		##diplomacy start+
		#(troop_get_type, reg4, ":quest_giver"),
		(call_script, "script_dplmc_store_troop_is_female_reg", ":quest_giver", 4),
		##diplomacy end+
	(try_end),

  ]],


  [anyone, "tavernkeeper_job_result", [
  	(store_sub, ":last_troop", mayors_end, 1),
	(lt, "$g_troop_list_no", ":last_troop"),
  ], "I have heard that {s7} {s9}{s10} You may want to speak with {reg4?her:him}.", "tavernkeeper_job_search",
   [
       ]],

  [anyone, "tavernkeeper_job_result", [
  (store_sub, ":last_troop", mayors_end, 1),
  (ge, "$g_troop_list_no", ":last_troop"),
  ], "There may be other work, of course -- lords and guildmasters often have other tasks which we don't hear about. Also, the villages around here frequently need help, although they'd be more likely to pay you with a wedge of cheese and goodwill than with cold hard denars.", "tavernkeeper_job_result_2",
   [
       ]],

  [anyone,"tavernkeeper_job_result_2", [], "I'll keep my ears open for other opportunities. You may want to ask again from time to time.", "close_window",[]],



  [anyone|plyr,"tavernkeeper_talk", [], "I guess I should leave now.", "close_window",[]],

#Tavern Talk (with companions)
#  [anyone, "companion_recruit_yes", [(neg|hero_can_join, "p_main_party"),], "I don't think can lead any more men than you do now.\
# You need to release someone from service if you want me to join your party.", "close_window", []],




#Tavern Talk (with ransom brokers)


  [anyone,"start", [(is_between, "$g_talk_troop", ransom_brokers_begin, ransom_brokers_end),
                    (eq, "$g_talk_troop_met", 0),
					##diplomacy start+
					#Use proper style of address in lieu of sir/madam if necessary (althoguh since these first-time
					#meetings are likely to occur near the game's start, this will usually not make a difference).
					(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),#Write {sir/madame} or replacement to {s0}
					],
   "Greetings to you, {s0}. You look like someone who should get to know me.", "ransom_broker_intro",[]],#changed {sir/madam} to {s0}
   ##diplomacy end+

  [anyone|plyr,"ransom_broker_intro",[], "Why is that?", "ransom_broker_intro_2",[]],
  [anyone, "ransom_broker_intro_2", [], "I broker ransoms for the poor wretches who are captured in these endless wars.\
 Normally I travel between the salt mines and the slave markets on the coast, on commission from those whose relatives have gone missing.\
 But if I'm out on my errands of mercy, and I come across a fellow dragging around a captive or two,\
 well, there's no harm in a little speculative investment, is there?\
 And you look like the type who might have a prisoner to sell.", "ransom_broker_info_talk",[(assign, "$ransom_broker_families_told",0),
                                                                                            (assign, "$ransom_broker_prices_told",0),
                                                                                            (assign, "$ransom_broker_ransom_me_told",0),
                                                                                            ]],

  [anyone|plyr,"ransom_broker_info_talk",[(eq, "$ransom_broker_families_told",0)], "What if their families can't pay?", "ransom_broker_families",[]],
  [anyone, "ransom_broker_families", [], "Oh, then I spin them a few heartwarming tales of life on the galleys.\
 You'd be surprised what sorts of treasures a peasant can dig out of his cowshed or wheedle out of his cousins,\
 assuming he's got the proper motivation!\
 And if in the end they cannot come up with the silver, then there are always slave merchants who are looking for galley slaves.\
 One cannot do Heaven's work with an empty purse, you see.", "ransom_broker_info_talk",[(assign, "$ransom_broker_families_told",1)]],
  [anyone|plyr,"ransom_broker_info_talk",[(eq, "$ransom_broker_prices_told",0)], "What can I get for a prisoner?", "ransom_broker_prices",[]],
  [anyone, "ransom_broker_prices", [], "It varies. I fancy that I have a fine eye for assessing a ransom.\
 There are a dozen little things about a man that will tell you whether he goes to bed hungry, or dines each night on soft dumplings and goose.\
 The real money of course is in the gentry, and if you ever want to do my job you'll want to learn about every landowning family in Calradia,\
 their estates, their heraldry, their offspring both lawful and bastard, and, of course, their credit with the merchants.", "ransom_broker_info_talk",[(assign, "$ransom_broker_prices_told",1)]],
  [anyone|plyr,"ransom_broker_info_talk",[(eq, "$ransom_broker_ransom_me_told",0)], "Would you be able to ransom me if I were taken?", "ransom_broker_ransom_me",[]],
  [anyone, "ransom_broker_ransom_me", [], "Of course. I'm welcome in every court in Calradia.\
 There's not many who can say that! So always be sure to keep a pot of denars buried somewhere,\
 and a loyal servant who can find it in a hurry.", "ransom_broker_info_talk",[(assign, "$ransom_broker_ransom_me_told",1)]],
  [anyone|plyr,"ransom_broker_info_talk",[], "That's all I need to know. Thank you.", "ransom_broker_pretalk",[]],

  [anyone,"start", [(is_between, "$g_talk_troop", ransom_brokers_begin, ransom_brokers_end),
  ],
   "Greetings. If you have any prisoners, I will be happy to buy them from you.", "ransom_broker_talk",[]],
  [anyone,"ransom_broker_pretalk", [],
   "Anyway, if you have any prisoners, I will be happy to buy them from you.", "ransom_broker_talk",[]],

  [anyone|plyr,"ransom_broker_talk",
   [[store_num_regular_prisoners,reg(0)],[ge,reg(0),1]],
   "Then you'd better bring your purse. I have got prisoners to sell.", "ransom_broker_sell_prisoners",[]],
  ## CC
  ##diplomacy start+
  [anyone|plyr,"ransom_broker_talk",
   [(store_num_regular_prisoners,reg0),(ge,reg0,1)],
   "I want to sell all the prisoners I have with me.", "ransom_broker_sell_prisoners_all",[]],
  [anyone,"ransom_broker_sell_prisoners_all", [
  (call_script, "script_dplmc_sell_all_prisoners", 0, 0),#do not actually sell
  (store_num_regular_prisoners, reg2),
  (val_sub, reg2, 1),
  ],
  "Let's see...  I'll give you {reg0} denars for your {reg1} {reg2?prisoners:prisoner}.  Do we have a deal?", "ransom_broker_sell_prisoners_all_2", []],
  [anyone|plyr,"ransom_broker_sell_prisoners_all_2", [],
   "We have a deal.", "ransom_broker_sell_prisoners_2", [(call_script, "script_dplmc_sell_all_prisoners", 1, 0),]
  ],
  [anyone|plyr,"ransom_broker_sell_prisoners_all_2", [],
   "Let me think about it again.", "ransom_broker_pretalk",[]],
  ##diplomacy end+
  ## CC
  [anyone|plyr,"ransom_broker_talk", [], "Tell me about what you do again.", "ransom_broker_intro_2",[]],


  [anyone|plyr,"ransom_broker_talk",[
  ], "I wish to ransom one of my companions.", "ransom_broker_ransom_companion",[]],

  [anyone,"ransom_broker_ransom_companion",[], "Whom do you wish to ransom?", "ransom_broker_ransom_companion_choose",[]],

  [anyone|plyr|repeat_for_troops,"ransom_broker_ransom_companion_choose",[
  (store_repeat_object, ":imprisoned_companion"),
  (neg|troop_slot_eq, ":imprisoned_companion", slot_troop_occupation, slto_kingdom_hero),
  (is_between, ":imprisoned_companion", companions_begin, companions_end),
  (troop_slot_ge, ":imprisoned_companion", slot_troop_prisoner_of_party, centers_begin),
  (str_store_troop_name, s4, ":imprisoned_companion"),
  ], "{s4}", "ransom_broker_ransom_companion_name_sum",[

  (store_repeat_object, "$companion_to_be_ransomed"),
  ]],

  [anyone|plyr,"ransom_broker_ransom_companion_choose",[
  ], "Never mind", "ransom_broker_pretalk",[]],


  [anyone,"ransom_broker_ransom_companion_name_sum",[], "Let me check my ledger, here... Yes. Your friend is being held in the dungeon at {s7}. How interesting! I remember hearing that the rats down there are unusually large -- like mastiffs, they say... Now... For the very reasonable sum of {reg5} denars, which includes both the ransom and my commission and expenses, we can arrange it so that {s5} can once again enjoy {reg4?her:his} freedom. What do you say?", "ransom_broker_ransom_companion_verify",[
  (str_store_troop_name, s5, "$companion_to_be_ransomed"),
  ##diplomacy start+
  #(troop_get_type, reg4, "$companion_to_be_ransomed"),
  (call_script, "script_dplmc_store_troop_is_female_reg", "$companion_to_be_ransomed", 4),
  ##diplomacy end+

  (troop_get_slot, ":prison_location", "$companion_to_be_ransomed", slot_troop_prisoner_of_party),
  (str_store_party_name, s7, ":prison_location"),

  (store_character_level, ":companion_level", "$companion_to_be_ransomed"),
  (store_add, "$companion_ransom_amount", ":companion_level", 20),
  (val_mul, "$companion_ransom_amount", ":companion_level"),
  (val_mul, "$companion_ransom_amount", 5), #Level 1: 110, level 40: 12,000
  (assign, reg5, "$companion_ransom_amount"),
  ]],

  [anyone|plyr,"ransom_broker_ransom_companion_verify",[
  (store_troop_gold, ":player_gold", "trp_player"),
  (ge, ":player_gold", "$companion_ransom_amount"),

  ], "Here's your money.", "ransom_broker_ransom_companion_accept",[
  (troop_remove_gold, "trp_player", "$companion_ransom_amount"),

  (troop_set_slot, "$companion_to_be_ransomed", slot_troop_occupation, slto_player_companion),
  (troop_set_slot, "$companion_to_be_ransomed", slot_troop_current_mission, npc_mission_rejoin_when_possible),
  (troop_set_slot, "$companion_to_be_ransomed", slot_troop_days_on_mission, 1),
  
   (try_begin),
	(troop_get_slot, ":held_at_prison", "$companion_to_be_ransomed", slot_troop_prisoner_of_party),
	##diplomacy start+ give ransom to one who was imprisoning the companion
	(try_begin),
		(is_between, ":held_at_prison", centers_begin, centers_end),
		(party_get_slot, ":town_lord", ":held_at_prison", slot_town_lord),
		(is_between, ":town_lord", heroes_begin, heroes_end),
		(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", "$companion_ransom_amount", ":town_lord"),
	(else_try),
	    #if the center has no lord, split it among the faction
		(store_faction_of_party, ":prison_faction", ":held_at_prison"),
		(call_script, "script_dplmc_faction_leader_splits_gold", ":prison_faction", "$companion_ransom_amount"),
	(try_end),
	##diplomacy end+
	(party_count_prisoners_of_type, ":holding_as_prisoner",  ":held_at_prison", "$companion_to_be_ransomed"),
	(gt, ":holding_as_prisoner", 0),
	(party_remove_prisoners, ":held_at_prison", "$companion_to_be_ransomed", 1),
  (try_end),
  (troop_set_slot, "$companion_to_be_ransomed", slot_troop_prisoner_of_party, -1),

  (troop_set_slot, "$companion_to_be_ransomed", slot_troop_personalityclash_penalties, 0),
  (troop_set_slot, "$companion_to_be_ransomed", slot_troop_morality_penalties, 0),

  ]],

  [anyone|plyr,"ransom_broker_ransom_companion_verify",[
  ], "I can't afford that right now.", "ransom_broker_ransom_companion_refuse",[]],


  [anyone,"ransom_broker_ransom_companion_accept",[], "Splendid! In a few days, I would think, you should find {s5} riding to rejoin you, blinking in the sunlight and no doubt very grateful! Is there any other way in which I can help you?", "ransom_broker_talk",[
  (str_store_troop_name, s5, "$companion_to_be_ransomed"),

  ]],

  [anyone,"ransom_broker_ransom_companion_refuse",[], "Of course, of course... Never mind what they say about the rats, by the way -- I've never actually seen one myself, on account of the pitch-black darkness. Anyway, I'm sure that {s5} will understand why it's important for you to control expenditures. Now... Was there anything else?", "ransom_broker_talk",[
  (str_store_troop_name, s5, "$companion_to_be_ransomed"),
  ]],


  [anyone|plyr,"ransom_broker_talk",[], "Not this time. Good-bye.", "close_window",[]],
  [anyone,"ransom_broker_sell_prisoners", [],
  "Let me see what you have...", "ransom_broker_sell_prisoners_2",
   [[change_screen_trade_prisoners]]],
#  [anyone, "ransom_broker_sell_prisoners_2", [], "You take more prisoners, bring them to me. I will pay well.", "close_window",[]],
  [anyone, "ransom_broker_sell_prisoners_2", [], "I will be staying here for a few days. Let me know if you need my services.", "close_window",[]],


#Tavern Talk (with travelers)
  [anyone, "start", [(is_between, "$g_talk_troop", tavern_travelers_begin, tavern_travelers_end),
                     (str_store_troop_name, s10, "$g_talk_troop"),
                     (eq,"$g_talk_troop_met",0),
                     ],
   "Greetings, friend. You look like the kind of {man/person} who'd do well to know me.\
 I travel a lot all across Calradia and keep an open ear.\
 I can provide you information that you might find useful. For a meager price of course.", "tavern_traveler_talk", [(assign, "$traveler_land_asked", 0)]],

  [anyone, "start",
   [
     (is_between, "$g_talk_troop", tavern_travelers_begin, tavern_travelers_end),
     (gt, "$last_lost_companion", 0),
     (assign, ":companion_found_town", -1),
     (troop_get_slot, ":companion_found_town", "$last_lost_companion", slot_troop_cur_center),
     (is_between, ":companion_found_town", towns_begin, towns_end),
     (str_store_troop_name, s10, "$last_lost_companion"),
     (str_store_party_name, s11, ":companion_found_town"),
     ],
   "Greetings, {playername}. I saw your companion {s10} at a tavern in {s11} some days ago. I thought you might like to know.", "tavern_traveler_lost_companion_thanks",
   [(assign, "$last_lost_companion", 0)]],

  [anyone|plyr, "tavern_traveler_lost_companion_thanks", [(troop_get_type, reg3, "$last_lost_companion")], "Thanks. I'll go and find {reg3?her:him} there.", "tavern_traveler_pretalk", []],
  [anyone|plyr, "tavern_traveler_lost_companion_thanks", [], "Thanks, but I don't really care.", "tavern_traveler_pretalk", []],

  [anyone, "start", [(is_between, "$g_talk_troop", tavern_travelers_begin, tavern_travelers_end),
                     ],
   "Greetings, {playername}.", "tavern_traveler_talk", [(assign, "$traveler_land_asked", 0)]],



  [anyone, "tavern_traveler_pretalk", [], "Yes?", "tavern_traveler_talk", []],

  [anyone|plyr, "tavern_traveler_talk", [(eq, "$traveler_land_asked", 0)], "What can you tell me about this land?", "tavern_traveler_tell_kingdoms", [(assign, "$traveler_land_asked", 1)]],
  [anyone, "tavern_traveler_tell_kingdoms", [], "Calradia is divided into rival kingdoms, which can neither manage to live in peace with their neighbours,\
 nor completely eliminate them.\
 As a result, there's seldom a break to the bitter wars which plague this land and drain its life blood.\
 Well, at least this must be a good place to be for an adventurer such as yourself.\
 With some luck and skill, you can make a name for yourself here, amass a fortune perhaps, or gain great power.\
 Opportunities are endless and so are the rewards, if you are willing to risk your life for them.", "tavern_traveler_tell_kingdoms_2", []],

  [anyone|plyr, "tavern_traveler_tell_kingdoms_2", [], "Tell me more about these opportunities.", "tavern_traveler_tell_kingdoms_3", []],
  [anyone|plyr, "tavern_traveler_tell_kingdoms_2", [], "Thank you. That was all I needed to know.", "close_window", []],

  [anyone, "tavern_traveler_tell_kingdoms_3", [(gt, "$player_has_homage", 0)], "Well, you probably know everything I could tell you already. You seem to be doing pretty well.",
   "tavern_traveler_tell_kingdoms_4", []],
  [anyone, "tavern_traveler_tell_kingdoms_3", [], "The kingdoms will pay good money for mercenaries if they are engaged in a war.\
 If you have done a bit of fighting, speaking with one of their lords will probably result in being offered a mercenary contract.\
 However the real rewards come if you can manage to become a vassal to a king.\
 A vassal can own villages, castles and towns and get rich with the taxes and revenues of these estates.\
 Normally, only nobles of the realm own land in this way,\
 but in time of war, a king will not hesitate to accept someone who distinguishes {himself/herself} on the battlefield as a vassal, and grant {him/her} the right to own land.",
   "tavern_traveler_tell_kingdoms_4a", []],

  [anyone, "tavern_traveler_tell_kingdoms_4a", [], "It is not unheard-of for adventurers to renounce allegiance to a Calradian king altogether, declare themselves kings, and claim land in their own name. This is a difficult path, however, as the great nobles of the land, with their long ancestries, are not likely to accept such upstarts as their monarch. Such rulers would need to be very careful in establishing their right to rule, or they would be set upon from all sides.",
   "tavern_traveler_tell_kingdoms_4", []],


  [anyone, "tavern_traveler_tell_kingdoms_4", [], "It might be easier for an adventurer like yourself to pledge support to an existing king's rival.\
  There are many such pretenders in Calradia -- those who are born to the right family, who go around and stir up trouble saying they have a better claim to the throne than the current king.\
 If those claim holders could find supporters, they could easily start civil wars and perhaps even replace the king one day.",
   "tavern_traveler_tell_kingdoms_5", []],

  [anyone|plyr, "tavern_traveler_tell_kingdoms_5", [], "Interesting. Where can I find these claim holders?", "tavern_traveler_tell_kingdoms_6", []],
  [anyone|plyr, "tavern_traveler_tell_kingdoms_5", [], "I guess I heard enough already. Thank you.", "close_window", []],

  [anyone, "tavern_traveler_tell_kingdoms_6", [], "A claim holder's life would be in danger in his own country of course.\
 Therefore, they usually stay at rival courts, raising support and hoping to find someone willing to champion their cause.\
 I usually hear news about some of them, and may be able to tell you their location with some precision.\
 But of course, I would ask for a little something for such a service.",
   "tavern_traveler_pretalk", [(assign, "$traveller_claimants_mentioned", 1)]],

  [anyone|plyr, "tavern_traveler_talk", [(eq, "$traveller_claimants_mentioned", 1)], "I want to know the location of a claimant.", "tavern_traveler_pretender_location", []],
  [anyone, "tavern_traveler_pretender_location", [], "Whose location do you want to know?", "tavern_traveler_pretender_location_ask", []],

  [anyone|plyr|repeat_for_troops, "tavern_traveler_pretender_location_ask",
   [
     (store_repeat_object, ":troop_no"),
     (is_between, ":troop_no", pretenders_begin, pretenders_end),
     (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
     (troop_slot_ge, ":troop_no", slot_troop_cur_center, 1),
     (str_store_troop_name, s11, ":troop_no"),
     (neq, ":troop_no", "$supported_pretender"),
     ],  "{s11}", "tavern_traveler_pretender_location_ask_2",
   [
     (store_repeat_object, "$temp"),
     ]],

  [anyone|plyr, "tavern_traveler_pretender_location_ask",
   [],  "Never mind.", "tavern_traveler_pretalk", []],


  [anyone, "tavern_traveler_pretender_location_ask_2", [], "I can reveal this information to you for a small price, let's say 30 denars.", "tavern_traveler_pretender_location_ask_money", []],

  [anyone|plyr, "tavern_traveler_pretender_location_ask_money",
   [
     (store_troop_gold, ":cur_gold", "trp_player"),
     (ge, ":cur_gold", 30),
   ],
   "All right. Here is 30 denars.", "tavern_traveler_pretender_location_tell",
   [
     (troop_remove_gold, "trp_player", 30),
   ]],

  [anyone|plyr, "tavern_traveler_pretender_location_ask_money", [], "Never mind.", "tavern_traveler_pretalk", []],

  [anyone, "tavern_traveler_pretender_location_tell", [], "{s15} is currently at {s11}.", "tavern_traveler_pretalk",
   [
     (str_store_troop_name, s15, "$temp"),
     (troop_get_slot, ":cur_center", "$temp", slot_troop_cur_center),
     (str_store_party_name, s11, ":cur_center"),
   ]],

  ##diplomacy start+
  #The tavern travellers can give the locations of than just pretenders and
  #the player's former travelling companions.  I've decided to add book sellers
  #and ransom brokers, but not lords.
  #Another alteration is that only booksellers / ransom brokers the player has
  #met can be located.
  #Code credit to rubik's Custom Commander
  # CC
  [anyone|plyr, "tavern_traveler_talk", [], "I am looking for book merchants...", "tavern_traveler_bookseller_location", []],

  [anyone, "tavern_traveler_bookseller_location", 
    [
      (assign, ":num_towns", 0),
      (try_for_range, ":town_no", towns_begin, towns_end),
        (neg|party_slot_eq, ":town_no", slot_center_tavern_bookseller, 0),
        (party_get_slot, ":seller", ":town_no", slot_center_tavern_bookseller),#addition - fixed 2011-03-29
        (troop_slot_ge, ":seller", slot_troop_met, 1),#addition # removed 2011-03-29
        (val_add, ":num_towns", 1),
      (try_end),
      (eq, ":num_towns", 0),
    ], "I am sorry I haven't run across any lately.", "tavern_traveler_pretalk", []],

  [anyone, "tavern_traveler_bookseller_location", [], "I might have crossed paths with one or two recently. For 100 denars, I'll tell you where.", "tavern_traveler_bookseller_location_ask_money", []],

  [anyone|plyr, "tavern_traveler_bookseller_location_ask_money",
   [
     (store_troop_gold, ":cur_gold", "trp_player"),
     (ge, ":cur_gold", 100),
     ], "All right. Here is 100 denars.", "tavern_traveler_bookseller_location_tell",
   [
     (troop_remove_gold, "trp_player", 100),
     ]],

  [anyone|plyr, "tavern_traveler_bookseller_location_ask_money", [], "Never mind.", "tavern_traveler_pretalk", []],

  [anyone, "tavern_traveler_bookseller_location_tell", [], "You can find them at {s11}.", "tavern_traveler_pretalk",
   [
      (assign, ":num_towns", 0),
      (try_for_range, ":town_no", towns_begin, towns_end),
        (neg|party_slot_eq, ":town_no", slot_center_tavern_bookseller, 0),
        (party_get_slot, ":seller", ":town_no", slot_center_tavern_bookseller),#addition - fixed 2011-03-29
        (troop_slot_ge, ":seller", slot_troop_met, 1),#addition
        (val_add, ":num_towns", 1),
        (try_begin),
          (eq, ":num_towns", 1),
          (str_store_party_name, s11, ":town_no"),
        (else_try),
          (eq, ":num_towns", 2),
          (str_store_party_name, s12, ":town_no"),
          (str_store_string, s11, "@{s12} and {s11}"),
        (try_end),
      (try_end),
      (display_message, "@You can find book merchants at {s11}."),
     ]],
    
  [anyone|plyr, "tavern_traveler_talk", [], "I am looking for ransom brokers...", "tavern_traveler_ransom_broker_location", []],

  [anyone, "tavern_traveler_ransom_broker_location", 
    [
      (assign, ":num_towns", 0),
      (try_for_range, ":town_no", towns_begin, towns_end),
        (neq, ":town_no", "p_town_2"),
        (neg|party_slot_eq, ":town_no", slot_center_ransom_broker, 0),
        (party_get_slot, ":broker", ":town_no", slot_center_ransom_broker),#addition - fixed 2011-03-29
        (troop_slot_ge, ":broker", slot_troop_met, 1),#addition
        (val_add, ":num_towns", 1),
      (try_end),
      (eq, ":num_towns", 0),
    ], "I am sorry I haven't run across any lately.", "tavern_traveler_pretalk", []],

  [anyone, "tavern_traveler_ransom_broker_location", [], "I know where they are. For 50 denars, I'll tell you.", "tavern_traveler_ransom_broker_location_ask_money", []],

  [anyone|plyr, "tavern_traveler_ransom_broker_location_ask_money",
   [
     (store_troop_gold, ":cur_gold", "trp_player"),
     (ge, ":cur_gold", 50),
     ], "All right. Here is 50 denars.", "tavern_traveler_ransom_broker_location_tell",
   [
     (troop_remove_gold, "trp_player", 50),
     ]],

  [anyone|plyr, "tavern_traveler_ransom_broker_location_ask_money", [], "Never mind.", "tavern_traveler_pretalk", []],

  [anyone, "tavern_traveler_ransom_broker_location_tell", [], "You can find them at {s11}.", "tavern_traveler_pretalk",
   [
      (assign, ":num_towns", 0),
      (try_for_range, ":town_no", towns_begin, towns_end),
        (neq, ":town_no", "p_town_2"),
        (neg|party_slot_eq, ":town_no", slot_center_ransom_broker, 0),
        (party_get_slot, ":broker", ":town_no", slot_center_ransom_broker),#addition - fixed 2011-03-29
        (troop_slot_ge, ":broker", slot_troop_met, 1),#addition # removed 2011-03-29
        (val_add, ":num_towns", 1),
        (try_begin),
          (eq, ":num_towns", 1),
          (str_store_party_name, s11, ":town_no"),
        (else_try),
          (str_store_party_name, s12, ":town_no"),
          (eq, ":num_towns", 2),
          (str_store_string, s11, "@{s12} and {s11}"),
        (else_try),
          (str_store_string, s11, "@{s12}, {s11}"),
        (try_end),
      (try_end),
      (display_message, "@You can find ransom brokers at {s11}."),
     ]],
  # CC
  ##diplomacy end+
  
	  ##diplomacy start+
	#Allow another method of revtrieving dismissed employees
		[anyone|plyr, "tavern_traveler_talk", [
	#Verify that the player in fact has dismissed employees, who are not
	#already on their way back.  Also verify that the player is capable
	#of taking them back.
	(assign, ":player_village", villages_end),
	(assign, ":player_castle", castles_end),
	(assign, ":player_town", towns_end),
	(try_for_range, ":center_no", villages_begin, ":player_village"),
		(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
		(assign, ":player_village", ":center_no"),#assign and break loop
	(try_end),
	(try_for_range, ":center_no", castles_begin, ":player_castle"),
		(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
		(assign, ":player_castle", ":center_no"),#assign and break loop
	(try_end),
	(try_for_range, ":center_no", towns_begin, ":player_town"),
		(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
		(assign, ":player_town", ":center_no"),#assign and break loop
	(try_end),

	(assign, ":exist_contactable_employees", 0),
	(try_begin),
	#Chamberlain?
		(eq, "$g_player_chamberlain", -1),
		(neg|troop_slot_eq, "trp_dplmc_chamberlain", slot_troop_met, 0),
		(this_or_next|is_between, ":player_village", villages_begin, villages_end),
		(this_or_next|is_between, ":player_castle", castles_begin, castles_end),
	   (is_between, ":player_town", towns_begin, towns_end),
		(assign, ":exist_contactable_employees", 1),
	(else_try),
	#Constable?
		(eq, "$g_player_constable", -1),
		(neg|troop_slot_eq, "trp_dplmc_constable", slot_troop_met, 0),
		(this_or_next|is_between, ":player_castle", castles_begin, castles_end),
	   (is_between, ":player_town", towns_begin, towns_end),
		(assign, ":exist_contactable_employees", 1),
	(else_try),
	#Chancellor?
		(eq, "$g_player_chancellor", -1),
		(neg|troop_slot_eq, "trp_dplmc_chancellor", slot_troop_met, 0),
		(is_between, ":player_town", towns_begin, towns_end),
		(assign, ":exist_contactable_employees", 1),
	(try_end),

	(neq, ":exist_contactable_employees", 0),

	], "I am looking for one of my former employees...", "dplmc_tavern_traveler_employee_1", []],

	  [anyone, "dplmc_tavern_traveler_employee_1", [], "Maybe I can help you. Who are you looking for?", "dplmc_tavern_traveler_employee_2", []],

	[anyone|plyr, "dplmc_tavern_traveler_employee_2",
	[
	#Check is chamberlain dismissed
	(eq, "$g_player_chamberlain", -1),
	(neg|troop_slot_eq, "trp_dplmc_chamberlain", slot_troop_met, 0),
	#Check if chamberlain could return
	(assign, ":player_center", centers_end),
	(try_for_range, ":center_no", centers_begin, ":player_center"),
	   (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
	   (assign, ":player_center", ":center_no"),#set result and break loop
	(try_end),
	(is_between, ":player_center", centers_begin, centers_end),
	(str_store_troop_name, s11, "trp_dplmc_chamberlain"),
	], "My fomer chamberlain, {s11}.", "dplmc_tavern_traveler_employee_3", [
	(assign, "$temp", "trp_dplmc_chamberlain"),
	]],

	[anyone|plyr, "dplmc_tavern_traveler_employee_2",
	[
	#Check is constable dismissed
	(eq, "$g_player_constable", -1),
	(neg|troop_slot_eq, "trp_dplmc_constable", slot_troop_met, 0),
	#Check if constable could return
	(assign, ":player_center", walled_centers_end),
	(try_for_range, ":center_no", walled_centers_begin, ":player_center"),
	   (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
	   (assign, ":player_center", ":center_no"),#set result and break loop
	(try_end),
	(is_between, ":player_center", walled_centers_begin, walled_centers_end),
	(str_store_troop_name, s11, "trp_dplmc_constable"),
	], "My fomer constable, {s11}.", "dplmc_tavern_traveler_employee_3", [
	(assign, "$temp", "trp_dplmc_constable"),
	]],

	[anyone|plyr, "dplmc_tavern_traveler_employee_2",
	[
	#Check is chancellor dismissed
	(eq, "$g_player_chancellor", -1),
	(neg|troop_slot_eq, "trp_dplmc_chancellor", slot_troop_met, 0),
	#Check if chancellor could return
	(assign, ":player_center", towns_end),
	(try_for_range, ":center_no", towns_begin, ":player_center"),
	   (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
	   (assign, ":player_center", ":center_no"),#set result and break loop
	(try_end),
	(is_between, ":player_center", towns_begin, towns_end),
	(str_store_troop_name, s11, "trp_dplmc_chancellor"),
	], "My fomer chancellor, {s11}.", "dplmc_tavern_traveler_employee_3", [
	(assign, "$temp", "trp_dplmc_chancellor"),
	]],

	[anyone|plyr, "dplmc_tavern_traveler_employee_2",
	   [],  "Never mind.", "tavern_traveler_pretalk", []],

	[anyone, "dplmc_tavern_traveler_employee_3",
	[
	(this_or_next|eq, "$temp", "trp_dplmc_chamberlain",),
	(this_or_next|eq, "$temp", "trp_dplmc_constable",),
	   (eq, "$temp", "trp_dplmc_chancellor",),
	(neg|troop_slot_eq, "$temp", slot_troop_occupation, dplmc_slto_dead),
	(neg|troop_slot_eq, "$temp", slot_troop_occupation, slto_kingdom_hero),
	(neg|troop_slot_ge, "$temp", slot_troop_prisoner_of_party, 1),#deliberately not 0, in case of uninitialized slotm

	(try_begin),
	   (eq, "$temp", "trp_dplmc_chamberlain",),
		(assign, "$g_player_chamberlain", 0),
	(else_try),
	   (eq, "$temp", "trp_dplmc_constable",),
	   (assign, "$g_player_constable", 0),
	(else_try),
	   (eq, "$temp", "trp_dplmc_chancellor",),
	   (assign, "$g_player_chancellor", 0),
	(try_end),
	(call_script, "script_dplmc_store_troop_is_female", "$temp"),
	], "I will send word to {reg0?her:him} that you are looking for {reg0?her:him}.",
	"tavern_traveler_pretalk", []],

	#Catch any errors.
	[anyone|plyr, "dplmc_tavern_traveler_employee_3",
	   [],  "I am afraid I'm not able to help you.", "tavern_traveler_pretalk", []],
	##diplomacy end+

  [anyone|plyr, "tavern_traveler_talk", [], "I am looking for one of my companions...", "tavern_traveler_companion_location", []],

  [anyone, "tavern_traveler_companion_location", [], "Maybe I can help you. Who are you looking for?", "tavern_traveler_companion_location_ask", []],

  [anyone|plyr|repeat_for_troops, "tavern_traveler_companion_location_ask",
   [
     (store_repeat_object, ":troop_no"),
     (is_between, ":troop_no", companions_begin, companions_end),

     (troop_slot_ge, ":troop_no", slot_troop_playerparty_history, 1),
##diplomacy start+ Verify that the troops are actually former companions.
     (neg|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
	 (neg|troop_slot_eq, ":troop_no", slot_troop_met, 0),
##diplomacy end+

     (assign, ":continue", 0),
     (try_begin),
       (this_or_next|troop_slot_ge, ":troop_no", slot_troop_cur_center, 1),
       (troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),

       (assign, ":continue", 1),
     (try_end),

     (eq, ":continue", 1),

     (str_store_troop_name, s11, ":troop_no"),
   ],
   "{s11}", "tavern_traveler_companion_location_ask_2",
   [
     (store_repeat_object, "$temp"),
   ]],

  [anyone|plyr, "tavern_traveler_companion_location_ask",
   [],  "Never mind.", "tavern_traveler_pretalk", []],

  [anyone, "tavern_traveler_companion_location_ask_2", [(str_store_troop_name, s15, "$temp")], "I guess I know where {s15} is. For 30 denars, I'll tell you.", "tavern_traveler_companion_location_ask_money", []],

  [anyone|plyr, "tavern_traveler_companion_location_ask_money",
   [
     (store_troop_gold, ":cur_gold", "trp_player"),
     (ge, ":cur_gold", 30),
     ], "All right. Here is 30 denars.", "tavern_traveler_companion_location_tell",
   [
     (troop_remove_gold, "trp_player", 30),
     ]],

  [anyone|plyr, "tavern_traveler_companion_location_ask_money", [], "Never mind.", "tavern_traveler_pretalk", []],

  [anyone, "tavern_traveler_companion_location_tell", [], "{s15} is currently at {s11}.{s12}", "tavern_traveler_pretalk",
   [
     (str_store_troop_name, s15, "$temp"),

     (try_begin),
       (troop_slot_ge, "$temp", slot_troop_cur_center, 1),
       (troop_get_slot, ":cur_center", "$temp", slot_troop_cur_center),
       (str_store_string, s12, "str_space"),
     (else_try),
       (troop_get_slot, ":cur_center", "$temp", slot_troop_prisoner_of_party),

       (try_begin),
         (is_between, ":cur_center", towns_begin, towns_end),
         (str_store_string, s13, "str_town"),
       (else_try),
         (str_store_string, s13, "str_castle"),
       (try_end),
	   (troop_get_type, reg4, "$temp"),
       (str_store_string, s12, "str__but_he_is_holding_there_as_a_prisoner_at_dungeon_of_s13"), #[TODO : Control Grammer] New text, control grammer of text later. s13 can be "castle" or "town".
     (try_end),

	 (try_begin),
		(party_is_active, ":cur_center"),
		(str_store_party_name, s11, ":cur_center"),
	 (else_try),
		(str_store_party_name, s11, "str_prisoner_at_large"),
	 (try_end),
     ]],

  [anyone|plyr, "tavern_traveler_talk", [],
   "Farewell.", "close_window", []],

  [anyone, "start", [(is_between, "$g_talk_troop", tavern_travelers_begin, tavern_travelers_end),
                     (party_get_slot, ":info_faction", "$g_encountered_party", slot_center_traveler_info_faction),
                     (str_store_faction_name, s17, ":info_faction"),
                     ],
   "Greetings. They say you're the kind of {man/woman} who'd be interested to hear that I travel frequently to {s17}. I'll tell you all I know for a mere 100 denars.", "tavern_traveler_answer", []],

  [anyone|plyr, "tavern_traveler_answer", [(store_troop_gold, ":cur_gold", "trp_player"),
                                            (ge, ":cur_gold", 100)],
   "Here's 100 denars. Tell me what you know.", "tavern_traveler_continue", [(party_get_slot, ":info_faction", "$g_encountered_party", slot_center_traveler_info_faction),
                                           (call_script, "script_update_faction_traveler_notes", ":info_faction"),
                                           (change_screen_notes, 2, ":info_faction"),
                                           ]],

  [anyone|plyr, "tavern_traveler_answer", [],
   "Sorry friend. I am not interested.", "close_window", []],

  [anyone, "tavern_traveler_continue", [],
   "Well, that's all I can tell you. Good bye.", "close_window", [(troop_remove_gold, "trp_player", 100),]],

#Tavern Talk (with book sellers)
  [anyone, "start", [(is_between, "$g_talk_troop", tavern_booksellers_begin, tavern_booksellers_end),
                     ],
   "Good day {sir/madam}, will you be looking at my books?", "bookseller_talk", []],
  [anyone|plyr, "bookseller_talk", [], "Yes. Show me what you have for sale.", "bookseller_buy", []],

  [anyone,"bookseller_buy", [], "Of course {sir/madam}.", "book_trade_completed",[[change_screen_trade]]],
  [anyone,"book_trade_completed", [], "Anything else?", "bookseller_talk",[]],

  [anyone|plyr,"bookseller_talk", [], "Nothing. Thanks.", "close_window",[]],

##Floris: Update from CC 1.321
## CC mystic merchant begin
  [anyone, "start", [(is_between, "$g_talk_troop", mystic_merchant_begin, mystic_merchant_end),
                     ],
   "Good day {sir/madam}, I have some unidentified items with me. I will sell these items to you by the base price of them. You probably buy an item with a good prefix by a low price or buy an item with a bad prefix by a hight price. Do you want to try your fortune?", "mystic_merchant_talk", []],
  [anyone|plyr, "mystic_merchant_talk", [], "That sounds good. I want to have a try.", "mystic_merchant_type", []],
  [anyone,"mystic_merchant_type", [], "Which type do you want to check?", "mystic_merchant_type_sel",[]],
  [anyone|plyr,"mystic_merchant_type_sel", [], "Weapons.", "mystic_merchant_type_items",[(assign, "$temp", 1),]],
  [anyone|plyr,"mystic_merchant_type_sel", [], "Armors.", "mystic_merchant_type_items",[(assign, "$temp", 2),]],
  [anyone|plyr,"mystic_merchant_type_sel", [], "Horses.", "mystic_merchant_type_items",[(assign, "$temp", 3),]],
  [anyone|plyr,"mystic_merchant_type_sel", [], "Never mind.", "mystic_merchant_pretalk",[]],
  [anyone,"mystic_merchant_type_items", [], "Which one?", "mystic_merchant_item_sel",[]],

  [anyone|plyr|repeat_for_100,"mystic_merchant_item_sel", 
    [
      (store_repeat_object, ":i_slot"),
      (troop_get_inventory_capacity, ":inv_cap", "$g_talk_troop"),
      (is_between, ":i_slot", 10, ":inv_cap"),
      (troop_get_inventory_slot, ":item_id", "$g_talk_troop", ":i_slot"),
      (gt, ":item_id", -1),
      (item_get_type, ":item_type", ":item_id"),
      (assign, ":continue", 0),
      (try_begin),
        (eq, "$temp", 1),
        (is_between, ":item_type", itp_type_one_handed_wpn, itp_type_goods),
        (assign, ":continue", 1),
      (else_try),
        (eq, "$temp", 2),
        (is_between, ":item_type", itp_type_head_armor, itp_type_pistol),
        (assign, ":continue", 1),
      (else_try),
        (eq, "$temp", 3),
        (eq, ":item_type", itp_type_horse),
        (assign, ":continue", 1),
      (try_end),
      (eq, ":continue", 1),
      (str_store_item_name, s1, ":item_id"),
      (store_item_value, ":base_value", ":item_id"),
      (call_script, "script_game_get_item_buy_price_factor", ":item_id"),
      (assign, ":buy_price_factor", reg0),
      (val_mul, ":base_value", ":buy_price_factor"),
      (val_div, ":base_value", 100),
      (assign, reg1, ":base_value"),
    ], "{s1}(price: {reg1}).", "mystic_merchant_pretalk",
    [
      (store_repeat_object, ":i_slot"),
      (troop_get_inventory_slot, ":item_id", "$g_talk_troop", ":i_slot"),
      (troop_get_inventory_slot_modifier, ":imod", "$g_talk_troop", ":i_slot"),
      (str_store_item_name, s3, ":item_id"),
      (store_sub, ":out_string", ":imod", imod_plain),
      (val_add, ":out_string", "str_imod_plain"),
      (str_store_string, s4, ":out_string"),
      (store_item_value, ":base_value", ":item_id"),
      (call_script, "script_game_get_item_buy_price_factor", ":item_id"),
      (assign, ":buy_price_factor", reg0),
      (val_mul, ":base_value", ":buy_price_factor"),
      (val_div, ":base_value", 100),
      (store_troop_gold, ":troop_gold", "trp_player"),
      (try_begin),
        (lt, ":troop_gold", ":base_value"),
        (display_message, "@You don't have enough money."),
      (else_try),
        (store_free_inventory_capacity, ":inv_cap", "trp_player"),
        (le, ":inv_cap", 0),
        (display_message, "@You don't have enough room."),
      (else_try),
        (troop_remove_gold, "trp_player", ":base_value"),
        (troop_set_inventory_slot, "$g_talk_troop", ":i_slot", -1),
        (set_show_messages, 0),
        (troop_add_item, "trp_player", ":item_id", ":imod"),
        (set_show_messages, 1),
        (try_begin),
          (item_slot_eq, ":imod", slot_item_modifier_quality, 1),
          (display_message, "@Good luck. You get a {s4}{s3}.", 0x00ff00),
        (else_try),
          (item_slot_eq, ":imod", slot_item_modifier_quality, -1),
          (display_message, "@Bad luck. You get a {s4}{s3}.", 0xff0000),
        (else_try),
          (display_message, "@You get a {s3}."),
        (try_end),
      (try_end),
    ]],
  [anyone|plyr,"mystic_merchant_item_sel", [], "Let me see something else.", "mystic_merchant_type",[]],

  [anyone,"mystic_merchant_pretalk", [], "Anything else?", "mystic_merchant_talk",[]],
  [anyone|plyr,"mystic_merchant_talk", [], "No, I must leave now.", "close_window",[]],
## CC Mystic Merchant end
##

 #Custom Troops begin
   [trp_custom_master, "start", [(eq, "$g_talk_troop_met", 0)],
     "Hail and well met, {sir/madam}. I am Master Sigmund of the Freelancers, at your service.",
     "ranger_introduce_1", []],
   [trp_custom_master|plyr, "ranger_introduce_1", [],
     "Greetings, sir. Who are the Freelancers?", "ranger_introduce_2", []],
   [trp_custom_master, "ranger_introduce_2", [],
     "We are soldiers from all the six corners of Calradia, seeking the development of the individual soldiers and mastery of all martial arts. Men from all countries who don't want to be bound to one fighting style have been trained under my service to be generalists, to be dynamic in the field, and to take various roles as archer, horseman, infantry, scout or anything that's needed at a moment's notice. We will wear any blazon, bear any standard, and lend our strength to any worthy cause, for a price.",
     "ranger_introduce_3", []],
   [trp_custom_master|plyr, "ranger_introduce_3", [],
     "I see. You're mercenaries. If you're really that good, why don't I see more of your kind in the war?",
     "ranger_introduce_4", []],
   [trp_custom_master, "ranger_introduce_4", [],
     "With this neverending war, all the kingdoms have developed highly specialized war machines, churning out soldiers by the hundreds, specifically trained in their preferred mode of warfare. They are blind for generalists who are skilled in all modes of combat",
     "ranger_introduce_5", []],
   [trp_custom_master|plyr, "ranger_introduce_5", [],
     "Well, if I were to recruit them, what kind of troops can I expect.",
     "ranger_introduce_6", []],
   [trp_custom_master, "ranger_introduce_6", [],
     "Currently I can offer you only recruits. But you'll find that they improve quickly. Just a few battles and they'll be formidable warriors.",
     "ranger_master_talk", []],
    
   [trp_custom_master, "start", [(eq, "$g_talk_troop_met", 1)],
     "Hello again, {playername}.", "ranger_master_talk", []],
   [trp_custom_master|plyr, "ranger_master_talk", [],
     "I'd like to hire some freelancer recruits.", "ranger_master_hire_male", [],],
   [trp_custom_master|plyr, "ranger_master_talk", 
   [(troop_get_slot, ":custom_state", "trp_custom_master", slot_troop_state),
    (neq, ":custom_state", 1),
    (neg|is_between, ":custom_state", towns_begin, towns_end)],								# Hire him! Only if you got a court of your own, and a positive renown.
     "I'd like you to take up residence at my hall and instruct young recruits about your way of warfare.", "ranger_master_hire_himself", []],
   [trp_custom_master|plyr, "ranger_master_talk", 
   [(troop_get_slot, ":custom_state", "trp_custom_master", slot_troop_state),
   (this_or_next|eq, ":custom_state", 1),
   (is_between, ":custom_state", towns_begin, towns_end)], 
     "I would like you to take up residence somewhere else.", "custom_master_reassign_location", []],

   [trp_custom_master|plyr, "ranger_master_talk", [], 
     "So how do I customize the gear of my freelancers?", "ranger_master_customize", []],
   [trp_custom_master, "ranger_master_customize", [],
     "Just talk to them and ask to change their gear. When the inventory screen appears, move items from the RIGHT panel of items into the LEFT panel (CTRL-click is a fast way of doing this). Just ignore the equipment slots in the middle panel. You can put as many items as will fit in the left panel. The Freelancer will randomly choose from his items if there are more than one of a given type.", "ranger_master_talk", []],
	[trp_custom_master|plyr, "ranger_master_talk", [], 
     "Tell me your story again.", "ranger_introduce_2", []],
   [trp_custom_master|plyr, "ranger_master_talk", [],
     "Goodbye.", "close_window", []],

   [trp_custom_master, "ranger_master_hire_male",
     [
        (assign, reg1, "$g_num_ranger_recruits"),
	   	## MTT
		(try_begin),
			(eq, "$troop_trees", troop_trees_0),
			(assign, ":ranger_recruit", "trp_custom_n_recruit"),
		(else_try),
			(eq, "$troop_trees", troop_trees_1),
		    (assign, ":ranger_recruit", "trp_custom_r_recruit"),
		(else_try),
			(eq, "$troop_trees", troop_trees_2),
			(assign, ":ranger_recruit", "trp_custom_e_recruit"),
		(try_end),	
		(try_begin),
		    (gt, reg1, 0),
		    (troop_slot_eq, "trp_custom_master", slot_troop_state, 1),
			(eq, "$talk_context", tc_court_talk),
		    (is_between, "$current_town", walled_centers_begin, walled_centers_end),
			(party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
			(party_slot_ge, "$current_town", slot_center_has_barracks, 1),
			(assign, ":end", 3),
			(try_for_range, ":unused", 0, ":end"),
				(store_random_in_range, reg0, 0, 2),
				(troop_get_upgrade_troop, reg0, ":ranger_recruit", reg0),
				(gt, reg0, 0),
				(assign, ":ranger_recruit", reg0),
				(store_random_in_range, reg0, 0, 3),
				(gt, reg0, 0), #1/3 chance to upgrade again (2 tries...1/6 to get tier 3)
				(assign, ":end", 0), #break
			(try_end),
		(try_end),
		(str_store_troop_name_plural, s1, ":ranger_recruit"),
		(assign, "$temp", ":ranger_recruit"),	   
     ],
     "I have {reg1?{reg1}:no} freelancer {s1} available for hire at the moment. {reg1?Each recruit costs 50 dinars to hire. How many do you want to hire?:}",
     "ranger_master_hire", []],

   [trp_custom_master|plyr|repeat_for_100, "ranger_master_hire",
     [
       (store_repeat_object, ":num"),
       (gt, ":num", 0),
      
       (assign, ":rangers_amount", "$g_num_ranger_recruits"),
       (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
       (val_min, ":rangers_amount", ":free_capacity"),
       (store_troop_gold, ":cur_gold", "trp_player"),
       (val_div, ":cur_gold", 50),
       (val_min, ":rangers_amount", ":cur_gold"),
       (le, ":num", ":rangers_amount"),
       (assign, reg0, ":num"),
     ],
     "{reg0}", "ranger_master_hire_done", 
      [	
         (store_repeat_object, ":num"),
         (try_begin),
           (party_add_members, "p_main_party", "$temp", ":num"),
           (val_sub, "$g_num_ranger_recruits", ":num"),
         (try_end),
         (store_mul, ":cost", ":num", 50),
         (troop_remove_gold, "trp_player", ":cost")
       ]
     ],

   [trp_custom_master|plyr, "ranger_master_hire", [],
     "Nevermind.", "ranger_master_hire_done", []],
   [trp_custom_master, "ranger_master_hire_done", [],
     "Anything else?", "ranger_master_talk", []],
# Custom Troops end

# Hire him! begin
# # The initial talk
   [trp_custom_master, "ranger_master_hire_himself", [(assign, reg1, 10000),(assign, reg2, 25)], 
     "Abandon the freedom that comes with roaming the taverns of the lands, and only train brave young men from your lands? You'll have to provide all the equipment, the training grounds, the tutor fees, and of course a little extra for the right to have me at your court. If you want me to stay at your court, it will cost you {reg1} denars to get us set up in one place. Then, a modest fee of {reg2} denars per week for administration should do.", "ranger_master_hire_self", []],

	[trp_custom_master|plyr, "ranger_master_hire_self",   [
	(store_troop_gold, ":cur_gold", "trp_player"),
    (ge, ":cur_gold", reg1),
   ],
     "You drive a hard bargain, but I'm sure you're worth it.", "ranger_master_agree",
	 [
	 (troop_remove_gold, "trp_player", reg1),
	 (troop_set_slot, "trp_custom_master", slot_troop_state, 1),
	 ]],

	 [trp_custom_master|plyr, "ranger_master_hire_self", 
   [
   (try_begin),
	 (store_troop_gold, ":cur_gold", "trp_player"),
	 (lt, ":cur_gold", reg1),
	 (str_store_string, s1, "@I must admit I can't afford to pay you at the moment."),
   (else_try),
	 (str_store_string, s1, "@Are you mad? That's not going to happen!"),
	(try_end),
   ], 
     "{s1}", "close_window", []],

 [trp_custom_master, "ranger_master_agree", 
	 [(assign, reg20, 0),
	 (try_for_range, ":center", walled_centers_begin, walled_centers_end),
		(party_get_slot, ":town_lord", ":center", slot_town_lord),
		(eq, ":town_lord", "trp_player"),
		(val_add, reg20, 1),
	 (try_end),
	 (ge,reg20, 1),], #Floris - bugfix, was eq so having more than 1 center caused a hang
     "A wise decission, {sir/madam}. I'll pack my gear and move to your court.", "close_window", []],
	 
 [trp_custom_master, "ranger_master_agree", 
	 [(assign, reg20, 0),
	 (try_for_range, ":center", walled_centers_begin, walled_centers_end),
		(party_get_slot, ":town_lord", ":center", slot_town_lord),
		(eq, ":town_lord", "trp_player"),
		(val_add, reg20, 1),
	 (try_end),
	 (eq,reg20, 0)],
     "It seems that you have no hall of your own, {sir/madam}. I'll wait for you in a tavern of your choice until that is resolved.", "choose_custom_tavern", []],	 
	 

 [trp_custom_master|plyr|repeat_for_parties, "choose_custom_tavern", 
	[
	(store_repeat_object, ":town"),
	(is_between, ":town", towns_begin, towns_end),
	(str_store_party_name, s1, ":town")],
	"{s1}", "close_window",
	[
	(store_repeat_object, reg1),
	(troop_set_slot, "trp_custom_master", slot_troop_state, 2), 
	(troop_set_slot, "trp_custom_master", slot_troop_cur_center, reg1)]],
	
[trp_custom_master, "custom_master_reassign_location", [], 
     "Where would you like me to go?", "choose_custom_location", []],
	 
[trp_custom_master|plyr, "choose_custom_location", 
	[(assign, reg20, 0),
	 (try_for_range, ":center", walled_centers_begin, walled_centers_end),
		(party_get_slot, ":town_lord", ":center", slot_town_lord),
		(eq, ":town_lord", "trp_player"),
		(val_add, reg20, 1),
	 (try_end),
	 (eq,reg20, 1)	
	], 
     "Wait at my court for me.", "close_window", 
	 [(troop_set_slot, "trp_custom_master", slot_troop_state, 1)]],

 [trp_custom_master|plyr|repeat_for_parties, "choose_custom_location", 
	[
	(store_repeat_object, ":town"),
	(is_between, ":town", towns_begin, towns_end),
	(str_store_party_name, s1, ":town")],
	"{s1}", "close_window",
	[
	(store_repeat_object, reg1),
	(troop_set_slot, "trp_custom_master", slot_troop_state, 2), 
	(troop_set_slot, "trp_custom_master", slot_troop_cur_center, reg1)]],	 
	
	
# # After having refused the first time, you ask him again.
  # [trp_custom_master, "ranger_master_hire_himself", [], 
    # "I see that you've changed your mind. Are you prepared to pay my monthly fee of {reg1} denars?", "ranger_master_hire_later", []],
  # [trp_custom_master|plyr, "ranger_master_hire_later", [],
    # "Alright, this time I will hire you. I hope you're worth it.", "ranger_master_agree_later", []],
  # [trp_custom_master|plyr, "ranger_master_hire_later", [], 
    # "I thought we could talk this over, but apparently not. I still can't afford it.", "close_window", []],
  # [trp_custom_master, "ranger_master_agree_later", [],
    # "A wise decission, {sir/madam}. I'll pack my gear and move to your court.", "close_window", []],


# # A warning that your renown is too far in the negative!
  # [trp_custom_master, "ranger_master_warning", [], 
    # "{Sir/Madam}, I don't want my recruits to be associated with a honourless scoundrel. The gossip in the taverns will soon hurt my good reputation. If you don't improve your renown, I'll be forced to leave.", "close_window", []],

# # Your renown is too negative, he leaves.
  # [trp_custom_master, "ranger_master_too_negative", [], 
    # "Despite my warning you just continued to act like a vile beast. I'm sorry, but under these circumstances I'll have to leave. When you cleared your name you can seek me out again.", "close_window", []],

# # Attempt to hire him again after negative renown, but still not positive.
  # [trp_custom_master, "ranger_master_negative_finances", [], 
    # "You dare, asking me to come back to your court while your name is still smeared with the dirtiest mud. Seek me out again when you redeemed yourself and cleared your name.", "close_window", []],

# # Hire him again after he has left
  # [trp_custom_master, "ranger_master_hire_himself_again", [], 
    # "I heared that the nasty business is over. I'm willing to give it another try, if you're still prepared to pay my monthly fee of {reg1} denars?", "ranger_master_hire_later2", []],
  # [trp_custom_master|plyr, "ranger_master_hire_later2", [],
    # "I am. I hope you forgive my previous mistake and join my court once again.", "ranger_master_agree_later2", []],
  # [trp_custom_master|plyr, "ranger_master_hire_later2", [], 
    # "I'm sorry, I can't afford that right now.", "close_window", []],
  # [trp_custom_master, "ranger_master_agree_later2", [],
    # "I'll forgive you this time, but don't let it happen again! I'll pack my gear and move to your court.", "close_window", []],

# # Hire him! end

#Tavern Talk (with minstrels)
  [anyone, "start", [(is_between, "$g_talk_troop", tavern_minstrels_begin, tavern_minstrels_end),],
   "Greetings to you, {most noble sir/most noble lady}.", "minstrel_1", []],

  [anyone|plyr, "minstrel_1", [(eq, "$minstrels_introduced", 0),],
   "What is it you do?", "minstrel_job_description",
   [(assign, "$minstrels_introduced", 1), ]],

  [anyone|plyr, "minstrel_1", [(eq, "$minstrels_introduced", 1)  ],
   "I have some questions about courtship in Calradia",
   "minstrel_courtship_questions", []],

  [anyone|plyr, "minstrel_1", [(eq, "$minstrels_introduced", 1)  ],
   "Can you teach me any poems?",
   "minstrel_courtship_poem", []],


  [anyone, "minstrel_courtship_poem", [
    (eq, "$allegoric_poem_recitations", 0),
	(this_or_next|eq, "$g_talk_troop", "trp_tavern_minstrel_1"),
		(eq, "$g_talk_troop", "trp_tavern_minstrel_5"),
  ],
   "I can teach you the poem, 'The Storming of the Castle of Love.' It is short enough to be easily learned. It is an allegoric poem, replete with symbols and metaphor. It describes how a brave but rough warrior wins the heart of his lady by learning the virtues of chivalry, becoming a true and noble knight. Its theme -- that the role of a woman is to inspire but also civilize a man -- is appreciated by some noble ladies, but not all.",
   "minstrel_courtship_poem_teach", [
    (assign, "$poem_selected", courtship_poem_allegoric),
   ]],

  [anyone, "minstrel_courtship_poem", [
    (eq, "$mystic_poem_recitations", 0),
	(this_or_next|eq, "$g_talk_troop", "trp_tavern_minstrel_3"),
		(eq, "$g_talk_troop", "trp_tavern_minstrel_1"),
  ],
   "I can teach you the poem, 'The Heart's Desire.' It is a lyrical poem, which can be interpreted either erotically or spiritually. The lover realizes the majesty of the divine by gazing upon the body of his beloved. I believe that it appeals to women of a certain romantic temperament, but you risk scandalizing or boring others.",
   "minstrel_courtship_poem_teach", [
   (assign, "$poem_selected", courtship_poem_mystic),
   ]],

#ashik poem
  [anyone, "minstrel_courtship_poem", [
  	(eq, "$tragic_poem_recitations", 0),
	(this_or_next|eq, "$g_talk_troop", "trp_tavern_minstrel_3"),
		(eq, "$g_talk_troop", "trp_tavern_minstrel_2"),  ],
   "I can teach you the tale of Kais and Layala. It is a sad and simple story -- the shepherd boy Kais and the nobleman's daughter Layala love each other, but they can never marry. The poem is Kais' lament as he wanders alone, unwilling to forget his true love, driving himself mad with longing. Some ladies melt at the sweetness of his sorrows; others glaze over at his self-pity.",
   "minstrel_courtship_poem_teach", [
   (assign, "$poem_selected", courtship_poem_tragic),

   ]],


#nord saga
  [anyone, "minstrel_courtship_poem", [
	(eq, "$heroic_poem_recitations", 0),
	(this_or_next|eq, "$g_talk_troop", "trp_tavern_minstrel_4"),
		(eq, "$g_talk_troop", "trp_tavern_minstrel_2"),

  ],
   "I can teach you part of the saga of Helgerad and Kara. It is a heroic tale, full of blood and battle. The shieldmaiden Kara chooses the warrior Helgered as her lover, as he is the only man who can defeat her in combat. Her father, who pledged her to another, comes with his sons and his huscarls to kill Helgered. They fight, and Helgered and Kara slaughter the entire host except for Kara's beloved younger brother -- who, alas, grows up to avenge his father by slaying Helgered. The depiction of warrior and shieldmaiden as equals will appeal to some women, but a mail-wearing, blood-spattered heroine will shock and repulse others.",
   "minstrel_courtship_poem_teach", [
   (assign, "$poem_selected", courtship_poem_heroic),
   ]],


  [anyone, "minstrel_courtship_poem", [
    (eq, "$comic_poem_recitations", 0),
	(this_or_next|eq, "$g_talk_troop", "trp_tavern_minstrel_5"),
		(eq, "$g_talk_troop", "trp_tavern_minstrel_4"),
  ],
   "I can teach you the poem, 'An Argument in the Garden.' It is a comic poem, which satirizes the conventions of courtly love. A lover steals into a garden in Veluca, and plies her with lots of witty lines to persuade his lover to submit to his embraces. She shoots down all of his advances one by one, then when he is downcast, she takes him in her arms and tells him that she wanted him all along, except on her terms, not his. A lady with a sense of humor may find it amusing, but others might feel that they are the ones who are being mocked.",
   "minstrel_courtship_poem_teach", [
   (assign, "$poem_selected", courtship_poem_comic),
   ]],


  [anyone, "minstrel_courtship_poem_teach", [],
   "To teach it to you, I will need some hours of your time -- and, of course, a small fee for my services. About 300 denars would suffice.",
   "minstrel_courtship_poem_teach_2", []],

  [anyone, "minstrel_courtship_poem", [],
   "I believe you already know the poems I am best equipped to teach.",
   "minstrel_pretalk", []],

  [anyone|plyr, "minstrel_courtship_poem_teach_2", [
  (store_troop_gold, ":gold", "trp_player"),
  (ge, ":gold", 300),
  ],
   "Yes -- teach me that one",
   "minstrel_courtship_poem_teach_3", []],

  [anyone|plyr, "minstrel_courtship_poem_teach_2", [],
   "Never mind",
   "minstrel_pretalk", []],


  [anyone, "minstrel_courtship_poem_teach_3", [
  (eq, "$poem_selected", courtship_poem_allegoric),
  ],
   "Very well -- repeat after me:^\
   I deflected her skeptical questioning darts^\
   with armor made of purest devotion^\
   purged in the forge of my heart^\
   from the slag of any baser emotion",
   "minstrel_courtship_poem_teach_4", []],


  [anyone, "minstrel_courtship_poem_teach_3", [
  (eq, "$poem_selected", courtship_poem_mystic),
  ],
   "Very well -- repeat after me:^\
   You are the first and the last^\
   the outer and the inner^\
   When I drink from the cup of love^\
   I escape the tread of time^\
   A moment in solitude with you^\
   Would have no beginning and no end",
   "minstrel_courtship_poem_teach_4", []],


  [anyone, "minstrel_courtship_poem_teach_3", [
  (eq, "$poem_selected", courtship_poem_tragic),
  ],
  "Very well -- repeat after me:^\
  The wind that blows the dry steppe dust^\
  Stirs the curtains in your tower^\
  The moon that lights my drunken path home^\
  Looks on you sleeping in your bower^\
  If I cried out to the wind^\
  Could it carry a message from my lips?^\
  If I wept before the moon^\
  Would it grant me just a glimpse?",
  "minstrel_courtship_poem_teach_4", [
   ]],


  [anyone, "minstrel_courtship_poem_teach_3", [
  (eq, "$poem_selected", courtship_poem_heroic),
  ],
  "Very well -- repeat after me:^\
   A light pierced the gloom over Wercheg cliffs...^\
   Where charge of surf broke on shieldwall of shore^\
   Grey-helmed and grey-cloaked the maiden stood^\
   On wave-steed's prow, the sailcloth snapping^\
   Over din of oars, of timbers cracking^\
   She cried out to her hearth-brothers, arrayed for war",
   "minstrel_courtship_poem_teach_4", [
   ]],


  [anyone, "minstrel_courtship_poem_teach_3", [
  (eq, "$poem_selected", courtship_poem_comic),
  ],
  "Very well -- repeat after me:^All the silks of Veluca, all the furs of Khudan^Would buy you not the briefest kiss^What I bestow, I bestow for love^And the sake of my own happiness^But brought you a gift? Let us see! Let us see!^Or should tell my father how you came to see me?",
  "minstrel_courtship_poem_teach_4", [
   ]],


  [anyone|plyr, "minstrel_courtship_poem_teach_4", [
  (eq, "$poem_selected", courtship_poem_allegoric),
  ],
  "'I deflected her skeptical questioning darts...'",
  "minstrel_learn_poem_continue", [
    (troop_remove_gold, "trp_player", 300),
    (val_add, "$allegoric_poem_recitations", 1),
  ]],


  [anyone|plyr, "minstrel_courtship_poem_teach_4", [
  (eq, "$poem_selected", courtship_poem_mystic),
  ],
  "'You are the first and the last..'",
  "minstrel_learn_poem_continue", [
    (troop_remove_gold, "trp_player", 300),
    (val_add, "$mystic_poem_recitations", 1),
  ]],




  [anyone|plyr, "minstrel_courtship_poem_teach_4", [
  (eq, "$poem_selected", courtship_poem_tragic),
  ],
  "'The wind that blows the dry steppe dust...'",
  "minstrel_learn_poem_continue", [
    (troop_remove_gold, "trp_player", 300),
	(val_add, "$tragic_poem_recitations", 1),
  ]],


  [anyone|plyr, "minstrel_courtship_poem_teach_4", [
  (eq, "$poem_selected", courtship_poem_heroic),
  ],
  "'A light pierced the gloom over Wercheg cliffs...'",
  "minstrel_learn_poem_continue", [
    (troop_remove_gold, "trp_player", 300),
	(val_add, "$heroic_poem_recitations", 1),
  ]],


  [anyone|plyr, "minstrel_courtship_poem_teach_4", [
  (eq, "$poem_selected", courtship_poem_comic),
  ],
  "'All the silks of Veluca...'",
  "minstrel_learn_poem_continue", [
    (troop_remove_gold, "trp_player", 300),
	(val_add, "$comic_poem_recitations", 1),
  ]],


  [anyone|plyr, "minstrel_courtship_poem_teach_4", [
  ],
  "Pshaw... What kind of doggerel is that?",
  "minstrel_courtship_poem_teach_reject", []],

  [anyone, "minstrel_courtship_poem_teach_reject", [
  ],
  "Very well. If the poem is not to your taste, then keep your money. But remember -- with poets and with lovers, what is important is not what pleases you. What is important is what your pleases your audience. If you wish to learn the poem, I am still willing to teach.",
  "minstrel_pretalk", []],


  [anyone, "minstrel_learn_poem_continue", [
  ],
   "Very good -- but there are many stanzas to go. Now, listen closely...", "close_window",
   [
    (try_begin),
      (try_begin),
        (eq, "$poem_selected", courtship_poem_mystic),
        (set_achievement_stat, ACHIEVEMENT_ROMANTIC_WARRIOR, 0, 1),
      (else_try),
        (eq, "$poem_selected", courtship_poem_tragic),
        (set_achievement_stat, ACHIEVEMENT_ROMANTIC_WARRIOR, 1, 1),
      (else_try),
        (eq, "$poem_selected", courtship_poem_heroic),
        (set_achievement_stat, ACHIEVEMENT_ROMANTIC_WARRIOR, 2, 1),
      (else_try),
        (eq, "$poem_selected", courtship_poem_comic),
        (set_achievement_stat, ACHIEVEMENT_ROMANTIC_WARRIOR, 3, 1),
      (else_try),
        (eq, "$poem_selected", courtship_poem_allegoric),
        (set_achievement_stat, ACHIEVEMENT_ROMANTIC_WARRIOR, 4, 1),
      (try_end),

      (assign, ":number_of_poems_player_know", 0),
      (try_for_range, ":poem_number", 0, 5),
        (get_achievement_stat, ":poem_is_known", ACHIEVEMENT_ROMANTIC_WARRIOR, ":poem_number"),
        (eq, ":poem_is_known", 1),
        (val_add, ":number_of_poems_player_know", 1),
      (try_end),

      (try_begin),
        (ge, ":number_of_poems_player_know", 3),
        (unlock_achievement, ACHIEVEMENT_ROMANTIC_WARRIOR),
      (try_end),
    (try_end),

    (assign, "$g_leave_town",1),
    (rest_for_hours, 2, 2, 0),
    (finish_mission),
   ]],


  [anyone|plyr, "minstrel_1", [(eq, "$minstrels_introduced", 1)  ],
   "Can you tell me anything about the eligible maidens in this realm?",
   "minstrel_gossip", [
   ]],

  [anyone, "minstrel_gossip",
  [],
   "About whom did you wish to know?",
   "minstrel_gossip_select", []],

  [anyone|plyr,"minstrel_gossip_select",
   [],
   "Just tell me the latest piece of gossip",
   "minstrel_gossip_maiden_selected_2", [

    (assign, "$lady_selected", -1),
	(assign, "$romantic_rival", -1),

    (try_for_range, ":log_entry", 0, "$num_log_entries"),
		(troop_get_slot, ":lady", "trp_log_array_actor", ":log_entry"),
		(is_between, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
		(neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":lady"),

		(troop_get_slot, ":type", "trp_log_array_entry_type", ":log_entry"),
		(is_between, ":type", 50, 65), #excludes log entries in which a party is an actor

		(store_faction_of_troop, ":lady_faction", ":lady"),
		(store_faction_of_party, ":town_faction", "$g_encountered_party"),
		(eq, ":lady_faction", ":town_faction"),
		(assign, "$lady_selected", ":lady"),
		(try_begin),
			(eq, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":lady"),
			(troop_get_slot, reg4, "trp_log_array_entry_type", ":log_entry"),
			(assign, reg5, "$num_log_entries"),
			(display_message, "str_log_entry_type_reg4_for_s4_total_entries_reg5"),
		(try_end),
	(try_end),

   ]],


  [anyone|plyr|repeat_for_troops,"minstrel_gossip_select",
   [
   (store_repeat_object, "$temp"),
   (troop_slot_eq, "$temp", slot_troop_occupation, slto_kingdom_lady),
   (troop_slot_eq, "$temp", slot_troop_spouse, -1),
   (store_faction_of_troop, ":lady_faction", "$temp"),
   (store_faction_of_party, ":town_faction", "$g_encountered_party"),
   (eq, ":lady_faction", ":town_faction"),
   (str_store_troop_name, s10, "$temp"),
   #LAZERAS MODIFIED  {Expanded Dialog Kit}
   ## Jrider + DIALOGS v1.0 modify the display string with relation
   (call_script, "script_change_minstrel_maiden_dialog_string", "$temp"),
   ## Jrider -
   #LAZERAS MODIFIED  {Expanded Dialog Kit}
   ],  
   "{s10}",
   "minstrel_gossip_maiden_selected", [
    (store_repeat_object, "$lady_selected"),
   ]],

  [anyone|plyr,"minstrel_gossip_select",
   [], "Never mind", "minstrel_pretalk", []],


   [anyone,"minstrel_gossip_maiden_selected",
   [
	(try_begin),
		(eq, "$cheat_mode", 1),
		(assign, reg3, "$lady_selected"),
		(display_message, "@{!}DEBUG: Gossip for troop {reg3}"),
		(gt, reg3, -1),
		(display_message, "@{!}DEBUG: {s3}"),
	(try_end),

	(try_begin),
	   (gt, "$lady_selected", -1),
	   (str_store_troop_name, s9, "$lady_selected"), #lady

      ##diplomacy start+ Make gender-correct
      (try_begin),
         (call_script, "script_cf_dplmc_troop_is_female", "$lady_selected"),
         (assign, reg4, 1),
      (else_try),
         (assign, reg4, 0),
      (try_end),
      #the strings below have been modified to use reg4 for gender
      ##diplomacy end+
	   (str_store_string, s10, "str_error__reputation_type_for_s9_not_within_range"),
	   (try_begin),
			(troop_slot_eq, "$lady_selected", slot_lord_reputation_type, lrep_conventional),
			(str_store_string, s16, "str_they_say_that_s9_is_a_most_conventional_maiden__devoted_to_her_family_of_a_kind_and_gentle_temperament_a_lady_in_all_her_way"),
	   (else_try),
			(troop_slot_eq, "$lady_selected", slot_lord_reputation_type, lrep_otherworldly),
			(str_store_string, s16, "str_they_say_that_s9_is_a_bit_of_a_romantic_a_dreamer__of_a_gentle_temperament_yet_unpredictable_she_is_likely_to_be_led_by_her_passions_and_will_be_trouble_for_her_family_ill_wager"),
	   (else_try),
			(troop_slot_eq, "$lady_selected", slot_lord_reputation_type, lrep_ambitious),
			(str_store_string, s16, "str_they_say_that_s9_is_determined_to_marry_well_and_make_her_mark_in_the_world_she_may_be_a_tremendous_asset_for_her_husband__provided_he_can_satisfy_her_ambition"),
	   (else_try),
			(troop_slot_eq, "$lady_selected", slot_lord_reputation_type, lrep_adventurous),
			(str_store_string, s16, "str_they_say_that_s9_loves_to_hunt_and_ride_maybe_she_wishes_she_were_a_man_whoever_she_marries_will_have_a_tough_job_keeping_the_upper_hand_i_would_say"),
	   (else_try),
			(troop_slot_eq, "$lady_selected", slot_lord_reputation_type, lrep_moralist),
			(str_store_string, s16, "str_they_say_that_s9_is_a_lady_of_the_highest_moral_standards_very_admirable_very_admirable__and_very_hard_to_please_ill_warrant"),
	   (try_end),

	   (call_script, "script_add_rumor_string_to_troop_notes", "$lady_selected", -1, 16),
   (try_end),
   ],
   "{s16}",
   "minstrel_gossip_maiden_selected_2", [
   ]],


   [anyone,"minstrel_gossip_maiden_selected_2",
   [
	##diplomacy+
	##OLD:
	#(troop_slot_eq, "trp_player", slot_troop_spouse, "$lady_selected"),
	#(is_between, "$lady_selected", kingdom_ladies_begin, kingdom_ladies_end),
	##NEW:
	(is_between, "$lady_selected", heroes_begin, heroes_end),
	(this_or_next|troop_slot_eq, "$lady_selected", slot_troop_spouse, "trp_player"),
		(troop_slot_eq, "trp_player", slot_troop_spouse, "$lady_selected"),
	(call_script, "script_dplmc_store_troop_is_female",  "$lady_selected"),#Add support for male version
	],#Next line, "She" -> {reg0?She:He} , "she" -> {reg0?she:he}
	"{reg0?She:He} is married to you, of course! Clearly, no one would dream that {reg0?she:he} would do anything to engender gossip.",
   "minstrel_postgossip",
   ##diplomacy end+
	[]],


   [anyone,"minstrel_gossip_maiden_selected_2",
   [
    (gt, "$lady_selected", -1),
	(assign, ":lady", "$lady_selected"),
	(neg|troop_slot_ge, ":lady", slot_troop_spouse, active_npcs_begin),
	(troop_get_slot, ":betrothed", ":lady", slot_troop_betrothed),
	(is_between, ":betrothed", active_npcs_begin, active_npcs_end),

	(str_store_troop_name, s9, ":lady"),
	(str_store_troop_name, s11, ":betrothed"),

	(str_store_string, s12, "str_s9_is_now_betrothed_to_s11_soon_we_believe_there_shall_be_a_wedding"),
	(try_begin),
		(troop_slot_eq, ":lady", slot_troop_met, 2),
		(assign, "$romantic_rival", ":betrothed"),
	(try_end),
	],
	"{s12}.",
   "minstrel_postgossip", []],





   [anyone,"minstrel_gossip_maiden_selected_2",
   [
      ##diplomacy start+ Make gender-correct
      #xxx TODO ensure this actually works, untangle how this is used
      #The strings below have been modified to use reg4 for gender
     (try_begin),
        (call_script, "script_cf_dplmc_troop_is_female", "$lady_selected"),
        (assign, reg4, 1),
	 (else_try),
        (assign, reg4, 0),
     (try_end),
      ##diplomacy end+
    (try_begin),
		(is_between, "$lady_selected", kingdom_ladies_begin, kingdom_ladies_end),
	    (str_store_string, s12, "str_i_have_not_heard_any_news_about_her"),

		(str_store_troop_name, s9, "$lady_selected"), #lady

		(try_begin),
			(eq, "$cheat_mode", 1), #for some reason, speaking to tavern merchant does not yield rumor. Try for Lady Baoth, Lord Etr
			(display_message, "str_searching_for_rumors_for_s9"),
		(try_end),

		(assign, "$romantic_rival", -1),
		(assign, ":last_lady_noted", 0),
		(try_for_range, ":log_entry", 0, "$num_log_entries"),
			(troop_slot_eq, "trp_log_array_actor", ":log_entry", "$lady_selected"),


			#Presumably possible for some events involving a lady to not involve troops
			(troop_get_slot, ":suitor", "trp_log_array_troop_object", ":log_entry"),
			(str_clear, s11),
			(try_begin),
				(is_between, ":suitor", 0, kingdom_ladies_end),
				(str_store_troop_name, s11, ":suitor"),
			(try_end),

			(troop_get_slot, ":third_party", "trp_log_array_center_object", ":log_entry"),
			(str_clear, s10),
			(try_begin),
				(is_between, ":third_party", 0, kingdom_ladies_end),
				(str_store_troop_name, s10, ":third_party"),
			(try_end),

			(assign, ":lady", "$lady_selected"),

			(try_begin),
				(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_favors_suitor),
				(str_store_string, s12, "str_they_say_that_s9_has_shown_favor_to_s11_perhaps_it_will_not_be_long_until_they_are_betrothed__if_her_family_permits"),
				(assign, ":last_lady_noted", ":lady"),
				(assign, ":last_suitor_noted", ":suitor"),

				(try_begin),
					(troop_slot_eq, ":lady", slot_troop_met, 2),
					(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_1, ":lady"),
					(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_2, ":lady"),
						(troop_slot_eq, ":suitor", slot_troop_love_interest_3, ":lady"),

					(assign, "$romantic_rival", ":suitor"),
				(try_end),
			(else_try),
				(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_betrothed_to_suitor_by_family),
				(str_store_string, s12, "str_they_say_that_s9_has_been_forced_by_her_family_into_betrothal_with_s11"),
				(assign, ":last_lady_noted", ":lady"),
				(assign, ":last_suitor_noted", ":suitor"),

				(try_begin),
					(troop_slot_eq, ":lady", slot_troop_met, 2),
					(assign, "$romantic_rival", ":suitor"),
				(try_end),
			(else_try),
				(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_betrothed_to_suitor_by_choice),
				(str_store_string, s12, "str_they_say_that_s9_has_agreed_to_s11s_suit_and_the_two_are_now_betrothed"),
				(assign, ":last_lady_noted", ":lady"),
				(assign, ":last_suitor_noted", ":suitor"),

				(try_begin),
					(troop_slot_eq, ":lady", slot_troop_met, 2),
					(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_1, ":lady"),
					(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_2, ":lady"),
						(troop_slot_eq, ":suitor", slot_troop_love_interest_3, ":lady"),


					(assign, "$romantic_rival", ":suitor"),
				(try_end),

			(else_try),
				(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_betrothed_to_suitor_by_pressure),
				(str_store_string, s12, "str_they_say_that_s9_under_pressure_from_her_family_has_agreed_to_betrothal_with_s11"),
				(assign, ":last_lady_noted", ":lady"),
				(assign, ":last_suitor_noted", ":suitor"),

				(try_begin),
					(troop_slot_eq, ":lady", slot_troop_met, 2),
					(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_1, ":lady"),
					(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_2, ":lady"),
						(troop_slot_eq, ":suitor", slot_troop_love_interest_3, ":lady"),

					(assign, "$romantic_rival", ":suitor"),
				(try_end),

			(else_try),

				(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_rejects_suitor),
				(str_store_string, s12, "str_they_say_that_s9_has_refused_s11s_suit"),
				(assign, ":last_lady_noted", ":lady"),
				(assign, ":last_suitor_noted", ":suitor"),

			(else_try),

				(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_rejected_by_suitor),
				(str_store_string, s12, "str_they_say_that_s11_has_tired_of_pursuing_s9"),
				(assign, ":last_lady_noted", ":lady"),
				(assign, ":last_suitor_noted", ":suitor"),


			(else_try),
				(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_father_rejects_suitor),
				(str_store_string, s12, "str_they_say_that_s9s_family_has_forced_her_to_renounce_s11_whom_she_much_loved"),
				(assign, ":last_lady_noted", ":lady"),
				(assign, ":last_suitor_noted", ":suitor"),

			(else_try),
				(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_elopes_with_lord),
				(str_store_string, s12, "str_they_say_that_s9_has_run_away_with_s11_causing_her_family_much_grievance"),
				(assign, ":last_lady_noted", ":lady"),
				(assign, ":last_suitor_noted", ":suitor"),

			(else_try),
				(troop_slot_eq, "trp_log_array_entry_type",  ":log_entry", logent_lady_marries_lord),
				(str_store_string, s12, "str_they_say_that_s9_and_s11_have_wed"),
				(assign, ":last_lady_noted", ":lady"),
				(assign, ":last_suitor_noted", ":suitor"),
			(else_try),
				(troop_get_slot, ":suitor", ":lady", slot_lady_last_suitor),
				(is_between, ":suitor", active_npcs_begin, active_npcs_end),
				(str_store_troop_name, s11, ":suitor"),

				(str_store_string, s12, "str_they_say_that_s9_was_recently_visited_by_s11_who_knows_where_that_might_lead"),
				(assign, ":last_lady_noted", ":lady"),
				(assign, ":last_suitor_noted", ":suitor"),
				(try_begin),
					(troop_slot_eq, ":lady", slot_troop_met, 2),
					(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_1, ":lady"),
					(this_or_next|troop_slot_eq, ":suitor", slot_troop_love_interest_2, ":lady"),
						(troop_slot_eq, ":suitor", slot_troop_love_interest_3, ":lady"),

					(assign, "$romantic_rival", ":suitor"),
				(try_end),
			(try_end),

		(try_end),

		(try_begin),
			(neq, ":last_suitor_noted", "$romantic_rival"),
			(assign, "$romantic_rival", -1),
		(try_end),

		(try_begin),
			(gt, ":last_lady_noted", 0),
			(call_script, "script_add_rumor_string_to_troop_notes", ":last_lady_noted", ":last_suitor_noted", 12),
		(try_end),
	(else_try),
		(eq, "$lady_selected", -1),
		(str_store_string, s12, "str_there_is_not_much_to_tell_but_it_is_still_early_in_the_season"),
	(else_try),
		(assign, reg4, "$lady_selected"),
		(str_store_troop_name, s9, "$lady_selected"),
		(str_store_string, s12, "str_error_lady_selected_=_s9"),
	(try_end),
   ],
   "{s12}.",
   "minstrel_postgossip", []],

  [anyone|plyr, "minstrel_postgossip", [],
   "Very interesting -- but let us speak of something else.",
   "minstrel_pretalk", []],

  [anyone|plyr, "minstrel_postgossip", [],
   "Very interesting -- is there any more news?",
   "minstrel_gossip", []],

  [anyone|plyr, "minstrel_postgossip", [
  (is_between, "$romantic_rival", active_npcs_begin, active_npcs_end),
  (neg|check_quest_active, "qst_duel_courtship_rival"),
  (neg|troop_slot_ge, "trp_player", slot_troop_spouse, kingdom_ladies_begin),
  #diplomacy start+ extra check since the wife may be a lord
  (neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
  #diplomacy end+
  ],
   "What? I'll make that miscreant face my sword",
   "minstrel_duel_confirm", []],

  [anyone, "minstrel_duel_confirm", [
  (str_store_troop_name, s11, "$romantic_rival"),
  ],
   "Do you mean that? {s11} will be honor-bound to fight you, but challenging a lord to duel over a woman is seen as a bit hot-headed, even in this warlike age.",
   "minstrel_duel_confirm_2", []],

  [anyone|plyr, "minstrel_duel_confirm_2", [
  (str_store_troop_name, s11, "$romantic_rival"),
  (str_store_troop_name, s12, "$lady_selected"),
  ],
   "Yes -- I intend to force {s11} to relinquish his suit of {s12}",
   "minstrel_duel_issued", []],

  [anyone|plyr, "minstrel_duel_confirm_2", [
  ],
   "No -- I let my passions run away with me, there",
   "minstrel_pretalk", []],

  [anyone, "minstrel_duel_issued", [
  ],
   "As you wish. I'll spead the word of your intentions, so that {s13} does not try to back out...",
   "minstrel_pretalk", [
	(str_store_troop_name, s11, "$lady_selected"),
    (str_store_troop_name_link, s13, "$romantic_rival"),
	 ##diplomacy start+ use correct pronoun for gender
	 (call_script, "script_dplmc_store_troop_is_female_reg", "$romantic_rival", 4),
	 ##diplomacy end+
    (str_store_string, s2, "str_you_intend_to_challenge_s13_to_force_him_to_relinquish_his_suit_of_s11"),
    (setup_quest_text, "qst_duel_courtship_rival"),
    (call_script, "script_start_quest", "qst_duel_courtship_rival", "$lady_selected"),
    (quest_set_slot, "qst_duel_courtship_rival", slot_quest_giver_troop, "$lady_selected"),

    (quest_set_slot, "qst_duel_courtship_rival", slot_quest_target_troop, "$romantic_rival"),
    (quest_set_slot, "qst_duel_courtship_rival", slot_quest_xp_reward, 400),
    (quest_set_slot, "qst_duel_courtship_rival", slot_quest_expiration_days, 60),
    (quest_set_slot, "qst_duel_courtship_rival", slot_quest_current_state, 0),
   ]],




  [anyone|plyr, "minstrel_1", [(eq, "$minstrels_introduced", 1)  ],
   "Do you know of any ongoing feasts?",
   "minstrel_courtship_locations", []],

  [anyone, "minstrel_courtship_locations", [

  (str_clear, s12),
  (assign, ":feast_found", 0),
  (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
	##zerilius changes begin
	##Bug Fix since they tell about feasts of eliminated kingdoms also.
	(faction_slot_eq, ":kingdom", slot_faction_state, sfs_active),
	##zerilius changes end
	(faction_slot_eq, ":kingdom", slot_faction_ai_state, sfai_feast),
    (assign, ":feast_found", 1),

	(faction_get_slot, ":feast_venue", ":kingdom", slot_faction_ai_object),
	(str_store_party_name, s4, ":feast_venue"),
	(str_store_faction_name, s3, ":kingdom"),

	(store_current_hours, ":hour"),
	# (store_sub, ":hours_since_start", ":hour", 72), #Floris - bugfix
	(faction_get_slot, ":feast_time", ":kingdom", slot_faction_last_feast_start_time),
	# (val_add, ":hours_since_start", ":feast_time"), #Floris - bugfix
	(store_sub, ":hours_since_start", ":hour", ":feast_time"), #Floris - bugfix

	(try_begin),
		(gt, ":hours_since_start", 48),
		(str_store_string, s12, "str_s12there_is_a_feast_of_the_s3_in_progress_at_s4_but_it_has_been_going_on_for_a_couple_of_days_and_is_about_to_end_"),
	(else_try),
		(gt, ":hours_since_start", 24),
		(str_store_string, s12, "str_s12there_is_a_feast_of_the_s3_in_progress_at_s4_which_should_last_for_at_least_another_day_"),
	(else_try),
		(str_store_string, s12, "str_s12there_is_a_feast_of_the_s3_in_progress_at_s4_which_has_only_just_begun_"),
	(try_end),
  (try_end),

  (try_begin),
    (eq, ":feast_found", 0),
	(str_store_string, s12, "str_not_at_this_time_no"),
  (else_try),
	(str_store_string, s12, "str_s12the_great_lords_bring_their_daughters_and_sisters_to_these_occasions_to_see_and_be_seen_so_they_represent_an_excellent_opportunity_to_make_a_ladys_acquaintance"),
  (try_end),

  ],
   "{s12}",
"minstrel_pretalk", []],

  [anyone|plyr, "minstrel_1", [],
   "Good-bye.", "close_window", []],

  [anyone, "minstrel_courtship_questions", [],
   "What do you wish to know?",
"minstrel_courtship_questions_2", []],

  [anyone, "minstrel_courtship_prequestions", [],
   "Can I answer any other questions for you?",
"minstrel_courtship_questions_2", []],

  [anyone|plyr, "minstrel_courtship_questions_2", [
  (eq, "$minstrels_discussed_love", 1),
  ],
   "Is there a place for me in the game of love?",
   "minstrel_player_role", [
   (assign, "$minstrels_discussed_player_role", 1),
   ]],

  [anyone|plyr, "minstrel_courtship_questions_2", [
   (eq, "$minstrels_discussed_player_role", 1),
  ],
   "How would a suitor meet a lady?",
   "minstrel_player_advice_meet", [
    (assign, "$minstrels_discussed_meetings", 1),
   ]],

  [anyone|plyr, "minstrel_courtship_questions_2", [
   (eq, "$minstrels_discussed_meetings", 1),
  ],
   "Having met a lady, how would the suitor woo her?",
   "minstrel_player_advice_woo", [
   ]],



  [anyone|plyr, "minstrel_courtship_questions_2", [],
   "Tell me about marriage and love among the nobility of Calradia",
   "minstrel_nobles", [
   (assign, "$minstrels_discussed_love", 1),
   ]],

  [anyone, "minstrel_nobles", [],
   "Nobles are an odd lot. In Calradia, a daughter is a political asset, to be given away to a lord with whom her father wishes to make an alliance. Yet the great families of this land idealize pure love between man and woman, and I have seen many a hardened warrior weep copious tears at the doomed ardour of Sahira and Janun in the songs -- even as he made plans to break his own daughter's heart.",
"minstrel_nobles_2", []],

  [anyone, "minstrel_nobles_2", [],
   "Fathers differ, of course. Some Calradian nobles will let their daughters choose a husband who pleases them. Others, however, feel that to allow their daughters any choice at all would be to diminish their own authority, and insist on imposing a groom whether she likes it or not.",
"minstrel_nobles_3", []],

  [anyone, "minstrel_nobles_3", [], "But the majority will steer a middle course -- they will want to make the final decision about a groom, but will weigh their daughter's preferences heavily. Among other factors, a happy marriage is more likely to produce heirs. So, there is a place for courtship, and for the use of skill and passion to win a lady's heart.",
"minstrel_prequestions", []],

  [anyone|plyr, "minstrel_courtship_questions_2", [
  (eq, "$minstrels_discussed_love", 1),
  ],
   "What if a lady and her father disagree about a suitor?",
   "minstrel_daughter_father", []],

  [anyone, "minstrel_daughter_father", [], "It happens sometimes that a bride elopes. This is a major blow to the father's prestige, leading to lasting enmities. Indeed, it is possible that a war may be fought over a woman. Now, that is a fine topic for a song.",
   "minstrel_daughter_father_2", []],

  [anyone, "minstrel_daughter_father_2", [], "In the end, however, most brides will submit to their parents' choice. A noblewoman's family is everything to her, and few are brave enough to risk its disapproval for the sake of man she barely knows. She may pine for her lover, but still accept the groom -- and without tragic love, what would we have to sing about?",
   "minstrel_prequestions", []],



   [anyone, "minstrel_player_role", [
   (troop_get_type, ":is_female", "trp_player"),
   (eq, ":is_female", 0),
   ], "Of course! Calradian lords make a great deal of lineage, but in the end, lands and money speak louder than one's ancestors. Even though you are a foreigner, if you are coming up in the world, then many parents will consider you a fine catch.",
   "minstrel_player_role_2", []],

   [anyone, "minstrel_player_role_2", [
   ], "You will have to compete with many other lords of your realm, however, who will have an advantage -- they have known these ladies from childhood, and will have been sized up as grooms by carefully discerning mothers and aunts. Some ladies may be fascinated by the stranger, yet opt for the familiar.",
   "minstrel_player_role_3", []],

   [anyone, "minstrel_player_role_3", [
   ], "So know this -- you may have your heart broken. But to enter the arena of love fearing heartbreak is like entering the battlefield fearing the enemy's arrows. Be brave, and shrug off the sting of rejection, and victory may yet be yours.",
   "minstrel_prequestions", []],

##diplomacy start+ Make either-gender version, if gender roles are reversed
  [anyone, "minstrel_player_role", [
   ], "{Sir/Lady} -- I will speak bluntly. Most of the {ladies/lords} of this land are looking for a demure {lad/maiden}, whose skin as fair as snow -- and your skin is burnt brown by the sun. They want a {boy/maiden} whose voice is soft as bells -- and your voice is hoarse from commanding {soldiers/men} in battle. Also, athough the {ladies/lords} of Calradia appreciate poems about love, most also want heirs, and few {men/women} can ride and fight while {caring for their children/with child}.",
   "minstrel_female_player_3", []],


  [anyone, "minstrel_female_player_3", [
   ], "However, not all {ladies/lords} will be so conventionally minded. We poets sing of shield {boys/maidens} and of {hunters/huntresses}, of {lads/women} who forged their own path without having sacrificed the chance for love. I would not tell you that it would be easy for you to find a devoted {wife/husband} who will accept your ways, but I would not say that it is impossible.",
   "minstrel_prequestions", []],
##diplomacy end+

  [anyone|plyr, "minstrel_courtship_questions_2", [
  (eq, "$minstrels_discussed_love", 1),
  ],
   "What advantage is there in seeking a {wife/husband}?",
   "minstrel_spouse_benefits", []],

  [anyone, "minstrel_spouse_benefits", [
  (troop_get_type, ":is_female", "trp_player"),
  (eq, ":is_female", 0),
  ],
   "Ah! You are quite the romantic, I see! Well, aside from the obvious benefits of love, companionship and other, em, domestic matters, to marry among the nobility brings great assets. You may forge a strong alliance with the bride's family, and a wife may also assist you in manipulating the politics of the realm to your advantage.",
   "minstrel_wife_benefits_2", []],

  [anyone, "minstrel_wife_benefits_2", [
  ],
   "What's more, most of the great families of Calradia have at some point intermarried with royalty, which would boost your own claim to rule -- should you ever choose to assert it...",
   "minstrel_prequestions", []],

  [anyone, "minstrel_spouse_benefits", [
  (troop_get_type, ":is_female", "trp_player"),
  (eq, ":is_female", 1),
  ],
   "Ah! You are quite the romantic, I see! Well, aside from the obvious benefits of love, companionship and other, em, domestic matters, to marry among the nobility brings great assets. You may have access to the groom's castles and properties, and be able to work with him to advance both of your standings in the realm.",
   "minstrel_wife_benefits_2", []],



   [anyone, "minstrel_player_advice_meet", [
   ], "Every so often, a king or great lord of Calradia will hold a feast. In towns they will often be accompanied by tournaments, and in castles they will be accompanied by hunts. The feasts provide a chance for the lords to repair some of the rivalries that may undermine the strength of the realm. They also provide an opportunity for families to show off their eligible daughters, and ladies will often be allowed to mingle unsupervised with the guests.",
   "minstrel_player_advice_meet_2", []],

   [anyone, "minstrel_player_advice_meet_2", [
   ], "If you have the opportunity, you may attempt to pay the lady a compliment. This indicates to her that you are a potential suitor, and she will usually know if she wishes you to continue your suit. Incidentally, if you come to her fresh from having distinguished yourself in the tournament or in the hunt, then you may make a stronger first impression than otherwise.",
   "minstrel_prequestions", []],


  [anyone, "minstrel_player_advice_woo", [
   ], "To woo a lady takes a certain amount of time and patience, and several meetings spaced over a period of months. A lady who is interested in you will often find ways of letting you know if she wishes you to come visit her. Alternately, you may simply go and ask her father or brother for permission. If you do not have permission from her guardian, it may be possible to arrange an assignation through other means.",
   "minstrel_player_advice_woo_2", []],

  [anyone, "minstrel_player_advice_woo_2", [
   ], "Having arranged an assignment, you may then attempt to charm her and win her favor. Perhaps one of the most difficult aspects of this is finding a topic of conversation. Most Calradian noblewomen lead a cloistered life, at least until they are married, and thus will have little to say that will interest you. On other hand, she will soon tire of hearing of your own deeds in the outside world.",
   "minstrel_player_advice_woo_3", []],

  [anyone, "minstrel_player_advice_woo_3", [
   ], "One time-tested mode of courtship is simply to recite a popular poem, and discuss it. This way, you are both on an equal footing, and neither will have an advantage in knowledge or experience. Of course, different ladies will have different tastes in poetry.",
   "minstrel_player_advice_woo_4", []],

  [anyone, "minstrel_player_advice_woo_4", [
   ], "At some point, you will be able to discuss directly the issue of marriage. She will then let you know if you measure up to what she wants in a husband. Some ladies will coolly assess who is the most prestigious of her suitors, others will be guided by their passions. Some will look to your companions, to see whether you are the kind of husband who will treat her as an equal, while others will follow the lead of their fathers.",
   "minstrel_player_advice_woo_5", []],

  [anyone, "minstrel_player_advice_woo_5", [
   ], "At any rate, it is a challenging business -- and do not forget, you may find that your suit prospers with a lady, only to have it falter on a father's political ambitions. So you must ask yourself: are you willing to risk disappointment and heartbreak? Alternately, are you willing to throw away your standing in society, to make enemies of allies, in pursuit of a forbidden love? Because if you are, then perhaps some day we will write poems about you.",
   "minstrel_prequestions", []],


  [anyone|plyr, "minstrel_courtship_questions_2", [],
   "What is it that you poets and musicians do again?",
   "minstrel_job_description", []],

   [anyone, "minstrel_job_description", [],
   "I compose and write songs for the lords of the land, and their ladies. Sometimes I sing about war, sometimes about the virtues of kings, and sometimes, for the more sophisticated audiences, about the virtues of wine. For most audiences, however, I sing of love.", "minstrel_courtship_prequestions", []],

  [anyone|plyr, "minstrel_courtship_questions_2", [],
   "No, that is all.",
   "minstrel_pretalk", []],

  [anyone, "minstrel_prequestions", [
   ], "Do you have any other questions?",
   "minstrel_courtship_questions_2", []],

  [anyone, "minstrel_pretalk", [],
   "Is there anything else?",
   "minstrel_1", []],







   
	##diplomacy start+
	##Tavern Talk (with farmers)
	##Alternate opening lines when the farmer should know who the player is.
	  [anyone, "start", [(eq, "$talk_context", tc_tavern_talk),
						 (eq, "$g_talk_troop", "trp_farmer_from_bandit_village"),
						 (neg|check_quest_active, "qst_eliminate_bandits_infesting_village"),
						 (neg|check_quest_active, "qst_deal_with_bandits_at_lords_village"),
						 (assign, ":end_cond", villages_end),
						 (try_for_range, ":cur_village", villages_begin, ":end_cond"),
						   (party_slot_eq, ":cur_village", slot_village_bound_center, "$g_encountered_party"),
						   (party_slot_ge, ":cur_village", slot_village_infested_by_bandits, 1),
						##Floris MTT begin
						   (party_template_get_slot,":woman_peasant","$troop_trees",slot_woman_peasant),
						   (neg|party_slot_eq, ":cur_village", slot_village_infested_by_bandits, ":woman_peasant"),#not insurrection
						##Floris MTT end
						   (str_store_party_name, s1, ":cur_village"),
						   (quest_set_slot, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, ":cur_village"),
						   (quest_set_slot, "qst_eliminate_bandits_infesting_village", slot_quest_current_state, 0),
						   (party_get_slot, ":village_elder", ":cur_village", slot_town_elder),
						   (quest_set_slot, "qst_eliminate_bandits_infesting_village", slot_quest_giver_troop, ":village_elder"),
						   (quest_set_slot, "qst_eliminate_bandits_infesting_village", slot_quest_giver_center, ":cur_village"),
						   (assign, ":end_cond", 0),
						 (try_end),
						#Player is a lord in this kingdom, or a notable lord is his own kingdom
						(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$g_encountered_party_faction"),
						(this_or_next|gt, reg0, DPLMC_FACTION_STANDING_MEMBER),#i.e. not just a mercenary
						   (troop_slot_ge, "trp_player", slot_troop_renown, 600),

						 (assign, "$temp", ":cur_village"),#Save the village for later use in the conversation
						 (assign, "$temp_2", 1),#Player is famous

								(call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$g_encountered_party"),
								(val_sub, reg0, 2),
								(val_max, reg0, 0),#i.e. only non-zero if >= 3
								(str_clear, s0),
						 ],
	   "{reg0?Your highness:My {lord/lady}}, we are in dire need of assistance.  Will you hear my plea?", "farmer_from_bandit_village_1", []],
	##diplomacy end+
	#Tavern Talk (with farmers)
	  [anyone, "start", [(eq, "$talk_context", tc_tavern_talk),
						 (eq, "$g_talk_troop", "trp_farmer_from_bandit_village"),
						 (neg|check_quest_active, "qst_eliminate_bandits_infesting_village"),
						 (neg|check_quest_active, "qst_deal_with_bandits_at_lords_village"),
						 (assign, ":end_cond", villages_end),
						 (try_for_range, ":cur_village", villages_begin, ":end_cond"),
						   (party_slot_eq, ":cur_village", slot_village_bound_center, "$g_encountered_party"),
						   (party_slot_ge, ":cur_village", slot_village_infested_by_bandits, 1),
						   ##diplomacy begin
							##Floris MTT begin
							(party_template_get_slot,":woman_peasant","$troop_trees",slot_woman_peasant),
						    (neg|party_slot_eq, ":cur_village", slot_village_infested_by_bandits, ":woman_peasant"),
							##Floris MTT end
						   ##diplomacy_end
						   (str_store_party_name, s1, ":cur_village"),
						   (quest_set_slot, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, ":cur_village"),
						   (quest_set_slot, "qst_eliminate_bandits_infesting_village", slot_quest_current_state, 0),
						   (party_get_slot, ":village_elder", ":cur_village", slot_town_elder),
						   (quest_set_slot, "qst_eliminate_bandits_infesting_village", slot_quest_giver_troop, ":village_elder"),
						   (quest_set_slot, "qst_eliminate_bandits_infesting_village", slot_quest_giver_center, ":cur_village"),
						   (assign, ":end_cond", 0),
						 (try_end),
						 ##diplomacy start+ Save the village for use later in the conversation
						 (assign, "$temp", ":cur_village"),
						 (assign, "$temp_2", 1),#player is not a lord of this faction or a well-known lord of another faction
						 ##diplomacy end+
						 ],
	   "{My lord/Madam}, you look like a {man/lady} of the sword and someone who could help us.\
 Will you hear my plea?", "farmer_from_bandit_village_1", []],

	  [anyone|plyr, "farmer_from_bandit_village_1", [
	  ##diplomacy start+ either gender
	  ],# "man" -> "{reg65?woman:man}"
	   "What is the matter, my good {reg65?woman:man}?", "farmer_from_bandit_village_2", []],
	   ##diplomacy end+
	   
	   [anyone|plyr, "farmer_from_bandit_village_1", [],
	   "What are you burbling about peasant? Speak out.", "farmer_from_bandit_village_2", []],

	##diplomacy start+
	##Add this if the lord is the player, to skip the "why don't you ask your lord?" line.
	  [anyone, "farmer_from_bandit_village_2", [
	   (assign, ":lord_is_player", 0),
	   (try_begin),
		  (party_slot_eq, "$temp", slot_town_lord, "trp_player"),
		  (store_faction_of_party, ":village_faction", "$temp"),
		  (this_or_next|eq, ":village_faction", "$players_kingdom"),
			 (eq, ":village_faction", "fac_player_supporters_faction"),
		  (assign, ":lord_is_player", 1),
	   (try_end),
	   (neq, ":lord_is_player", 0),

	  (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
	  ],
	   "A band of brigands have taken refuge in our village. They take everything we have, force us to serve them, and do us much evil.\
 If one of us so much as breathes a word of protest, they kill the poor soul on the spot right away.\
 Our lives have become unbearable. I risked my skin and ran away to find someone who can help us.\
 Please {s0}, you are a {man/lady} of valor and a fearsome warrior, with many friends and soldiers at your service.\
 If there is anyone who can help us, it's you.", "farmer_from_bandit_village_5", [(assign, "$temp", 0)]],
	##diplomacy end+

  [anyone, "farmer_from_bandit_village_2", [],
   "A band of brigands have taken refuge in our village. They take everything we have, force us to serve them, and do us much evil.\
 If one of us so much as breathes a word of protest, they kill the poor soul on the spot right away.\
 Our lives have become unbearable. I risked my skin and ran away to find someone who can help us.", "farmer_from_bandit_village_3", []],

##diplomacy start+
## If the town has a lord that the player has met, use the correct gender.
#  [anyone|plyr, "farmer_from_bandit_village_3", []
#   "Why don't you go to the lord of your village? He should take care of the vermin.", "farmer_from_bandit_village_4", []],
  [anyone|plyr, "farmer_from_bandit_village_3", [
     (assign, reg0, 0),
	  (try_begin),
	     (gt, "$temp", 1),
		  (party_slot_ge, "$temp", slot_town_lord, 1),
		  (party_get_slot, ":town_lord", "$temp", slot_town_lord),
		  (troop_slot_ge, ":town_lord", slot_troop_met, 1),
		  (call_script, "script_dplmc_store_troop_is_female", ":town_lord"),
	  (try_end),
  ],
   "Why don't you go to the {reg0?mistress:lord} of your village? {reg0?She:He} should take care of the vermin.", "farmer_from_bandit_village_4", []],

##Different line if the village lord is in captivity
  [anyone, "farmer_from_bandit_village_4", [  
  (gt, "$temp", 1),
  (party_slot_ge, "$temp", slot_town_lord, 1),
  (party_get_slot, ":town_lord", "$temp", slot_town_lord),
  (troop_slot_ge, ":town_lord", slot_troop_prisoner_of_party, 0),
  (call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$g_encountered_party"),
  (call_script, "script_dplmc_store_troop_is_female", ":town_lord"),
  (assign, reg1, "$temp_2"),
  ],
   "Our {reg0?lady:lord} is imprisoned, so we cannot go to {reg0?her:him} for protection.\
 Please {s0}, you {reg1?are:look like} a {man/lady} of valor, {reg1?with:and you have no doubt} many friends and soldiers at your service. \
 If there is anyone who can help us, it's you.", "farmer_from_bandit_village_5", [(assign, "$temp", 0)]],

##Different line if the village has no lord
  [anyone, "farmer_from_bandit_village_4", [  
  (gt, "$temp", 1),
  (neg|party_slot_ge, "$temp", slot_town_lord, 1),
  (call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$g_encountered_party"),
  (assign, reg1, "$temp_2"),
  ],
   "We have no lord, so we cannot go to him for protection.\
 Please {s0}, you {reg1?are:look like} a {man/lady} of valor, {reg1?with:and you have no doubt} many friends and soldiers at your service. \
 If there is anyone who can help us, it's you.", "farmer_from_bandit_village_5", [(assign, "$temp", 0)]],

##Alter the default line to be different when the player is recognized
  [anyone, "farmer_from_bandit_village_4", [
  (call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$g_encountered_party"),
  (party_get_slot, ":town_lord", "$temp", slot_town_lord),
  (call_script, "script_dplmc_store_troop_is_female", ":town_lord"),
  (assign, reg1, "$temp_2"),
  ],
   "I did, {s0}, but our {reg0?lady:lord}'s {reg0?servants:men} did not let me see {reg0?her:him} and said {reg0?she:he} was occupied with more important matters and that we should deal with our own problem ourselves.\
 Please {s0}, you {reg1?are:look like} a {man/lady} of valor and a fearsome warrior, {reg1?with:and you have no doubt} many friends and soldiers at your service. \
 If there is anyone who can help us, it's you.", "farmer_from_bandit_village_5", [(assign, "$temp", 0)]],
##diplomacy end+

  [anyone|plyr, "farmer_from_bandit_village_5", [],
   "Very well, I'll help you. Where is this village?", "farmer_from_bandit_village_accepted", []],
  [anyone|plyr, "farmer_from_bandit_village_5", [],
   "I can't be bothered with this right now.", "farmer_from_bandit_village_denied", []],
  [anyone|plyr, "farmer_from_bandit_village_5", [(eq, "$temp", 0)],
   "Why would I fight these bandits? What's in it for me?", "farmer_from_bandit_village_barter", []],


  [anyone, "farmer_from_bandit_village_accepted", [##diplomacy start+
    (call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$g_encountered_party"),
  ],#Next line, replace {sir/madam} with {s0}
   #"God bless you, {sir/madam}. Our village is {s7}. It is not too far from here.", "close_window",
   "God bless you, {s0}. Our village is {s7}. It is not too far from here.", "close_window",
   ##diplomacy end+
   [(quest_get_slot, ":target_center", "qst_eliminate_bandits_infesting_village", slot_quest_target_center),
    (str_store_party_name_link,s7,":target_center"),
    (setup_quest_text, "qst_eliminate_bandits_infesting_village"),
    (str_store_string, s2, "@A villager from {s7} begged you to save their village from the bandits that took refuge there."),
    (call_script, "script_start_quest", "qst_eliminate_bandits_infesting_village", "$g_talk_troop"),
    ]],

  [anyone, "farmer_from_bandit_village_denied", [],"As you say {sir/madam}. Forgive me for bothering you.", "close_window", []],

  [anyone, "farmer_from_bandit_village_barter", [##diplomacy start+
  (call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$g_encountered_party"),
    ],#Next line, replace {sir/madam} with {s0}
   "We are but poor farmers {s0}, and the bandits have already got most of what we have on this world.\
 but we'll be glad to share with you whatever we have got.\
 And we'll always be in your gratitude if you help us.", "farmer_from_bandit_village_5", [(assign, "$temp", 1)]],
##diplomacy end+

  [anyone, "start", [(eq, "$talk_context", tc_tavern_talk),
                     (eq, "$g_talk_troop", "trp_farmer_from_bandit_village"),
                     (check_quest_active, "qst_eliminate_bandits_infesting_village"),
    ##diplomacy start+
    ##OLD:
    #                 ],
    #"Thank you for helping us {sir/madam}. Crush those bandits!", "close_window", []],
    ##NEW:
                     (call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$g_encountered_party"),
                      ],
    "Thank you for helping us {s0}. Crush those bandits!", "close_window", []],
    ##diplomacy end+


#Tavern Talk (with troops)

  [anyone, "start", [
                     (eq, "$talk_context", tc_tavern_talk),
					 (neg|troop_is_hero, "$g_talk_troop"),
                     (neg|is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
					 (assign, ":mercenary_amount", -1),
                     #(party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type),
                     #(party_get_slot, ":mercenary_amount", "$g_encountered_party", slot_center_mercenary_troop_amount),
                     (try_begin),                                            #Extra mercenaries in tavern
						 (party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type),
						 (eq, "$g_talk_troop", ":mercenary_troop"),
						 (party_get_slot, ":mercenary_amount", "$g_encountered_party", slot_center_mercenary_troop_amount),
                     (else_try),
						(party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type_2),
						(eq, "$g_talk_troop", ":mercenary_troop"),
						(party_get_slot, ":mercenary_amount", "$g_encountered_party", slot_center_mercenary_troop_amount_2),
                     (try_end),                                              #Tavern end
                     (gt, ":mercenary_amount", 0),
                     (store_sub, reg3, ":mercenary_amount", 1),
                     (store_sub, reg4, reg3, 1),
                     (call_script, "script_game_get_join_cost", ":mercenary_troop"),
                     (assign, ":join_cost", reg0),
                     (store_mul, reg5, ":mercenary_amount", reg0),
                     (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
                     (val_min, ":mercenary_amount", ":free_capacity"),
                     (store_troop_gold, ":cur_gold", "trp_player"),
                     (try_begin),
                       (gt, ":join_cost", 0),
                       (val_div, ":cur_gold", ":join_cost"),
                       (val_min, ":mercenary_amount", ":cur_gold"),
                     (try_end),
                     (assign, "$temp", ":mercenary_amount"),
                     ],
   "Do you have a need for mercenaries, {sir/madam}?\
 {reg3?Me and {reg4?{reg3} of my mates:one of my mates} are:I am} looking for a master.\
 We'll join you for {reg5} denars.", "mercenary_tavern_talk", []],

  [anyone, "start", [
  (eq, "$talk_context", tc_tavern_talk),
  ],
   "Any orders, {sir/madam}?", "mercenary_after_recruited", []],

  [anyone|plyr, "mercenary_after_recruited", [],
   "Make your preparations. We'll be moving at dawn.", "mercenary_after_recruited_2", []],
  [anyone|plyr, "mercenary_after_recruited", [],
   "Take your time. We'll be staying in this town for a while.", "mercenary_after_recruited_2", []],

  [anyone, "mercenary_after_recruited_2", [], "Yes {sir/madam}. We'll be ready when you tell us to leave.", "close_window", []],

  [anyone|plyr, "mercenary_tavern_talk", [(try_begin),     #More Mercaneries Tavern
                                          (party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type),
                                          (eq, "$g_talk_troop", ":mercenary_troop"),                     
                                          (party_get_slot, ":mercenary_amount", "$g_encountered_party", slot_center_mercenary_troop_amount),
                                          (else_try),
                                          (party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type_2),
                                          (party_get_slot, ":mercenary_amount", "$g_encountered_party", slot_center_mercenary_troop_amount_2),
                                          (try_end),
                                          (eq, ":mercenary_amount", "$temp"),
                                         #(party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type),
                                          (call_script, "script_game_get_join_cost", ":mercenary_troop"),
                                          (store_mul, reg5, "$temp", reg0), #Tavern End
                                          ],
   "All right. I will hire all of you. Here is {reg5} denars.", "mercenary_tavern_talk_hire", []],

  [anyone|plyr, "mercenary_tavern_talk", [(try_begin),     #More Mercaneries Tavern
                                          (party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type),
                                          (eq, "$g_talk_troop", ":mercenary_troop"),                     
                                          (party_get_slot, ":mercenary_amount", "$g_encountered_party", slot_center_mercenary_troop_amount),
                                          (else_try),
                                          (party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type_2),
                                          (party_get_slot, ":mercenary_amount", "$g_encountered_party", slot_center_mercenary_troop_amount_2),
                                          (try_end),
                                          (lt, "$temp", ":mercenary_amount"),
                                          (gt, "$temp", 0),
                                          (assign, reg6, "$temp"),
                                          #(party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type),
                                          (call_script, "script_game_get_join_cost", ":mercenary_troop"),
                                          (store_mul, reg5, "$temp", reg0),
                                          ],
   "All right. But I can only hire {reg6} of you. Here is {reg5} denars.", "mercenary_tavern_talk_hire", []],


  [anyone, "mercenary_tavern_talk_hire", [(store_random_in_range, ":rand", 0, 4),
                                          (try_begin),
                                            (eq, ":rand", 0),
                                            (gt, "$temp", 1),
											##diplomacy start+ lads -> {reg65?companions:lads}; {sir/madame} -> {s0}
											(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
                                            (str_store_string, s17,
                                             "@You chose well, {s0}. My {reg65?companions:lads} know how to keep their word and earn their pay."),
											 ##diplomacy end+
                                          (else_try),
                                            (eq, ":rand", 1),
											##diplomacy start+ {sir/madame} -> {s0}
											(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
                                            (str_store_string, s17,
                                             "@Well done, {s0}. Keep the money and wine coming our way, and there's no foe in Calradia you need fear."),
											 ##diplomacy end+
                                          (else_try),
                                            (eq, ":rand", 2),
											##diplomacy start+ {sir/madame} -> {s0}
											(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
                                            (str_store_string, s17,
                                             "@We are at your service, {s0}. Point us in the direction of those who need hurting, and we'll do the rest."),
											 ##diplomacy end+
                                          (else_try),
                                            (str_store_string, s17,
                                             "str_you_will_not_be_disappointed_sirmadam_you_will_not_find_better_warriors_in_all_calradia"),
                                          (try_end),],
   "{s17}", "close_window", [
#                                          (party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type),
                                          (try_begin),     #More Mercaneries Tavern
                                          (party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type),
                                          (eq, "$g_talk_troop", ":mercenary_troop"),                     
                                          (assign, ":slot", slot_center_mercenary_troop_amount),
                                          (else_try),
                                          (party_get_slot, ":mercenary_troop", "$g_encountered_party", slot_center_mercenary_troop_type_2),
                                          (assign, ":slot", slot_center_mercenary_troop_amount_2),
                                          (try_end),
                                          (call_script, "script_game_get_join_cost", ":mercenary_troop"),
                                          (store_mul, ":total_cost", "$temp", reg0),
                                          (troop_remove_gold, "trp_player", ":total_cost"),
                                          (party_add_members, "p_main_party", ":mercenary_troop", "$temp"),
#                                          (party_set_slot, "$g_encountered_party", slot_center_mercenary_troop_amount, 0),
										  (party_set_slot, "$g_encountered_party", ":slot", 0),
                                          ]],

  [anyone|plyr, "mercenary_tavern_talk", [(eq, "$temp", 0),
                                          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
                                          (ge, ":free_capacity", 1)],
##diplomacy start+ Gender-check to avoid accidental absurdities if there are female mercenaries
   "That sounds good. But I can't afford to hire any more {reg65?soldiers:men} right now.", "tavern_mercenary_cant_lead", []],
##diplomacy end+

  [anyone, "tavern_mercenary_cant_lead", [], "That's a pity. Well, {reg3?we will:I will} be lingering around here for a while,\
 if you need to hire anyone.", "close_window", []],

  [anyone|plyr, "mercenary_tavern_talk", [(eq, "$temp", 0),
                                          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
                                          (eq, ":free_capacity", 0)],
##diplomacy start+ Gender-check to avoid accidental absurdities if there are female mercenaries
   "That sounds good. But I can't lead any more {reg65?soldiers:men} right now.", "tavern_mercenary_cant_lead", []],
##diplomacy end+

  [anyone|plyr, "mercenary_tavern_talk", [],
   "Sorry. I don't need any other men right now.", "close_window", []],

#Trainers
  [anyone,"start", [(is_between, "$g_talk_troop", training_gound_trainers_begin, training_gound_trainers_end),
                    (eq, "$g_talk_troop_met", 0)],
   "Good day to you {lad/lass}. You look like another adventurer who has come to try {his/her} chance in these lands.\
 Well, trust my word, you won't be able to survive long here unless you know how to fight yourself out of a tight spot.", "trainer_intro_1",[]],

  [anyone|plyr, "trainer_intro_1", [],
   "Thank you for your advice. This place looks like a training field. Maybe I can learn about fighting here?", "trainer_intro_2", []],

  [anyone,"trainer_intro_2", [],
   "Indeed you can. I am a veteran soldier... fought a good deal in the wars in my time. But these days, I train young novices in this area.\
 I can find you some opponents to practice with if you like. Or if you have any questions about the theory of combat, feel free to ask.", "trainer_intro_3",[]],

  [anyone|plyr, "trainer_intro_3", [],
   "Yes, I do have a few questions.", "trainer_intro_4a", []],
  [anyone|plyr, "trainer_intro_3", [],
   "Actually, I can move on to practice.", "trainer_intro_4b", []],

  [anyone, "trainer_intro_4a", [],
   "Well, ask anything you like.", "trainer_talk_combat", []],
  [anyone, "trainer_intro_4b", [],
   "Good. It's good to find someone eager for practice. Let's see what you will do.", "trainer_practice_1", []],

 [anyone,"start", [(is_between, "$g_talk_troop", training_gound_trainers_begin, training_gound_trainers_end),
                   (neq,"$waiting_for_training_fight_result", 0),
                   (neq,"$training_fight_won", 0)],
 "That was a good fight. ", "trainer_practice_1",
  [(val_sub, "$num_opponents_to_beat_in_a_row", 1),
   (assign,"$waiting_for_training_fight_result",0),
   ]],
  [anyone,"start", [(is_between, "$g_talk_troop", training_gound_trainers_begin, training_gound_trainers_end),
                    (neq, "$waiting_for_training_fight_result", 0)],
 "Ha! Looks like you've developed a bit of a limp there. Don't worry, even losses have their value, provided you learn from them. Shake the stars out of your eyes and get back in there. There's no other way to win.", "trainer_practice_1",
   [(assign,"$num_opponents_to_beat_in_a_row",3),(assign,"$waiting_for_training_fight_result",0)]],

    [anyone,"start", [(is_between, "$g_talk_troop", training_gound_trainers_begin, training_gound_trainers_end)],
   "Good day. Ready for some training today?", "trainer_talk",[]],

    [anyone,"trainer_pretalk", [],
   "Ah, are you ready for some training?", "trainer_talk",[]],

    [anyone|plyr,"trainer_talk", [],
   "I am ready for some practice.", "trainer_practice_1",[]],

    [anyone|plyr,"trainer_talk", [],
   "First, tell me something about combat...", "trainer_combat_begin",[]],

##    [anyone|plyr,"trainer_talk", [],
##   "I have some novice soldiers with me. Can you train them?", "trainer_train_novices_1",[]],

    [anyone|plyr,"trainer_talk", [],
   "I need to leave now. Farewell.", "close_window",[]],


    [anyone,"trainer_combat_begin", [],
   "What do you want to know?", "trainer_talk_combat",[]],
    [anyone,"trainer_combat_pretalk", [],
   "What else do you want to know?", "trainer_talk_combat",[]],

    [anyone|plyr,"trainer_talk_combat", [], "Tell me about defending myself.", "trainer_explain_defense",[]],
    [anyone|plyr,"trainer_talk_combat", [], "Tell me about attacking with weapons.", "trainer_explain_attack",[]],
    [anyone|plyr,"trainer_talk_combat", [], "Tell me about fighting on horseback.", "trainer_explain_horseback",[]],
#    [anyone|plyr,"trainer_talk_combat", [], "Tell me about using ranged weapons.", "trainer_explain_ranged",[]],
#    [anyone|plyr,"trainer_talk_combat", [], "Tell me about weapon types.", "trainer_explain_weapon_types",[]],
    [anyone|plyr,"trainer_talk_combat", [], "I guess I know all the theory I need. Let's talk about something else.", "trainer_pretalk",[]],

   [anyone,"trainer_explain_defense", [], "Good question. The first thing you should know as a fighter is how to defend yourself.\
 Keeping yourself out of harm's way is the first rule of combat, and it is much more important than giving harm to others.\
 Everybody can swing a sword around and hope to cut some flesh, but only those fighters that are experts at defense live to tell of it.",
	"trainer_explain_defense_2",[]],
  [anyone,"trainer_explain_defense_2", [], "Now. Defending yourself is easiest if you are equipped with a shield.\
 Just block with your shield. [Hold down the right mouse button to defend yourself with the shield.] In this state, you will be able to deflect all attacks that come from your front. However, you will still be open to strikes from your sides or your back.", "trainer_explain_defense_3",[]],
  [anyone|plyr,"trainer_explain_defense_3", [], "What if I don't have a shield?", "trainer_explain_defense_4",[]],
  [anyone,"trainer_explain_defense_4", [], "Then you will have to use your weapon to block your opponent.\
 This is a bit more difficult than defending with a shield.\
 Defending with a weapon, you can block against only ONE attack direction.\
 That is, you block against either overhead swings, side swings or thrusts.\
 Therefore you must watch your opponent carefully and start to block AFTER he starts his attack.\
 In this way you will be able to block against the direction of his current attack.\
 If you start to block BEFORE he makes his move, he may just attack in another direction than the one you are blocking against and score a hit.", "trainer_combat_pretalk",[]],
  [anyone,"trainer_explain_attack", [], "Good question. Attacking is the best defence, they say.\
 A tactic many fighters find useful is taking an offensive stance and readying your weapon for attack, waiting for the right moment for swinging it.\
 [You can ready your weapon for attack by pressing and holding down the left mouse button.]", "trainer_explain_attack_2",[]],
  [anyone|plyr,"trainer_explain_attack_2", [], "That sounds useful.", "trainer_explain_attack_3",[]],
  [anyone,"trainer_explain_attack_3", [], "It is a good tactic, but remember that, your opponent may see that and take a defensive stance against the direction you are swinging your weapon.\
 If that happens, you must break your attack and quickly attack from another direction\
 [You may cancel your current attack by quickly tapping the right mouse button].", "trainer_explain_attack_4",[]],
  [anyone|plyr,"trainer_explain_attack_4", [], "If my opponent is defending against the direction I am attacking from, I will break and use another direction.", "trainer_explain_attack_5",[]],
  [anyone,"trainer_explain_attack_5", [], "Yes, selecting the direction you swing your weapon is a crucial skill.\
 There are four main directions you may use: right swing, left swing, overhead swing and thrust. You must use each one wisely.\
 [to control your swing direction with default controls, move your mouse in the direction you want to swing from as you press the left mouse button].", "trainer_combat_pretalk",[]],
  [anyone,"trainer_explain_horseback", [], "Very good question. A horse may be a warrior's most powerful weapon in combat.\
 It gives you speed, height, power and initiative. A lot of deadly weapons will become even deadlier on horseback.\
 However you must pay particular attention to horse-mounted enemies couching their lances, as they may take down any opponent in one hit.\
 [To use the couched lance yourself, wield a lance or similar weapon, and speed up your horse without pressing attack or defense buttons.\
 after you reach a speed, you'll lower your lance. Then try to target your enemies by maneuvering your horse.]", "trainer_combat_pretalk",[]],

  [anyone,"trainer_practice_1", [(eq,"$training_system_explained", 0)],
 "I train novices in four stages, each tougher than the one before.\
 To finish a stage and advance to the next one, you have to win three fights in a row.", "trainer_practice_1",
   [
     (assign, "$num_opponents_to_beat_in_a_row", 3),
     (assign, "$novicemaster_opponent_troop", "trp_novice_fighter"),
     (assign, "$training_system_explained", 1),
     ]],
  [anyone,"trainer_practice_1",
   [(ge,"$novice_training_difficulty",4)],
 "You have passed all stages of training. But if you want you can still practice. Are you ready?", "novicemaster_are_you_ready",
   [(assign,"$num_opponents_to_beat_in_a_row",99999)]],
  [anyone,"trainer_practice_1",
   [(eq,"$num_opponents_to_beat_in_a_row",0),(eq,"$novice_training_difficulty",0)],
 "Way to go {lad/lass}. With this victory, you have advanced to the next training level. From now on your opponents will be regular fighters, not the riff-raff off the street, so be on your toes.",
   "trainer_practice_1",
   [[assign,"$num_opponents_to_beat_in_a_row",3],
    [val_add,"$novice_training_difficulty",1],
    [add_xp_to_troop,100],
    [assign,"$novicemaster_opponent_troop","trp_regular_fighter"]]],
  [anyone,"trainer_practice_1",
   [[eq,"$num_opponents_to_beat_in_a_row",0],[eq,"$novice_training_difficulty",1]],
 "Way to go {lad/lass}. Welcome to the third training level. From now on your opponents will be veteran fighters; soldiers and arena regulars and the like. These guys know some dirty tricks, so keep your defense up.",
   "trainer_practice_1",
   [[assign,"$num_opponents_to_beat_in_a_row",3],
    [val_add,"$novice_training_difficulty",1],
    [add_xp_to_troop,100],
    [assign,"$novicemaster_opponent_troop","trp_veteran_fighter"]]],
  [anyone,"trainer_practice_1",
   [[eq,"$num_opponents_to_beat_in_a_row",0],[eq,"$novice_training_difficulty",2]],
 "You've got the heart of a champion, {lad/lass}, and the sword arm to match. From now on your opponents will be champion fighters.\
 These are the cream of the crop, the finest warriors I have trained. If you can best three of them in a row, you will join their ranks.",
   "trainer_practice_1",
   [[assign,"$num_opponents_to_beat_in_a_row",3],
    [val_add,"$novice_training_difficulty",1],
    [add_xp_to_troop,100],
    [assign,"$novicemaster_opponent_troop","trp_champion_fighter"]]],
  [anyone,"trainer_practice_1",
   [[eq,"$num_opponents_to_beat_in_a_row",0],[eq,"$novice_training_difficulty",3]],
 "It does my heart good to see such a promising talent. You have passed all tiers of training. You can now tell everyone that you have been trained by the master of the training field.",
   "novicemaster_finish_training",
   [[assign,"$num_opponents_to_beat_in_a_row",3],
    [val_add,"$novice_training_difficulty",1],
    [add_xp_to_troop,300]]],
  [anyone|plyr,"novicemaster_finish_training", [], "Thank you master.", "novicemaster_finish_training_2",[]],
  [anyone,"novicemaster_finish_training_2", [], "I wish you good luck in the tournaments. And, don't forget,\
  if you want to practice your swordwork anytime, just come and say the word.", "close_window",[]],
  [anyone,"trainer_practice_1",
   [
     (assign, reg8, "$num_opponents_to_beat_in_a_row"),
     (str_store_troop_name, s9, "$novicemaster_opponent_troop"),
     ],
 "Your next opponent will be a {s9}. You need to win {reg8} more\
 fights in a row to advance to the next stage. Are you ready?", "novicemaster_are_you_ready",
   []],
  [anyone|plyr,"novicemaster_are_you_ready", [], "Yes I am.", "novicemaster_ready_to_fight",[]],
  [anyone,"novicemaster_ready_to_fight", [], "Here you go then. Good luck.", "close_window",
   [
     (assign, "$training_fight_won", 0),
     (assign, "$waiting_for_training_fight_result", 1),
     (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
     (reset_visitors),
     (assign, reg0, 0),
     (assign, reg1, 1),
     (assign, reg2, 2),
     (assign, reg3, 3),
     (shuffle_range, 0, 4),
     (set_visitor, reg0, "trp_player"),
     (set_visitor, reg1, "$novicemaster_opponent_troop"),
     (set_visitor, 4, "$g_talk_troop"),
     (set_jump_mission, "mt_training_ground_trainer_training"),
     (jump_to_scene, "$g_training_ground_melee_training_scene"),
     ]],

  [anyone|plyr,"novicemaster_are_you_ready", [], "Just a minute. I am not ready yet.", "novicemaster_not_ready",[]],
  [anyone,"novicemaster_not_ready", [], "Hey, You will never make it if you don't practice.", "close_window",[]],


#Crooks

##  [anyone ,"start", [(is_between,"$g_talk_troop",crooks_begin,crooks_end),(eq,"$g_talk_troop_met",0),(eq,"$sneaked_into_town",0),(store_random_in_range, reg2, 2)],
##   "You {reg2?looking for:want} something?:", "crook_intro_1",[]],
##  [anyone|plyr,"crook_intro_1",[],"I am trying to learn my way around the town.", "crook_intro_2",[]],
##
##  [anyone,"crook_intro_2",[(eq,"$crook_talk_order",0),(val_add,"$crook_talk_order",1),(str_store_troop_name,s1,"$g_talk_troop")],
##"Then you came to the right guy. My name is {s1}, and I know everyone and everything that goes around in this town.\
## Anyone you want to meet, I can arrange it. Anything you need to know, I can find out. For the the right price, of course. Do you have gold?", "crook_intro_2a",[]],
##  [anyone|plyr,"crook_intro_2a",[],"I have gold. Plenty of it.", "crook_intro_2a_1a",[]],
##  [anyone|plyr,"crook_intro_2a",[],"Not really.", "crook_intro_2a_1b",[]],
##  [anyone,"crook_intro_2a_1a",[],"Good. That means you and I will be great friends.", "crook_talk",[]],
##  [anyone,"crook_intro_2a_1b",[],"Then you should look into earning some. Listen to me now, for I'll give you some free advice.\
## The easiest way to make money is to fight in the tournaments and bet on yourself. If you are good, you'll quickly get yourself enough money to get going.", "crook_talk",[]],
##
##  [anyone,"crook_intro_2",[(eq,"$crook_talk_order",1),(val_add,"$crook_talk_order",1),(str_store_troop_name,s1,"$g_talk_troop")],
##"Then you need to go no further. I am {s1}, and I can provide you anything... For the the right price.", "crook_intro_2b",[]],
##  [anyone|plyr,"crook_intro_2b",[],"Are you a dealer?", "crook_intro_2b_1",[]],
##  [anyone,"crook_intro_2b_1",[],"A dealer? Yes. I deal in knowledge... connections.. lies... secrets... Those are what I deal in. Interested?", "crook_talk",[]],
##
##  [anyone,"crook_intro_2",[(eq,"$crook_talk_order",2),(val_add,"$crook_talk_order",1),(str_store_troop_name,s1,"$g_talk_troop")],
##"Then this is your lucky day. Because you are talking to {s1}, and I know every piss-stained brick of this wicked town.\
##I know every person, every dirty little secret. And all that knowledge can be yours. For a price.", "crook_talk",[]],
##
##  [anyone,"crook_intro_2",[(val_add,"$crook_talk_order",1),(str_store_troop_name,s1,"$g_talk_troop")],
## "Then {s1} is at your service {sir/madam}. If you want to know what's really going on in this town, or arrange a meeting in secret, then come to me. I can help you.", "crook_talk",[]],
##
##  [anyone ,"start", [(is_between,"$g_talk_troop",crooks_begin,crooks_end),(eq,"$g_talk_troop_met",0),(eq,"$sneaked_into_town",1),(eq,"$crook_sneak_intro_order",0),(val_add,"$crook_sneak_intro_order",1)],
##   "Good day. {playername} right?", "crook_intro_sneak_1",[]],
##  [anyone|plyr,"crook_intro_sneak_1", [], "You must be mistaken. I'm just a poor pilgrim. I don't answer to that name.", "crook_intro_sneak_2",[]],
##  [anyone,"crook_intro_sneak_2", [(str_store_troop_name,s1,"$g_talk_troop")], "Of course you do. And if the town guards knew you were here, they'd be upon you this minute.\
## But don't worry. Noone knows it is {playername} under that hood. Except me of course. But I am {s1}. It is my business to know things.", "crook_intro_sneak_3",[]],
##  [anyone|plyr,"crook_intro_sneak_3", [], "You won't tip off the guards about my presence?", "crook_intro_sneak_4",[]],
##  [anyone,"crook_intro_sneak_4", [], "What? Of course not! Well, maybe I would, but the new captain of the guards is a dung-eating cheat.\
## I led him to this fugitive, and the man was worth his weight in silver as prize money. But I swear, I didn't see a penny of it.\
## The bastard took it all to himself. So your secret is safe with me.", "crook_intro_sneak_5",[]],
##  [anyone,"crook_intro_sneak_5", [], "Besides, I heard you have a talent for surviving any kind of ordeal.\
## I wouldn't want you to survive this one as well and then come after me with a sword. Ha-hah.", "crook_talk",[]],
##
##
##  [anyone ,"start", [(is_between,"$g_talk_troop",crooks_begin,crooks_end),(eq,"$g_talk_troop_met",0),(eq,"$sneaked_into_town",1),(str_store_troop_name,s1,"$g_talk_troop")],
##   "{s1} is at your service {sir/madam}. If you want to know what's really going on in this town, or arrange a meeting in secret, then come to me. I can help you.", "crook_talk",[]],
##
##  [anyone ,"start", [(is_between,"$g_talk_troop",crooks_begin,crooks_end),(store_character_level, ":cur_level", "trp_player"),(lt,":cur_level",8)],
##   "{You again?/Delighted to see you again my pretty.}", "crook_talk",[]],
##  [anyone ,"start", [(is_between,"$g_talk_troop",crooks_begin,crooks_end)],
##   "I see that you need my services {sir/madam}...", "crook_talk",[]],
##  [anyone ,"crook_pretalk", [],
##   "Is that all?", "crook_talk",[]],



##  [anyone|plyr,"crook_talk", [], "I'm looking for a person...", "crook_search_person",[]],
##  [anyone|plyr,"crook_talk", [], "I want you to arrange me a meeting with someone...", "crook_request_meeting",[]],
##  [anyone|plyr,"crook_talk", [], "[Leave]", "close_window",[]],



#  [anyone,"crook_enter_dungeon", [],
#   "Alright but this will cost you 50 denars.", "crook_enter_dungeon_2", []],

#  [anyone|plyr, "crook_enter_dungeon_2", [(store_troop_gold, ":cur_gold", "trp_player"),
#                                            (ge, ":cur_gold", 50)],
#   "TODO: Here it is. 50 denars.", "crook_enter_dungeon_3_1",[(troop_remove_gold, "trp_player", 50)]],

#  [anyone|plyr, "crook_enter_dungeon_2", [(store_troop_gold, ":cur_gold", "trp_player"),
#                                            (ge, ":cur_gold", 50)],
#   "Never mind then.", "crook_pretalk",[]],

#  [anyone|plyr, "crook_enter_dungeon_2", [(store_troop_gold, ":cur_gold", "trp_player"),
#                                            (lt, ":cur_gold", 50)],
#   "TODO: I don't have that much money.", "crook_enter_dungeon_3_2",[]],

#  [anyone,"crook_enter_dungeon_3_1", [],
#   "TODO: There you go.", "close_window", [(call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle")]],

#  [anyone,"crook_enter_dungeon_3_2", [],
#   "TODO: Come back later then.", "crook_pretalk",[]],


##  [anyone, "crook_request_meeting", [],
##   "Who do you want to meet with?", "crook_request_meeting_2",[]],
##  [anyone|plyr|repeat_for_troops,"crook_request_meeting_2", [(store_encountered_party, ":center_no"),
##                                                             (store_repeat_object, ":troop_no"),
##                                                             (is_between, ":troop_no", heroes_begin, heroes_end),
##                                                             (troop_get_slot, ":cur_center", ":troop_no", slot_troop_cur_center),
##                                                             (call_script, "script_get_troop_attached_party", ":troop_no"),
##                                                             (assign, ":cur_center_2", reg0),
##                                                             (this_or_next|eq, ":cur_center", ":center_no"),
##                                                             (eq, ":cur_center_2", ":center_no"),
##                                                             (neg|party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),#Neglect the ruler of the center
##                                                             (str_store_troop_name, s1, ":troop_no")],
##   "{s1}", "crook_request_meeting_3", [(store_repeat_object, "$selected_troop")]],
##
##  [anyone|plyr,"crook_request_meeting_2", [], "Never mind.", "crook_pretalk", []],
##
##  [anyone,"crook_request_meeting_3", [],
##   "Alright but this will cost you 50 denars.", "crook_request_meeting_4", []],
##
##  [anyone|plyr, "crook_request_meeting_4", [(store_troop_gold, ":cur_gold", "trp_player"),
##                                            (ge, ":cur_gold", 50)],
##   "TODO: Here it is. 50 denars.", "crook_search_person_5_1",[(troop_remove_gold, "trp_player", 50)]],
##
##  [anyone|plyr, "crook_request_meeting_4", [(store_troop_gold, ":cur_gold", "trp_player"),
##                                            (ge, ":cur_gold", 50)],
##   "Never mind then.", "crook_pretalk",[]],
##
##  [anyone|plyr, "crook_request_meeting_4", [(store_troop_gold, ":cur_gold", "trp_player"),
##                                            (lt, ":cur_gold", 50)],
##   "TODO: I don't have that much money.", "crook_search_person_5_2",[]],
##
##  [anyone, "crook_search_person_5_1", [],
##   "TODO: Ok.", "close_window",[(party_get_slot, ":town_alley", "$g_encountered_party", slot_town_alley),
##                                (modify_visitors_at_site,":town_alley"),(reset_visitors),
##                                (set_visitor,0,"trp_player"),
##                                (set_visitor,17,"$selected_troop"),
##                                (set_jump_mission,"mt_conversation_encounter"),
##                                (jump_to_scene,":town_alley"),
##                                (assign, "$talk_context", tc_back_alley),
##                                (change_screen_map_conversation, "$selected_troop")]],
##
##  [anyone, "crook_search_person_5_2", [],
##   "TODO: Come back later then.", "crook_pretalk",[]],
##
##  [anyone, "crook_search_person", [],
##   "TODO: Who are you searching for?", "crook_search_person_2",[]],
##  [anyone|plyr|repeat_for_factions,"crook_search_person_2", [(store_repeat_object, ":faction_no"),
##                                                             (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
##                                                             (str_store_faction_name, s1, ":faction_no")],
##   "TODO: I'm looking for a {s1}.", "crook_search_person_3", [(store_repeat_object, "$selected_faction")]],
##
##  [anyone|plyr,"crook_search_person_2", [], "Never mind.", "crook_pretalk", []],
##
##
##  [anyone, "crook_search_person_3", [],
##   "TODO: Who?", "crook_search_person_4",[]],
##
##  [anyone|plyr|repeat_for_troops,"crook_search_person_4", [(store_repeat_object, ":troop_no"),
##                                                           (is_between, ":troop_no", heroes_begin, heroes_end),
##                                                           (store_troop_faction, ":faction_no", ":troop_no"),
##                                                           (eq, ":faction_no", "$selected_faction"),
##                                                           (str_store_troop_name, s1, ":troop_no")],
##   "{s1}", "crook_search_person_5", [(store_repeat_object, "$selected_troop")]],
##
##  [anyone|plyr,"crook_search_person_4", [], "Never mind.", "crook_pretalk", []],
##
##  [anyone, "crook_search_person_5", [(call_script, "script_get_information_about_troops_position", "$selected_troop", 0),
##                                     (eq, reg0, 1),
##                                     (str_store_troop_name, s1, "$selected_troop")],
##   "TODO: I know where {s1} is at the moment, but hearing it will cost you 50 denars.", "crook_search_person_6",[]],
##
##  [anyone, "crook_search_person_5", [],
##   "TODO: Sorry I don't know anything.", "crook_pretalk",[]],
##
##  [anyone|plyr, "crook_search_person_6", [(store_troop_gold, ":cur_gold", "trp_player"),
##                                          (ge, ":cur_gold", 50)],
##   "TODO: Here it is. 50 denars.", "crook_search_person_7_1",[(troop_remove_gold, "trp_player", 50)]],
##
##  [anyone|plyr, "crook_search_person_6", [(store_troop_gold, ":cur_gold", "trp_player"),
##                                          (ge, ":cur_gold", 50)],
##   "Never mind then.", "crook_pretalk",[]],
##
##  [anyone|plyr, "crook_search_person_6", [(store_troop_gold, ":cur_gold", "trp_player"),
##                                          (lt, ":cur_gold", 50)],
##   "TODO: I don't have that much money.", "crook_search_person_7_2",[]],
##
##  [anyone, "crook_search_person_7_1", [(call_script, "script_get_information_about_troops_position", "$selected_troop", 0)],
##   "{s1}", "crook_pretalk",[]],
##
##  [anyone, "crook_search_person_7_2", [],
##   "TODO: Come back later then.", "crook_pretalk",[]],
##

  [anyone|auto_proceed,"start", [
  (is_between,"$g_talk_troop","trp_town_1_master_craftsman", "trp_zendar_chest"),
  (party_get_slot, ":days_until_complete", "$g_encountered_party", slot_center_player_enterprise_days_until_complete),
  (ge, ":days_until_complete", 2),
  (assign, reg4, ":days_until_complete"),
  ],
   "{!}.", "start_craftsman_soon",[]],

  [anyone,"start_craftsman_soon", [
  ],
   "Good day, my {lord/lady}. We hope to begin production in about {reg4} days", "close_window",[]],

  [anyone,"start", [
  (is_between,"$g_talk_troop","trp_town_1_master_craftsman", "trp_zendar_chest"),
  ],
   "Good day, my {lord/lady}. We are honored that you have chosen to visit us. What do you require?", "master_craftsman_talk",[]],

  [anyone,"master_craftsman_pretalk", [],
   "Very good, my {lord/lady}. Do you require anything else?", "master_craftsman_talk",[]],

  [anyone|plyr,"master_craftsman_talk", [],
   "Let's go over the accounts.", "master_craftsman_accounts",[]],

  [anyone|plyr,"master_craftsman_talk", [],
   "Let's check the inventories.", "master_craftsman_pretalk",[
   (change_screen_loot, "$g_talk_troop"),
   ]],

  [anyone|plyr,"master_craftsman_talk", [
  (party_slot_eq, "$g_encountered_party", slot_center_player_enterprise_production_order, 1),
  ],
   "I'd like you to sell goods as they are produced.", "master_craftsman_pretalk",[
  (party_set_slot, "$g_encountered_party", slot_center_player_enterprise_production_order, 0),
   ]],

  [anyone|plyr,"master_craftsman_talk", [
  (party_slot_eq, "$g_encountered_party", slot_center_player_enterprise_production_order, 0),
  ],
   "I'd like you to keep all goods in the warehouse until I arrive.", "master_craftsman_pretalk",[
  (party_set_slot, "$g_encountered_party", slot_center_player_enterprise_production_order, 1),
   ]],

  [anyone,"master_craftsman_accounts", [
  ], "We currently produce {s3} worth {reg1} denars each week, while the quantity of {s4} needed to manufacture it costs {reg2}, and labor and upkeep are {reg3}.{s9} This means that we theoretically make a {s12} of {reg0} denars a week, assuming that we have no raw materials in the inventories, and that we sell directly to the market.", "master_craftsman_pretalk",
  [
    (party_get_slot, ":item_produced", "$g_encountered_party", slot_center_player_enterprise),
    (call_script, "script_process_player_enterprise", ":item_produced", "$g_encountered_party"),

    (try_begin),
	  (ge, reg0, 0),
	  (str_store_string, s12, "str_profit"),
    (else_try),
	  (str_store_string, s12, "str_loss"),
    (try_end),

    (str_store_item_name, s3, ":item_produced"),
    (item_get_slot, ":primary_raw_material", ":item_produced", slot_item_primary_raw_material),
    (str_store_item_name, s4, ":primary_raw_material"),

    (item_get_slot, ":secondary_raw_material", ":item_produced", slot_item_secondary_raw_material),
    (str_clear, s9),
    (try_begin),
	  (gt, ":secondary_raw_material", 0),
	  (str_store_item_name, s11, ":secondary_raw_material"),
	  (str_store_string, s9, "str_describe_secondary_input"),
    (try_end),
  ]],



  [anyone|plyr,"master_craftsman_talk", [
  ], "Could you explain my options related to production?", "master_craftsman_production_options",[]],

  [anyone,"master_craftsman_production_options", [
  (str_store_party_name, s5, "$g_encountered_party"),
  ], "Certainly, my {lord/lady}. Most of the time, the most profitable thing for you to do would be to let us buy raw materials and sell the finished goods directly to the market. Because of our longstanding relations with the local merchants, we can usually get a very good price.", "master_craftsman_production_options_2",[]],

  [anyone,"master_craftsman_production_options_2", [
  (str_store_party_name, s5, "$g_encountered_party"),
  ], "However, if you find that you can acquire raw materials cheaper outside {s5}, you may place them in the inventories, and we will use them instead of buying from the market. Likewise, if you feel that you can get a better price for the finished goods elsewhere, then you may ask us to deposit what we produce in our warehouses for you to take.", "master_craftsman_pretalk",[]],

  [anyone|plyr,"master_craftsman_talk", [
  ], "It will no longer be possible for me to continue operating this enterprise.", "master_craftsman_auction_price",[]],

  [anyone,"master_craftsman_auction_price", [
  (party_get_slot, ":item_produced", "$g_encountered_party", slot_center_player_enterprise),
  (item_get_slot, ":base_price",":item_produced", slot_item_base_price),
  (item_get_slot, ":number_runs", ":item_produced", slot_item_output_per_run),
  (store_mul, "$liquidation_price", ":base_price", ":number_runs"),
  (val_mul, "$liquidation_price", 4),

  (troop_get_inventory_capacity, ":total_capacity", "$g_talk_troop"),
  (try_for_range, ":capacity_iterator", 0, ":total_capacity"),
		(troop_get_inventory_slot, ":item_in_slot", "$g_talk_troop", ":capacity_iterator"),
		(gt, ":item_in_slot", 0),
		(item_get_slot, ":price_for_inventory_item", ":item_in_slot", slot_item_base_price),
#		(troop_inventory_slot_get_item_amount, ":item_ammo", "$g_talk_troop", ":capacity_iterator"),
#		(troop_inventory_slot_get_item_max_amount, ":item_max_ammo", "$g_talk_troop", ":capacity_iterator"),
#		(try_begin),
#			(lt, ":item_ammo", ":item_max_ammo"),
#			(val_mul, ":price_for_inventory_item", ":item_ammo"),
#			(val_div, ":price_for_inventory_item", ":item_max_ammo"),
#		(try_end),

        (store_sub, ":item_slot_no", ":item_in_slot", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":index", "$g_encountered_party", ":item_slot_no"),
		(val_mul, ":price_for_inventory_item", ":index"),
		(val_div, ":price_for_inventory_item", 1200),
		#modify by site
		#divide by 1200 not 1000
		(val_add, "$liquidation_price", ":price_for_inventory_item"),
  (try_end),

  (assign, reg4, "$liquidation_price"),

  ], "A pity, my {lord/lady}. If we sell the land and the equipment, and liquidate the inventories, I estimate that we can get {reg4} denars.", "master_craftsman_auction_decide",[]],

  [anyone|plyr,"master_craftsman_auction_decide", [
  ], "That sounds reasonable. Please proceed with the sale.", "master_craftsman_liquidation",[
  (troop_add_gold, "trp_player", "$liquidation_price"),
  (troop_clear_inventory, "$g_talk_troop"),
  (party_set_slot, "$g_encountered_party", slot_center_player_enterprise, 0),
  (party_set_slot, "$g_encountered_party", slot_center_player_enterprise_production_order, 0),

  ]],

  [anyone|plyr,"master_craftsman_auction_decide", [
  ], "Hmm. Let's hold off on that.", "master_craftsman_pretalk",[]],

  [anyone,"master_craftsman_liquidation", [
  ], "As you wish. It was an honor to have been in your employ.", "close_window",[
    (finish_mission),
  ]],

  [anyone|plyr,"master_craftsman_talk", [
  (eq, 1, 0),
  ], "{!}As you wish, {sir/my lady}. It was an honor to work in your employ.", "close_window",[]],

  [anyone|plyr,"master_craftsman_talk", [],
   "That is all for now.", "close_window",[]],





#Mayor talk (town elder)

  [anyone ,"start", [(is_between,"$g_talk_troop",mayors_begin,mayors_end),(eq,"$g_talk_troop_met",0),
                     (this_or_next|eq, "$players_kingdom", "$g_encountered_party_faction"),
                     (             eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
					 ##diplomacy start+
					 #Change "my lord" to "my lord/my lady" or "your highnes" as appropriate.
					 (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),#Write {sir/madame} or replacement to {s0}
					 ],
   "Good day, {s0}.", "mayor_begin",[]],#Changed "my lord" to {s0}
   ##diplomacy end+
  [anyone ,"start", [(is_between,"$g_talk_troop",mayors_begin,mayors_end),(eq,"$g_talk_troop_met",0),
                     (str_store_party_name, s9, "$current_town")],
   "Hello stranger, you seem to be new to {s9}. I am the guild master of the town.", "mayor_talk",[]],

  [anyone ,"start", [(is_between,"$g_talk_troop",mayors_begin,mayors_end)],
   "Good day, {playername}.", "mayor_begin",
   [
     #Delete last offered quest if peace is formed.
     (try_begin),
       (eq, "$merchant_offered_quest", "qst_persuade_lords_to_make_peace"),
       (quest_get_slot, ":target_faction", "qst_persuade_lords_to_make_peace", slot_quest_target_faction),
       (quest_get_slot, ":object_faction", "qst_persuade_lords_to_make_peace", slot_quest_object_faction),
       (store_relation, ":reln", ":target_faction", ":object_faction"),
       (ge, ":reln", 0),
       (assign, "$merchant_quest_last_offerer", -1),
       (assign, "$merchant_offered_quest", -1),
     (try_end),
     ]],

##Floris: Removed to make savegame compatible.
## CC
#  [anyone,"mayor_begin", 
#    [
#      (call_script, "script_centers_init_bandit_leader_quest"),
#      (party_get_slot, ":dest_quest", "$current_town", slot_center_bandit_leader_quest),
#      (neg|check_quest_active, ":dest_quest"),
#      (party_get_slot, ":dest_pt_no", "$current_town", slot_center_bandit_leader_pt_no),
#      (party_template_slot_eq, ":dest_pt_no", slot_party_template_has_hero, 1),
#      (party_template_get_slot, ":hero_id", ":dest_pt_no", slot_party_template_hero_id),
#      (party_template_get_slot, ":bandit_hero_name", ":dest_pt_no", slot_party_template_hero_pre_name),
#      (str_store_string, s1, ":bandit_hero_name"),
#
#      (store_sub, ":dest_string", ":dest_pt_no", "pt_forest_bandits"),
#      (val_add, ":dest_string", "trp_bandit_e_forest"),
#      (str_store_troop_name_plural, s2, ":dest_string"),
#      
#      (store_character_level, ":player_level", "trp_player"),
#      (store_character_level, ":hero_level", ":hero_id"),
#      (store_mul, ":quest_gold_reward", ":player_level", 2),
#      (val_mul, ":quest_gold_reward", ":hero_level"),
#      (val_add, ":quest_gold_reward", 2000),
#      (try_begin),
#        (this_or_next|eq, ":hero_id", "trp_steppe_bandit_hero"),
#        (eq, ":hero_id", "trp_desert_bandit_hero"),
#        (val_mul, ":quest_gold_reward", 3),
#        (val_div, ":quest_gold_reward", 2),
#      (try_end),
#      (assign, reg1, ":quest_gold_reward"),
#    ],
#   "Good day, {playername}. Unfortunately, I have bad news to report, but you might be the right person to talk to. Recently, a bandit hero called {s1} has appeared. Due to his powerful leadership, all the parties of {s2} are rallying to accompany him. Seperated bandits are a nuisance, but an organised bunch is a major threat for the town and its outskirts. Therefore, we have collect {reg1} denars as a reward for the man who can deal with {s1}. You look like a {man/lady} of valor and a fearsome warrior, and you have no doubt many friends and soldiers at your service. I think you are competent for the difficult task. Do you want to give it a try?", "mayor_deal_with_bandit_hero",
#    []],
#    
#  [anyone|plyr,"mayor_deal_with_bandit_hero", [],
#   "Aye, I'll do it.", "mayor_deal_with_bandit_hero_accept",[]],
#  [anyone|plyr,"mayor_deal_with_bandit_hero", [],
#   "I'm afraid I can't take the job at the moment.", "mayor_deal_with_bandit_hero_refuse",[]],
#  
#  [anyone,"mayor_deal_with_bandit_hero_accept", [
#    (party_get_slot, ":dest_pt_no", "$current_town", slot_center_bandit_leader_pt_no),
#    (party_template_slot_eq, ":dest_pt_no", slot_party_template_has_hero, 1),
#    (party_template_get_slot, ":bandit_hero_name", ":dest_pt_no", slot_party_template_hero_pre_name),
#    (str_store_string, s1, ":bandit_hero_name"),
#    (party_get_slot, ":dest_quest", "$current_town", slot_center_bandit_leader_quest),
#    (str_store_party_name_link, s13, "$g_encountered_party"),
#    (store_sub, ":dest_string", ":dest_pt_no", "pt_forest_bandits"),
#    (val_add, ":dest_string", "trp_bandit_e_forest"),
#    (str_store_troop_name_plural, s12, ":dest_string"),
#    (setup_quest_text, ":dest_quest"),
#    (str_store_string, s2, "@The Guildmaster of {s13} has asked you to deal with {s1}, the bandit hero of {s12}."),
#    
#    (party_template_get_slot, ":hero_id", ":dest_pt_no", slot_party_template_hero_id),
#    (party_template_get_slot, ":hero_party", ":dest_pt_no", slot_party_template_hero_party_id),
#    (quest_set_slot, ":dest_quest", slot_quest_target_party, ":hero_party"),
#    (quest_set_slot, ":dest_quest", slot_quest_target_troop, ":bandit_hero_name"),
#    (quest_set_slot, ":dest_quest", slot_quest_target_party_template, ":dest_pt_no"),
#    (quest_set_slot, ":dest_quest", slot_quest_expiration_days, 0),
#    (quest_set_slot, ":dest_quest", slot_quest_dont_give_again_period, 0),
#    
#    (store_character_level, ":player_level", "trp_player"),
#    (store_character_level, ":hero_level", ":hero_id"),
#    (store_mul, ":quest_gold_reward", ":player_level", 2),
#    (val_mul, ":quest_gold_reward", ":hero_level"),
#    (val_add, ":quest_gold_reward", 2000),
#    (try_begin),
#      (this_or_next|eq, ":hero_id", "trp_steppe_bandit_hero"),
#      (eq, ":hero_id", "trp_desert_bandit_hero"),
#      (val_mul, ":quest_gold_reward", 3),
#      (val_div, ":quest_gold_reward", 2),
#    (try_end),
#    (store_mul, ":quest_xp_reward", ":quest_gold_reward", 4),
#    (quest_set_slot, ":dest_quest", slot_quest_gold_reward, ":quest_gold_reward"),
#    (quest_set_slot, ":dest_quest", slot_quest_xp_reward, ":quest_xp_reward"),
#    (call_script, "script_start_quest", ":dest_quest", "$g_talk_troop"),
#    
#    (call_script, "script_get_closest_center", ":hero_party"),
#    (str_store_party_name_link, s3, reg0),
#    (str_store_string, s2, ":bandit_hero_name"),
#    (str_store_string, s1, "@{s2} is in the field and he should be close to {s3} at the moment."),
#    (str_store_string, s5, "@At the time quest was given:^{s1}"),
#    (add_quest_note_from_sreg, ":dest_quest", 3, s5, 1),
#    (assign, "$g_leave_encounter",1),
#  ],
#   "Excellent! We will wait the good news about it. {s1}", "close_window",
#   []],
#  
#  [anyone , "mayor_deal_with_bandit_hero_refuse", 
#    [
#      (party_get_slot, ":dest_pt_no", "$current_town", slot_center_bandit_leader_pt_no),
#      (party_template_get_slot, ":bandit_hero_name", ":dest_pt_no", slot_party_template_hero_pre_name),
#      (str_store_string, s1, ":bandit_hero_name"),
#    ],
#   "Well, the job will be available until {s1} is defeated by others. Tell me if you decide to take it.", "mayor_pretalk",[]],
#   
#  [anyone,"mayor_begin", 
#    [
#      (party_get_slot, ":dest_quest", "$current_town", slot_center_bandit_leader_quest),
#      (check_quest_active, ":dest_quest"),
#      (quest_slot_eq, ":dest_quest", slot_quest_giver_troop, "$g_talk_troop"),
#      (check_quest_succeeded, ":dest_quest"),
#      (assign, "$temp", ":dest_quest"),
#    ],
#   "Very nice work, {playername}, you had defeated {s1}. Thank you kindly for all your help, and please accept this bounty of {reg1} denars.", "mayor_deal_with_bandit_hero_completed",
#   [
#     (quest_get_slot, ":quest_gold_reward", "$temp", slot_quest_gold_reward),
#     (quest_get_slot, ":quest_xp_reward", "$temp", slot_quest_xp_reward),
#     (quest_get_slot, ":bandit_hero_name", "$temp", slot_quest_target_troop),
#     (add_xp_as_reward, ":quest_xp_reward"),
#     (call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
#     (try_for_range, ":cur_center", centers_begin, centers_end),
#       (party_slot_eq, ":cur_center", slot_center_bandit_leader_quest, "$temp"),
#       (call_script, "script_change_player_relation_with_center", ":cur_center", 1),
#     (try_end),
#     (call_script, "script_end_quest", "$temp"),
#     (store_div, ":quest_renown_reward", ":quest_gold_reward", 50),
#     (call_script, "script_change_troop_renown", "trp_player", ":quest_renown_reward"),
#     (str_store_string, s1, ":bandit_hero_name"),
#     (assign, reg1, ":quest_gold_reward"),
#    ]],
#
#  [anyone|plyr, "mayor_deal_with_bandit_hero_completed", [],
#   "It was my pleasure, {s65}.", "close_window",[]],
## CC
##

  [anyone,"mayor_begin", [(check_quest_active, "qst_persuade_lords_to_make_peace"),
                          (quest_slot_eq, "qst_persuade_lords_to_make_peace", slot_quest_giver_troop, "$g_talk_troop"),
                          (check_quest_succeeded, "qst_persuade_lords_to_make_peace"),
                          (quest_get_slot, ":quest_target_troop", "qst_persuade_lords_to_make_peace", slot_quest_target_troop),
                          (quest_get_slot, ":quest_object_troop", "qst_persuade_lords_to_make_peace", slot_quest_object_troop),
                          (val_mul, ":quest_target_troop", -1),
                          (val_mul, ":quest_object_troop", -1),
                          (quest_get_slot, ":quest_target_faction", "qst_persuade_lords_to_make_peace", slot_quest_target_faction),
                          (quest_get_slot, ":quest_object_faction", "qst_persuade_lords_to_make_peace", slot_quest_object_faction),
                          (str_store_troop_name, s12, ":quest_target_troop"),
                          (str_store_troop_name, s13, ":quest_object_troop"),
                          (str_store_faction_name, s14, ":quest_target_faction"),
                          (str_store_faction_name, s15, ":quest_object_faction"),
                          (str_store_party_name, s19, "$current_town"),
                         ],
   "{playername}, it was an incredible feat to get {s14} and {s15} make peace, and you made it happen.\
 Your involvement has not only saved our town from disaster, but it has also saved thousands of lives, and put an end to all the grief this bitter war has caused.\
 As the townspeople of {s19}, know that we'll be good on our word, and we are ready to pay the {reg12} denars we promised.", "lord_persuade_lords_to_make_peace_completed",
   [(quest_get_slot, ":quest_target_faction", "qst_persuade_lords_to_make_peace", slot_quest_target_faction),
    (quest_get_slot, ":quest_object_faction", "qst_persuade_lords_to_make_peace", slot_quest_object_faction),
    #Forcing 2 factions to make peace within 72 hours.
    (assign, "$g_force_peace_faction_1", ":quest_target_faction"),
    (assign, "$g_force_peace_faction_2", ":quest_object_faction"),
    (quest_get_slot, ":quest_reward", "qst_persuade_lords_to_make_peace", slot_quest_gold_reward),
    (assign, reg12, ":quest_reward"),
    #TODO: Change these values
    (add_xp_as_reward, 4000),
    ]],


  [anyone|plyr,"lord_persuade_lords_to_make_peace_completed", [],
   "Thank you. Let me have the money.", "lord_persuade_lords_to_make_peace_pay",[]],
  [anyone|plyr,"lord_persuade_lords_to_make_peace_completed", [],
   "No need for a payment. I only did what was right.", "lord_persuade_lords_to_make_peace_no_pay",[]],

  [anyone ,"lord_persuade_lords_to_make_peace_pay", [],
   "Oh, yes, of course. We had already got the money for you.\
 Here, please accept these {reg12} denars together with our most sincere thanks.\
 Me and the people of our town will not forget your help.", "close_window",
   [(quest_get_slot, ":quest_reward", "qst_persuade_lords_to_make_peace", slot_quest_gold_reward),
    (call_script, "script_troop_add_gold", "trp_player", ":quest_reward"),
    (call_script, "script_change_player_relation_with_center", "$current_town", 5),
    (call_script, "script_end_quest", "qst_persuade_lords_to_make_peace"),
    (quest_get_slot, ":quest_reward", "qst_persuade_lords_to_make_peace", slot_quest_gold_reward),
    (assign, reg12, ":quest_reward")
    ]],

  [anyone ,"lord_persuade_lords_to_make_peace_no_pay", [],
   "You are indeed an extraordenary person, {sir/madame}, and it is an honour for me to have known you.\
 You not only did what was impossible and put an end to this terrible war, but you won't even accept a reward for it.\
 Very well, I will not insist on the matter, but please know that you will have our eternal respect and gratitude.", "close_window",
   [
    (call_script, "script_change_player_honor", 3),
    (call_script, "script_change_player_relation_with_center", "$current_town", 8),
    (call_script, "script_end_quest", "qst_persuade_lords_to_make_peace"),
    ]],

  [anyone,"mayor_begin", [(check_quest_active, "qst_deal_with_night_bandits"),
                          (quest_slot_eq, "qst_deal_with_night_bandits", slot_quest_giver_troop, "$g_talk_troop"),
                          (check_quest_succeeded, "qst_deal_with_night_bandits"),
                         ],
   "Very nice work, {playername}, you made short work of those lawless curs.\
 Thank you kindly for all your help, and please accept this bounty of 150 denars.", "lord_deal_with_night_bandits_completed",
   [
     (add_xp_as_reward,200),
     (call_script, "script_troop_add_gold", "trp_player", 150),
     (call_script, "script_change_player_relation_with_center", "$current_town", 1),
     (call_script, "script_end_quest", "qst_deal_with_night_bandits"),
    ]],


  [anyone|plyr,"lord_deal_with_night_bandits_completed", [],
   "It was my pleasure, {s65}.", "close_window",[]],

# Ryan BEGIN
  [anyone,"mayor_begin", [(check_quest_active, "qst_deal_with_looters"),
                          (quest_slot_eq, "qst_deal_with_looters", slot_quest_giver_troop, "$g_talk_troop"),
                         ],
   "Ah, {playername}. Have you any progress to report?", "mayor_looters_quest_response",
   [
    ]],

  [anyone|plyr,"mayor_looters_quest_response",
   [
		##Floris MTT begin
		(try_begin),
			(eq, "$troop_trees", troop_trees_0),
			 (store_num_parties_destroyed_by_player, ":num_looters_destroyed", "pt_looters"),
			 (party_template_get_slot,":previous_looters_destroyed","pt_looters",slot_party_template_num_killed),
		(else_try),
			(eq, "$troop_trees", troop_trees_1),
			 (store_num_parties_destroyed_by_player, ":num_looters_destroyed", "pt_looters_r"),
			 (party_template_get_slot,":previous_looters_destroyed","pt_looters_r",slot_party_template_num_killed),
		(else_try),
			(eq, "$troop_trees", troop_trees_2),
			 (store_num_parties_destroyed_by_player, ":num_looters_destroyed", "pt_looters_e"),
			 (party_template_get_slot,":previous_looters_destroyed","pt_looters_e",slot_party_template_num_killed),
		(try_end),
		##Floris MTT end
     (val_sub,":num_looters_destroyed",":previous_looters_destroyed"),
     (quest_get_slot,":looters_paid_for","qst_deal_with_looters",slot_quest_current_state),
     (lt,":looters_paid_for",":num_looters_destroyed"),
     ],
   "I've killed some looters.", "mayor_looters_quest_destroyed",[]],
  [anyone|plyr,"mayor_looters_quest_response", [(eq,1,0)
  ],
   "I've brought you some goods.", "mayor_looters_quest_goods",[]],
  [anyone|plyr,"mayor_looters_quest_response", [
  ],
   "Not yet, sir. Farewell.", "close_window",[]],

  [anyone,"mayor_looters_quest_destroyed", [],
   "Aye, my scouts saw the whole thing. That should make anyone else think twice before turning outlaw!\
 The bounty is 40 denars for every band, so that makes {reg1} in total. Here is your money, as promised.",
   "mayor_looters_quest_destroyed_2",[
		##Floris MTT begin
		(try_begin),
			(eq, "$troop_trees", troop_trees_0),
		  (store_num_parties_destroyed_by_player, ":num_looters_destroyed", "pt_looters"),
		  (party_template_get_slot,":previous_looters_destroyed","pt_looters",slot_party_template_num_killed),
		(else_try),
			(eq, "$troop_trees", troop_trees_1),
		  (store_num_parties_destroyed_by_player, ":num_looters_destroyed", "pt_looters_r"),
		  (party_template_get_slot,":previous_looters_destroyed","pt_looters_r",slot_party_template_num_killed),
		(else_try),
			(eq, "$troop_trees", troop_trees_2),
		  (store_num_parties_destroyed_by_player, ":num_looters_destroyed", "pt_looters_e"),
		  (party_template_get_slot,":previous_looters_destroyed","pt_looters_e",slot_party_template_num_killed),
		(try_end),
		##Floris MTT end
      (val_sub,":num_looters_destroyed",":previous_looters_destroyed"),
      (quest_get_slot,":looters_paid_for","qst_deal_with_looters",slot_quest_current_state),
      (store_sub,":looter_bounty",":num_looters_destroyed",":looters_paid_for"),
      (val_mul,":looter_bounty",40),
      (assign,reg1,":looter_bounty"),
      (call_script, "script_troop_add_gold", "trp_player", ":looter_bounty"),
      (assign,":looters_paid_for",":num_looters_destroyed"),
      (quest_set_slot,"qst_deal_with_looters",slot_quest_current_state,":looters_paid_for"),
      ]],
  [anyone,"mayor_looters_quest_destroyed_2", [
      (quest_get_slot,":total_looters","qst_deal_with_looters",slot_quest_target_amount),
      (quest_slot_ge,"qst_deal_with_looters",slot_quest_current_state,":total_looters"), # looters paid for >= total looters
      (quest_get_slot,":xp_reward","qst_deal_with_looters",slot_quest_xp_reward),
      (quest_get_slot,":gold_reward","qst_deal_with_looters",slot_quest_gold_reward),
      (add_xp_as_reward, ":xp_reward"),
      (call_script, "script_troop_add_gold", "trp_player", ":gold_reward"),
      (call_script, "script_change_troop_renown", "trp_player", 1),
      (call_script, "script_change_player_relation_with_center", "$current_town", 5),
      (call_script, "script_end_quest", "qst_deal_with_looters"),
      (try_for_parties, ":cur_party_no"),
        (party_get_template_id, ":cur_party_template", ":cur_party_no"),
				##Floris MTT begin
        (this_or_next|eq, ":cur_party_template", "pt_looters"),
        (this_or_next|eq, ":cur_party_template", "pt_looters_r"),
        (eq, ":cur_party_template", "pt_looters_e"),
				##Floris MTT end
        (party_set_flags, ":cur_party_no", pf_quest_party, 0),
      (try_end),
  ],
   "And that's not the only good news! Thanks to you, the looters have ceased to be a threat. We've not had a single attack reported for some time now.\
 If there are any of them left, they've either run off or gone deep into hiding. That's good for business,\
 and what's good for business is good for the town!\
 I think that concludes our arrangement, {playername}. Please accept this silver as a token of my gratitude. Thank you, and farewell.",
   "close_window",[
      ]],
  [anyone,"mayor_looters_quest_destroyed_2", [],
   "Anything else you need?",
   "mayor_looters_quest_response",[
      ]],

  [anyone,"mayor_looters_quest_goods", [
      (quest_get_slot,reg1,"qst_deal_with_looters",slot_quest_target_item),
  ],
   "Hah, I knew I could count on you! Just tell me which item to take from your baggage, and I'll send some men to collect it.\
 I still need {reg1} denars' worth of goods.",
   "mayor_looters_quest_goods_response",[
      ]],
  [anyone|plyr|repeat_for_100,"mayor_looters_quest_goods_response", [
      (store_repeat_object,":goods"),
      (val_add,":goods",trade_goods_begin),
      (is_between,":goods",trade_goods_begin,trade_goods_end),
      (player_has_item,":goods"),
      (str_store_item_name,s5,":goods"),
  ],
   "{s5}.", "mayor_looters_quest_goods_2",[
      (store_repeat_object,":goods"),
      (val_add,":goods",trade_goods_begin),
      (troop_remove_items,"trp_player",":goods",1),
      (assign,":value",reg0),
      (call_script, "script_troop_add_gold", "trp_player", ":value"),
      (quest_get_slot,":gold_num","qst_deal_with_looters",slot_quest_target_item),
      (val_sub,":gold_num",":value"),
      (quest_set_slot,"qst_deal_with_looters",slot_quest_target_item,":gold_num"),
      (str_store_item_name,s6,":goods"),
   ]],
  [anyone|plyr,"mayor_looters_quest_goods_response", [
  ],
   "Nothing at the moment, sir.", "mayor_looters_quest_goods_3",[]],

  [anyone,"mayor_looters_quest_goods_3", [
  ],
   "Anything else you need?",
   "mayor_looters_quest_response",[
      ]],

  [anyone,"mayor_looters_quest_goods_2", [
      (quest_slot_ge,"qst_deal_with_looters",slot_quest_target_item,1),
      (quest_get_slot,reg1,"qst_deal_with_looters",slot_quest_target_item),
  ],
   "Excellent, here is the money for your {s6}. Do you have any more goods to give me? I still need {reg1} denars' worth of goods.",
   "mayor_looters_quest_goods_response",[
      ]],
  [anyone,"mayor_looters_quest_goods_2", [
      (neg|quest_slot_ge,"qst_deal_with_looters",slot_quest_target_item,1),
      (quest_get_slot,":xp_reward","qst_deal_with_looters",slot_quest_xp_reward),
      (quest_get_slot,":gold_reward","qst_deal_with_looters",slot_quest_gold_reward),
      (add_xp_as_reward, ":xp_reward"),
      (call_script, "script_troop_add_gold", "trp_player", ":gold_reward"),
#      (call_script, "script_change_troop_renown", "trp_player", 1),
      (call_script, "script_change_player_relation_with_center", "$current_town", 3),
      (call_script, "script_end_quest", "qst_deal_with_looters"),
      (try_for_parties, ":cur_party_no"),
        (party_get_template_id, ":cur_party_template", ":cur_party_no"),
				##Floris MTT begin
        (this_or_next|eq, ":cur_party_template", "pt_looters"),
        (this_or_next|eq, ":cur_party_template", "pt_looters_r"),
        (eq, ":cur_party_template", "pt_looters_e"),
				##Floris MTT end
        (party_set_flags, ":cur_party_no", pf_quest_party, 0),
      (try_end),
  ],
   "Well done, {playername}, that's the last of the goods I need. Here is the money for your {s6}, and a small bonus for helping me out.\
 I'm afraid I won't be paying for any more goods, nor bounties on looters, but you're welcome to keep hunting the bastards if any remain.\
 Thank you for your help, I won't forget it.",
   "close_window",[
      ]],
# Ryan END



  [anyone,"mayor_begin", [(check_quest_active, "qst_move_cattle_herd"),
                          (quest_slot_eq, "qst_move_cattle_herd", slot_quest_giver_troop, "$g_talk_troop"),
                          (check_quest_succeeded, "qst_move_cattle_herd"),
                          ],
   "Good to see you again {playername}. I have heard that you have delivered the cattle successfully.\
 I will tell the merchants how reliable you are.\
 And here is your pay, {reg8} denars.", "close_window",
   [(quest_get_slot, ":quest_gold_reward", "qst_move_cattle_herd", slot_quest_gold_reward),
    (call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
    (store_div, ":xp_reward", ":quest_gold_reward", 3),
    (add_xp_as_reward, ":xp_reward"),
    (call_script, "script_change_troop_renown", "trp_player", 1),
    (call_script, "script_change_player_relation_with_center", "$current_town", 3),
    (call_script, "script_end_quest", "qst_move_cattle_herd"),
    (assign, reg8, ":quest_gold_reward"),
    ]],

  [anyone,"mayor_begin", [(check_quest_active, "qst_move_cattle_herd"),
                          (quest_slot_eq, "qst_move_cattle_herd", slot_quest_giver_troop, "$g_talk_troop"),
                          (check_quest_failed, "qst_move_cattle_herd"),
                          ],
   "I heard that you have lost the cattle herd on your way to {s9}.\
 I had a very difficult time explaining your failure to the owner of that herd, {sir/madam}.\
 Do you have anything to say?", "move_cattle_herd_failed",
   []],

  [anyone|plyr ,"move_cattle_herd_failed", [],
   "I am sorry. But I was attacked on the way.", "move_cattle_herd_failed_2",[]],
  [anyone|plyr ,"move_cattle_herd_failed", [],
   "I am sorry. The stupid animals wandered off during the night.", "move_cattle_herd_failed_2",[]],

  [anyone,"move_cattle_herd_failed_2", [],
   "Well, it was your responsibility to deliver that herd safely, no matter what.\
 You should know that the owner of the herd demanded to be compensated for his loss, and I had to pay him 1000 denars.\
 So you now owe me that money.", "merchant_ask_for_debts",
   [(assign, "$debt_to_merchants_guild", 1000),
    (call_script, "script_end_quest", "qst_move_cattle_herd"),]],

  [anyone,"mayor_begin", [(check_quest_active, "qst_kidnapped_girl"),
                          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 4),
                          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_giver_troop, "$g_talk_troop"),
                          ],
   "{playername} -- I am in your debt for bringing back my friend's daughter.\
  Please take these {reg8} denars that I promised you.\
  My friend wished he could give more but paying that ransom brought him to his knees.", "close_window",
   [(quest_get_slot, ":quest_gold_reward", "qst_kidnapped_girl", slot_quest_gold_reward),
    (call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
    (assign, reg8, ":quest_gold_reward"),
    (assign, ":xp_reward", ":quest_gold_reward"),
    (val_mul, ":xp_reward", 2),
    (val_add, ":xp_reward", 100),
    (add_xp_as_reward, ":xp_reward"),
    (call_script, "script_change_troop_renown", "trp_player", 3),
    (call_script, "script_change_player_relation_with_center", "$current_town", 2),
    (call_script, "script_end_quest", "qst_kidnapped_girl"),
    ]],

  [anyone,"mayor_begin", [(check_quest_active, "qst_track_down_bandits"),
                          (check_quest_succeeded, "qst_track_down_bandits"),
                          (quest_slot_eq, "qst_track_down_bandits", slot_quest_giver_troop, "$g_talk_troop"),
                          ],
   "Well -- it sounds like you were able to track down the bandits, and show them what happens to those who would disrupt the flow of commerce.\
 Here is your reward: {reg5} denars.\
 It is well earned, and we are most grateful.",
   "mayor_friendly_pretalk", [(quest_get_slot, ":quest_gold_reward", "qst_track_down_bandits", slot_quest_gold_reward),
                              (call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
                              (assign, ":xp_reward", ":quest_gold_reward"),
                              (val_mul, ":xp_reward", 2),
                              (add_xp_as_reward, ":xp_reward"),
                              (call_script, "script_change_player_relation_with_center", "$current_town", 2),
                              (call_script, "script_change_troop_renown", "trp_player", 3),
                              (call_script, "script_end_quest", "qst_track_down_bandits"),
                              (assign, reg5, ":quest_gold_reward"),
                              ]],

  [anyone,"mayor_begin", [(check_quest_active, "qst_troublesome_bandits"),
                          (check_quest_succeeded, "qst_troublesome_bandits"),
                          (quest_slot_eq, "qst_troublesome_bandits", slot_quest_giver_troop, "$g_talk_troop"),
                          ],
   "I have heard about your deeds. You have given those bandits the punishment they deserved.\
 You are really as good as they say.\
 Here is your reward: {reg5} denars.\
 I would like to give more but those bandits almost brought me to bankruptcy.",
   "mayor_friendly_pretalk", [(quest_get_slot, ":quest_gold_reward", "qst_troublesome_bandits", slot_quest_gold_reward),
                              (call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
                              (assign, ":xp_reward", ":quest_gold_reward"),
                              (val_mul, ":xp_reward", 2),
                              (add_xp_as_reward, ":xp_reward"),
                              (call_script, "script_change_player_relation_with_center", "$current_town", 2),
                              (call_script, "script_change_troop_renown", "trp_player", 3),
                              (call_script, "script_end_quest", "qst_troublesome_bandits"),
                              (assign, reg5, ":quest_gold_reward"),
                              ]],

  #destroy lair quest end dialogs taken from here

  [anyone,"mayor_begin", [(ge, "$debt_to_merchants_guild", 50)],
   "According to my accounts, you owe the merchants guild {reg1} denars.\
 I'd better collect that now.", "merchant_ask_for_debts",[(assign,reg(1),"$debt_to_merchants_guild")]],
  [anyone|plyr,"merchant_ask_for_debts", [[store_troop_gold,reg(5),"trp_player"],[ge,reg(5),"$debt_to_merchants_guild"]],
   "Alright. I'll pay my debt to you.", "merchant_debts_paid",[[troop_remove_gold, "trp_player","$debt_to_merchants_guild"],
                                                                [assign,"$debt_to_merchants_guild",0]]],
  [anyone, "merchant_debts_paid", [], "Excellent. I'll let my fellow merchants know that you are clear of any debts.", "mayor_pretalk",[]],

  [anyone|plyr, "merchant_ask_for_debts", [], "I'm afraid I can't pay that sum now.", "merchant_debts_not_paid",[]],
  [anyone, "merchant_debts_not_paid", [(assign,reg(1),"$debt_to_merchants_guild")], "In that case, I am afraid, I can't deal with you. Guild rules...\
 Come back when you can pay the {reg1} denars.\
 And know that we'll be charging an interest to your debt.\
 So the sooner you pay it, the better.", "close_window",[]],


  [anyone,"mayor_begin", [], "What can I do for you?", "mayor_talk", []],
  [anyone,"mayor_friendly_pretalk", [], "Now... What else may I do for you?", "mayor_talk",[]],
  [anyone,"mayor_pretalk", [], "Yes?", "mayor_talk",[]],

  [anyone|plyr,"mayor_talk", [], "Can you tell me about what you do?", "mayor_info_begin",[]],

  [anyone|plyr,"mayor_talk", [(store_partner_quest, ":partner_quest"),
                              (lt, ":partner_quest", 0),
                              (neq, "$merchant_quest_last_offerer", "$g_talk_troop")],
   "Do you happen to have a job for me?", "merchant_quest_requested",[
     (assign,"$merchant_quest_last_offerer", "$g_talk_troop"),
     (call_script, "script_get_quest", "$g_talk_troop"),
     (assign, "$random_merchant_quest_no", reg0),
     (assign,"$merchant_offered_quest","$random_merchant_quest_no"),
     ]],

  [anyone|plyr,"mayor_talk", [(store_partner_quest, ":partner_quest"),
                              (lt, ":partner_quest", 0),
                              (eq,"$merchant_quest_last_offerer", "$g_talk_troop"),
                              (gt,"$merchant_offered_quest", 0) #not sure why was zero
                              ],
   "About that job you offered me...", "merchant_quest_last_offered_job",[]],

  [anyone|plyr,"mayor_talk", [(store_partner_quest,reg(2)),(ge,reg(2),0)],
   "About the job you gave me...", "merchant_quest_about_job",[]],

  [anyone|plyr,"mayor_talk",[], "I have some questions of a political nature.", "mayor_political_talk",[]],

  [anyone|plyr,"mayor_talk",[], "How is trade around here?", "mayor_economy_report_1",[
  (call_script, "script_merchant_road_info_to_s42", "$g_encountered_party"), #also does items to s32
  ]],

  [anyone|plyr,"mayor_talk",[
  ], "How does the wealth of this region compare with the rest of Calradia?", "mayor_wealth_comparison_1",[
  ]],


  [anyone|plyr,"mayor_talk",[
  (item_slot_ge, "itm_trade_velvet", slot_item_secondary_raw_material, "itm_trade_raw_dyes"), #ie, the item information has been updated, to ensure savegame compatibility
  ], "I wish to buy land in this town for a productive enterprise", "mayor_investment_possible",[
  ]],





  [anyone,"mayor_investment_possible",[
  (party_slot_ge, "$g_encountered_party", slot_center_player_enterprise, 1),
  (party_get_slot, ":item_produced", "$g_encountered_party", slot_center_player_enterprise),
  (call_script, "script_get_enterprise_name", ":item_produced"),
  (str_store_string, s4, reg0),
  ], "You already operate a {s4} here. There probably aren't enough skilled tradesmen to start a second enterprise.", "mayor_pretalk",[
  ]],

  [anyone,"mayor_investment_possible",[
  (ge, "$cheat_mode", 3)
  ], "{!}CHEAT: Yes, we're playtesting this feature, and you're in cheat mode. Go right ahead.", "mayor_investment_advice",[
  ]],

  [anyone,"mayor_investment_possible",[
  (lt,"$g_encountered_party_relation",0),
  (str_store_string, s9, "str_enterprise_enemy_realm"),
	], "{s9}", "mayor_pretalk",[
	]],

  [anyone,"mayor_investment_possible",[
  (party_slot_eq, "$g_encountered_party", slot_town_lord, "trp_player"),
  ##diplomacy start+ Replace {sir/my lady} with {s0}
  (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
#  ], "Of course, {sir/my lady}. You are the lord of this town, and no one is going to stop you.", "mayor_investment_advice",[
  ], "Of course, {s0}. You are the lord of this town, and no one is going to stop you.", "mayor_investment_advice",[
##diplomacy end+
  ]],

  [anyone,"mayor_investment_possible",[
  (party_get_slot, ":town_liege", "$g_encountered_party", slot_town_lord),
  ##diplomacy start+ Add support for ladies etc.
  #(is_between, ":town_liege", active_npcs_begin, active_npcs_end),
  (is_between, ":town_liege", heroes_begin, heroes_end),
  ##diplomacy end+
  (call_script, "script_troop_get_relation_with_troop", "trp_player", ":town_liege"),
  (assign, ":relation", reg0),
  (lt, ":relation", 0),
  (str_store_troop_name, s4, ":town_liege"),
  ], "Well... Given your relationship with our liege, {s4}, I think that you will not find many here who are brave enough to sell you any land.", "mayor_investment",[
  ]],

  [anyone|auto_proceed,"mayor_investment",[], "{!}.", "mayor_pretalk",[]],


  [anyone,"mayor_investment_possible",[
  ##diplomacy start+ Optional economic change, increase relation required
  ##OLD:
  #	(neg|party_slot_ge, "$current_town", slot_center_player_relation, 0),
  ##NEW:
  (assign, ":required_relation", 0),#need 0+ normally
  (try_begin),
	(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
	(neq, "$g_encountered_party", "$g_starting_town"),
	(val_add, ":required_relation", 1),#need 1+ with economic changes on medium+
  (try_end),
  (neg|party_slot_ge, "$current_town", slot_center_player_relation, ":required_relation"),
  ##diplomacy end+
  ], "Well... To be honest, I think that we in the guild would like to know you a little better. We can be very particular about outsiders coming in here and buying land.", "mayor_pretalk",[
  ]],

  [anyone,"mayor_investment_possible",[
  ##diplomacy start+ Replace {sir/my lady} with {s0}
  (call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$g_encountered_party"),
#  ], "Very good, {sir/my lady}. We in the guild know and trust you, and I think I could find someone to sell you the land you need.", "mayor_investment_advice",[]],
  ], "Very good, {s0}. We in the guild know and trust you, and I think I could find someone to sell you the land you need.", "mayor_investment_advice",[]],
##diplomacy end+

  [anyone,"mayor_investment_advice",[], "A couple of things to keep in mind -- skilled laborers are always at a premium, so I doubt that you will be able to open up more than one enterprise here. In order to make a profit for yourself, you should choose a commodity which is in relatively short supply, but for which the raw materials are cheap. What sort of enterprise would you like to start?", "investment_choose_enterprise",[
  ]],

  [anyone|plyr,"investment_choose_enterprise",[], "A mill and bakery, to make bread from grain", "investment_summary",[
  (assign, "$enterprise_production", "itm_trade_bread"),
  ]],

  [anyone|plyr,"investment_choose_enterprise",[], "A brewery, to make ale from grain", "investment_summary",[
  (assign, "$enterprise_production", "itm_trade_ale"),
  ]],

  [anyone|plyr,"investment_choose_enterprise",[], "A tannery, to make leather from hides", "investment_summary",[
  (assign, "$enterprise_production", "itm_trade_leatherwork"),
  ]],

  [anyone|plyr,"investment_choose_enterprise",[], "A wine press, to make wine from grapes", "investment_summary",[
  (assign, "$enterprise_production", "itm_trade_wine"),
  ]],

  [anyone|plyr,"investment_choose_enterprise",[], "An oil press, to make oil from olives", "investment_summary",[
  (assign, "$enterprise_production", "itm_trade_oil"),
  ]],

  [anyone|plyr,"investment_choose_enterprise",[], "An ironworks, to make tools from iron", "investment_summary",[
  (assign, "$enterprise_production", "itm_trade_tools"),
  ]],

  [anyone|plyr,"investment_choose_enterprise",[], "A weavery and dyeworks, to make velvet from silk and dye", "investment_summary",[
  (assign, "$enterprise_production", "itm_trade_velvet"),
  ]],

  [anyone|plyr,"investment_choose_enterprise",[], "A weavery, to make wool cloth from wool", "investment_summary",[
  (assign, "$enterprise_production", "itm_trade_wool_cloth"),
  ]],

  [anyone|plyr,"investment_choose_enterprise",[], "A weavery, to make linen from flax", "investment_summary",[
  (assign, "$enterprise_production", "itm_trade_linen"),
  ]],

  [anyone|plyr,"investment_choose_enterprise",[], "Never mind", "mayor_pretalk",[
  ]],

  [anyone,"investment_summary",[], "Very good, sir. The land and the materials on which you may build your {s3} will cost you {reg7} denars. Right now, your {s3} will produce {s4} worth {reg1} denars each week, while the {s6} needed to manufacture that batch will be {reg2} and labor and upkeep will be {reg3}.{s9} I should guess that your profit would be {reg0} denars a week. This assumes of course that prices remain constant -- which, I can virtually guarantee you, they will not. Do you wish to proceed?", "mayor_investment_confirm",
  [
    #(item_get_slot, ":base_price", "$enterprise_production", slot_item_base_price),
    #(item_get_slot, ":number_runs", "$enterprise_production", slot_item_output_per_run),
    #(store_mul, "$enterprise_cost", ":base_price", ":number_runs"),
    #(val_mul, "$enterprise_cost", 5),
    (item_get_slot, "$enterprise_cost", "$enterprise_production", slot_item_enterprise_building_cost),

    (assign, reg7, "$enterprise_cost"),

    (str_store_item_name, s4, "$enterprise_production"),

    (call_script, "script_get_enterprise_name", "$enterprise_production"),
    (str_store_string, s3, reg0),

    (call_script, "script_process_player_enterprise", "$enterprise_production", "$g_encountered_party"),
    #reg0: Profit per cycle
    #reg1: Selling price of total goods
    #reg2: Selling price of total goods

    (item_get_slot, ":primary_raw_material", "$enterprise_production", slot_item_primary_raw_material),
    (str_store_item_name, s6, ":primary_raw_material"),
	##diplomacy start+ For testing, print some additional diagnostics
	(assign, ":save_reg0", reg0),
	(assign, ":save_reg1", reg1),
	(try_begin),
		(ge, "$cheat_mode", 1),
		(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
		(try_begin),
			(call_script, "script_dplmc_good_produced_at_center_or_its_villages", ":primary_raw_material", "$g_encountered_party"),
			(ge, reg0, 1),
			(display_message, "@{!}There is a local supply of {s6}."),
		(else_try),
			(store_sub, ":item_slot_no", ":primary_raw_material", trade_goods_begin),
			(val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
			(item_get_slot, reg0, ":primary_raw_material", slot_item_base_price),
			(party_get_slot, reg1, "$g_encountered_party", ":item_slot_no"),
			(val_mul, reg0, reg1),
			(val_div, reg0, average_price_factor),
			(assign, ":base_price", reg0),
			(call_script, "script_dplmc_assess_ability_to_purchase_good_from_center", ":primary_raw_material", "$g_encountered_party"),
			(item_get_slot, reg1, ":primary_raw_material", slot_item_base_price),
			(val_mul, reg1, reg0),
			(val_div, reg1, average_price_factor),
			(assign, reg0, ":base_price"),
			(display_message, "@{!}{s6} must be imported, modifying the price from {reg0} to {reg1}."),
		(try_end),
	(try_end),
	##diplomacy end+

    (str_clear, s9),
    (assign, ":cost_of_secondary_input", reg10),
    (try_begin),
	  (gt, ":cost_of_secondary_input", 0),
	  (item_get_slot, ":secondary_raw_material", "$enterprise_production", slot_item_secondary_raw_material),
      (str_store_item_name, s11, ":secondary_raw_material"),
      (str_store_string, s9, "str_describe_secondary_input"),
    (try_end),
	##diplomacy end+
	(try_begin),
		(ge, "$cheat_mode", 1),
		(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
		(gt, ":cost_of_secondary_input", 0),
		(try_begin),
			(call_script, "script_dplmc_good_produced_at_center_or_its_villages", ":secondary_raw_material", "$g_encountered_party"),
			(ge, reg0, 1),
			(display_message, "@{!}There is a local supply of {s11}."),
		(else_try),
			(store_sub, ":item_slot_no", ":secondary_raw_material", trade_goods_begin),
			(val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
			(item_get_slot, reg0, ":secondary_raw_material", slot_item_base_price),
			(party_get_slot, reg1, "$g_encountered_party", ":item_slot_no"),
			(val_mul, reg0, reg1),
			(val_div, reg0, average_price_factor),
			(assign, ":base_price", reg0),
			(call_script, "script_dplmc_assess_ability_to_purchase_good_from_center", ":secondary_raw_material", "$g_encountered_party"),
			(item_get_slot, reg1, ":secondary_raw_material", slot_item_base_price),
			(val_mul, reg1, reg0),
			(val_div, reg1, average_price_factor),
			(assign, reg0, ":base_price"),
			(display_message, "@{!}{s9} must be imported, modifying the price from {reg0} to {reg1}."),
		(try_end),
	(try_end),
	(assign, reg0, ":save_reg0"),
	(assign, reg1, ":save_reg1"),
	##diplomacy end+
  ]],


  [anyone|plyr,"mayor_investment_confirm",[
  (store_troop_gold, ":player_gold", "trp_player"),
  (ge, ":player_gold","$enterprise_cost"),
  ], "Yes. Here is money for the land.", "mayor_investment_purchase",[
  (party_set_slot, "$g_encountered_party", slot_center_player_enterprise, "$enterprise_production"),
  (party_set_slot, "$g_encountered_party", slot_center_player_enterprise_days_until_complete, 7),

  (troop_remove_gold, "trp_player", "$enterprise_cost"),
  (store_sub, ":current_town_order", "$current_town", towns_begin),
  (store_add, ":craftsman_troop", ":current_town_order", "trp_town_1_master_craftsman"),
  (try_begin),
	(eq, "$enterprise_production", "itm_trade_bread"),
    (troop_set_name, ":craftsman_troop", "str_master_miller"),
  (else_try),
	(eq, "$enterprise_production", "itm_trade_ale"),
    (troop_set_name, ":craftsman_troop", "str_master_brewer"),
  (else_try),
	(eq, "$enterprise_production", "itm_trade_oil"),
    (troop_set_name, ":craftsman_troop", "str_master_presser"),
  (else_try),
	(eq, "$enterprise_production", "itm_trade_tools"),
    (troop_set_name, ":craftsman_troop", "str_master_smith"),
  (else_try),
	(eq, "$enterprise_production", "itm_trade_wool_cloth"),
    (troop_set_name, ":craftsman_troop", "str_master_weaver"),
  (else_try),
	(eq, "$enterprise_production", "itm_trade_linen"),
    (troop_set_name, ":craftsman_troop", "str_master_weaver"),
  (else_try),
	(eq, "$enterprise_production", "itm_trade_leatherwork"),
    (troop_set_name, ":craftsman_troop", "str_master_tanner"),
  (else_try),
	(eq, "$enterprise_production", "itm_trade_velvet"),
    (troop_set_name, ":craftsman_troop", "str_master_dyer"),
  (else_try),
	(eq, "$enterprise_production", "itm_trade_wine"),
    (troop_set_name, ":craftsman_troop", "str_master_vinter"),
  (try_end),
  ]],

  [anyone|plyr,"mayor_investment_confirm",[], "No -- that's not economical for me at the moment.", "mayor_investment_advice",[   ##Floris - change from "mayor_pretalk"
  ]],

  [anyone,"mayor_investment_purchase",[], "Very good. Your enterprise should be up and running in about a week. When next you come, and thereafter, you should speak to your {s4} about its operations.", "mayor_pretalk",[
  (store_sub, ":current_town_order", "$current_town", towns_begin),
  (store_add, ":craftsman_troop", ":current_town_order", "trp_town_1_master_craftsman"),
  (str_store_troop_name, s4, ":craftsman_troop"),

  ]],




  [anyone|plyr,"mayor_talk", [], "[Leave]", "close_window",[]],

  [anyone, "mayor_info_begin", [(str_store_party_name, s9, "$current_town")],
   "I am the guildmaster of {s9}. You can say I am the leader of the good people of {s9}.\
 I can help you find a job if you are looking for some honest work.", "mayor_info_talk",[(assign, "$mayor_info_lord_told",0)]],

  [anyone|plyr,"mayor_info_talk",[(eq, "$mayor_info_lord_told",0)], "Who rules this town?", "mayor_info_lord",[]],
  ##diplomacy start+ make gender correct
  [anyone, "mayor_info_lord", #moto fix
   [
    (party_get_slot, ":town_lord","$current_town",slot_town_lord), 
    (try_begin), 
        (eq, ":town_lord", "trp_player"), 
        (str_store_string, s10, "str_your_excellency"), 
    (else_try), 
        (is_between, ":town_lord", active_npcs_begin, active_npcs_end), 
        (str_store_troop_name, s10, ":town_lord"), 
    (else_try), 
        (faction_get_slot, ":faction_leader", "$g_encountered_party_faction", slot_faction_leader), 
        (str_store_troop_name, s10, ":faction_leader"), 
    (try_end), 
    (call_script, "script_dplmc_store_troop_is_female", ":town_lord"),],#Next line, He -> {reg0?She:He}
   "Our town's lord and protector is {s10}. {reg0?She:He} owns the castle and sometimes resides there, and collects taxes from the town.\
 However we regulate ourselves in most of the matters that concern ourselves.\
 As the town's guildmaster I have the authority to decide those things.", "mayor_info_talk",[(assign, "$mayor_info_lord_told",1)]],
 ##diplomacy end+

  [anyone|plyr,"mayor_info_talk",[], "That's all I need to know. Thanks.", "mayor_pretalk",[]],


  [anyone, "mayor_political_talk", [(faction_get_slot, ":faction_leader","$g_encountered_party_faction",slot_faction_leader),
									(str_store_troop_name, s10, ":faction_leader"),
									(party_get_slot, ":town_lord","$current_town",slot_town_lord),
									(try_begin),
										(eq, ":town_lord", "trp_player"),
										(str_store_string, s10, "str_your_excellency"),
									(else_try),
										(is_between, ":town_lord", active_npcs_begin, active_npcs_end),
										(neq, ":town_lord", ":faction_leader"),
										(str_store_troop_name, s11, ":town_lord"),
										(neq, ":town_lord", ":faction_leader"),
										(str_store_string, s10, "str_s10_and_s11"),
									(try_end),
									],
   "Politics? Good heaven, the guild has nothing to do with politics. We are loyal servants of {s10}. We merely govern our own affairs, and pass on the townspeople's concerns to our lords and masters, and maybe warn them from time to time against evil advice. Anyway, what did you wish to ask?", "mayor_political_questions",[]],

  [anyone,"mayor_prepolitics",[ (faction_get_slot, ":faction_leader","$g_encountered_party_faction",slot_faction_leader),
								(try_begin),
									(eq, ":faction_leader", "trp_player"),
									(str_store_string, s9, "str_your_loyal_subjects"),
								(else_try),
									(str_store_troop_name, s10, ":faction_leader"),
									(str_store_string, s9, "str_loyal_subjects_of_s10"),
								(try_end),
  ], "Did I mention that we here are all {s9}? Because I can't stress that enough... Anyway... Is there anything else?", "mayor_political_questions",[]],

   [anyone|plyr,"mayor_political_questions",[], "What is the cause of all these wars in Calradia?", "mayor_war_description_1",[
  ]],

  [anyone,"mayor_war_description_1",[ (faction_get_slot, ":faction_leader","$g_encountered_party_faction",slot_faction_leader),
								(str_store_troop_name, s10, ":faction_leader"),
								(str_store_string, s22, "str_the"),
								(try_begin),
									(eq, "$g_encountered_party_faction", "fac_kingdom_5"),
									(str_store_string, s22, "str_we"),
								(try_end),
								(val_max, "$g_mayor_given_political_dialog", 1),

  ], "Well, to answer your question generally, each monarch claims to be the rightful heir to the old Calradic emperors. Some of these claims are based on forgotten dynastic marriages and others are based on obscure promises, while {s22} Rhodoks invoke the empire's unwritten constitution. So in theory, any one realm has the right to declare war on any other realm at any time.", "mayor_war_description_2",[]],

  [anyone,"mayor_war_description_2",[ (faction_get_slot, ":faction_leader","$g_encountered_party_faction",slot_faction_leader),
								(str_store_troop_name, s10, ":faction_leader"),
								(troop_get_type, reg4, ":faction_leader"),
  ], "In practice, to make war is exhausting work. It is easy enough to lay waste to the enemy's farmland, but crops will grow back, and it is a far different matter to capture an enemy stronghold and to hold it. So the monarchs of Calradia will fight a little, sign a truce, fight a little more, and so on and so forth. Often, a monarch will go to war when another realm provokes them. At such times, some bad influences who look to enrich themselves with ransoms and pillage will clamor for retribution, and thus the damage caused by war to a monarch's treasury is less than the damage caused by doing nothing would be to his authority... I'm of course not talking about {s10}, as no one would ever question {reg4?her:his} authority", "mayor_war_description_3",[]],

  [anyone,"mayor_war_description_3",[
 	(faction_get_slot, ":faction_leader","$g_encountered_party_faction",slot_faction_leader),
	(troop_get_type, reg4, ":faction_leader"),

  ], "I would stress again that we in the guild have nothing to do with politics. But if {s10} were to ask for my advice on these matters, as a loyal subject, I would tell {reg4?her:him} that while {reg4?her:his} claim to all of Calradia is truly just, even the most legitimate claim must be backed by armed men, and armed men want money, and money comes from trade, and war ruins trade, so sometimes the best way to push a claim is not to push it, if you know what I mean...", "mayor_war_description_4",[]],

  [anyone,"mayor_war_description_4",[
    (str_store_party_name, s4, "$g_encountered_party"),
	(faction_get_slot, ":faction_leader","$g_encountered_party_faction",slot_faction_leader),
	(troop_get_type, reg4, ":faction_leader"),

  ], "You may tell {s10} this if you see {reg4?her:him}. Don't mention my name specifically -- just say 'the people of {s4}' told you this. Our personal opinion, of course, as to what would be in {s10}'s best interests. None of us would ever dream of questioning a monarch's sovereign right to push {reg4?her:his} legitimate claims.", "mayor_prepolitics",[
  ]],

  [anyone|plyr,"mayor_political_questions",[
	(faction_get_slot, ":faction_leader","$g_encountered_party_faction",slot_faction_leader),
	(str_store_troop_name, s10, ":faction_leader"),
	(ge, "$g_mayor_given_political_dialog", 1),
	(assign, ":continue", 0),
	(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
	  (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
	  (neq, ":cur_faction", "$g_encountered_party_faction"),
	  (assign, ":continue", 1), #at least 1 faction is active
	(try_end),
	(eq, ":continue", 1),
  ], "What is {s10}'s policy in regards to the other realms of Calradia?", "mayor_politics_assess",[
  ]],

  [anyone,"mayor_politics_assess",[], "Which realm did you have in mind?", "mayor_politics_assess_realm",[
  ]],

  [anyone|plyr|repeat_for_factions,"mayor_politics_assess_realm",[
  (store_repeat_object, ":faction"),
  (is_between, ":faction", kingdoms_begin, kingdoms_end),
  (faction_slot_eq, ":faction", slot_faction_state, sfs_active),
  (neq, ":faction", "$g_encountered_party_faction"),
  (str_store_faction_name, s11, ":faction"),
  ], "{s11}", "mayor_politics_give_realm_assessment",[
  (store_repeat_object, "$faction_selected"),
  ]],

  [anyone,"mayor_politics_give_realm_assessment",[], "{s14}", "mayor_prepolitics",[
  (call_script, "script_npc_decision_checklist_peace_or_war", "$g_encountered_party_faction", "$faction_selected", -1),
  ]],

   [anyone|plyr,"mayor_political_questions",[], "What can you say about the internal politics of the realms?", "mayor_internal_politics",[
  ]],

  [anyone,"mayor_internal_politics",[
  (str_store_faction_name, s4, "$g_encountered_party_faction"),
  (faction_get_slot, ":leader", "$g_encountered_party_faction", slot_faction_leader),
  (str_store_troop_name, s5, ":leader"),
  (troop_get_type, reg4, ":leader"),
  ], "Well, here in the {s4} we are all united by our love for {s5} and support for {reg4?her:his} legitimate claim to the rulership of all Calradia. But I have heard some talk of internal bickering in other realms...", "mayor_internal_politics_2",[
  ]],

  [anyone,"mayor_internal_politics_2",[], "The lords of a realm often have very different ideas about honor, strategy, and the way a nobleman should behave. In addition, they compete with each other for the ruler's favor, and are constantly weighing up their position -- how they stand, how their friends and family stand, and how their enemies stand.", "mayor_internal_politics_3", []],

  [anyone,"mayor_internal_politics_3",[], "Underlying all the tensions is the possibility that a lord may abandon his liege, and pledge vassalhood to another. In theory, each lord has sworn an oath of vassalage, but in practice, a vassal can always find an excuse to absolve himself. The vassal may claim that the liege has failed to hold up his end of the bargain, to protect the vassal and treat him justly. Or, the vassal may claim that his liege is in fact a usurper, and another has a better claim to the kingship.", "mayor_internal_politics_4", []],

  [anyone,"mayor_internal_politics_4",[], "Lieges and vassals still watch each other carefully. If a king believes that his vassal is going to change sides or rebel, he may indict the vassal for treason and seize his properties. Likewise, if a vassal fears that he will be indicted, he may rebel. Usually, whoever makes the first move will be able to control the vassal's fortresses.", "mayor_internal_politics_5", []],

  [anyone,"mayor_internal_politics_5",[], "Now, men do not trust a vassal who turns coat easily, nor do they trust a king who lightly throws around charges of treason. Those two factors can keep a realm together. But if relations between a vassal and a liege deteriorate far enough, things can become very tense indeed... In other lands, of course. These things could never happen here in the {s4}.", "mayor_prepolitics", []],

  [anyone|plyr, "mayor_political_questions", [], "That is all. Thank you.", "mayor_pretalk", []],


  [anyone,"merchant_quest_about_job", [], "What about it?", "merchant_quest_about_job_2",[]],
  [anyone|plyr,"merchant_quest_about_job_2", [], "What if I can't finish it?", "merchant_quest_what_if_fail",[]],
  [anyone|plyr,"merchant_quest_about_job_2", [], "Well, I'm still working on it.", "merchant_quest_about_job_working",[]],
  [anyone,"merchant_quest_about_job_working", [], "Good. I'm sure you will handle it.", "mayor_pretalk",[]],


  [anyone,"merchant_quest_last_offered_job", [], "Eh, you want to reconsider that. Good...", "merchant_quest_brief",
   [[assign,"$random_merchant_quest_no","$merchant_offered_quest"]]],


  [anyone,"merchant_quest_what_if_fail", [(store_partner_quest,":partner_quest"),(eq,":partner_quest","qst_deliver_wine")],
   "I hope you don't fail. In that case, I'll have to ask for the price of the cargo you were carrying.", "mayor_pretalk",[]],
  [anyone,"merchant_quest_what_if_fail", [], "Well, just do your best to finish it.", "mayor_pretalk",[]],

  [anyone,"merchant_quest_taken", [], "Excellent. I am counting on you then. Good luck.", "mayor_pretalk",
   []],
  [anyone,"merchant_quest_stall", [], "Well, the job will be available for a few more days I guess. Tell me if you decide to take it.", "mayor_pretalk",[]],


  [anyone,"mayor_economy_report_1", [], "{s32}", "mayor_economy_report_2",
   []],

  [anyone,"mayor_economy_report_2", [], "{s42}", "mayor_economy_report_3",
   []],

   [anyone,"mayor_economy_report_3", [], "{s47}", "mayor_pretalk",
   []],


###################################################################3
# Random Merchant quests....
##############################

# Ryan BEGIN
  # deal with looters

  [anyone,"merchant_quest_requested",
   [
     (eq,"$random_merchant_quest_no","qst_deal_with_looters"),
     ],
   "Well, you look able enough. I think I might have something you could do.", "merchant_quest_brief", []],

  [anyone,"merchant_quest_brief",
   [
     (eq,"$random_merchant_quest_no","qst_deal_with_looters"),
     (try_begin),
       (party_slot_eq,"$g_encountered_party",slot_party_type,spt_town),
       (str_store_string,s5,"@town"),
     (else_try),
       (party_slot_eq,"$g_encountered_party",slot_party_type,spt_village),
       (str_store_string,s5,"@village"),
     (try_end),
     ],
   "We've had some fighting near the {s5} lately, with all the chaos that comes with it,\
 and that's led some of our less upstanding locals to try and make their fortune out of looting the shops and farms during the confusion.\
 A lot of valuable goods were taken. I need somebody to teach those bastards a lesson.\
 Sound like your kind of work?", "merchant_quest_looters_choice", []],

  [anyone|plyr,"merchant_quest_looters_choice", [], "Aye, I'll do it.", "merchant_quest_looters_brief", []],

  [anyone|plyr,"merchant_quest_looters_choice", [], "I'm afraid I can't take the job at the moment.", "merchant_quest_stall",[]],

  [anyone,"merchant_quest_looters_brief", [
   (try_begin),
	(party_slot_eq,"$g_encountered_party",slot_party_type,spt_town),
	(str_store_string,s5,"@town"),
   (else_try),
	(party_slot_eq,"$g_encountered_party",slot_party_type,spt_village),
	(str_store_string,s5,"@village"),
   (try_end),

#     (party_get_slot,":merchant","$current_town",slot_town_merchant),
#     (troop_clear_inventory,":merchant"),
   (store_random_in_range,":random_num_looters",3,7),
   (quest_set_slot,"qst_deal_with_looters",slot_quest_target_amount,":random_num_looters"),
   (try_for_range,":unused",0,":random_num_looters"),
     (store_random_in_range,":random_radius",5,14),
     (set_spawn_radius,":random_radius"),
		##Floris MTT begin
		(try_begin),
			(eq, "$troop_trees", troop_trees_0),
			(spawn_around_party,"$g_encountered_party","pt_looters"),
		(else_try),
			(eq, "$troop_trees", troop_trees_1),
			(spawn_around_party,"$g_encountered_party","pt_looters_r"),
		(else_try),
			(eq, "$troop_trees", troop_trees_2),
			(spawn_around_party,"$g_encountered_party","pt_looters_e"),
		(try_end),
		##Floris MTT end
     (party_set_flags, reg0, pf_quest_party, 1),
     (party_set_ai_behavior, reg0, ai_bhvr_patrol_location),
     (party_set_ai_patrol_radius, reg0, 2),
     (party_get_position, pos0, reg0),
     (party_set_ai_target_position, reg0, pos0),
   (try_end),
   (str_store_troop_name_link, s9, "$g_talk_troop"),
   (str_store_party_name_link, s13, "$g_encountered_party"),
   (str_store_party_name, s4, "$g_encountered_party"),
   (setup_quest_text, "qst_deal_with_looters"),
   (str_store_string, s2, "@The Guildmaster of {s13} has asked you to deal with looters in the surrounding countryside."),
   (call_script, "script_start_quest", "qst_deal_with_looters", "$g_talk_troop"),
   (assign, "$g_leave_encounter",1),
  ],
   "Excellent! You'll find the looters roaming around the countryside, probably trying to rob more good people.\
 Kill or capture the bastards, I don't care what you do with them.\
 I'll pay you a bounty of 40 denars on every band of looters you destroy,\
 until all the looters are dealt with.", "close_window",
   []],
# Ryan END

#The following few quests are non-random -- they will be checked every time a player asks for a job. If circumstances allow it, then the player will
  [anyone,"merchant_quest_requested", [
  (eq,"$random_merchant_quest_no","qst_retaliate_for_border_incident"),

  (quest_get_slot, ":target_faction", "qst_retaliate_for_border_incident", slot_quest_target_faction),
  (call_script, "script_faction_get_adjective_to_s10", ":target_faction"),

  (faction_get_slot, ":leader", "$g_encountered_party_faction", slot_faction_leader),
  (str_store_troop_name, s5, ":leader"),
##diplomacy start+ Use forrect gender for faction leader
  (call_script, "script_dplmc_store_troop_is_female", ":leader"),
#Next line, fix pronouns with reg0
	], "Well, there is a very great favor which you could do us... As you may have heard, some {s10}s have come across the border to attack our people. {s5} is under great pressure from some of the more bellicose of {reg0?her:his} vassals to respond with a declaration of war. Unfortunately, while the great lords of this land grow rich from bloodshed, we of the commons will be caught in the middle, and will suffer.",
	"merchant_quest_explain_2", []],
##diplomacy end+

  [anyone,"merchant_quest_explain_2", [
  (eq,"$random_merchant_quest_no","qst_retaliate_for_border_incident"),
  (quest_get_slot, ":target_troop", "qst_retaliate_for_border_incident", slot_quest_target_troop),
  (str_store_troop_name, s7, ":target_troop"),
##diplomacy start+ Use correct gender for faction leader
  (faction_get_slot, ":leader", "$g_encountered_party_faction", slot_faction_leader),
  (call_script, "script_dplmc_store_troop_is_female", ":leader"),
##diplomacy end+
  ],
##diplomacy start+ Fix pronouns with reg0
  "We are not saying that {s5} should overlook this aggression -- far from it! But if {reg0?she:he} charges one of {reg0?her:his} own lords to respond, then the cycle of provocation will necessarily lead to a full-fledged confrontation. Now, if an outsider were to step in and defeat a {s10} lord in battle, then honor would be done, and it would defuse the clamor for war. If the defeated lord were a known troublemaker -- {s7} -- then the {s10}s might be able to overlook it.",
  "merchant_quest_brief",[]],
##diplomacy end+

  [anyone,"merchant_quest_brief", [
  (eq,"$random_merchant_quest_no","qst_retaliate_for_border_incident"),
  (quest_get_slot, ":target_troop", "qst_retaliate_for_border_incident", slot_quest_target_troop),
  (str_store_troop_name, s7, ":target_troop"),
  ],
  "We need you to attack and defeat {s7}. This will not be an easy task, and that outsider would damage {his/her} relationship with the {s10}s, but we would be very grateful. We could not acknowledge a connection with that outsider, but we could be sure that {he/she} would be handsomely rewarded... Could you do this?",
  "merchant_quest_retaliate_confirm",[]],

  [anyone|plyr,"merchant_quest_retaliate_confirm", [], "Aye, I can do it.", "merchant_quest_track_bandits_brief", [
#    (quest_set_slot, "qst_retaliate_for_border_incident", slot_quest_target_troop, "$g_target_leader"),
#    (quest_set_slot, "qst_retaliate_for_border_incident", slot_quest_target_faction, "$g_target_faction"),

	(str_store_faction_name, s11, "$g_encountered_party_faction"),
    (setup_quest_text, "qst_retaliate_for_border_incident"),
    (str_store_string, s2, "str_track_down_s7_and_defeat_him_defusing_calls_for_war_within_the_s11"),
    (call_script, "script_start_quest", "qst_retaliate_for_border_incident", "$g_talk_troop"),
  ]],

  [anyone|plyr,"merchant_quest_retaliate_confirm", [], "I would prefer not to get mixed up in such things", "merchant_pretalk", [
	(quest_set_slot, "qst_retaliate_for_border_incident", slot_quest_dont_give_again_remaining_days, 5),
  ]],



  [anyone,"destroy_lair_quest_brief", [
     (eq,"$random_quest_no", "qst_destroy_bandit_lair"),
	 (quest_get_slot, ":bandit_lair", "qst_destroy_bandit_lair", slot_quest_target_party),
	 (party_get_template_id, ":bandit_type", ":bandit_lair"),
				##Floris MTT begin
	 (this_or_next|eq, ":bandit_type", "pt_sea_raider_lair"),
	 (this_or_next|eq, ":bandit_type", "pt_sea_raider_lair_r"),
	 (eq, ":bandit_type", "pt_sea_raider_lair_e"),
				##Floris MTT end
	 ],
	"The raiders are likely to have laid up their ships in a well-concealed cove, somewhere along the coastline, preferably next to a small stream where they have some water. The best way to discover its location would be to find a group of sea raiders who appear to be heading back to their base to resupply, and follow them.", "merchant_quest_track_bandit_lair_choice",
   []],

  [anyone,"destroy_lair_quest_brief", [
     (eq,"$random_quest_no", "qst_destroy_bandit_lair"),
	 (quest_get_slot, ":bandit_lair", "qst_destroy_bandit_lair", slot_quest_target_party),
	 (party_get_template_id, ":bandit_type", ":bandit_lair"),
				##Floris MTT begin
	 (this_or_next|eq, ":bandit_type", "pt_desert_bandit_lair"),
	 (this_or_next|eq, ":bandit_type", "pt_desert_bandit_lair_r"),
	 (eq, ":bandit_type", "pt_desert_bandit_lair_e"),
				##Floris MTT end
	 ],
	"Bandits such as these usually establish their hideouts in the foothills on the edge of the desert, often in a canyon near a spring. This gives them both water and concealment. The best way to discover its location would be to find a group of desert bandits who appear to be heading back to their base to resupply, and follow them.", "merchant_quest_track_bandit_lair_choice",
   []],

  [anyone,"destroy_lair_quest_brief", [
     (eq,"$random_quest_no", "qst_destroy_bandit_lair"),
	 (quest_get_slot, ":bandit_lair", "qst_destroy_bandit_lair", slot_quest_target_party),
	 (party_get_template_id, ":bandit_type", ":bandit_lair"),
				##Floris MTT begin
	 (this_or_next|eq, ":bandit_type", "pt_mountain_bandit_lair"),
	 (this_or_next|eq, ":bandit_type", "pt_mountain_bandit_lair_r"),
	 (eq, ":bandit_type", "pt_mountain_bandit_lair_e"),
				##Floris MTT end
	 ],
	"Bandits such as these will usually establish a base in the highlands, often on an steep ledge where they have a view of the surrounding countryside. This makes them difficult to surprise. The best way to discover its location would be to find a group of mountain bandits who appear to be heading back to their base to resupply, and follow them.", "merchant_quest_track_bandit_lair_choice",
   []],

  [anyone,"destroy_lair_quest_brief", [
     (eq,"$random_quest_no", "qst_destroy_bandit_lair"),
	 (quest_get_slot, ":bandit_lair", "qst_destroy_bandit_lair", slot_quest_target_party),
	 (party_get_template_id, ":bandit_type", ":bandit_lair"),
				##Floris MTT begin
	 (this_or_next|eq, ":bandit_type", "pt_forest_bandit_lair"),
	 (this_or_next|eq, ":bandit_type", "pt_forest_bandit_lair_r"),
	 (eq, ":bandit_type", "pt_forest_bandit_lair_e"),
				##Floris MTT end
	 ],
	"Bandits such as these will usually set up their encampments deep in the woods, sometimes in the middle of a swamp. The best way to discover its location would be to find a group of forest bandits who appear to be heading back to their base to resupply, and follow them.", "merchant_quest_track_bandit_lair_choice",
   []],

  [anyone,"destroy_lair_quest_brief", [
     (eq,"$random_quest_no", "qst_destroy_bandit_lair"),
	 (quest_get_slot, ":bandit_lair", "qst_destroy_bandit_lair", slot_quest_target_party),
	 (party_get_template_id, ":bandit_type", ":bandit_lair"),
				##Floris MTT begin
	 (this_or_next|eq, ":bandit_type", "pt_steppe_bandit_lair"),
	 (this_or_next|eq, ":bandit_type", "pt_steppe_bandit_lair_r"),
	 (eq, ":bandit_type", "pt_steppe_bandit_lair_e"),
				##Floris MTT end
	 ],
	"Bandits such as these will usually set up their encampments in the woodland on the steppe, where they have some concealment. The best way to discover its location would be to find a group of steppe bandits who appear to be heading back to their base to resupply, and follow them.", "merchant_quest_track_bandit_lair_choice",
   []],

  [anyone,"destroy_lair_quest_brief", [
     (eq,"$random_quest_no", "qst_destroy_bandit_lair"),
	 (quest_get_slot, ":bandit_lair", "qst_destroy_bandit_lair", slot_quest_target_party),
	 (party_get_template_id, ":bandit_type", ":bandit_lair"),
				##Floris MTT begin
	 (this_or_next|eq, ":bandit_type", "pt_taiga_bandit_lair"),
	 (this_or_next|eq, ":bandit_type", "pt_taiga_bandit_lair_r"),
	 (eq, ":bandit_type", "pt_taiga_bandit_lair_e"),
				##Floris MTT end
	 ],
	"Bandits such as these will usually set up their encampments deep in the woods. The best way to discover its location would be to find a group of tundra bandits who appear to be heading back to their base to resupply, and follow them.", "merchant_quest_track_bandit_lair_choice",
   []],

  [anyone|plyr,"merchant_quest_track_bandit_lair_choice", [], "Aye, I'll do it.", "merchant_quest_destroy_lair_brief", [

    (quest_get_slot, ":target_party", "qst_destroy_bandit_lair", slot_quest_target_party),
    (party_set_flags, ":target_party", pf_quest_party, 1),
#    (quest_set_slot, "qst_track_down_bandits", slot_quest_target_party, "$g_bandit_party_for_bounty"), #WHY IS THIS COMMENTED OUT?
    (quest_set_slot, "qst_destroy_bandit_lair", slot_quest_giver_troop, "$g_talk_troop"),
    (quest_set_slot, "qst_destroy_bandit_lair", slot_quest_giver_center, "$g_encountered_party"),

    (str_store_troop_name_link, s11, "$g_talk_troop"),
    (str_store_party_name, s9, ":target_party"),
    (setup_quest_text, "qst_destroy_bandit_lair"),
    (str_store_string, s2, "str_bandit_lair_quest_description"),
    (call_script, "script_start_quest", "qst_destroy_bandit_lair", "$g_talk_troop"),
  ]],

  [anyone|plyr,"merchant_quest_track_bandit_lair_choice", [], "I'm afraid I can't take the job at the moment.", "lord_pretalk",[
  (quest_set_slot, "qst_destroy_bandit_lair", slot_quest_dont_give_again_remaining_days, 1),
  ]],

   [anyone,"merchant_quest_destroy_lair_brief", [
  ], "Very good. We will await word of your success.", "close_window",
   [
   (assign, "$g_leave_encounter", 1),
   ]],



  [anyone,"merchant_quest_requested", [
  (eq,"$random_merchant_quest_no", "qst_track_down_bandits"),
  ], "We have heard that {s4}, some travellers on the road {reg4?to:from} {s5} were attacked by {s7}.", "merchant_quest_brief",
   [
   (call_script,"script_merchant_road_info_to_s42", "$g_encountered_party"),
   (assign, "$g_bandit_party_for_bounty", reg0),
   (assign, ":origin", reg1),
   (assign, ":destination", reg2),
   (assign, ":hours_ago", reg3),
   (try_begin),
	(lt, ":hours_ago", 24),
	(str_store_string, s4, "str_a_short_while_ago"),
   (else_try),
	(lt, ":hours_ago", 48),
	(str_store_string, s4, "str_one_day_ago"),
   (else_try),
 	(lt, ":hours_ago", 72),
	(str_store_string, s4, "str_two_days_day_ago"),
   (else_try),
 	(lt, ":hours_ago", 144),
	(str_store_string, s4, "str_earlier_this_week"),
   (else_try),
	(str_store_string, s4, "str_about_a_week_ago"),
   (try_end),


   (try_begin),
	(eq, ":origin", "$g_encountered_party"),
	(str_store_party_name, s5, ":destination"),
	(assign, reg4, 0),
   (else_try),
	(eq, ":destination", "$g_encountered_party"),
	(str_store_party_name, s5, ":origin"),
	(assign, reg4, 1),
   (try_end),

   (str_store_party_name, s7, "$g_bandit_party_for_bounty"),
   ###
   (quest_set_slot, "qst_track_down_bandits", slot_quest_target_party, "$g_bandit_party_for_bounty"),
   ]],

  [anyone,"merchant_quest_brief", [
     (eq,"$random_merchant_quest_no", "qst_track_down_bandits"),
     (quest_get_slot, ":target_party", "qst_track_down_bandits", slot_quest_target_party),
	 (str_store_party_name, s4, ":target_party"),
	 ],
	"We would like you to track these {s4} down. The merchants of the town were able to get a description of their leader, and have put together a bounty. If you can hunt them down and destroy them, we'll make it worth your while...", "merchant_quest_track_bandits_choice",
   []],

  [anyone|plyr,"merchant_quest_track_bandits_choice", [], "Aye, I'll do it.", "merchant_quest_track_bandits_brief", [
    (assign, "$merchant_offered_quest", 0),
	(assign,"$merchant_quest_last_offerer", "$g_talk_troop"),

    (quest_get_slot, ":target_party", "qst_track_down_bandits", slot_quest_target_party),
    (party_set_flags, ":target_party", pf_quest_party, 1),
#    (quest_set_slot, "qst_track_down_bandits", slot_quest_target_party, "$g_bandit_party_for_bounty"), #WHY IS THIS COMMENTED OUT?
    (quest_set_slot, "qst_track_down_bandits", slot_quest_giver_troop, "$g_talk_troop"),
    (quest_set_slot, "qst_track_down_bandits", slot_quest_giver_center, "$g_encountered_party"),

    (str_store_party_name_link, s8, "$g_encountered_party"),
    (str_store_party_name, s9, ":target_party"),
    (setup_quest_text, "qst_track_down_bandits"),
    (str_store_string, s2, "str_track_down_the_s9_who_attacked_travellers_near_s8_then_report_back_to_the_town"),
    (call_script, "script_start_quest", "qst_track_down_bandits", "$g_talk_troop"),
  ]],


   [anyone,"merchant_quest_track_bandits_brief", [
  ], "Very good. The band may not have lingered long in the area, but chances are that they will be spotted by other travellers on the road.", "close_window",
   [
   (assign, "$g_leave_encounter", 1),
   ]],

  [anyone|plyr,"merchant_quest_track_bandits_choice", [], "I'm afraid I can't take the job at the moment.", "merchant_quest_stall",[
  (quest_set_slot, "qst_track_down_bandits", slot_quest_dont_give_again_remaining_days, 1),
  ]],



  #Random quests begin here. Deliver wine:
  [anyone,"merchant_quest_requested", [(eq,"$random_merchant_quest_no","qst_deliver_wine"),], "You're looking for a job?\
 Actually I was looking for someone to deliver some {s4}.\
 Perhaps you can do that...", "merchant_quest_brief",
   [(quest_get_slot, ":quest_target_item", "qst_deliver_wine", slot_quest_target_item),
    (str_store_item_name, s4, ":quest_target_item"),
    ]],

  [anyone,"merchant_quest_brief", [(eq,"$random_merchant_quest_no","qst_deliver_wine")],
   "I have a cargo of {s6} that needs to be delivered to the tavern in {s4}.\
 If you can take {reg5} units of {s6} to {s4} in 7 days, you may earn {reg8} denars.\
 What do you say?", "merchant_quest_brief_deliver_wine",
   [(quest_get_slot, reg5, "qst_deliver_wine", slot_quest_target_amount),
    (quest_get_slot, reg8, "qst_deliver_wine", slot_quest_gold_reward),
    (quest_get_slot, ":quest_target_item", "qst_deliver_wine", slot_quest_target_item),
    (quest_get_slot, ":quest_target_center", "qst_deliver_wine", slot_quest_target_center),
    (str_store_troop_name, s9, "$g_talk_troop"),
    (str_store_party_name_link, s3, "$g_encountered_party"),
    (str_store_party_name_link, s4, ":quest_target_center"),
    (str_store_item_name, s6, ":quest_target_item"),
    (setup_quest_text,"qst_deliver_wine"),
    (str_store_string, s2, "@{s9} of {s3} asked you to deliver {reg5} units of {s6} to the tavern in {s4} in 7 days."),
    #s2 should not be changed until the decision is made
   ]],

  [anyone|plyr,"merchant_quest_brief_deliver_wine", [(store_free_inventory_capacity,":capacity"),
                                                     (quest_get_slot, ":quest_target_amount", "qst_deliver_wine", slot_quest_target_amount),
                                                     (ge, ":capacity", ":quest_target_amount"),
                                                     ],
      "Alright. I will make the delivery.", "merchant_quest_taken",
   [(quest_get_slot, ":quest_target_amount", "qst_deliver_wine", slot_quest_target_amount),
    (quest_get_slot, ":quest_target_item", "qst_deliver_wine", slot_quest_target_item),
    (troop_add_items, "trp_player", ":quest_target_item",":quest_target_amount"),
    (call_script, "script_start_quest", "qst_deliver_wine", "$g_talk_troop"),
    ]],

  [anyone|plyr,"merchant_quest_brief_deliver_wine", [], "I am afraid I can't carry all that cargo now.", "merchant_quest_stall",[]],

#escort merchant caravan:
  [anyone,"merchant_quest_requested", [(eq,"$random_merchant_quest_no","qst_escort_merchant_caravan")], "You're looking for a job?\
 Actually I was looking for someone to escort a caravan.\
 Perhaps you can do that...", "merchant_quest_brief",
   []],

  [anyone,"merchant_quest_brief", [(eq, "$random_merchant_quest_no", "qst_escort_merchant_caravan")],
   "I am going to send a caravan of goods to {s8}.\
 However with all those bandits and deserters on the roads, I don't want to send them out without an escort.\
 If you can lead that caravan to {s8} in 15 days, you will earn {reg8} denars.\
 Of course your party needs to be at least {reg4} strong to offer them any protection.", "escort_merchant_caravan_quest_brief",
   [(quest_get_slot, reg8, "qst_escort_merchant_caravan", slot_quest_gold_reward),
    (quest_get_slot, reg4, "qst_escort_merchant_caravan", slot_quest_target_amount),
    (quest_get_slot, ":quest_target_center", "qst_escort_merchant_caravan", slot_quest_target_center),
    (str_store_party_name, s8, ":quest_target_center"),
   ]],

  [anyone|plyr,"escort_merchant_caravan_quest_brief", [(store_party_size_wo_prisoners, ":party_size", "p_main_party"),
                                                       (quest_get_slot, ":quest_target_amount", "qst_escort_merchant_caravan", slot_quest_target_amount),
                                                       (ge,":party_size",":quest_target_amount"),
                                                       ],
   "Alright. I will escort the caravan.", "merchant_quest_taken",
   [(quest_get_slot, ":quest_target_center", "qst_escort_merchant_caravan", slot_quest_target_center),
    (set_spawn_radius, 1),
	##Floris MTT begin
	(try_begin),
		(eq, "$troop_trees", troop_trees_0),
		(spawn_around_party,"$g_encountered_party","pt_merchant_caravan"),
	(else_try),
		(eq, "$troop_trees", troop_trees_1),
		(spawn_around_party,"$g_encountered_party","pt_merchant_caravan_r"),
	(else_try),
		(eq, "$troop_trees", troop_trees_2),
		(spawn_around_party,"$g_encountered_party","pt_merchant_caravan_e"),
	(try_end),
	##Floris MTT end
    (assign, ":quest_target_party", reg0),
    (party_set_ai_behavior, ":quest_target_party", ai_bhvr_track_party),
    (party_set_ai_object, ":quest_target_party", "p_main_party"),
    (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
    (quest_set_slot, "qst_escort_merchant_caravan", slot_quest_target_party, ":quest_target_party"),
    (quest_set_slot, "qst_escort_merchant_caravan", slot_quest_current_state, 0),
    (str_store_party_name_link, s8, ":quest_target_center"),
    (setup_quest_text, "qst_escort_merchant_caravan"),
    (str_store_string, s2, "@Escort the merchant caravan to the town of {s8}."),
    (call_script, "script_start_quest", "qst_escort_merchant_caravan", "$g_talk_troop"),
    ]],

  [anyone|plyr,"escort_merchant_caravan_quest_brief", [(store_party_size_wo_prisoners, ":party_size", "p_main_party"),
                                                       (quest_get_slot, ":quest_target_amount", "qst_escort_merchant_caravan", slot_quest_target_amount),
                                                       (lt,":party_size",":quest_target_amount"),],
   "I am afraid I don't have that many soldiers with me.", "merchant_quest_stall",[]],
  [anyone|plyr,"escort_merchant_caravan_quest_brief", [(store_party_size_wo_prisoners, ":party_size", "p_main_party"),
                                                       (quest_get_slot, ":quest_target_amount", "qst_escort_merchant_caravan", slot_quest_target_amount),
                                                       (ge,":party_size",":quest_target_amount"),],
   "Sorry. I can't do that right now", "merchant_quest_stall",[]],

  [party_tpl|pt_merchant_caravan,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq,"$g_encountered_party",":quest_target_party"),
                                           (quest_slot_eq,"qst_escort_merchant_caravan", slot_quest_current_state, 2),
                                           ],
   "We can cover the rest of the way ourselves. Thanks.", "close_window",[(assign, "$g_leave_encounter", 1)]],

  [party_tpl|pt_merchant_caravan,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq,"$g_encountered_party",":quest_target_party"),
                                           (quest_get_slot, ":quest_target_center", "qst_escort_merchant_caravan", slot_quest_target_center),
                                           (store_distance_to_party_from_party, ":dist", ":quest_target_center",":quest_target_party"),
                                           (lt,":dist",4),
                                           (quest_slot_eq, "qst_escort_merchant_caravan", slot_quest_current_state, 1),
                                           ],
   "Well, we have almost reached {s21}. We can cover the rest of the way ourselves.\
 Here's your pay... {reg14} denars.\
 Thanks for escorting us. Good luck.", "close_window",[(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                                       (quest_get_slot, ":quest_target_center", "qst_escort_merchant_caravan", slot_quest_target_center),
                                                       (quest_get_slot, ":quest_giver_center", "qst_escort_merchant_caravan", slot_quest_giver_center),
                                                       (quest_get_slot, ":quest_gold_reward", "qst_escort_merchant_caravan", slot_quest_gold_reward),
                                                       (party_set_ai_behavior, ":quest_target_party", ai_bhvr_travel_to_party),
                                                       (party_set_ai_object, ":quest_target_party", ":quest_target_center"),
                                                       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                                                       (str_store_party_name, s21, ":quest_target_center"),
                                                       (call_script, "script_change_player_relation_with_center", ":quest_giver_center", 1),
                                                       (call_script, "script_end_quest","qst_escort_merchant_caravan"),
                                                       (quest_set_slot, "qst_escort_merchant_caravan", slot_quest_current_state, 2),
                                                       (call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
                                                       (assign, ":xp_reward", ":quest_gold_reward"),
                                                       (val_mul, ":xp_reward", 5),
                                                       (val_add, ":xp_reward", 100),
                                                       (add_xp_as_reward, ":xp_reward"),
                                                       (call_script, "script_change_troop_renown", "trp_player", 2),
                                                       (assign, reg14, ":quest_gold_reward"),
                                                       (assign, "$g_leave_encounter", 1),
                                                       ]],

  [party_tpl|pt_merchant_caravan,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq,"$g_encountered_party",":quest_target_party"),
                                           (quest_slot_eq, "qst_escort_merchant_caravan", slot_quest_current_state, 0),
                                           ],
   "Greetings. You must be our escort, right?", "merchant_caravan_intro_1",[(quest_set_slot, "qst_escort_merchant_caravan", slot_quest_current_state, 1),]],
   
   ##Floris MTT Begin
     [party_tpl|pt_merchant_caravan_r,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq,"$g_encountered_party",":quest_target_party"),
                                           (quest_slot_eq,"qst_escort_merchant_caravan", slot_quest_current_state, 2),
                                           ],
   "We can cover the rest of the way ourselves. Thanks.", "close_window",[(assign, "$g_leave_encounter", 1)]],

  [party_tpl|pt_merchant_caravan_r,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq,"$g_encountered_party",":quest_target_party"),
                                           (quest_get_slot, ":quest_target_center", "qst_escort_merchant_caravan", slot_quest_target_center),
                                           (store_distance_to_party_from_party, ":dist", ":quest_target_center",":quest_target_party"),
                                           (lt,":dist",4),
                                           (quest_slot_eq, "qst_escort_merchant_caravan", slot_quest_current_state, 1),
                                           ],
   "Well, we have almost reached {s21}. We can cover the rest of the way ourselves.\
 Here's your pay... {reg14} denars.\
 Thanks for escorting us. Good luck.", "close_window",[(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                                       (quest_get_slot, ":quest_target_center", "qst_escort_merchant_caravan", slot_quest_target_center),
                                                       (quest_get_slot, ":quest_giver_center", "qst_escort_merchant_caravan", slot_quest_giver_center),
                                                       (quest_get_slot, ":quest_gold_reward", "qst_escort_merchant_caravan", slot_quest_gold_reward),
                                                       (party_set_ai_behavior, ":quest_target_party", ai_bhvr_travel_to_party),
                                                       (party_set_ai_object, ":quest_target_party", ":quest_target_center"),
                                                       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                                                       (str_store_party_name, s21, ":quest_target_center"),
                                                       (call_script, "script_change_player_relation_with_center", ":quest_giver_center", 1),
                                                       (call_script, "script_end_quest","qst_escort_merchant_caravan"),
                                                       (quest_set_slot, "qst_escort_merchant_caravan", slot_quest_current_state, 2),
                                                       (call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
                                                       (assign, ":xp_reward", ":quest_gold_reward"),
                                                       (val_mul, ":xp_reward", 5),
                                                       (val_add, ":xp_reward", 100),
                                                       (add_xp_as_reward, ":xp_reward"),
                                                       (call_script, "script_change_troop_renown", "trp_player", 2),
                                                       (assign, reg14, ":quest_gold_reward"),
                                                       (assign, "$g_leave_encounter", 1),
                                                       ]],

  [party_tpl|pt_merchant_caravan_r,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq,"$g_encountered_party",":quest_target_party"),
                                           (quest_slot_eq, "qst_escort_merchant_caravan", slot_quest_current_state, 0),
                                           ],
   "Greetings. You must be our escort, right?", "merchant_caravan_intro_1",[(quest_set_slot, "qst_escort_merchant_caravan", slot_quest_current_state, 1),]],
    [party_tpl|pt_merchant_caravan_r,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq, "$g_encountered_party", ":quest_target_party"),
                                           ],
   "Eh. We've made it this far... What do you want us to do?", "escort_merchant_caravan_talk",[]],
   
     [party_tpl|pt_merchant_caravan_e,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq,"$g_encountered_party",":quest_target_party"),
                                           (quest_slot_eq,"qst_escort_merchant_caravan", slot_quest_current_state, 2),
                                           ],
   "We can cover the rest of the way ourselves. Thanks.", "close_window",[(assign, "$g_leave_encounter", 1)]],

  [party_tpl|pt_merchant_caravan_e,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq,"$g_encountered_party",":quest_target_party"),
                                           (quest_get_slot, ":quest_target_center", "qst_escort_merchant_caravan", slot_quest_target_center),
                                           (store_distance_to_party_from_party, ":dist", ":quest_target_center",":quest_target_party"),
                                           (lt,":dist",4),
                                           (quest_slot_eq, "qst_escort_merchant_caravan", slot_quest_current_state, 1),
                                           ],
   "Well, we have almost reached {s21}. We can cover the rest of the way ourselves.\
 Here's your pay... {reg14} denars.\
 Thanks for escorting us. Good luck.", "close_window",[(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                                       (quest_get_slot, ":quest_target_center", "qst_escort_merchant_caravan", slot_quest_target_center),
                                                       (quest_get_slot, ":quest_giver_center", "qst_escort_merchant_caravan", slot_quest_giver_center),
                                                       (quest_get_slot, ":quest_gold_reward", "qst_escort_merchant_caravan", slot_quest_gold_reward),
                                                       (party_set_ai_behavior, ":quest_target_party", ai_bhvr_travel_to_party),
                                                       (party_set_ai_object, ":quest_target_party", ":quest_target_center"),
                                                       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                                                       (str_store_party_name, s21, ":quest_target_center"),
                                                       (call_script, "script_change_player_relation_with_center", ":quest_giver_center", 1),
                                                       (call_script, "script_end_quest","qst_escort_merchant_caravan"),
                                                       (quest_set_slot, "qst_escort_merchant_caravan", slot_quest_current_state, 2),
                                                       (call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
                                                       (assign, ":xp_reward", ":quest_gold_reward"),
                                                       (val_mul, ":xp_reward", 5),
                                                       (val_add, ":xp_reward", 100),
                                                       (add_xp_as_reward, ":xp_reward"),
                                                       (call_script, "script_change_troop_renown", "trp_player", 2),
                                                       (assign, reg14, ":quest_gold_reward"),
                                                       (assign, "$g_leave_encounter", 1),
                                                       ]],

  [party_tpl|pt_merchant_caravan_e,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq,"$g_encountered_party",":quest_target_party"),
                                           (quest_slot_eq, "qst_escort_merchant_caravan", slot_quest_current_state, 0),
                                           ],
   "Greetings. You must be our escort, right?", "merchant_caravan_intro_1",[(quest_set_slot, "qst_escort_merchant_caravan", slot_quest_current_state, 1),]],
  [party_tpl|pt_merchant_caravan_e,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq, "$g_encountered_party", ":quest_target_party"),
                                           ],
   "Eh. We've made it this far... What do you want us to do?", "escort_merchant_caravan_talk",[]],
   ##Floris MTT End

  [anyone|plyr,"merchant_caravan_intro_1", [], "Yes. My name is {playername}. I will lead you to {s1}.",
   "merchant_caravan_intro_2",[(quest_get_slot, ":quest_target_center", "qst_escort_merchant_caravan", slot_quest_target_center),
                               (str_store_party_name, s1, ":quest_target_center"),
                               ]],

  [anyone,"merchant_caravan_intro_2", [], "Well, It is good to know we won't travel alone. What do you want us to do now?", "escort_merchant_caravan_talk",[]],

  [party_tpl|pt_merchant_caravan,"start", [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                                           (eq, "$g_encountered_party", ":quest_target_party"),
                                           ],
   "Eh. We've made it this far... What do you want us to do?", "escort_merchant_caravan_talk",[]],

  [anyone|plyr,"escort_merchant_caravan_talk", [], "You follow my lead. I'll take you through a safe route.", "merchant_caravan_follow_lead",[]],
  [anyone,"merchant_caravan_follow_lead", [], "Alright. We'll be right behind you.", "close_window",[(assign, "$escort_merchant_caravan_mode", 0),
                                                                                                     (assign, "$g_leave_encounter", 1)]],
  [anyone|plyr,"escort_merchant_caravan_talk", [], "You stay here for a while. I'll go ahead and check the road.", "merchant_caravan_stay_here",[]],
  [anyone,"merchant_caravan_stay_here", [], "Alright. We'll be waiting here for you.", "close_window",[(assign, "$escort_merchant_caravan_mode", 1),
                                                                                                       (assign, "$g_leave_encounter", 1)]],
#  [anyone|plyr,"escort_merchant_caravan_talk", [], "You go ahead to {s1}. I'll catch up with you.", "merchant_caravan_go_to_destination",[]],
#  [anyone,"merchant_caravan_go_to_destination", [], "Alright. But stay close.", "close_window",[[assign,"escort_merchant_caravan_mode",2]]],


# Troublesome bandits:
  [anyone,"merchant_quest_requested", [(eq, "$random_merchant_quest_no", "qst_troublesome_bandits")],
 "Actually, I was looking for an able adventurer like you.\
 There's this group of particularly troublesome bandits.\
 They have infested the vicinity of our town and are preying on my caravans.\
 They have avoided all the soldiers and the militias up to now.\
 If someone doesn't stop them soon, I am going to be ruined...", "merchant_quest_brief",
   []],

  [anyone,"merchant_quest_brief", [(eq,"$random_merchant_quest_no", "qst_troublesome_bandits")],
  "I will pay you {reg8} denars if you hunt down those troublesome bandits.\
 It's dangerous work. But I believe that you are the {man/one} for it.\
 What do you say?", "troublesome_bandits_quest_brief",[(quest_get_slot, reg8, "qst_troublesome_bandits", slot_quest_gold_reward),
                                                       ]],

  [anyone|plyr,"troublesome_bandits_quest_brief", [],
   "Very well. I will hunt down those bandits.", "merchant_quest_taken_bandits",
   [(set_spawn_radius,7),
    (quest_get_slot, ":quest_giver_center", "qst_troublesome_bandits", slot_quest_giver_center),
	##Floris MTT begin
	(try_begin),
		(eq, "$troop_trees", troop_trees_0),
		(spawn_around_party,":quest_giver_center","pt_troublesome_bandits"),
		(quest_set_slot, "qst_troublesome_bandits", slot_quest_target_party, reg0),
		(store_num_parties_destroyed,"$qst_troublesome_bandits_eliminated","pt_troublesome_bandits"),
		(store_num_parties_destroyed_by_player, "$qst_troublesome_bandits_eliminated_by_player", "pt_troublesome_bandits"),
	(else_try),
		(eq, "$troop_trees", troop_trees_1),
		(spawn_around_party,":quest_giver_center","pt_troublesome_bandits_r"),
		(quest_set_slot, "qst_troublesome_bandits", slot_quest_target_party, reg0),
		(store_num_parties_destroyed,"$qst_troublesome_bandits_eliminated","pt_troublesome_bandits_r"),
		(store_num_parties_destroyed_by_player, "$qst_troublesome_bandits_eliminated_by_player", "pt_troublesome_bandits_r"),
	(else_try),
		(eq, "$troop_trees", troop_trees_2),
		(spawn_around_party,":quest_giver_center","pt_troublesome_bandits_e"),
		(quest_set_slot, "qst_troublesome_bandits", slot_quest_target_party, reg0),
		(store_num_parties_destroyed,"$qst_troublesome_bandits_eliminated","pt_troublesome_bandits_e"),
		(store_num_parties_destroyed_by_player, "$qst_troublesome_bandits_eliminated_by_player", "pt_troublesome_bandits_e"),
	(try_end),
	##Floris MTT end
    (str_store_troop_name, s9, "$g_talk_troop"),
    (str_store_party_name_link, s4, "$g_encountered_party"),
    (setup_quest_text,"qst_troublesome_bandits"),
    (str_store_string, s2, "@The merchant {s9} of {s4} asked you to hunt down the troublesome bandits in the vicinity of the town."),
    (call_script, "script_start_quest", "qst_troublesome_bandits", "$g_talk_troop"),
    ]],
  [anyone,"merchant_quest_taken_bandits", [], "You will? Splendid. Good luck to you.", "close_window",
   []],

  [anyone|plyr,"troublesome_bandits_quest_brief", [],
   "Sorry. I don't have time for this right now.", "merchant_quest_stall",[]],

# Kidnapped girl:
  [anyone,"merchant_quest_requested", [(eq, "$random_merchant_quest_no", "qst_kidnapped_girl")],
 "Actually, I was looking for a reliable {man/helper} that can undertake an important mission.\
 A group of bandits have kidnapped the daughter of a friend of mine and are holding her for ransom.\
 My friend is ready to pay them, but we still need\
 someone to take the money to those rascals and bring the girl back to safety.", "merchant_quest_brief",
   []],

  [anyone,"merchant_quest_brief", [(eq, "$random_merchant_quest_no", "qst_kidnapped_girl")],
  "The amount the bandits ask as ransom is {reg12} denars.\
 I will give you that money once you accept to take the quest.\
 You have 15 days to take the money to the bandits who will be waiting near the village of {s4}.\
 Those bastards said that they are going to kill the poor girl if they don't get the money by that time.\
 You will get your pay of {reg8} denars when you bring the girl safely back here.",
   "kidnapped_girl_quest_brief",[(quest_get_slot, ":quest_target_center", "qst_kidnapped_girl", slot_quest_target_center),
                                 (str_store_party_name, s4, ":quest_target_center"),
                                 (quest_get_slot, reg8, "qst_kidnapped_girl", slot_quest_gold_reward),
                                 (quest_get_slot, reg12, "qst_kidnapped_girl", slot_quest_target_amount),
                                 ]],

  [anyone|plyr,"kidnapped_girl_quest_brief", [],
      "All right. I will take the ransom money to the bandits and bring back the girl.",
   "kidnapped_girl_quest_taken",[(set_spawn_radius, 4),
                                 (quest_get_slot, ":quest_target_center", "qst_kidnapped_girl", slot_quest_target_center),
                                 (quest_get_slot, ":quest_target_amount", "qst_kidnapped_girl", slot_quest_target_amount),
								##Floris MTT begin
								(try_begin),
									(eq, "$troop_trees", troop_trees_0),
									(spawn_around_party,":quest_target_center","pt_bandits_awaiting_ransom"),
								(else_try),
									(eq, "$troop_trees", troop_trees_1),
									(spawn_around_party,":quest_target_center","pt_bandits_awaiting_ransom_r"),
								(else_try),
									(eq, "$troop_trees", troop_trees_2),
									(spawn_around_party,":quest_target_center","pt_bandits_awaiting_ransom_e"),
								(try_end),
								##Floris MTT end
                                 (assign, ":quest_target_party", reg0),
                                 (quest_set_slot, "qst_kidnapped_girl", slot_quest_target_party, ":quest_target_party"),
                                 (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
                                 (party_set_ai_object, ":quest_target_party", "p_main_party"),
                                 (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                                 (call_script, "script_troop_add_gold", "trp_player", ":quest_target_amount"),
                                 (assign, reg12, ":quest_target_amount"),
                                 (str_store_troop_name, s1, "$g_talk_troop"),
                                 (str_store_party_name_link, s4, "$g_encountered_party"),
                                 (str_store_party_name_link, s3, ":quest_target_center"),
                                 (setup_quest_text, "qst_kidnapped_girl"),
                                 (str_store_string, s2, "@Guildmaster of {s4} gave you {reg12} denars to pay the ransom of a girl kidnapped by bandits.\
 You are to meet the bandits near {s3} and pay them the ransom fee.\
 After that you are to bring the girl back to {s4}."),
                                 (call_script, "script_start_quest", "qst_kidnapped_girl", "$g_talk_troop"),
                                 ]],

  [anyone,"kidnapped_girl_quest_taken", [], "Good. I knew we could trust you at this.\
 Here is the ransom money, {reg12} denars.\
 Count it before taking it.\
 And please, don't attempt to do anything rash.\
 Keep in mind that the girl's well being is more important than anything else...", "close_window",
   []],

  [anyone|plyr,"kidnapped_girl_quest_brief", [],
   "Sorry. I don't have time for this right now.", "merchant_quest_stall",[]],


  [trp_kidnapped_girl,"start",
   [
     (eq, "$talk_context", tc_entering_center_quest_talk),
     ],
   "Thank you so much for bringing me back!\
  I can't wait to see my family. Good-bye.",
   "close_window",
   [(remove_member_from_party, "trp_kidnapped_girl"),
    (quest_set_slot, "qst_kidnapped_girl", slot_quest_current_state, 4),
    ]],



  [trp_kidnapped_girl|plyr,"kidnapped_girl_liberated_map", [], "Yes. Come with me. We are going home.", "kidnapped_girl_liberated_map_2a",[]],
  [trp_kidnapped_girl,"kidnapped_girl_liberated_map_2a", [(neg|party_can_join)], "Unfortunately you do not seem to have room for me.", "close_window",[(assign, "$g_leave_encounter",1)]],
  [trp_kidnapped_girl,"kidnapped_girl_liberated_map_2a", [], "Oh really? Thank you so much!",
   "close_window", [(party_join),
                    (quest_set_slot, "qst_kidnapped_girl", slot_quest_current_state, 3),
                    (assign, "$g_leave_encounter",1)]],
  [trp_kidnapped_girl|plyr,"kidnapped_girl_liberated_map", [], "Wait here a while longer. I'll come back for you.", "kidnapped_girl_liberated_map_2b",[]],
  [trp_kidnapped_girl,"kidnapped_girl_liberated_map_2b", [], "Oh, please {sir/madam}, do not leave me here all alone!", "close_window",[(assign, "$g_leave_encounter",1)]],


  [trp_kidnapped_girl,"start", [],
   "Oh {sir/madam}. Thank you so much for rescuing me. Will you take me to my family now?", "kidnapped_girl_liberated_map",[]],

  [trp_kidnapped_girl|plyr,"kidnapped_girl_liberated_battle", [], "Yes. Come with me. We are going home.", "kidnapped_girl_liberated_battle_2a",[]],
  [trp_kidnapped_girl,"kidnapped_girl_liberated_battle_2a", [(neg|hero_can_join, "p_main_party")], "Unfortunately you do not seem to have room for me.", "kidnapped_girl_liberated_battle_2b",[]],
  [trp_kidnapped_girl,"kidnapped_girl_liberated_battle_2a", [], "Oh really? Thank you so much!",
   "close_window",[(party_add_members, "p_main_party","trp_kidnapped_girl",1),
                   (quest_set_slot, "qst_kidnapped_girl", slot_quest_current_state, 3),
                   ]],
  [trp_kidnapped_girl|plyr,"kidnapped_girl_liberated_battle", [], "Wait here a while longer. I'll come back for you.", "kidnapped_girl_liberated_battle_2b",[]],
  [trp_kidnapped_girl,"kidnapped_girl_liberated_battle_2b", [], "Oh, please {sir/madam}, do not leave me here all alone!",
   "close_window", [(add_companion_party,"trp_kidnapped_girl"),
                    (assign, "$g_leave_encounter",1)]],

  [trp_kidnapped_girl,"start", [], "Can I come with you now?", "kidnapped_girl_liberated_map",[]],


  [party_tpl|pt_bandits_awaiting_ransom,"start", [(quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 0),],
 "Are you the one that brought the ransom?\
 Quick, give us the money now.", "bandits_awaiting_ransom_intro_1",[(quest_set_slot, "qst_kidnapped_girl", slot_quest_current_state, 1),]],
  [party_tpl|pt_bandits_awaiting_ransom,"start", [(quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 1),],
   "You came back?\
 Quick, give us the money now.", "bandits_awaiting_ransom_intro_1",[]],
 
 ##Floris MTT begin
   [party_tpl|pt_bandits_awaiting_ransom_r,"start", [(quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 0),],
 "Are you the one that brought the ransom?\
 Quick, give us the money now.", "bandits_awaiting_ransom_intro_1",[(quest_set_slot, "qst_kidnapped_girl", slot_quest_current_state, 1),]],
  [party_tpl|pt_bandits_awaiting_ransom_r,"start", [(quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 1),],
   "You came back?\
 Quick, give us the money now.", "bandits_awaiting_ransom_intro_1",[]],
   [party_tpl|pt_bandits_awaiting_ransom_e,"start", [(quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 0),],
 "Are you the one that brought the ransom?\
 Quick, give us the money now.", "bandits_awaiting_ransom_intro_1",[(quest_set_slot, "qst_kidnapped_girl", slot_quest_current_state, 1),]],
  [party_tpl|pt_bandits_awaiting_ransom_e,"start", [(quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 1),],
   "You came back?\
 Quick, give us the money now.", "bandits_awaiting_ransom_intro_1",[]],
 ##Floris MTT end
 
  [anyone|plyr, "bandits_awaiting_ransom_intro_1", [(store_troop_gold, ":cur_gold"), ##Floris MTT - was party_tpl|pt_bandits_awaiting_ransom
                                                                                  (quest_get_slot, ":quest_target_amount", "qst_kidnapped_girl", slot_quest_target_amount),
                                                                                  (ge, ":cur_gold", ":quest_target_amount")
                                                                                  ],
   "Here, take the money. Just set the girl free.", "bandits_awaiting_ransom_pay",[]],
  [anyone, "bandits_awaiting_ransom_pay", [], ##Floris MTT - was party_tpl|pt_bandits_awaiting_ransom
   "Heh. You've brought the money all right.\
 You can take the girl now.\
 It was a pleasure doing business with you...", "close_window",
   [(quest_get_slot, ":quest_target_amount", "qst_kidnapped_girl", slot_quest_target_amount),
    (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party),
    (quest_get_slot, ":quest_target_center", "qst_kidnapped_girl", slot_quest_target_center),
    (troop_remove_gold, "trp_player", ":quest_target_amount"),
    (remove_member_from_party, "trp_kidnapped_girl", ":quest_target_party"),
    (set_spawn_radius, 1),
    (spawn_around_party, ":quest_target_party", "pt_kidnapped_girl"),
    (assign, ":girl_party", reg0),
    (party_set_ai_behavior, ":girl_party", ai_bhvr_hold),
    (party_set_flags, ":girl_party", pf_default_behavior, 0),
    (quest_set_slot, "qst_kidnapped_girl", slot_quest_current_state, 2),
    (party_set_ai_behavior, ":quest_target_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, ":quest_target_party", ":quest_target_center"),
    (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
    (add_gold_to_party, ":quest_target_amount", ":quest_target_party"),
    (assign, "$g_leave_encounter",1),
    ]],

  [anyone|plyr, "bandits_awaiting_ransom_intro_1", [],
   "No way! You release the girl first.", "bandits_awaiting_ransom_b",[]],
  [anyone, "bandits_awaiting_ransom_b", [],
   "You fool! Stop playing games and give us the money! ", "bandits_awaiting_ransom_b2",[]],
  [anyone|plyr, "bandits_awaiting_ransom_b2", [(store_troop_gold, ":cur_gold"),
                                               (quest_get_slot, ":quest_target_amount", "qst_kidnapped_girl", slot_quest_target_amount),
                                               (ge, ":cur_gold", ":quest_target_amount")],
   "All right. Here's your money. Let the girl go now.", "bandits_awaiting_ransom_pay",[]],
  [anyone|plyr, "bandits_awaiting_ransom_b2", [],
   "I had left the money in a safe place. Let me go fetch it.", "bandits_awaiting_ransom_no_money",[]],
  [anyone, "bandits_awaiting_ransom_no_money", [],
   "Are you testing our patience or something?  Go and bring that money here quickly.", "close_window",[(assign, "$g_leave_encounter",1)]],
  [anyone|plyr, "bandits_awaiting_ransom_b2", [],
   "I have no intention to pay you anything. I demand that you release the girl now!", "bandits_awaiting_ransom_fight",[]],
  [anyone, "bandits_awaiting_ransom_fight", [],
   "You won't be demanding anything when you're dead.", "close_window",[(encounter_attack),]],

  [party_tpl|pt_bandits_awaiting_ransom,"start", [(quest_slot_ge, "qst_kidnapped_girl", slot_quest_current_state, 2),],
   "What's it? You have given us the money. We have no more business.", "bandits_awaiting_remeet",[]], 
  ##Floris  MTT Begin
    [party_tpl|pt_bandits_awaiting_ransom_r,"start", [(quest_slot_ge, "qst_kidnapped_girl", slot_quest_current_state, 2),],
   "What's it? You have given us the money. We have no more business.", "bandits_awaiting_remeet",[]],
     [party_tpl|pt_bandits_awaiting_ransom_e,"start", [(quest_slot_ge, "qst_kidnapped_girl", slot_quest_current_state, 2),],
   "What's it? You have given us the money. We have no more business.", "bandits_awaiting_remeet",[]],
   ##Floris MTT End
  [anyone|plyr,"bandits_awaiting_remeet", [],
   "Sorry to bother you. I'll be on my way now.", "close_window",[(assign, "$g_leave_encounter",1)]],
  [anyone|plyr,"bandits_awaiting_remeet", [],
   "We have one more business. You'll give the money back to me.", "bandits_awaiting_remeet_2",[]],
  [anyone,"bandits_awaiting_remeet_2", [],
   "Oh, that business! Of course. Let us get down to it.", "close_window",[(encounter_attack)]],

  [party_tpl|pt_kidnapped_girl,"start", [],
   "Oh {sir/madam}. Thank you so much for rescuing me. Will you take me to my family now?", "kidnapped_girl_encounter_1",[]],
  [anyone|plyr,"kidnapped_girl_encounter_1", [], "Yes. Come with me. I'll take you home.", "kidnapped_girl_join",[]],
  [anyone,"kidnapped_girl_join", [(neg|party_can_join)], "Unfortunately you do not seem to have room for me.", "close_window",[(assign, "$g_leave_encounter",1)]],
  [anyone,"kidnapped_girl_join", [], "Oh, thank you so much!",
   "close_window",[(party_join),
                   (quest_set_slot, "qst_kidnapped_girl", slot_quest_current_state, 3),
                   (assign, "$g_leave_encounter",1)]],
  [anyone|plyr,"kidnapped_girl_encounter_1", [], "Wait here a while longer. I'll come back for you.", "kidnapped_girl_wait",[]],
  [anyone,"kidnapped_girl_wait", [], "Oh, please {sir/madam}, do not leave me here all alone!", "close_window",[(assign, "$g_leave_encounter",1)]],

  [anyone|plyr,"merchant_quest_about_job_2", [(store_partner_quest, ":partner_quest"),
                                              (eq, ":partner_quest", "qst_kidnapped_girl"),
                                              (quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 3),
                                              (neg|main_party_has_troop, "trp_kidnapped_girl")],
   "Unfortunately I lost the girl on the way here...", "lost_kidnapped_girl",[]],
  [anyone,"lost_kidnapped_girl", [],
   "Oh no! How am I going to tell this to my friend?", "lost_kidnapped_girl_2",[]],
  [anyone|plyr,"lost_kidnapped_girl_2", [],
   "I'm sorry. I could do nothing about it.", "lost_kidnapped_girl_3",[]],
  [anyone,"lost_kidnapped_girl_3", [],
   "You let me down {playername}. I had trusted you.\
 I will let people know of your incompetence at this task.\
 Also, I want back that {reg8} denars I gave you as the ransom fee.", "lost_kidnapped_girl_4",
   [(quest_get_slot, reg8, "qst_kidnapped_girl", slot_quest_target_amount),
    (try_for_parties, ":cur_party"),
      (party_count_members_of_type, ":num_members", ":cur_party", "trp_kidnapped_girl"),
      (gt, ":num_members", 0),
      (party_remove_members, ":cur_party", "trp_kidnapped_girl", 1),
      (party_remove_prisoners, ":cur_party", "trp_kidnapped_girl", 1),
    (try_end),
    (call_script, "script_end_quest", "qst_kidnapped_girl"),
    (call_script, "script_change_troop_renown", "trp_player", -5),
    ]],
  [anyone|plyr, "lost_kidnapped_girl_4", [(store_troop_gold,":gold"),
                                          (quest_get_slot, ":quest_target_amount", "qst_kidnapped_girl", slot_quest_target_amount),
                                          (ge,":gold",":quest_target_amount"),
                                          ],
   "Of course. Here you are...", "merchant_quest_about_job_5a",[(quest_get_slot, ":quest_target_amount", "qst_kidnapped_girl", slot_quest_target_amount),
                                                                (troop_remove_gold, "trp_player",":quest_target_amount"),
                                                                ]],
  [anyone,"merchant_quest_about_job_5a", [],
   "At least you have the decency to return the money.", "close_window",[]],
  [anyone|plyr,"lost_kidnapped_girl_4", [],
   "Sorry. I don't have that amount with me.", "merchant_quest_about_job_5b",[]],
  [anyone,"merchant_quest_about_job_5b", [],
   "Do you expect me to believe that? You are going to pay that ransom fee back! Go and bring the money now!",
   "close_window",[(quest_get_slot, ":quest_target_amount", "qst_kidnapped_girl", slot_quest_target_amount),
                   (val_add, "$debt_to_merchants_guild", ":quest_target_amount"),
                   ]],


#  Give us the money now. Quick.
# Here, take the money. Just set the girl free.
# Heh, It was a pleasure doing business with you.

# You set the girl free first. You'll have the money afterwards.
# Stop playing games.

#persuade_lords_to_make_peace
  [anyone,"merchant_quest_requested", [(eq, "$random_merchant_quest_no", "qst_persuade_lords_to_make_peace"),
                                       (quest_get_slot, ":quest_target_faction", "qst_persuade_lords_to_make_peace", slot_quest_target_faction),
                                       (quest_get_slot, ":quest_object_troop", "qst_persuade_lords_to_make_peace", slot_quest_object_troop),
                                       (quest_get_slot, ":quest_target_troop", "qst_persuade_lords_to_make_peace", slot_quest_target_troop),
                                       (str_store_troop_name_link, s12, ":quest_object_troop"),
                                       (str_store_troop_name_link, s13, ":quest_target_troop"),
                                       (str_store_faction_name_link, s14, ":quest_target_faction"),
                                       (str_store_faction_name_link, s15, "$g_encountered_party_faction"),],
   "This war between {s15} and {s14} has brought our town to the verge of ruin.\
 Our caravans get raided before they can reach their destination.\
 Our merchants are afraid to leave the safety of the town walls.\
 And as if those aren't enough, the taxes to maintain the war take away the last bits of our savings.\
 If peace does not come soon, we can not hold on for much longer.", "merchant_quest_persuade_peace_1",
   []],

  [anyone|plyr,"merchant_quest_persuade_peace_1", [], "You are right. But who can stop this madness called war?", "merchant_quest_brief",[]],
  [anyone|plyr,"merchant_quest_persuade_peace_1", [], "It is your duty to help the nobles in their war effort. You shouldn't complain about it.", "merchant_quest_persuade_peace_reject",[]],

  [anyone,"merchant_quest_persuade_peace_reject", [], "Hah. The nobles fight their wars for their greed and their dreams of glory.\
 And it is poor honest folk like us who have to bear the real burden.\
 But you obviously don't want to hear about that.", "close_window",[]],

  [anyone,"merchant_quest_brief", [(eq,"$random_merchant_quest_no","qst_persuade_lords_to_make_peace"),
  ##diplomacy start+ gender correct
  (quest_get_slot, ":quest_object_troop", "qst_persuade_lords_to_make_peace", slot_quest_object_troop),
  (call_script, "script_dplmc_store_troop_is_female", ":quest_object_troop"),
  (try_begin),
     (eq, reg0, 0),
	  (quest_get_slot, ":quest_target_troop", "qst_persuade_lords_to_make_peace", slot_quest_target_troop),
	  (call_script, "script_dplmc_store_troop_is_female", ":quest_target_troop"),
  (try_end),
  #Avoid saying "men" if either/both are female
  ],
#   "There have been attempts to reconcile the two sides and reach a settlement.\
# However, there are powerful lords on both sides whose interests lie in continuing the war.\
# These men urge all others not to heed to the word of sensible men, but to keep fighting.\
# While these leaders remain influential, no peace settlement can be reached.", "merchant_quest_persuade_peace_3",[]],
   "There have been attempts to reconcile the two sides and reach a settlement.\
 However, there are powerful lords on both sides whose interests lie in continuing the war.\
 {reg0?They:These men} urge all others not to heed to the word of sensible men, but to keep fighting.\
 While these leaders remain influential, no peace settlement can be reached.", "merchant_quest_persuade_peace_3",[]],
##diplomacy end+

  [anyone|plyr,"merchant_quest_persuade_peace_3", [], "Who are these warmongers who block the way of peace?", "merchant_quest_persuade_peace_4",[]],
  [anyone|plyr,"merchant_quest_persuade_peace_3", [], "Who are these lords you speak of?", "merchant_quest_persuade_peace_4",[]],

  [anyone,"merchant_quest_persuade_peace_4", [], "They are {s12} from {s15} and {s13} from {s14}. Until they change their mind or lose their influence,\
 there will be no chance of having peace between the two sides.", "merchant_quest_persuade_peace_5",[
       (quest_get_slot, ":quest_target_faction", "qst_persuade_lords_to_make_peace", slot_quest_target_faction),
       (quest_get_slot, ":quest_object_troop", "qst_persuade_lords_to_make_peace", slot_quest_object_troop),
       (quest_get_slot, ":quest_target_troop", "qst_persuade_lords_to_make_peace", slot_quest_target_troop),
       (str_store_troop_name_link, s12, ":quest_object_troop"),
       (str_store_troop_name_link, s13, ":quest_target_troop"),
       (str_store_faction_name_link, s14, ":quest_target_faction"),
       (str_store_faction_name_link, s15, "$g_encountered_party_faction"),
     ]],

  [anyone|plyr,"merchant_quest_persuade_peace_5", [], "What can be done about this?", "merchant_quest_persuade_peace_6",[]],
  [anyone|plyr,"merchant_quest_persuade_peace_5", [], "Alas, it seems nothing can be done about it.", "merchant_quest_persuade_peace_6",[]],

  [anyone,"merchant_quest_persuade_peace_6", [], "There is a way to resolve the issue.\
 A particularly determined person can perhaps persuade one or both of these lords to accept making peace.\
 And even if that fails, it can be possible to see that these lords are defeated by force and taken prisoner.\
 If they are captive, they will lose their influence and they can no longer oppose a settlement... What do you think? Can you do it?",
   "merchant_quest_persuade_peace_7",[]],

  [anyone|plyr,"merchant_quest_persuade_peace_7", [], "It seems difficult. But I will try.", "merchant_quest_persuade_peace_8",[]],
  [anyone|plyr,"merchant_quest_persuade_peace_7", [], "If the price is right, I may.", "merchant_quest_persuade_peace_8",[]],
  [anyone|plyr,"merchant_quest_persuade_peace_7", [], "Forget it. This is not my problem.", "merchant_quest_persuade_peace_8",[]],

  [anyone,"merchant_quest_persuade_peace_8", [], "Most of the merchants in the town will gladly open up their purses to support such a plan.\
 I think we can collect {reg12} denars between ourselves.\
 We will be happy to reward you with that sum, if you can work this out.\
 Convince {s12} and {s13} to accept a peace settlement,\
 and if either of them proves too stubborn, make sure he falls captive and can not be ransomed until a peace deal is settled.",
   "merchant_quest_persuade_peace_9",[
       (quest_get_slot, ":quest_object_troop", "qst_persuade_lords_to_make_peace", slot_quest_object_troop),
       (quest_get_slot, ":quest_target_troop", "qst_persuade_lords_to_make_peace", slot_quest_target_troop),
       (str_store_troop_name_link, s12, ":quest_object_troop"),
       (str_store_troop_name_link, s13, ":quest_target_troop"),
       (quest_get_slot, ":quest_reward", "qst_persuade_lords_to_make_peace", slot_quest_gold_reward),
       (assign, reg12, ":quest_reward")]],

  [anyone|plyr,"merchant_quest_persuade_peace_9", [], "All right. I will do my best.", "merchant_quest_persuade_peace_10",[]],
  [anyone|plyr,"merchant_quest_persuade_peace_9", [], "Sorry. I can not do this.", "merchant_quest_persuade_peace_no",[]],

  [anyone,"merchant_quest_persuade_peace_10", [], "Excellent. You will have our blessings.\
 I hope you can deal with those two old goats.\
 We will be waiting and hoping for the good news.", "close_window",[
     (str_store_party_name_link, s4, "$g_encountered_party"),
     (quest_get_slot, ":quest_target_faction", "qst_persuade_lords_to_make_peace", slot_quest_target_faction),
     (quest_get_slot, ":quest_object_troop", "qst_persuade_lords_to_make_peace", slot_quest_object_troop),
     (quest_get_slot, ":quest_target_troop", "qst_persuade_lords_to_make_peace", slot_quest_target_troop),
     (quest_get_slot, ":quest_reward", "qst_persuade_lords_to_make_peace", slot_quest_gold_reward),
     (assign, reg12, ":quest_reward"),
     (str_store_troop_name_link, s12, ":quest_object_troop"),
     (str_store_troop_name_link, s13, ":quest_target_troop"),
     (str_store_faction_name_link, s14, ":quest_target_faction"),
     (str_store_faction_name_link, s15, "$g_encountered_party_faction"),
     (setup_quest_text,"qst_persuade_lords_to_make_peace"),
     (str_store_string, s2, "@Guildmaster of {s4} promised you {reg12} denars if you can make sure that\
 {s12} and {s13} no longer pose a threat to a peace settlement between {s15} and {s14}.\
 In order to do that, you must either convince them or make sure they fall captive and remain so until a peace agreement is made."),
     (call_script, "script_start_quest", "qst_persuade_lords_to_make_peace", "$g_talk_troop"),
     (quest_get_slot, ":quest_object_troop", "qst_persuade_lords_to_make_peace", slot_quest_object_troop),
     (quest_get_slot, ":quest_target_troop", "qst_persuade_lords_to_make_peace", slot_quest_target_troop),
     (call_script, "script_report_quest_troop_positions", "qst_persuade_lords_to_make_peace", ":quest_object_troop", 3),
     (call_script, "script_report_quest_troop_positions", "qst_persuade_lords_to_make_peace", ":quest_target_troop", 4),
     ]],

  [anyone,"merchant_quest_persuade_peace_no", [], "Don't say no right away. Think about this for some time.\
 If there is a {man/lady} who can manage to do this, it is you.",
   "close_window",[]],


#deal with night bandits
  [anyone,"merchant_quest_requested",
   [
     (eq, "$random_merchant_quest_no", "qst_deal_with_night_bandits"),
     ],
   "Do I indeed! There's a group of bandits infesting the town, and I'm at the end of my rope as to how to deal with them.\
 They've been ambushing and robbing townspeople under the cover of night,\
 and then fading away quick as lightning when the guards finally show up. We've not been able to catch a one of them.\
 They only attack lone people, never daring to show themselves when there's a group about.\
 I need someone who can take on these bandits alone and win. That seems to be the only way of bringing them to justice.\
 Are you up to the task?", "merchant_quest_deal_with_night_bandits",
   []],

  [anyone,"merchant_quest_brief",
   [
     (eq,"$random_merchant_quest_no","qst_deal_with_night_bandits"),
     ],
   "There's a group of bandits infesting the town, and I'm at the end of my rope as to how to deal with them.\
 They've been ambushing and robbing townspeople under the cover of night,\
 and then fading away quick as lightning when the guards finally show up. We've not been able to catch a one of them.\
 They only attack lone people, never daring to show themselves when there's a group about.\
 I need someone who can take on these bandits alone and win. That seems to be the only way of bringing them to justice.\
 Are you up to the task?", "merchant_quest_deal_with_night_bandits",
   []],

  [anyone|plyr,"merchant_quest_deal_with_night_bandits", [],
   "Killing bandits? Why, certainly!",
   "deal_with_night_bandits_quest_taken",
   [
     (str_store_party_name_link, s14, "$g_encountered_party"),
     (setup_quest_text, "qst_deal_with_night_bandits"),
     (str_store_string, s2, "@The Guildmaster of {s14} has asked you to deal with a group of bandits terrorising the streets of {s14}. They only come out at night, and only attack lone travellers on the streets."),
     (call_script, "script_start_quest", "qst_deal_with_night_bandits", "$g_talk_troop"),
     ]],

  [anyone|plyr, "merchant_quest_deal_with_night_bandits", [],
   "My apologies, I'm not interested.", "merchant_quest_stall",[]],

  [anyone,"deal_with_night_bandits_quest_taken", [], "That takes a weight off my shoulders, {playername}.\
 You can expect a fine reward if you come back successful. Just don't get yourself killed, eh?", "mayor_pretalk",[]],


#move cattle herd
  [anyone,"merchant_quest_requested", [(eq, "$random_merchant_quest_no", "qst_move_cattle_herd"),
                                       (quest_get_slot, ":target_center", "qst_move_cattle_herd", slot_quest_target_center),
                                       (str_store_party_name,s13,":target_center"),],
   "One of the merchants here is looking for herdsmen to take his cattle to the market at {s13}.", "merchant_quest_brief",
   []],

  [anyone,"merchant_quest_brief",
   [
    (eq,"$random_merchant_quest_no","qst_move_cattle_herd"),
    (quest_get_slot, reg8, "qst_move_cattle_herd", slot_quest_gold_reward),
    (quest_get_slot, ":target_center", "qst_move_cattle_herd", slot_quest_target_center),
    (str_store_party_name, s13, ":target_center"),
    ],
   "The cattle herd must be at {s13} within 30 days. Sooner is better, much better,\
 but it must be absolutely no later than 30 days.\
 If you can do that, I'd be willing to pay you {reg8} denars for your trouble. Interested?", "move_cattle_herd_quest_brief",
   []],

  [anyone|plyr,"move_cattle_herd_quest_brief", [],  "Aye, I can take the herd to {s13}.",
   "move_cattle_herd_quest_taken",
   [
     (call_script, "script_create_cattle_herd", "$g_encountered_party", 0),
     (quest_set_slot, "qst_move_cattle_herd", slot_quest_target_party, reg0),
     (str_store_party_name_link, s10,"$g_encountered_party"),
     (quest_get_slot, ":target_center", "qst_move_cattle_herd", slot_quest_target_center),
     (str_store_party_name_link, s13, ":target_center"),
     (quest_get_slot, reg8, "qst_move_cattle_herd", slot_quest_gold_reward),
     (setup_quest_text, "qst_move_cattle_herd"),
     (str_store_string, s2, "@Guildmaster of {s10} asked you to move a cattle herd to {s13}. You will earn {reg8} denars in return."),
     (call_script, "script_start_quest", "qst_move_cattle_herd", "$g_talk_troop"),
     ]],
  [anyone|plyr,"move_cattle_herd_quest_brief", [],
   "I am sorry, but no.", "merchant_quest_stall",[]],

  [anyone,"move_cattle_herd_quest_taken", [], "Splendid. You can find the herd right outside the town.\
 After you take the animals to {s13}, return back to me and I will give you your pay.", "mayor_pretalk",[]],


#################################################
#################### Random merchant quests end

  [anyone,"merchant_quest_requested", [], "I am afraid I can't offer you a job right now.", "mayor_pretalk",[]],


#Village elders

  [anyone,"start", [(is_between,"$g_talk_troop",village_elders_begin,village_elders_end),
                    (store_partner_quest,":elder_quest"),
                    (eq,":elder_quest","qst_deliver_cattle"),
                    (check_quest_succeeded, ":elder_quest"),
                    (quest_get_slot, reg5, "qst_deliver_cattle", slot_quest_target_amount)],
   "My good {sir/madam}. Our village is grateful for your help. Thanks to the {reg5} heads of cattle you have brought, we can now raise our own herd.", "village_elder_deliver_cattle_thank",
   [(add_xp_as_reward, 400),
#    (quest_get_slot, ":num_cattle", "qst_deliver_cattle", slot_quest_target_amount),
#    (party_set_slot, "$current_town", slot_village_number_of_cattle, ":num_cattle"),
    (call_script, "script_change_center_prosperity", "$current_town", 4),
    (call_script, "script_change_player_relation_with_center", "$current_town", 5),
    (call_script, "script_end_quest", "qst_deliver_cattle"),
#Troop commentaries begin
    (call_script, "script_add_log_entry", logent_helped_peasants, "trp_player",  "$current_town", -1, -1),
#Troop commentaries end

    ]],

  [anyone,"village_elder_deliver_cattle_thank", [],
   "My good {lord/lady}, please, is there anything I can do for you?", "village_elder_talk",[]],


##  [anyone,"start",
##   [
##     (is_between, "$g_talk_troop", village_elders_begin, village_elders_end),
##     (store_partner_quest, ":elder_quest"),
##     (eq, ":elder_quest", "qst_train_peasants_against_bandits"),
##     (check_quest_succeeded, ":elder_quest"),
##     (quest_get_slot, reg5, "qst_train_peasants_against_bandits", slot_quest_target_amount)],
##   "Oh, thank you so much for training our men. Now we may stand a chance against those accursed bandits if they come again.", "village_elder_train_peasants_against_bandits_thank",
##   [
##     (add_xp_as_reward, 400),
##     (call_script, "script_change_player_relation_with_center", "$current_town", 5),
##     (call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
##     (call_script, "script_add_log_entry", logent_helped_peasants, "trp_player",  "$current_town", -1, -1),
##    ]],

#  [anyone,"village_elder_train_peasants_against_bandits_thank", [],
#   "Now, good {sire/lady}, is there anything I can do for you?", "village_elder_talk",[]],


##diplomacy start+
##
#Move this village_elder_talk line below, otherwise it wouldn't be able to trigger.
#  [anyone,"start", [(is_between,"$g_talk_troop", village_elders_begin, village_elders_end),(eq,"$g_talk_troop_met",0),
#                    (str_store_party_name, s9, "$current_town")],
#   "Good day, {sir/madam}, and welcome to {s9}. I am the elder of this village.", "village_elder_talk",[]],
##diplomacy end+

  [anyone,"start", [(is_between,"$g_talk_troop", village_elders_begin, village_elders_end),(eq,"$g_talk_troop_met",0),
                    (str_store_party_name, s9, "$current_town"),
                    (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
					##diplomacy start+
					#Replace "my {lord/lady}" with "your highness" if appropriate.
					(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
					(try_begin),
						#override default behavior to write "my {lord/lady}" if a less respectful form of address would have ben chosen
						(lt, reg0, 2),
						(str_store_string, s0, "str_dplmc_my_lordlady"),
					(try_end),
					],
   "Welcome to {s9}, {s0}. We were rejoiced by the news that you are the new {lord/lady} of our humble village.\
 I am the village elder and I will be honoured to serve you in any way I can.", "village_elder_talk",[]],#Replced "my {lord/lady}" with "{s0}"

##Moved this village_elder_talk line from above, otherwise it wouldn't be able to trigger.
  [anyone,"start", [(is_between,"$g_talk_troop", village_elders_begin, village_elders_end),(eq,"$g_talk_troop_met",0),
                    (str_store_party_name, s9, "$current_town"),
					(call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$current_town"),#added this line
					],
   "Good day, {s0}, and welcome to {s9}. I am the elder of this village.", "village_elder_talk",[]],#replaced {sir/madam} with {s0}

##Replace "My {lord/lady}" with "Your highness" if appropriate.
   [anyone ,"start", [(is_between,"$g_talk_troop",village_elders_begin,village_elders_end),
                     (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
					 #We aren't going to use the contents of {s0}, just checking the return value
					 (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
					 (ge, reg0, 3),#"your highness"
					 ],
   "Your highness, you honour our humble village with your presence.", "village_elder_talk",[]],
  ##diplomacy end+

  [anyone ,"start", [(is_between,"$g_talk_troop",village_elders_begin,village_elders_end),
                     (party_slot_eq, "$current_town", slot_town_lord, "trp_player")],
   "{My lord/My lady}, you honour our humble village with your presence.", "village_elder_talk",[]],

  [anyone ,"start", [(is_between,"$g_talk_troop",village_elders_begin,village_elders_end),
  ##diplomacy start+
  (call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$current_town"),
  ],
   "Good day, {s0}.", "village_elder_talk",[]],#replaced {sir/madam} with {s0}
  ##diplomacy end+

  [anyone ,"village_elder_pretalk", [],
   "Is there anything else I can do for you?", "village_elder_talk",[]],

  [anyone|plyr,"village_elder_talk", [(check_quest_active, "qst_hunt_down_fugitive"),
                                      (neg|check_quest_concluded, "qst_hunt_down_fugitive"),
                                      (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
                                      (quest_get_slot, ":quest_target_dna", "qst_hunt_down_fugitive", slot_quest_target_dna),
                                      (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
                                      (str_store_string, s4, s50),
                                      ],
   "I am looking for a man by the name of {s4}. I was told he may be hiding here.", "village_elder_ask_fugitive",[]],

  [anyone ,"village_elder_ask_fugitive", [
  ##diplomacy start+
   (call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$current_town"),#added (used in next two)
   (is_currently_night),
   ],
   "Strangers come and go to our village, {s0}. But I doubt you'll run into him at this hour of the night. You would have better luck during the day.", "village_elder_pretalk",[]],#changed {sir/madam} to {s0}
  [anyone ,"village_elder_ask_fugitive", [],
   "Strangers come and go to our village, {s0}. If he is hiding here, you will surely find him if you look around.", "close_window",[]],#changed {sir/madam} to {s0}
  ##diplomacy end+

  [anyone|plyr,"village_elder_talk", [(store_partner_quest,":elder_quest"),(ge,":elder_quest",0)],
   "About the task you asked of me...", "village_elder_active_mission_1",[]],

  [anyone|plyr,"village_elder_talk", [(ge, "$g_talk_troop_faction_relation", 0),(store_partner_quest,":elder_quest"),(lt,":elder_quest",0)],
   "Do you have any tasks I can help you with?", "village_elder_request_mission_ask",[]],

  [anyone|plyr,"village_elder_talk", [(party_slot_eq, "$current_town", slot_village_state, 0),
                                      (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),],
   "I want to buy some supplies. I will pay with gold.", "village_elder_trade_begin",[]],


  [anyone ,"village_elder_trade_begin", [], "Of course, {sir/madam}. Do you want to buy goods or cattle?", "village_elder_trade_talk",[]],

  [anyone|plyr,"village_elder_trade_talk", [], "I want to buy food and supplies.", "village_elder_trade",[]],

  [anyone ,"village_elder_trade", [],
   "We have some food and other supplies in our storehouse. Come have a look.", "village_elder_pretalk",[(change_screen_trade, "$g_talk_troop"),]],

  [anyone|plyr,"village_elder_trade_talk", [(party_slot_eq, "$current_town", slot_village_state, 0),
                                      (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                                      (assign, ":quest_village", 0),
                                      (try_begin),
                                        (check_quest_active, "qst_deliver_cattle"),
                                        (quest_slot_eq, "qst_deliver_cattle", slot_quest_target_center, "$current_town"),
                                        (assign, ":quest_village", 1),
                                      (try_end),
                                      (eq, ":quest_village", 0),
                                      ],
   "I want to buy some cattle.", "village_elder_buy_cattle",[]],

  [anyone|plyr,"village_elder_trade_talk", [], "I changed my mind. I don't need to buy anything.", "village_elder_pretalk",[]],

  [anyone|plyr,"village_elder_talk",
   [
     ],
   "Have you seen any enemies around here recently?", "village_elder_ask_enemies",[]],

  [anyone,"village_elder_ask_enemies",
   [
     (assign, ":give_report", 0),
     (party_get_slot, ":original_faction", "$g_encountered_party", slot_center_original_faction),
     (store_relation, ":original_faction_relation", ":original_faction", "fac_player_supporters_faction"),
     (try_begin),
       (gt, ":original_faction_relation", 0),
       (party_slot_ge, "$g_encountered_party", slot_center_player_relation, 0),
       (assign, ":give_report", 1),
     (else_try),
       (party_slot_ge, "$g_encountered_party", slot_center_player_relation, 30),
       (assign, ":give_report", 1),
     (try_end),
     (eq, ":give_report", 0),
	 ##diplomacy start+
	 (call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$current_town"),#added
     ],
   "I am sorry, {s0}. We have neither seen nor heard of any war parties in this area.", "village_elder_pretalk",#replaced {sir/madam} with {s0}
   ##diplomacy end+
   []],

  [anyone,"village_elder_ask_enemies",
   [],
   "Hmm. Let me think about it...", "village_elder_tell_enemies",
   [
     (assign, "$temp", 0),
     ]],

  [anyone,"village_elder_tell_enemies",
   [
     (assign, ":target_hero_index", "$temp"),
     (assign, ":end_cond", active_npcs_end),
     (try_for_range, ":cur_troop", active_npcs_begin, ":end_cond"),
	   (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
       (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
       (gt, ":cur_party", 0),
       (store_troop_faction, ":cur_faction", ":cur_troop"),
       (store_relation, ":reln", ":cur_faction", "fac_player_supporters_faction"),
       (lt, ":reln", 0),
       (store_distance_to_party_from_party, ":dist", "$g_encountered_party", ":cur_party"),
       (lt, ":dist", 10),
       (call_script, "script_get_information_about_troops_position", ":cur_troop", 0),
       (eq, reg0, 1), #Troop's location is known.
       (val_sub, ":target_hero_index", 1),
       (lt, ":target_hero_index", 0),
       (assign, ":end_cond", 0),
       (str_store_string, s2, "@He is not commanding any men at the moment."),
       (assign, ":num_troops", 0),
       (assign, ":num_wounded_troops", 0),
       (party_get_num_companion_stacks, ":num_stacks", ":cur_party"),
       (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
         (party_stack_get_troop_id, ":stack_troop", ":cur_party", ":i_stack"),
         (neg|troop_is_hero, ":stack_troop"),
         (party_stack_get_size, ":stack_size", ":cur_party", ":i_stack"),
         (party_stack_get_num_wounded, ":num_wounded", ":cur_party", ":i_stack"),
         (val_add, ":num_troops", ":stack_size"),
         (val_add, ":num_wounded_troops", ":num_wounded"),
       (try_end),
       (gt, ":num_troops", 0),
       (call_script, "script_round_value", ":num_wounded_troops"),
       (assign, reg1, reg0),
       (call_script, "script_round_value", ":num_troops"),
       (str_store_string, s2, "@He currently commands {reg0} men{reg1?, of which around {reg1} are wounded:}."),
     (try_end),
     (eq, ":end_cond", 0),
     ],
   "{s1} {s2}", "village_elder_tell_enemies",
   [
     (val_add, "$temp", 1),
     ]],

  [anyone,"village_elder_tell_enemies",
  ##diplomacy start+
   [(eq, "$temp", 0),
   	(call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$current_town"),#added
   ],
   "No, {s0}. We haven't seen any war parties in this area for some time.", "village_elder_pretalk",#replaced {sir/madam} with {s0}
  ##diplomacy end+
   []],

  [anyone,"village_elder_tell_enemies",
   [],
   "Well, I guess that was all.", "village_elder_pretalk",
   []],





  #(fire set up dialogs begin) Asking village elder to set up fire for making prison break easier.
  [anyone|plyr,"village_elder_talk",
  [
    (party_get_slot, ":bound_center", "$current_town", slot_village_bound_center),

    (assign, ":num_heroes_in_dungeon", 0),
    (assign, ":num_heroes_given_parole", 0),

    (party_get_num_prisoner_stacks, ":num_stacks", ":bound_center"),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_prisoner_stack_get_troop_id, ":stack_troop",":bound_center",":i_stack"),
      (troop_is_hero, ":stack_troop"),
      (try_begin),
        (call_script, "script_cf_prisoner_offered_parole", ":stack_troop"),
        (party_add_members, "p_temp_party_2", ":stack_troop", 1),
        (val_add, ":num_heroes_given_parole", 1),
      (else_try),
        (party_add_members, "p_temp_party", ":stack_troop", 1),
        (val_add, ":num_heroes_in_dungeon", 1),
      (try_end),
    (try_end),

    (ge, ":num_heroes_in_dungeon", 1),
  ],
   "I need you to set a large fire on the outskirts of this village.", "village_elder_ask_set_fire",[]],

  [anyone,"village_elder_ask_set_fire",
   [
     ##diplomacy start+
	 (call_script, "script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", "$current_town"),#added (re-used several times below)
	 ##diplomacy end+
     (eq, "$g_village_elder_did_not_liked_money_offered", 0),
     (party_get_slot, ":bound_center", "$current_town", slot_village_bound_center),
     (party_get_slot, ":fire_time", ":bound_center", slot_town_last_nearby_fire_time),
     (store_current_hours, ":cur_time"),
     (ge, ":fire_time", ":cur_time"),
   ],
   ##diplomacy start+
   "We have already agreed upon this, {s0}. I will do my best. You can trust me.", "close_window",[]],#changed {sir/my lady} to {s0}
   ##diplomacy end+

  [anyone,"village_elder_ask_set_fire",
   [
     (eq, "$g_village_elder_did_not_liked_money_offered", 0),
   ],
   ##diplomacy start+
   "A fire, {s0}! Fires are dangerous! Why would you want such a thing?", "village_elder_ask_set_fire_1",[]],#changed {sir/madam} to {s0}
   ##diplomacy end+

  [anyone,"village_elder_ask_set_fire", #elder did not accepted 100 denars before
   [
     (eq, "$g_village_elder_did_not_liked_money_offered", 1),
   ],
   ##diplomacy start+
   "I believe that we have already discussed this issue, {s0}.", "village_elder_ask_set_fire_5",[]],#changed {sir/my lady} to {s0}
   ##diplomacy end+

  [anyone,"village_elder_ask_set_fire", #elder did not accepted 100 and 200 denars before
   [
     (eq, "$g_village_elder_did_not_liked_money_offered", 2),
   ],
   ##diplomacy start+
   #changed {sir/madam} to {s0}, and moved it to the other side of the word "before"
   "We talked about this before {s0} and your previous offers were low compared to risk you want me to take.",
   ##diplomacy end+
   "village_elder_ask_set_fire_5",[]],

  [anyone|plyr,"village_elder_ask_set_fire_1",[],
   "I have my reasons, and you will have yours -- a purse of silver. Will you do it, or not?", "village_elder_ask_set_fire_2",[]],

  [anyone|plyr,"village_elder_ask_set_fire_1",[],
  "Given the risk you are taking, you are entitled to know my plan.", "village_elder_ask_set_fire_explain_plan",[]],

  [anyone|plyr,"village_elder_ask_set_fire_explain_plan",[
  (party_get_slot, ":bound_center", "$g_encountered_party", slot_village_bound_center),
  (str_store_party_name, s4, ":bound_center"),
  ],
   "I wish to rescue a prisoner from {s4}. When you light the fire, the guards in {s4} will see the smoke, and some of them will rush outside to see what is going on. ", "village_elder_ask_set_fire_2",[]],


  [anyone,"village_elder_ask_set_fire_2",[
  (gt, "$g_talk_troop_effective_relation", 9),
  ],
##diplomacy start+ change {sir/my lady} to {s0}
   "As you wish, {s0}. You have been a good friend to this village, and, even though there is a risk, we should be glad to return the favor. When do you want this fire to start?", "village_elder_ask_set_fire_9",[]],
##diplomacy end+
   
  [anyone,"village_elder_ask_set_fire_2",[
  (lt, "$g_talk_troop_relation", 0),
  ],
##diplomacy start+ change {sir/my lady} to {s0}
   "I'm sorry, {s0}. You will forgive me for saying this, but we don't exactly have good reason to trust you. This is too dangerous.", "close_window",[]],
##diplomacy end+

  [anyone,"village_elder_ask_set_fire_2",[],
 ##diplomacy start+ change {sir/my lady} to {s0}
   "As you say, {s0}. But in doing this, we are taking a very great risk. What's in it for us?", "village_elder_ask_set_fire_3",[]],
##diplomacy end+

  [anyone|plyr,"village_elder_ask_set_fire_3",
  [
    (store_troop_gold, ":cur_gold", "trp_player"),
    (ge, ":cur_gold", 100),
  ],
   "I can give you 100 denars.", "village_elder_ask_set_fire_4",[(assign, "$g_last_money_offer_to_elder", 100),]],

  [anyone|plyr,"village_elder_ask_set_fire_3",
  [
    (store_troop_gold, ":cur_gold", "trp_player"),
    (ge, ":cur_gold", 200),
  ],
   "I can give you 200 denars.", "village_elder_ask_set_fire_6",[(assign, "$g_last_money_offer_to_elder", 200),]],

  [anyone|plyr,"village_elder_ask_set_fire_3",
  [
    (store_troop_gold, ":cur_gold", "trp_player"),
    (ge, ":cur_gold", 300),
  ],
   "I can give you 300 denars.", "village_elder_ask_set_fire_6",[(assign, "$g_last_money_offer_to_elder", 300),]],

  [anyone|plyr,"village_elder_ask_set_fire_3",[],
   "Never mind.", "close_window",[]],

  [anyone,"village_elder_ask_set_fire_4",
   [
     (eq, "$g_village_elder_did_not_liked_money_offered", 0),
   ],
   "This is madness. I cannot take such a risk.", "village_elder_talk",
   [
     (assign, "$g_village_elder_did_not_liked_money_offered", 1),
   ]],

  [anyone|plyr,"village_elder_ask_set_fire_5",
   [
     (eq, "$g_village_elder_did_not_liked_money_offered", 1),
     (store_troop_gold, ":cur_gold", "trp_player"),
     (ge, ":cur_gold", 200),
   ],
   "Then let's increase your reward to 200 denars.", "village_elder_ask_set_fire_7", [(assign, "$g_last_money_offer_to_elder", 200),]],

  [anyone|plyr,"village_elder_ask_set_fire_5",
   [
     (eq, "$g_village_elder_did_not_liked_money_offered", 1),
     (store_troop_gold, ":cur_gold", "trp_player"),
     (ge, ":cur_gold", 300),
   ],
   "Then let's increase your reward to 300 denars.", "village_elder_ask_set_fire_6",[(assign, "$g_last_money_offer_to_elder", 300),]],

  [anyone|plyr,"village_elder_ask_set_fire_5",
   [
     (eq, "$g_village_elder_did_not_liked_money_offered", 2),
     (store_troop_gold, ":cur_gold", "trp_player"),
     (ge, ":cur_gold", 300),
   ],
   "Then let's increase your reward to 300 denars. This is my last offer.", "village_elder_ask_set_fire_6",[(assign, "$g_last_money_offer_to_elder", 300),]],

  [anyone|plyr,"village_elder_ask_set_fire_5",[],
   "Never mind.", "close_window",[]],

  [anyone,"village_elder_ask_set_fire_6",[],
   "Very well. You are asking me to take a very great risk, but I will do it. When do you want this fire to start?", "village_elder_ask_set_fire_9",
   [
     (troop_remove_gold, "trp_player", "$g_last_money_offer_to_elder"),
   ]],

  [anyone,"village_elder_ask_set_fire_7",[],
   "I cannot do such a dangerous thing for 200 denars.", "village_elder_talk",
   [
     (assign, "$g_village_elder_did_not_liked_money_offered", 2),
   ]],

  [anyone|plyr,"village_elder_ask_set_fire_9",[],
   "Continue with your preparations. One hour from now, I need that fire.", "village_elder_ask_set_fire_10",
   [
     (party_get_slot, ":bound_center", "$current_town", slot_village_bound_center),
     (store_current_hours, ":cur_time"),
	 (val_add, ":cur_time", 1), ##CC 1.324
     (assign, ":fire_time", ":cur_time"),
     (party_set_slot, ":bound_center", slot_town_last_nearby_fire_time, ":fire_time"),
     (try_begin),
       (is_between, "$next_center_will_be_fired", villages_begin, villages_end),
       (party_get_slot, ":is_there_already_fire", "$next_center_will_be_fired", slot_village_smoke_added),
       (eq, ":is_there_already_fire", 0),
       (party_get_slot, ":fire_time", "$next_center_will_be_fired", slot_town_last_nearby_fire_time),
       (store_current_hours, ":cur_hours"),
       (store_sub, ":cur_time_sub_fire_duration", ":cur_hours", fire_duration),
       (val_sub, ":cur_time_sub_fire_duration", 1),
       (ge, ":fire_time", ":cur_time_sub_fire_duration"),
       (party_clear_particle_systems, "$next_center_will_be_fired"),
     (try_end),
     (assign, "$next_center_will_be_fired", "$current_town"),
     (assign, "$g_village_elder_did_not_liked_money_offered", 0),
   ]],

  [anyone|plyr,"village_elder_ask_set_fire_9",
   [
     (store_time_of_day, ":cur_day_hour"),
     (ge, ":cur_day_hour", 6),
     (lt, ":cur_day_hour", 23),
   ],
   "Do this in at the stroke of midnight. I will wait exactly one hour.", "village_elder_ask_set_fire_11",
   [
     (party_get_slot, ":bound_center", "$current_town", slot_village_bound_center),
     (store_time_of_day, ":cur_day_hour"),
     (store_current_hours, ":cur_time"),
     (store_sub, ":difference", 24, ":cur_day_hour"), #fire will be at 24 midnight today ##1.134
     (store_add, ":fire_time", ":cur_time", ":difference"),
     (party_set_slot, ":bound_center", slot_town_last_nearby_fire_time, ":fire_time"),
     (try_begin),
       (is_between, "$next_center_will_be_fired", villages_begin, villages_end),
       (party_get_slot, ":is_there_already_fire", "$next_center_will_be_fired", slot_village_smoke_added),
       (eq, ":is_there_already_fire", 0),
       (party_get_slot, ":fire_time", "$next_center_will_be_fired", slot_town_last_nearby_fire_time),
       (store_current_hours, ":cur_hours"),
       (store_sub, ":cur_time_sub_fire_duration", ":cur_hours", fire_duration),
       (val_sub, ":cur_time_sub_fire_duration", 1),
       (ge, ":fire_time", ":cur_time_sub_fire_duration"),
       (party_clear_particle_systems, "$next_center_will_be_fired"),
     (try_end),
     (assign, "$next_center_will_be_fired", "$current_town"),
     (assign, "$g_village_elder_did_not_liked_money_offered", 0),
    ]],

  [anyone,"village_elder_ask_set_fire_10",[],
   "Very well, {sir/my lady}. We will make our preparations. Now you make yours.", "close_window",
   [
   (assign, ":maximum_distance", -1),
   (try_for_agents, ":cur_agent"),
     (agent_get_troop_id, ":troop_id", ":cur_agent"),
     (is_between, ":troop_id", village_elders_begin, village_elders_end),
     (agent_get_position, pos0, ":cur_agent"),
     (try_for_range, ":entry_point_id", 0, 64),
       (entry_point_get_position, pos1, ":entry_point_id"),
       (get_distance_between_positions, ":dist", pos0, pos1),
       (gt, ":dist", ":maximum_distance"),
       (assign, ":maximum_distance", ":dist"),
       (copy_position, pos2, pos1),
       (assign, ":village_elder_agent", ":cur_agent"),
     (try_end),
     (try_begin),
       (gt, ":maximum_distance", -1),
       (agent_set_scripted_destination, ":village_elder_agent", pos2),
     (try_end),
   (try_end),
   ]],

  [anyone,"village_elder_ask_set_fire_11",[],
   "As you wish, {sir/my lady}. May the heavens protect you.", "close_window",[]],
  #(fire set up dialogs end)






  [anyone|plyr,"village_elder_talk", [(call_script, "script_cf_village_recruit_volunteers_cond"),],
   "Are there any lads from this village who might want to seek their fortune in the wars?", "village_elder_recruit_start",[]],

  [anyone|plyr,"village_elder_talk", [],
   "[Leave]", "close_window",[]],



  [anyone ,"village_elder_buy_cattle", [(party_get_slot, reg5, "$g_encountered_party", slot_village_number_of_cattle),
                                        (gt, reg5, 0),
                                        (store_item_value, ":cattle_cost", "itm_trade_cattle_meat"),
                                        (call_script, "script_game_get_item_buy_price_factor", "itm_trade_cattle_meat"),
                                        (val_mul, ":cattle_cost", reg0),
                                        #Multiplied by 2 and divided by 100
                                        (val_div, ":cattle_cost", 50),
                                        (assign, "$temp", ":cattle_cost"),
                                        (assign, reg6, ":cattle_cost"),
                                        ],
   "We have {reg5} heads of cattle, each for {reg6} denars. How many do you want to buy?", "village_elder_buy_cattle_2",[]],

  [anyone ,"village_elder_buy_cattle", [],
   "I am afraid we have no cattle left in the village {sir/madam}.", "village_elder_buy_cattle_2",[]],


  [anyone|plyr,"village_elder_buy_cattle_2", [(party_get_slot, ":num_cattle", "$g_encountered_party", slot_village_number_of_cattle),
                                              (ge, ":num_cattle", 1),
                                              (store_troop_gold, ":gold", "trp_player"),
                                              (ge, ":gold", "$temp"),],
   "One.", "village_elder_buy_cattle_complete",[(call_script, "script_buy_cattle_from_village", "$g_encountered_party", 1, "$temp"),
                                                       ]],

  [anyone|plyr,"village_elder_buy_cattle_2", [(party_get_slot, ":num_cattle", "$g_encountered_party", slot_village_number_of_cattle),
                                              (ge, ":num_cattle", 2),
                                              (store_troop_gold, ":gold", "trp_player"),
                                              (store_mul, ":cost", "$temp", 2),
                                              (ge, ":gold", ":cost"),],
   "Two.", "village_elder_buy_cattle_complete",[(call_script, "script_buy_cattle_from_village", "$g_encountered_party", 2, "$temp"),
                                                       ]],

  [anyone|plyr,"village_elder_buy_cattle_2", [(party_get_slot, ":num_cattle", "$g_encountered_party", slot_village_number_of_cattle),
                                              (ge, ":num_cattle", 3),
                                              (store_troop_gold, ":gold", "trp_player"),
                                              (store_mul, ":cost", "$temp", 3),
                                              (ge, ":gold", ":cost"),],
   "Three.", "village_elder_buy_cattle_complete",[(call_script, "script_buy_cattle_from_village", "$g_encountered_party", 3, "$temp"),
                                                       ]],

  [anyone|plyr,"village_elder_buy_cattle_2", [(party_get_slot, ":num_cattle", "$g_encountered_party", slot_village_number_of_cattle),
                                              (ge, ":num_cattle", 4),
                                              (store_troop_gold, ":gold", "trp_player"),
                                              (store_mul, ":cost", "$temp", 4),
                                              (ge, ":gold", ":cost"),],
   "Four.", "village_elder_buy_cattle_complete",[(call_script, "script_buy_cattle_from_village", "$g_encountered_party", 4, "$temp"),
                                                       ]],

  [anyone|plyr,"village_elder_buy_cattle_2", [(party_get_slot, ":num_cattle", "$g_encountered_party", slot_village_number_of_cattle),
                                              (ge, ":num_cattle", 5),
                                              (store_troop_gold, ":gold", "trp_player"),
                                              (store_mul, ":cost", "$temp", 5),
                                              (ge, ":gold", ":cost"),],
   "Five.", "village_elder_buy_cattle_complete",[(call_script, "script_buy_cattle_from_village", "$g_encountered_party", 5, "$temp"),
                                                       ]],

  [anyone|plyr,"village_elder_buy_cattle_2", [],
   "Forget it.", "village_elder_pretalk",[]],

  [anyone ,"village_elder_buy_cattle_complete", [],
   "I will tell the herders to round up the animals and bring them to you, {sir/madam}. I am sure you will be satisfied with your purchase.", "village_elder_pretalk",[]],


  [anyone ,"village_elder_recruit_start", [(party_get_slot, ":num_volunteers", "$current_town", slot_center_volunteer_troop_amount),
                                           (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
                                           (val_min, ":num_volunteers", ":free_capacity"),
                                           (store_troop_gold, ":gold", "trp_player"),
                                           (store_div, ":gold_capacity", ":gold", 10),#10 denars per man
                                           (val_min, ":num_volunteers", ":gold_capacity"),
                                           (le, ":num_volunteers", 0),
                                           ],
   "I don't think anyone would be interested, {sir/madam}. Is there anything else I can do for you?", "village_elder_talk",[]],

  [anyone ,"village_elder_recruit_start", [(party_get_slot, ":num_volunteers", "$current_town", slot_center_volunteer_troop_amount),
                                           (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
                                           (val_min, ":num_volunteers", ":free_capacity"),
                                           (store_troop_gold, ":gold", "trp_player"),
                                           (store_div, ":gold_capacity", ":gold", 10),#10 denars per man
                                           (val_min, ":num_volunteers", ":gold_capacity"),
                                           (assign, "$temp",  ":num_volunteers"),
                                           (assign, reg5, ":num_volunteers"),
                                           (store_add, reg7, ":num_volunteers", -1),
                                           ],
   "I can think of {reg5} whom I suspect would jump at the chance. If you could pay 10 denars {reg7?each for their equipment:for his equipment}.\
 Does that suit you?", "village_elder_recruit_decision",[]],

#not used:
##  [anyone|plyr,"village_elder_recruit_decision", [(party_get_slot, ":num_volunteers", "$current_town", slot_center_volunteer_troop_amount),
##                                                  (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
##                                                  (val_min, ":num_volunteers", ":free_capacity"),
##                                                  (store_troop_gold, ":gold", "trp_player"),
##                                                  (store_div, ":gold_capacity", ":gold", 10),#10 denars per man
##                                                  (val_min, ":num_volunteers", ":gold_capacity"),
##                                                  (eq, ":num_volunteers", 0),],
##   "So be it.", "village_elder_pretalk",
##   [
##     (try_begin),
##       (party_slot_eq, "$current_town", slot_center_volunteer_troop_amount, 0), #do not change the value if it is above 0
##       (party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
##     (try_end),]],

  [anyone|plyr,"village_elder_recruit_decision", [(assign, ":num_volunteers", "$temp"),
                                                  (ge, ":num_volunteers", 1),
                                                  (store_add, reg7, ":num_volunteers", -1)],
   "Tell {reg7?them:him} to make ready.", "village_elder_pretalk",[(call_script, "script_village_recruit_volunteers_recruit"),]],

  [anyone|plyr,"village_elder_recruit_decision", [(party_slot_ge, "$current_town", slot_center_volunteer_troop_amount, 1)],
   "No, not now.", "village_elder_pretalk",[]],

  [anyone,"village_elder_active_mission_1", [], "Yes {sir/madam}, have you made any progress on it?", "village_elder_active_mission_2",[]],

  [anyone|plyr,"village_elder_active_mission_2",[(store_partner_quest,":elder_quest"),
                                                 (eq, ":elder_quest", "qst_deliver_grain"),
                                                 (quest_get_slot, ":quest_target_amount", "qst_deliver_grain", slot_quest_target_amount),
                                                 (call_script, "script_get_troop_item_amount", "trp_player", "itm_trade_grain"),
                                                 (assign, ":cur_amount", reg0),
                                                 (ge, ":cur_amount", ":quest_target_amount"),
                                                 (assign, reg5, ":quest_target_amount"),
                                                 ],
   "Indeed. I brought you {reg5} packs of grain.", "village_elder_deliver_grain_thank",
   []],

  [anyone,"village_elder_deliver_grain_thank", [(str_store_party_name, s13, "$current_town")],
   "My good {lord/lady}. You have saved us from hunger and desperation. We cannot thank you enough, but you'll always be in our prayers.\
 The village of {s13} will not forget what you have done for us.", "village_elder_deliver_grain_thank_2",
   [(quest_get_slot, ":quest_target_amount", "qst_deliver_grain", slot_quest_target_amount),
#    (troop_remove_items, "trp_player", "itm_trade_grain", ":quest_target_amount"),
#    (add_xp_as_reward, 400),
#    (call_script, "script_change_center_prosperity", "$current_town", 4),
#    (call_script, "script_change_player_relation_with_center", "$current_town", 5),
########################################################################################################################
# LAV MODIFICATIONS START (TRADE GOODS MOD)
########################################################################################################################
    #(troop_remove_items, "trp_player", "itm_grain", ":quest_target_amount"),
    (troop_get_inventory_capacity, ":inv_size", "trp_player"),
    (assign, ":result_xp_reward", 300), # Was 400
    (assign, ":result_prosperity", 3),  # Was 4
    (assign, ":result_relation", 4),    # Was 5
    (try_for_range, ":i_slot", 0, ":inv_size"),
      (troop_get_inventory_slot, ":cur_item", "trp_player", ":i_slot"),
      (eq, ":cur_item", "itm_trade_grain"),
      (troop_get_inventory_slot_modifier, ":cur_modifier", "trp_player", ":i_slot"),
      (try_begin),
        (eq, ":cur_modifier", imod_large_bag), # These men are starving, they only care about quantity, so no bonus or penalty for quality
        (val_add, ":result_xp_reward", 50),
        (val_add, ":result_prosperity", 1),
        (val_add, ":result_relation", 1),
      (try_end),
      (troop_remove_item, "trp_player", "itm_trade_grain", 1), ##Floris 2.54 bugfix - missing the "trp_player" argument
      (val_sub, ":quest_target_amount", 1),
      (lt, ":quest_target_amount", 1),
      (assign, ":inv_size", 0), #break
    (try_end),
    (add_xp_as_reward, ":result_xp_reward"),
    (call_script, "script_change_center_prosperity", "$current_town", ":result_prosperity"),
    (call_script, "script_change_player_relation_with_center", "$current_town", ":result_relation"),
########################################################################################################################
# LAV MODIFICATIONS END (TRADE GOODS MOD)
########################################################################################################################
    (call_script, "script_end_quest", "qst_deliver_grain"),
#Troop commentaries begin
    (call_script, "script_add_log_entry", logent_helped_peasants, "trp_player",  "$current_town", -1, -1),
#Troop commentaries end
   ]],

  [anyone,"village_elder_deliver_grain_thank_2", [],
   "My good {lord/lady}, please, is there anything I can do for you?", "village_elder_talk",[]],


  [anyone|plyr,"village_elder_active_mission_2", [], "I am still working on it.", "village_elder_active_mission_3",[]],
  [anyone|plyr,"village_elder_active_mission_2", [], "I am afraid I won't be able to finish it.", "village_elder_mission_failed",[]],

  [anyone,"village_elder_active_mission_3",
  ##diplomacy start+ change to use script_dplmc_print_subordinate_says_sir_madame_to_s0
  #[], "Thank you, {sir/madam}. We are praying for your success everyday.", "village_elder_pretalk",[]],
  [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
  "Thank you, {s0}. We are praying for your success everyday.", "village_elder_pretalk",[]],
  ##diplomacy end+
  
  ##diplomacy start+ change to use script_dplmc_print_subordinate_says_sir_madame_to_s0
  [anyone,"village_elder_mission_failed", #[], "Ah, I am sorry to hear that {sir/madam}. I'll try to think of something else.",
  [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
  "Ah, I am sorry to hear that {s0}. I'll try to think of something else.",
  ##diplomacy end+
  "village_elder_pretalk",
   [(store_partner_quest,":elder_quest"),
    (call_script, "script_abort_quest", ":elder_quest", 1)]],
##
##  [anyone,"village_elder_generic_mission_thank", [],
##   "You have been so helpful {sir/madam}. I do not know how to thank you.", "village_elder_generic_mission_completed",[]],
##
##  [anyone|plyr,"village_elder_generic_mission_completed", [],
##   "Speak not of it. I only did what needed to be done.", "village_elder_pretalk",[]],

# Currently not needed.
##  [anyone|plyr,"village_elder_generic_mission_failed", [],
##   "TODO: I'm sorry I failed you sir. It won't happen again.", "village_elder_pretalk",
##   [(store_partner_quest,":elder_quest"),
##    (call_script, "script_finish_quest", ":elder_quest", 0),
##    ]],


  [anyone,"village_elder_request_mission_ask",
  ##diplomacy start+ change to use script_dplmc_print_subordinate_says_sir_madame_to_s0
  #[(store_partner_quest,":elder_quest"),(ge,":elder_quest",0)],
  [(store_partner_quest,":elder_quest"),
   (ge,":elder_quest",0),
   (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
  #"Well {sir/madam}, you are already engaged with a task helping us. We cannot ask more from you.", "village_elder_pretalk",[]],
  "Well {s0} you are already engaged with a task helping us. We cannot ask more from you.", "village_elder_pretalk",[]],
  ##diplomacy end+
  
  ##diplomacy start+ change to use script_dplmc_print_subordinate_says_sir_madame_to_s0
  [anyone,"village_elder_request_mission_ask", #[(troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 1)],
   [(troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 1),
    (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
   #"No {sir/madam}, We don't have any other tasks for you.", "village_elder_pretalk",[]],
   "No {s0}, We don't have any other tasks for you.", "village_elder_pretalk",[]],
   ##diplomacy end+

  [anyone|auto_proceed,"village_elder_request_mission_ask", [], "A task?", "village_elder_tell_mission",
   [
       (call_script, "script_get_quest", "$g_talk_troop"),
       (assign, "$random_quest_no", reg0),
   ]],


  [anyone,"village_elder_tell_mission", [(eq,"$random_quest_no","qst_deliver_grain")],
   "{My good sir/My good lady}, our village has been going through such hardships lately.\
 The harvest has been bad, and recently some merciless bandits took away our seed grain that we had reserved for the planting season.\
 If we cannot find some grain soon, we will not be able to plant our fields and then we will have nothing to eat for the coming year.\
 If you can help us, we would be indebted to you forever.", "village_elder_tell_deliver_grain_mission",
   [
     (quest_get_slot, ":quest_target_center", "$random_quest_no", slot_quest_target_center),
     (str_store_party_name_link,s3,":quest_target_center"),
     (quest_get_slot, reg5, "$random_quest_no", slot_quest_target_amount),
     (setup_quest_text,"$random_quest_no"),
     (str_store_string, s2, "@The elder of the village of {s3} asked you to bring them {reg5} packs of grain."),
   ]],

  [anyone|plyr,"village_elder_tell_deliver_grain_mission", [],
   "Hmmm. How much grain do you need?", "village_elder_tell_deliver_grain_mission_2",[]],
  [anyone|plyr,"village_elder_tell_deliver_grain_mission", [],
   "I can't be bothered with this. Ask help from someone else.", "village_elder_deliver_grain_mission_reject",[]],

  [anyone,"village_elder_tell_deliver_grain_mission_2", [(quest_get_slot, reg5, "$random_quest_no", slot_quest_target_amount)],
   "I think {reg5} packs of grain will let us start the planting. Hopefully, we can find charitable people to help us with the rest.", "village_elder_tell_deliver_grain_mission_3",[]],

  [anyone|plyr,"village_elder_tell_deliver_grain_mission_3", [],
   "Then I will go and find you the grain you need.", "village_elder_deliver_grain_mission_accept",[]],
  [anyone|plyr,"village_elder_tell_deliver_grain_mission_3", [],
   "I am afraid I don't have time for this. You'll need to find help elsewhere.", "village_elder_deliver_grain_mission_reject",[]],
  ##diplomacy start+ replace {sir/madam} with {my lord/my lady} or your highness if appropriate
  [anyone,"village_elder_deliver_grain_mission_accept", #[], "Thank you, {sir/madam}. We'll be praying for you night and day.", "close_window",
   [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
   "Thank you, {s0}. We'll be praying for you night and day.", "close_window",
  ##diplomacy end+
   [(assign, "$g_leave_encounter",1),
    (call_script, "script_change_player_relation_with_center", "$current_town", 5),
    (call_script, "script_start_quest", "$random_quest_no", "$g_talk_troop"),
    ]],

##diplomacy start+ replace {sir/madam} with {my lord/my lady} or your highness if appropriate
  [anyone,"village_elder_deliver_grain_mission_reject", #[], "Yes {sir/madam}, of course. I am sorry if I have bothered you with our troubles.", "close_window",
  [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "Yes {s0}, of course. I am sorry if I have bothered you with our troubles.", "close_window",
##diplomacy end+
   [(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 1),
    ]],



  [anyone,"village_elder_tell_mission", [(eq,"$random_quest_no", "qst_train_peasants_against_bandits")],
   "We are suffering greatly at the hands of a group of bandits. They take our food and livestock,\
 and kill anyone who doesn't obey them immediately. Our men are angry that we cannot defend ourselves, but we are only simple farmers...\
 However, with some help, I think that some of the people here could be more than that.\
 We just need an experienced warrior to teach us how to fight.",
   "village_elder_tell_train_peasants_against_bandits_mission",
   [
     (quest_get_slot, ":quest_target_center", "$random_quest_no", slot_quest_target_center),
     (str_store_party_name_link, s13, ":quest_target_center"),
     (quest_get_slot, reg5, "$random_quest_no", slot_quest_target_amount),
     (setup_quest_text, "$random_quest_no"),
     (str_store_string, s2, "@The elder of the village of {s13} asked you to train {reg5} peasants to fight against local bandits."),
   ]],

  [anyone|plyr, "village_elder_tell_train_peasants_against_bandits_mission", [],
   "I can teach you how to defend yourself.", "village_elder_train_peasants_against_bandits_mission_accept",[]],
  [anyone|plyr, "village_elder_tell_train_peasants_against_bandits_mission", [],
   "You peasants have no business taking up arms. Just pay the bandits and be off with it.", "village_elder_train_peasants_against_bandits_mission_reject",[]],

  ##diplomacy start+ replace {sir/madam} with {my lord/my lady} or your highness if appropriate
  [anyone,"village_elder_train_peasants_against_bandits_mission_accept",
   [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
   "You will? Oh, splendid! We would be deeply indebted to you, {s0}. I'll instruct the village folk to assemble here and receive your training. If you can teach us how to defend ourselves, I promise you'll receive everything we can give you in return for your efforts.", "close_window",
	##diplomacy end+
   [
     (assign, "$g_leave_encounter",1),
     #TODO: Change this value
     (call_script, "script_change_player_relation_with_center", "$current_town", 3),
     (call_script, "script_start_quest", "$random_quest_no", "$g_talk_troop"),
     ]],

##diplomacy start+ replace {sir/madam} with {my lord/my lady} or your highness if appropriate
  [anyone,"village_elder_train_peasants_against_bandits_mission_reject", #[], "Yes, of course {sir/madam}.\
  [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
  "Yes, of course {s0}.  Thank you for your counsel.", "close_window",
##diplomacy end+
   [
     (troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 1),
     ]],


  [anyone,"village_elder_tell_mission", [(eq,"$random_quest_no","qst_deliver_cattle")],
   "Bandits have driven away our cattle. Our pastures are empty. If we had just a few heads of cattle we could start to raise a herd again.",
   "village_elder_tell_deliver_cattle_mission",
   [
     (quest_get_slot, ":quest_target_center", "$random_quest_no", slot_quest_target_center),
     (str_store_party_name_link,s3,":quest_target_center"),
     (quest_get_slot, reg5, "$random_quest_no", slot_quest_target_amount),
     (setup_quest_text,"$random_quest_no"),
     (str_store_string, s2, "@The elder of the village of {s3} asked you to bring them {reg5} heads of cattle."),
   ]],

  [anyone|plyr,"village_elder_tell_deliver_cattle_mission", [],
   "How many animals do you need?", "village_elder_tell_deliver_cattle_mission_2",[]],
  [anyone|plyr,"village_elder_tell_deliver_cattle_mission", [],
   "I don't have time for this. Ask help from someone else.", "village_elder_deliver_cattle_mission_reject",[]],

  [anyone,"village_elder_tell_deliver_cattle_mission_2", [(quest_get_slot, reg5, "$random_quest_no", slot_quest_target_amount)],
   "I think {reg5} heads will suffice for a small herd.", "village_elder_tell_deliver_cattle_mission_3",[]],

  [anyone|plyr,"village_elder_tell_deliver_cattle_mission_3", [],
   "Then I will bring you the cattle you need.", "village_elder_deliver_cattle_mission_accept",[]],
  [anyone|plyr,"village_elder_tell_deliver_cattle_mission_3", [],
   "I am afraid I don't have time for this. You'll need to find help elsewhere.", "village_elder_deliver_cattle_mission_reject",[]],

  ##diplomacy start+ replace {sir/madam} with {my lord/my lady} or your highness if appropriate
  [anyone,"village_elder_deliver_cattle_mission_accept", [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "Thank you, {s0}. We'll be praying for you night and day.", "close_window",
  ##diplomacy end+
   [(assign, "$g_leave_encounter",1),
    (call_script, "script_change_player_relation_with_center", "$current_town", 3),
    (call_script, "script_start_quest", "$random_quest_no", "$g_talk_troop"),
    ]],

  ##diplomacy start+ replace {sir/madam} with {my lord/my lady} or your highness if appropriate
  [anyone,"village_elder_deliver_cattle_mission_reject", [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "Yes {s0}, of course. I am sorry if I have bothered you with our troubles.", "close_window",
  ##diplomacy end+
   [(troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 1),
    ]],

  #diplomacy start+ replace {sir/madam} with {my lord/my lady} or your highness if appropriate	
  [anyone,"village_elder_tell_mission", [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "Thank you, {s0}, but we do not really need anything right now.", "village_elder_pretalk",[]],
  #diplomacy end+

##  [anyone|plyr,"village_elder_mission_told", [], "TODO: As you wish sir. You can count on me.", "village_elder_mission_accepted",[]],
##  [anyone|plyr,"village_elder_mission_told", [], "TODO: I'm afraid I can't carry out this mission right now, sir.", "village_elder_mission_rejected",[]],
##
##  [anyone,"village_elder_mission_accepted", [], "TODO: Excellent. Do this {playername}. I really have high hopes for you.", "close_window",
##   [(assign, "$g_leave_encounter",1),
##    (try_begin),
##    #TODO: Add quest initializations here
##    (try_end),
##    (call_script, "script_start_quest", "$random_quest_no", "$g_talk_troop"),
##    ]],

##  [anyone,"village_elder_mission_rejected", [], "TODO: Is that so? Perhaps you are not up for the task anyway...", "close_window",
##   [(assign, "$g_leave_encounter",1),
##    (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -1),
##    (troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 1),
##    ]],




#Goods Merchants

  [anyone ,"start", [(is_between,"$g_talk_troop",goods_merchants_begin,goods_merchants_end),
                     (party_slot_eq, "$current_town", slot_town_lord, "trp_player")],
   "{My lord/my lady}, you honour my humble shop with your presence.", "goods_merchant_talk",[]],
  ##diplomacy start+ replace {sir/madam} with {my lord/my lady} or your highness if appropriate
  [anyone ,"start", [(is_between,"$g_talk_troop",goods_merchants_begin,goods_merchants_end),
			         (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
   "Welcome {s0}. What can I do for you?", "goods_merchant_talk",[]],
  ##diplomacy end+
#  [trp_salt_mine_merchant,"start", [], "Hello.", "goods_merchant_talk",[]],

#  [anyone,"merchant_begin", [], " What can I do for you?", "goods_merchant_talk",[]],

  [anyone,"goods_merchant_pretalk", [], "Anything else?", "goods_merchant_talk",[]],

  [anyone|plyr,"goods_merchant_talk", [], "I want to buy a few items... and perhaps sell some.", "goods_trade_requested",[]],
  [anyone,"goods_trade_requested", [], "Sure, sure... Here, have a look at my stock...", "goods_trade_completed",[[change_screen_trade]]],
  [anyone,"goods_trade_completed", [], "Anything else?", "goods_merchant_talk",[]],

  [anyone|plyr,"goods_merchant_talk", [], "What goods should I buy here to trade with other towns?", "trade_info_request",[]],

  [anyone|plyr,"goods_merchant_talk", [], "Nothing. Thanks.", "close_window",[]],

  [anyone,"trade_info_request", [], "That information can be best obtained from caravan masters\
 and travelling merchants. If you want I can send you to the district where foreign merchants stay at when they come to the town.\
 If you spend some time there and listen to the talk,\
 you can learn a lot about what to buy and where to sell it.", "trade_info_request_2",[]],

  [anyone|plyr,"trade_info_request_2", [], "Then I'll go and spend some time with these merchants.", "close_window",
   [
       (jump_to_menu,"mnu_town_trade_assessment_begin"),
       (finish_mission),
    ]],

  [anyone|plyr,"trade_info_request_2", [], "I have no time for this right now.", "goods_merchant_pretalk",[]],


#  [anyone|plyr,"goods_merchant_talk", [], "What do caravans buy and sell in this town?", "goods_merchant_town_info",[]],
#  [anyone,"goods_merchant_town_info_completed", [], "Anything else?", "goods_merchant_talk",[]],


##  [anyone,"goods_merchant_town_info", [],
##   "TODO: We produce {s1}, and we consume {s2}.", "goods_merchant_town_info_completed",
##   [(call_script, "script_print_productions_above_or_below_50", "$g_encountered_party", 1),
##    (str_store_string_reg, s1, s51),
##    (call_script, "script_print_productions_above_or_below_50", "$g_encountered_party", -1),
##    (str_store_string_reg, s2, s51)]],
##
##  [anyone,"goods_merchant_town_info", [(store_encountered_party,reg(1)),(eq,reg(1),"p_zendar")],
##"You can buy tools from here at a very good price.\
## The best place to sell them would be Tulga. Heard they pay quite well for tools over there.\
## And next time you come here bring some salt. I will pay well for salt.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [(store_encountered_party,reg(1)),(eq,reg(1),"p_town_1")],
##"Sargoth is famous for its fine linen. Many caravans come here to buy that.\
## I heard you can sell it at Halmar and make a nice profit.\
## And next time you come here bring some iron. I will pay well for iron.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_2"]],
##"I can sell you some smoked fish with a special price.\
## I heard that caravans take smoked fish to Uxkhal and make a good profit.\
## And next time you come here bring some wool. I will pay you well for wool.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_3"]],
##"I can sell you some wine with a special price.\
## I heard that caravans buy wine from here and sell it at Wercheg, making a good profit.\
## And next time you come here, bring some dried meat. I will pay you well for dried meat.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_4"]],
##"I have a stock of oil which I can sell you with a good price.\
## They say they offer a fortune for oil in Rivacheg, so maybe you can sell it there.\
## And next time you come here, bring some furs. I will pay you well for furs.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_5"]],
##"Jelkala is famous for its velvet. Many caravans come here to buy that.\
## They say merchants will buy it at insane prices in Reyvadin, so maybe you can take it there.\
## And next time you come here, bring some pottery. I will pay you well for pottery.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_6"]],
##"We produce some excellent ale here in Praven. Most caravans come here to buy that.\
## They say that the folks at Khudan will sell their right arms for ale, so maybe you can take it there.\
## And next time you come here, bring some spice. I have sold out my stock of spice and I will pay you well for it.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_7"]],
##"We produce mostly wheat here in Uxkhal. I would suggest you buy that.\
## I heard you can sell it with a good profit in Tulga, so maybe you can take it there.\
## And next time you come here, bring some smoked fish. I will pay you well for it.", "goods_merchant_town_info_completed",[]],
##
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_8"]],
##"Most caravans come to Reyvadin to buy wool.\
## I heard that they take it to Tihr where they pay well for wool.\
## And next time you come here, bring some velvet. I will buy it from you at a good price.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_9"]],
##"Most caravans come to Khudan to buy furs.\
## I heard that they take it to Suno where they pay well for it.\
## And next time you come here, bring some ale. I will buy it from you at a good price.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_10"]],
##"Most caravans come to Tulga to buy spice.\
## They say that in Praven they pay well for spice, so you may think of selling it to the mechants there.\
## And next time you come here, bring some wheat. I will buy it from you at a good price.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_11"]],
##"We mine a lot of iron here in Curaw. I would suggest you buy that.\
## I heard you can take it to Sargoth and sell it with a good profit.\
## And next time you come here, bring some dried meat. I will pay you well for it.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_12"]],
##"I can sell you some smoked fish with a special price.\
## I heard that caravans take smoked fish to Uxkhal and make a good profit.\
## And next time you come here bring some wine. I will pay you well for wine.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_13"]],
##"I have a stock of dried meat which I can sell you with a good price.\
## They say they pay very well for dried meat in Veluca, so maybe you can sell it there.\
## And next time you come here, bring some oil. I have sold out my stock of oil and I will pay you well for it.", "goods_merchant_town_info_completed",[]],
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_town_14"]],
##"We produce some good quality pottery here in Halmar. Most caravans come here to buy that.\
## I heard that caravans buy pottery from here and sell it at Jelkala, making a good profit.\
## And next time you come here, bring some linen. I have sold out my stock of linen and I will pay you well for it.", "goods_merchant_town_info_completed",[]],
##
##  [anyone,"goods_merchant_town_info", [[store_encountered_party,reg(1)],[eq,reg(1),"p_salt_mine"]],
##"Heh. Are you joking with me? This is the salt mine. Merchants come here to buy salt.", "goods_merchant_town_info_completed",[]],
##
##  [anyone,"goods_merchant_town_info", [
##                                       (store_encountered_party,reg(9)),
##                                       (party_get_slot,reg(5),reg(9),slot_town_export_good),
##                                       (party_get_slot,reg(6),reg(9),slot_town_import_good),
##                                       (ge,reg(5),1),
##                                       (ge,reg(6),1),
##                                       (str_store_item_name,1,reg(5)),
##                                       (str_store_item_name,2,reg(6)),
##                                       ],
##  "I can sell you some {s1} with a special price.\
##And next time you come here bring some {s2}. I will pay you well for that.", "goods_merchant_town_info_completed",[]],
##
##  [anyone,"goods_merchant_town_info", [
##                                       (store_encountered_party,reg(9)),
##                                       (party_get_slot,reg(5),reg(9),slot_town_export_good),
##                                       (ge,reg(5),1),
##                                       (str_store_item_name,1,reg(5)),
##                                       ],
##  "I can sell you some {s1} with a special price.", "goods_merchant_town_info_completed",[]],
##
##  [anyone,"goods_merchant_town_info", [
##                                       (store_encountered_party,reg(9)),
##                                       (party_get_slot,reg(6),reg(9),slot_town_import_good),
##                                       (ge,reg(6),1),
##                                       (str_store_item_name,2,reg(6)),
##                                       ],
##  "If you have some {s2} with you, I am ready to pay you good money for it.", "goods_merchant_town_info_completed",[]],
##
##  [anyone,"goods_merchant_town_info", [],
##"Sorry. Caravans hardly ever trade anything here.", "goods_merchant_town_info_completed",[]],






#############################################################################
#### ARENA MASTERS
#############################################################################
  [anyone ,"start", [(store_conversation_troop,reg(1)),
                     (is_between,reg(1),arena_masters_begin,arena_masters_end),
                     (assign, "$arena_reward_asked", 0), #set some variables.
                     (assign, "$arena_tournaments_asked", 0),
                     (eq,1,0),
                     ],
   "{!}.", "arena_intro_1",[]],
  [anyone ,"start", [(store_conversation_troop,reg(1)),
                     (is_between,reg(1),arena_masters_begin,arena_masters_end),
                     (eq,"$arena_master_first_talk", 0),
                     ],
   "Good day friend. If you came to watch the tournaments you came in vain. There won't be a tournament here anytime soon.", "arena_intro_1",[(assign,"$arena_master_first_talk", 1)]],
  [anyone|plyr,"arena_intro_1", [], "Tournaments? So they hold the tournaments here...", "arena_intro_2",[]],
  [anyone,"arena_intro_2", [], "Yes. You should see this place during one of the tournament fights.\
 Everyone from the town and nearby villages comes here. The crowd becomes mad with excitement.\
 Anyway, as I said, there won't be an event here soon, so there isn't much to see.\
 Except, there is an official duel every now and then, and  of course we have melee fights almost every day.", "arena_intro_3",[]],
  [anyone|plyr,"arena_intro_3", [], "Tell me about the melee fights.", "arena_training_melee_intro",[]],
  [anyone,"arena_training_melee_intro", [], "The fighters and knights get bored waiting for the next tournament,\
 so they have invented the training melee. It is a simple idea really.\
 Fighters jump into the arena with a weapon. There are no rules, no teams.\
 Everyone beats at each other until there is only one fighter left standing.\
 Sounds like fun, eh?", "arena_training_melee_intro_2",[]],
  [anyone|plyr,"arena_training_melee_intro_2", [(eq, "$arena_reward_asked", 0)], "Is there a reward?", "arena_training_melee_intro_reward",[(assign, "$arena_reward_asked", 1)]],
  [anyone,"arena_training_melee_intro_reward", [(assign, reg1, arena_tier1_opponents_to_beat),(assign, reg11, arena_tier1_prize),
      (assign, reg2, arena_tier2_opponents_to_beat),(assign, reg12, arena_tier2_prize),
      (assign, reg3, arena_tier3_opponents_to_beat),(assign, reg13, arena_tier3_prize),
      (assign, reg4, arena_tier4_opponents_to_beat),(assign, reg14, arena_tier4_prize),
      (assign, reg15, arena_grand_prize)
    ], "There is, actually. Some of the wealthy townsmen offer prizes for those fighters who show great skill in the fights.\
 If you can beat {reg1} opponents before going down, you'll earn {reg11} denars. You'll get {reg12} denars for striking down at least {reg2} opponents,\
 {reg13} denars if you can defeat {reg3} opponents, and {reg14} denars if you can survive long enough to beat {reg4} opponents.\
 If you can manage to be the last {man/fighter} standing, you'll earn the great prize of the fights, {reg15} denars. Sounds good, eh?", "arena_training_melee_intro_2",[(assign, "$arena_tournaments_asked", 1),]],
  [anyone,"arena_training_melee_explain_reward", [
      (assign, reg1, arena_tier1_opponents_to_beat),(assign, reg11, arena_tier1_prize),
      (assign, reg2, arena_tier2_opponents_to_beat),(assign, reg12, arena_tier2_prize),
      (assign, reg3, arena_tier3_opponents_to_beat),(assign, reg13, arena_tier3_prize),
      (assign, reg4, arena_tier4_opponents_to_beat),(assign, reg14, arena_tier4_prize),
      (assign, reg15, arena_grand_prize)
      ], "Some of the wealthy townsmen offer prizes for those fighters who show great skill in the fights.\
 If you can beat {reg1} opponents before going down, you'll earn {reg11} denars. You'll get {reg12} denars for striking down at least {reg2} opponents,\
 {reg13} denars if you can defeat {reg3} opponents, and {reg14} denars if you can survive long enough to beat {reg4} opponents.\
 If you can manage to be the last {man/fighter} standing, you'll earn the great prize of the fights, {reg15} denars. Sounds good, eh?", "arena_master_melee_pretalk",[]],
  [anyone|plyr,"arena_training_melee_intro_2", [], "Can I join too?", "arena_training_melee_intro_3",[]],
  [anyone,"arena_training_melee_intro_3", [], "Ha ha. You would have to be out of your mind not to. Of course. The melee fights are open to all.\
 Actually there is going to be a fight soon. You can go and hop in if you want to.", "arena_master_melee_talk",[]],


  [anyone ,"start", [(store_conversation_troop,reg(1)),
                     (is_between,reg(1),arena_masters_begin,arena_masters_end),
                     (eq,"$g_talk_troop_met", 0),
                     ],
   "Hello. You seem to be new here. Care to share your name?", "arena_master_intro_1",[]],
  [anyone|plyr,"arena_master_intro_1", [], "I am {playername}.", "arena_master_intro_2",[]],
  [anyone,"arena_master_intro_2", [(store_encountered_party,reg(2)),(str_store_party_name,1,reg(2))],
   "Well met {playername}. I am the master of the tournaments here at {s1}. Talk to me if you want to join the fights.", "arena_master_pre_talk",[]],


  [anyone|auto_proceed ,"start", [(store_conversation_troop,reg(1)),(is_between,reg(1),arena_masters_begin,arena_masters_end),
                     (eq, "$last_training_fight_town", "$current_town"),
                     (store_current_hours,":cur_hours"),
                     (val_add, ":cur_hours", -4),
                     (lt, ":cur_hours", "$training_fight_time")],
   ".", "arena_master_fight_result",[(assign, "$arena_reward_asked", 0)]],

  [anyone ,"arena_master_fight_result",
   [
     (eq, "$g_arena_training_won", 0),
     (eq, "$g_arena_training_kills", 0)
     ],
   "Ha-ha, that's quite the bruise you're sporting. But don't worry; everybody gets trounced once in awhile. The important thing is to pick yourself up, dust yourself off and keep fighting. That's what champions do.", "arena_master_pre_talk",[(assign, "$last_training_fight_town", -1)]],

  [anyone ,"arena_master_fight_result",
   [
     (eq, "$g_arena_training_won", 0),
     (lt, "$g_arena_training_kills", arena_tier1_opponents_to_beat),
     (assign, reg8, "$g_arena_training_kills")
     ],
   "Hey, you managed to take down {reg8} opponents. Not bad. But that won't bring you any prize money.\
 Now, if I were you, I would go back there and show everyone what I can do...", "arena_master_pre_talk",[(assign, "$last_training_fight_town", -1)]],

  [anyone ,"arena_master_fight_result",
   [
     (eq, "$g_arena_training_won", 0),
     (lt, "$g_arena_training_kills", arena_tier2_opponents_to_beat),
     (assign, reg8, "$g_arena_training_kills"),
     (assign, reg10, arena_tier1_prize),
     ],
   "You put up quite a good fight there. Good moves. You definitely show promise.\
 And you earned a prize of {reg10} denars for knocking down {reg8} opponents.", "arena_master_pre_talk",[
     (call_script, "script_troop_add_gold", "trp_player", arena_tier1_prize),
     (add_xp_to_troop,5,"trp_player"),
     (assign, "$last_training_fight_town", -1)]],

  [anyone ,"arena_master_fight_result",
   [
     (eq, "$g_arena_training_won", 0),
     (lt, "$g_arena_training_kills", arena_tier3_opponents_to_beat),
     (assign, reg8, "$g_arena_training_kills"),
     (assign, reg10, arena_tier2_prize),
     (assign, reg12, arena_tier2_opponents_to_beat),
     ],
   "That was a good fight you put up there. You managed to take down no less than {reg8} opponents.\
 And of course, you earned a prize money of {reg10} denars.", "arena_master_pre_talk",[
     (call_script, "script_troop_add_gold", "trp_player", arena_tier2_prize),
     (add_xp_to_troop,10,"trp_player"),
     (assign, "$last_training_fight_town", -1)]],

  [anyone ,"arena_master_fight_result",
   [
     (eq, "$g_arena_training_won", 0),
     (lt, "$g_arena_training_kills", arena_tier4_opponents_to_beat),
     (assign, reg8, "$g_arena_training_kills"),
     (assign, reg10, arena_tier3_prize)
     ],
   "Your performance was amazing! You are without doubt a very skilled fighter.\
 Not everyone can knock down {reg8} people in the fights. Of course you deserve a prize with that performance: {reg10} denars. Nice, eh?", "arena_master_pre_talk",[
     (call_script, "script_troop_add_gold", "trp_player", arena_tier3_prize),
     (add_xp_to_troop,10,"trp_player"),
     (assign, "$last_training_fight_town", -1)]],

  [anyone ,"arena_master_fight_result",
   [
     (eq, "$g_arena_training_won", 0),
     (assign, reg8, "$g_arena_training_kills"),
     (assign, reg10, arena_tier4_prize),
     ],
   "That was damned good fighting, {playername}. You have very good moves, excellent tactics.\
 And you earned a prize of {reg10} denars for knocking down {reg8} opponents.", "arena_master_pre_talk",
   [
     (call_script, "script_troop_add_gold", "trp_player", arena_tier4_prize),
     (add_xp_to_troop,10,"trp_player"),
     (assign, "$last_training_fight_town", -1),
     ]],

  [anyone ,"arena_master_fight_result", [(assign, reg10, arena_grand_prize)],
   "Congratulations champion! Your fight there was something to remember! You managed to be the last fighter standing beating down everyone else. And of course you won the grand prize of the fights: {reg10} denars.", "arena_master_pre_talk",[
     (call_script, "script_troop_add_gold", "trp_player", arena_grand_prize),
     (add_xp_to_troop,200,"trp_player"),
     (assign, "$last_training_fight_town", -1)]],


  [anyone ,"start", [(store_conversation_troop,reg(1)),(is_between,reg(1),arena_masters_begin,arena_masters_end)],
   "Hello {playername}. Good to see you again.", "arena_master_pre_talk",[(assign, "$arena_reward_asked", 0)]],


  [anyone,"arena_master_pre_talk", [], "What would you like to do?", "arena_master_talk",[]],


#  [anyone|plyr,"arena_master_talk", [], "About the arena fights...", "arena_master_melee",[]],
  [anyone|plyr,"arena_master_talk", [], "About the melee fights...", "arena_master_melee_pretalk",[]],
  #LAZERAS MODIFIED  {spar troops}
  [anyone|plyr,"arena_master_talk", [(party_get_num_companions,":troops","p_main_party"),(gt,":troops",1)], "I would like to spar with some of my men.", "arena_master_spar_teams",[]], # Jinnai
  #LAZERAS MODIFIED  {spar troops} 
  [anyone|plyr,"arena_master_talk", [(eq, "$arena_tournaments_asked", 0)], "Will there be a tournament in nearby towns soon?", "arena_master_ask_tournaments",[(assign, "$arena_tournaments_asked", 1)]],
  [anyone|plyr,"arena_master_talk", [], "I need to leave now. Good bye.", "close_window",[]],
#LAZERAS MODIFIED  {spar troops}
## Arena sparring begin - Jinnai
  [anyone,"arena_master_spar_teams", [], "Certainly. The arena is currently available. Of course, you will have to supply your own gear, which means there will be no team uniforms.  But that aside, how many teams would you like?",
     "arena_master_spar_teams_choose",[(try_for_range,":slot",1,33),(troop_set_slot, "trp_temp_array_a", ":slot", -1),(try_end),(troop_set_slot, "trp_temp_array_a", 1, "trp_player"),(assign,"$temp",1)]],
  [anyone|plyr,"arena_master_spar_teams_choose", [], "Two.", "arena_master_spar_team_one",[(assign, "$g_tournament_next_num_teams", 2),]],
  [anyone|plyr,"arena_master_spar_teams_choose", [(party_get_num_companions,":troops","p_main_party"),(gt,":troops",2)], "Three.", "arena_master_spar_team_one",[(assign, "$g_tournament_next_num_teams", 3),]],
  [anyone|plyr,"arena_master_spar_teams_choose", [(party_get_num_companions,":troops","p_main_party"),(gt,":troops",3)], "Four.", "arena_master_spar_team_one",[(assign, "$g_tournament_next_num_teams", 4),]],
  [anyone|plyr,"arena_master_spar_teams_choose", [], "Never mind. I've changed my mind.", "arena_master_pre_talk",[]],
  [anyone,"arena_master_spar_team_one", [(eq,"$temp",8)], "Team One is full. Team Two is next.", "arena_master_spar_team_two",[(assign,"$temp",0)]],
  [anyone,"arena_master_spar_team_one", [(assign,reg0,"$temp"),(store_sub,reg1,reg0,1)], "There {reg1?are:is} currently {reg0} {reg1?troops:troop} on Team One.  Which troop would you like to add?", "arena_master_spar_team_one_choose",[]],
  [anyone|plyr|repeat_for_troops, "arena_master_spar_team_one_choose",
   [
     (store_repeat_object, ":troop"),
     (party_get_num_companion_stacks,":num_stacks","p_main_party"),
     (assign,":include",0),
     (try_for_range,":stack",0,":num_stacks"),
       (eq,":include",0),
       (party_stack_get_troop_id,":troop_id","p_main_party",":stack"),
       (ge,":troop_id",0),
       (eq,":troop_id",":troop"),
       (assign,":num_in",0),
       (try_for_range,":counting",1,33),
         (troop_get_slot,":already_in","trp_temp_array_a",":counting"),
         (eq,":already_in",":troop"),
         (val_add,":num_in",1),
       (try_end),
       (party_stack_get_size,":available","p_main_party",":stack"),
       (gt,":available",":num_in"),
       (assign,":include",1),
     (try_end),
     (eq,":include",1),
     (store_sub,reg0,":available",":num_in"),
     (str_store_troop_name,s11,":troop"),
     ],
   "{s11}. ({reg0} left.)", "arena_master_spar_team_one_add",
   [
     (store_repeat_object, "$temp_2"),
     (val_add,"$temp",1),
     (store_add,":offset","$temp",0),
     (troop_set_slot, "trp_temp_array_a", ":offset", "$temp_2"),
     (str_store_troop_name,s11,"$temp_2")
     ]],
  [anyone,"arena_master_spar_team_one_add", [], "{s11} has been added to Team One.", "arena_master_spar_team_one",[]],
  [anyone|plyr,"arena_master_spar_team_one_choose", [], "I am finished with Team One.  Let's move on to Team Two.", "arena_master_spar_team_two",[(assign,"$temp",0)]],
  [anyone|plyr,"arena_master_spar_team_one_choose", [], "Never mind. I'm calling the whole thing off.", "arena_master_pre_talk",[]],
  [anyone,"arena_master_spar_team_two", [(gt,"$g_tournament_next_num_teams",2),(eq,"$temp",8)], "Team Two is full. Team Three is next.", "arena_master_spar_team_three",[(assign,"$temp",0)]],
  [anyone,"arena_master_spar_team_two", [(eq,"$g_tournament_next_num_teams",2),(eq,"$temp",8)], "Team Two is full. Let the match begin!", "arena_master_spar_start_it_up",[]],
  [anyone,"arena_master_spar_team_two", [(assign,reg0,"$temp"),(store_sub,reg1,reg0,1)], "There {reg1?are:is} currently {reg0} {reg1?troops:troop} on Team Two.  Which troop would you like to add?", "arena_master_spar_team_two_choose",[]],
  [anyone|plyr|repeat_for_troops, "arena_master_spar_team_two_choose",
   [
     (store_repeat_object, ":troop"),
     (party_get_num_companion_stacks,":num_stacks","p_main_party"),
     (assign,":include",0),
     (try_for_range,":stack",0,":num_stacks"),
       (eq,":include",0),
       (party_stack_get_troop_id,":troop_id","p_main_party",":stack"),
       (ge,":troop_id",0),
       (eq,":troop_id",":troop"),
       (assign,":num_in",0),
       (try_for_range,":counting",1,33),
         (troop_get_slot,":already_in","trp_temp_array_a",":counting"),
         (eq,":already_in",":troop"),
         (val_add,":num_in",1),
       (try_end),
       (party_stack_get_size,":available","p_main_party",":stack"),
       (gt,":available",":num_in"),
       (assign,":include",1),
     (try_end),
     (eq,":include",1),
     (store_sub,reg0,":available",":num_in"),
     (str_store_troop_name,s11,":troop"),
     ],
   "{s11}. ({reg0} left.)", "arena_master_spar_team_two_add",
   [
     (store_repeat_object, "$temp_2"),
     (val_add,"$temp",1),
     (store_add,":offset","$temp",8),
     (troop_set_slot, "trp_temp_array_a", ":offset", "$temp_2"),
     (str_store_troop_name,s11,"$temp_2")
     ]],
  [anyone,"arena_master_spar_team_two_add", [], "{s11} has been added to Team Two.", "arena_master_spar_team_two",[]],
  [anyone|plyr,"arena_master_spar_team_two_choose", [(gt,"$g_tournament_next_num_teams",2)], "I am finished with Team Two.  Let's move on to Team Three.", "arena_master_spar_team_three",[(assign,"$temp",0)]],
  [anyone|plyr,"arena_master_spar_team_two_choose", [(eq,"$g_tournament_next_num_teams",2)], "I am finished with Team Two.  Let's begin the match.", "arena_master_spar_start_it_up",[]],
  [anyone|plyr,"arena_master_spar_team_two_choose", [], "Never mind. I'm calling the whole thing off.", "arena_master_pre_talk",[]],
  [anyone,"arena_master_spar_team_three", [(gt,"$g_tournament_next_num_teams",3),(eq,"$temp",8)], "Team Three is full. Team Four is next.", "arena_master_spar_team_four",[(assign,"$temp",0)]],
  [anyone,"arena_master_spar_team_three", [(eq,"$g_tournament_next_num_teams",3),(eq,"$temp",8)], "Team Three is full. Let the match begin!", "arena_master_spar_start_it_up",[]],
  [anyone,"arena_master_spar_team_three", [(assign,reg0,"$temp"),(store_sub,reg1,reg0,1)], "There {reg1?are:is} currently {reg0} {reg1?troops:troop} on Team Three.  Which troop would you like to add?", "arena_master_spar_team_three_choose",[]],
  [anyone|plyr|repeat_for_troops, "arena_master_spar_team_three_choose",
   [
     (store_repeat_object, ":troop"),
     (party_get_num_companion_stacks,":num_stacks","p_main_party"),
     (assign,":include",0),
     (try_for_range,":stack",0,":num_stacks"),
       (eq,":include",0),
       (party_stack_get_troop_id,":troop_id","p_main_party",":stack"),
       (ge,":troop_id",0),
       (eq,":troop_id",":troop"),
       (assign,":num_in",0),
       (try_for_range,":counting",1,33),
         (troop_get_slot,":already_in","trp_temp_array_a",":counting"),
         (eq,":already_in",":troop"),
         (val_add,":num_in",1),
       (try_end),
       (party_stack_get_size,":available","p_main_party",":stack"),
       (gt,":available",":num_in"),
       (assign,":include",1),
     (try_end),
     (eq,":include",1),
     (store_sub,reg0,":available",":num_in"),
     (str_store_troop_name,s11,":troop"),
     ],
   "{s11}. ({reg0} left.)", "arena_master_spar_team_three_add",
   [
     (store_repeat_object, "$temp_2"),
     (val_add,"$temp",1),
     (store_add,":offset","$temp",16),
     (troop_set_slot, "trp_temp_array_a", ":offset", "$temp_2"),
     (str_store_troop_name,s11,"$temp_2")
     ]],
  [anyone,"arena_master_spar_team_three_add", [], "{s11} has been added to Team Three.", "arena_master_spar_team_three",[]],
  [anyone|plyr,"arena_master_spar_team_three_choose", [(gt,"$g_tournament_next_num_teams",3)], "I am finished with Team Three.  Let's move on to Team Four.", "arena_master_spar_team_four",[(assign,"$temp",0)]],
  [anyone|plyr,"arena_master_spar_team_three_choose", [(eq,"$g_tournament_next_num_teams",3)], "I am finished with Team Three.  Let's begin the match.", "arena_master_spar_start_it_up",[]],
  [anyone|plyr,"arena_master_spar_team_three_choose", [], "Never mind. I'm calling the whole thing off.", "arena_master_pre_talk",[]],
  [anyone,"arena_master_spar_team_four", [(eq,"$temp",8)], "Team Four is full. Let the match begin!", "arena_master_spar_start_it_up",[]],
  [anyone,"arena_master_spar_team_four", [(assign,reg0,"$temp"),(store_sub,reg1,reg0,1)], "There {reg1?are:is} currently {reg0} {reg1?troops:troop} on Team Four.  Which troop would you like to add?", "arena_master_spar_team_four_choose",[]],
  [anyone|plyr|repeat_for_troops, "arena_master_spar_team_four_choose",
   [
     (store_repeat_object, ":troop"),
     (party_get_num_companion_stacks,":num_stacks","p_main_party"),
     (assign,":include",0),
     (try_for_range,":stack",0,":num_stacks"),
       (eq,":include",0),
       (party_stack_get_troop_id,":troop_id","p_main_party",":stack"),
       (ge,":troop_id",0),
       (eq,":troop_id",":troop"),
       (assign,":num_in",0),
       (try_for_range,":counting",1,33),
         (troop_get_slot,":already_in","trp_temp_array_a",":counting"),
         (eq,":already_in",":troop"),
         (val_add,":num_in",1),
       (try_end),
       (party_stack_get_size,":available","p_main_party",":stack"),
       (gt,":available",":num_in"),
       (assign,":include",1),
     (try_end),
     (eq,":include",1),
     (store_sub,reg0,":available",":num_in"),
     (str_store_troop_name,s11,":troop"),
     ],
   "{s11}. ({reg0} left.)", "arena_master_spar_team_four_add",
   [
     (store_repeat_object, "$temp_2"),
     (val_add,"$temp",1),
     (store_add,":offset","$temp",24),
     (troop_set_slot, "trp_temp_array_a", ":offset", "$temp_2"),
     (str_store_troop_name,s11,"$temp_2")
     ]],
  [anyone,"arena_master_spar_team_four_add", [], "{s11} has been added to Team Four.", "arena_master_spar_team_four",[]],
  [anyone|plyr,"arena_master_spar_team_four_choose", [], "I am finished with Team Four.  Let's begin the match.", "arena_master_spar_start_it_up",[]],
  [anyone|plyr,"arena_master_spar_team_four_choose", [], "Never mind. I'm calling the whole thing off.", "arena_master_pre_talk",[]],

  [anyone,"arena_master_spar_start_it_up", [], "Here you go then. Good luck.", "close_window",
   [
     (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
     (modify_visitors_at_site, ":arena_scene"),
     (reset_visitors),
     (try_for_range,":num",1,33),
       (troop_get_slot,":troop","trp_temp_array_a",":num"),
       (ge,":troop",0),
       (store_sub,":offset",":num",1), #Oops, easier to add this than go back and fix all the other instances
       (set_visitor, ":offset", ":troop"),
     (try_end),
     (set_jump_mission, "mt_arena_spar_fight"),
     (jump_to_scene, ":arena_scene"),
     (change_screen_mission),
     ]],
## Arena sparring end
#LAZERAS MODIFIED  {spar troops}


  [anyone,"arena_master_ask_tournaments", [], "{reg2?There won't be any tournaments any time soon.:{reg1?Tournaments are:A tournament is} going to be held at {s15}.}", "arena_master_talk",
   [
       (assign, ":num_tournaments", 0),
       (try_for_range_backwards, ":town_no", towns_begin, towns_end),
         (party_slot_ge, ":town_no", slot_town_has_tournament, 1),
         (val_add, ":num_tournaments", 1),
         (try_begin),
           (eq, ":num_tournaments", 1),
           (str_store_party_name, s15, ":town_no"),
         (else_try),
           (str_store_party_name, s16, ":town_no"),
           (eq, ":num_tournaments", 2),
           (str_store_string, s15, "@{s16} and {s15}"),
         (else_try),
           (str_store_string, s15, "@{!}{s16}, {s15}"),
         (try_end),
       (try_end),
       (try_begin),
         (eq, ":num_tournaments", 0),
         (assign, reg2, 1),
       (else_try),
         (assign, reg2, 0),
         (store_sub, reg1, ":num_tournaments", 1),
       (try_end),
   ]],

  [anyone,"arena_master_melee_pretalk", [], "There will be a fight here soon. You can go and jump in if you like.", "arena_master_melee_talk",[]],
  ## CC
  [anyone|plyr,"arena_master_melee_talk", [], "Good. That's what I am going to do.", "arena_master_melee_weapon_select", []],
  [anyone,"arena_master_melee_weapon_select", [], "Well, please choose a weapon which you like.", "arena_player_melee_weapon_select",[]],
  [anyone|plyr,"arena_player_melee_weapon_select", [], "Two-handed sword.", "close_window",
    [
      (store_random_in_range, ":random_num", 0, 60),
      (try_begin),
        (le, ":random_num", 30),
        (assign, "$g_player_entry_point", 32),
      (else_try),
        (assign, "$g_player_entry_point", 38),
      (try_end),
      (assign, "$last_training_fight_town", "$current_town"),
      (store_current_hours,"$training_fight_time"),
      (assign, "$g_mt_mode", abm_training),
      (party_get_slot, ":scene","$current_town",slot_town_arena),
      (modify_visitors_at_site,":scene"),
      (reset_visitors),
      (set_visitor, "$g_player_entry_point", "trp_player"),
      (set_jump_mission,"mt_arena_melee_fight"),
      (jump_to_scene, ":scene"),
    ]],
  [anyone|plyr,"arena_player_melee_weapon_select", [], "Staff.", "close_window",
    [
      (store_random_in_range, ":random_num", 0, 60),
      (try_begin),
        (le, ":random_num", 20),
        (assign, "$g_player_entry_point", 33),
      (else_try),
        (le, ":random_num", 40),
        (assign, "$g_player_entry_point", 35),
      (else_try),
        (assign, "$g_player_entry_point", 39),
      (try_end),
      (assign, "$last_training_fight_town", "$current_town"),
      (store_current_hours,"$training_fight_time"),
      (assign, "$g_mt_mode", abm_training),
      (party_get_slot, ":scene","$current_town",slot_town_arena),
      (modify_visitors_at_site,":scene"),
      (reset_visitors),
      (set_visitor, "$g_player_entry_point", "trp_player"),
      (set_jump_mission,"mt_arena_melee_fight"),
      (jump_to_scene, ":scene"),
    ]],
  [anyone|plyr,"arena_player_melee_weapon_select", [], "One-handed sword with a shield.", "close_window",
    [
      (store_random_in_range, ":random_num", 0, 60),
      (try_begin),
        (le, ":random_num", 30),
        (assign, "$g_player_entry_point", 34),
      (else_try),
        (assign, "$g_player_entry_point", 37),
      (try_end),
      (assign, "$last_training_fight_town", "$current_town"),
      (store_current_hours,"$training_fight_time"),
      (assign, "$g_mt_mode", abm_training),
      (party_get_slot, ":scene","$current_town",slot_town_arena),
      (modify_visitors_at_site,":scene"),
      (reset_visitors),
      (set_visitor, "$g_player_entry_point", "trp_player"),
      (set_jump_mission,"mt_arena_melee_fight"),
      (jump_to_scene, ":scene"),
    ]],
  [anyone|plyr,"arena_player_melee_weapon_select", [], "Bow.", "close_window",
    [
      (assign, "$g_player_entry_point", 36),
      (assign, "$last_training_fight_town", "$current_town"),
      (store_current_hours,"$training_fight_time"),
      (assign, "$g_mt_mode", abm_training),
      (party_get_slot, ":scene","$current_town",slot_town_arena),
      (modify_visitors_at_site,":scene"),
      (reset_visitors),
      (set_visitor, "$g_player_entry_point", "trp_player"),
      (set_jump_mission,"mt_arena_melee_fight"),
      (jump_to_scene, ":scene"),
    ]],
  ## CC
  [anyone|plyr,"arena_master_melee_talk", [], "Thanks. But I will give my bruises some time to heal.", "arena_master_melee_reject",[]],
  [anyone,"arena_master_melee_reject", [], "Good {man/girl}. That's clever of you.", "arena_master_pre_talk",[]],

  [anyone|plyr,"arena_master_melee_talk", [(eq, "$arena_reward_asked", 0)], "Actually, can you tell me about the rewards again?", "arena_training_melee_explain_reward",[(assign, "$arena_reward_asked", 1)]],

#  [anyone,"arena_master_pre_talk",
#   [(eq,"$arena_join_or_watch",1),
#    (ge,"$arena_bet_amount",1),
#    (eq,"$arena_bet_team","$arena_winner_team"),
#    (assign,reg(5),"$arena_win_amount")],
# "You've won the bet, eh? Let me see. The sum you have earned amounts to {reg5} denars. Here you go.", "arena_master_pre_talk",
#   [(call_script, "script_troop_add_gold", "trp_player", "$arena_win_amount"),
#    (assign,"$arena_bet_amount",0),
#    (assign,"$arena_win_amount",0),
#    ]],

#  [anyone,"arena_master_pre_talk",
#   [(eq,"$arena_join_or_watch",0),
#    (ge,"$arena_bet_amount",1),
#    (eq,"$arena_fight_won",1),
#    (assign,reg(5),"$arena_win_amount"),
#   ],
# "And you had the good sense to bet on yourself too. Hmm let me see. You have won yourself some {reg5} denars. Here you are.", "arena_master_pre_talk",
#   [(call_script, "script_troop_add_gold", "trp_player", "$arena_win_amount"),
#    (assign,"$arena_bet_amount",0),
#    (assign,"$arena_win_amount",0)]],

#  [anyone,"start", [(store_conversation_troop,reg(1)),(is_between,reg(1),arena_masters_begin,arena_masters_end),(eq,"$waiting_for_arena_fight_result",1),(eq,"$arena_join_or_watch",0),(eq,"$arena_fight_won",1)],
# "Congratulations champion. You made some pretty good moves out there. Here is your share of share of the prize money, 2 denars.", "arena_master_pre_talk",
#   [(assign,"$waiting_for_arena_fight_result",0),(add_xp_to_troop,20,"trp_player"),(call_script, "script_troop_add_gold", "trp_player",2)]],
#  [anyone,"start", [(store_conversation_troop,reg(1)),(is_between,reg(1),arena_masters_begin,arena_masters_end),(eq,"$waiting_for_arena_fight_result",1),(eq,"$arena_join_or_watch",0)],
# "That's quite the bruise you're sporting. But don't worry; everybody gets trounced once in awhile. The important thing is to pick yourself up, dust yourself off and keep fighting. That's what champions do.", "arena_master_pre_talk",[[assign,"$waiting_for_arena_fight_result"]]],
#  [anyone,"start", [(store_conversation_troop,reg(1)),(is_between,reg(1),arena_masters_begin,arena_masters_end),(eq,"$waiting_for_arena_fight_result",1)],
# "That was exciting wasn't it? Nothing like a good fight to get the blood flowing.", "arena_master_pre_talk",[(assign,"$waiting_for_arena_fight_result",0)]],

##  [anyone,"arena_master_melee", [], "The next arena fight will start in a while. Hurry up if you want to take part in it.", "arena_master_melee_talk",[
##    (party_get_slot, ":arena_cur_tier","$current_town",slot_town_arena_melee_cur_tier),
##    (try_begin), #reg3 = num teams, reg4 = team size
##      (eq, ":arena_cur_tier", 0),
##      (party_get_slot, "$_num_teams","$current_town",slot_town_arena_melee_1_num_teams),
##      (party_get_slot, "$_team_size","$current_town",slot_town_arena_melee_1_team_size),
##    (else_try),
##      (eq, ":arena_cur_tier", 1),
##      (party_get_slot, "$_num_teams","$current_town",slot_town_arena_melee_2_num_teams),
##      (party_get_slot, "$_team_size","$current_town",slot_town_arena_melee_2_team_size),
##    (else_try),
##      (party_get_slot, "$_num_teams","$current_town",slot_town_arena_melee_3_num_teams),
##      (party_get_slot, "$_team_size","$current_town",slot_town_arena_melee_3_team_size),
##    (try_end),
##   ]],
##  [anyone|plyr,"arena_master_melee_talk", [], "I want to join the next fight", "arena_master_next_melee_join",[(assign,"$arena_join_or_watch",0)]],
##  [anyone|plyr,"arena_master_melee_talk", [], "I would like to watch the next fight", "arena_master_next_melee_watch",
##   [(assign,"$arena_join_or_watch",1)]],
##  [anyone|plyr,"arena_master_melee_talk", [], "No. perhaps later.", "arena_master_we_will_fight_not",[]],
##  [anyone,"arena_master_we_will_fight_not", [], "Alright. Talk to me when you are ready.", "close_window",[]],
##  [anyone,"arena_master_next_melee_join", [
##    (assign,"$arena_bet_amount"),
##    (assign,"$arena_bet_team",0),
##    (party_get_slot, ":player_odds", "$g_encountered_party", slot_town_player_odds),
##    (store_div, ":divider", ":player_odds", 20),
##    (store_mul, ":odds_simple", ":divider", 20),
##    (val_sub, ":odds_simple", ":player_odds"),
##    (try_begin),
##      (lt, ":odds_simple", 0),
##      (val_add, ":divider", 1),
##    (try_end),
##    (val_max, ":divider", 50),
##    (store_div, ":odds_player", ":player_odds", ":divider"),
##    (store_div, ":odds_other", 1000, ":divider"),
##    (try_for_range, ":unused", 0, 5),
##      (assign, ":last_divider", 21),
##      (try_for_range, ":cur_divider", 2, ":last_divider"),
##        (store_div, ":odds_player_test", ":odds_player", ":cur_divider"),
##        (val_mul, ":odds_player_test", ":cur_divider"),
##        (eq, ":odds_player_test", ":odds_player"),
##        (store_div, ":odds_other_test", ":odds_other", ":cur_divider"),
##        (val_mul, ":odds_other_test", ":cur_divider"),
##        (eq, ":odds_other_test", ":odds_other"),
##        (val_div, ":odds_player", ":cur_divider"),
##        (val_div, ":odds_other", ":cur_divider"),
##        (assign, ":last_divider", 0),
##      (try_end),
##    (try_end),
##    (assign, reg5, ":odds_player"),
##    (assign, reg6, ":odds_other"),], "Do you want to place a bet on yourself? The odds against you are {reg5} to {reg6}.", "arena_master_will_you_bet",
##   []],
##
##  [anyone|plyr,"arena_master_will_you_bet", [], "No.", "arena_master_start_fight",[]],
##  [anyone|plyr,"arena_master_will_you_bet", [(store_troop_gold,reg(0)),(ge,reg(0),10)], "I want to bet 10 denars.",
##   "arena_master_bet_placed",[(assign,"$arena_bet_amount",10),(troop_remove_gold, "trp_player",10)]],
##  [anyone|plyr,"arena_master_will_you_bet", [(store_troop_gold,reg(0)),(ge,reg(0),50)], "I want to bet 50 denars.",
##   "arena_master_bet_placed",[(assign,"$arena_bet_amount",50),(troop_remove_gold, "trp_player",50)]],
##  [anyone|plyr,"arena_master_will_you_bet", [(store_troop_gold,reg(0)),(ge,reg(0),100)], "I want to bet 100 denars.",
##   "arena_master_bet_placed",[(assign,"$arena_bet_amount",100),(troop_remove_gold, "trp_player",100)]],
##  [anyone,"arena_master_next_melee_watch", [], "Do you want to place a bet?", "arena_master_will_you_bet",[]],
##  [anyone,"arena_master_bet_placed", [(eq,"$arena_join_or_watch",1)], "Hmm. That's good. If you win, you'll get {reg5} denars. And which team do you want to place your bet on?", "arena_master_select_team",
##   [(store_mul, "$arena_win_amount", "$arena_bet_amount", "$_num_teams"),
##    (val_mul, "$arena_win_amount", 9),
##    (val_div, "$arena_win_amount", 10),
##    (assign, reg5, "$arena_win_amount"),
##    ]],
##  [anyone|plyr,"arena_master_select_team", [], "The red team. I have a feeling they will win this one.",
##   "arena_master_start_fight",[(assign,"$arena_bet_team",0)]],
##  [anyone|plyr,"arena_master_select_team", [], "The blue team. They will sweep the ground with the reds.",
##   "arena_master_start_fight",[(assign,"$arena_bet_team",1)]],
##  [anyone|plyr,"arena_master_select_team", [(ge,"$_num_teams",3)], "The green team. My money is on them this time.",
##   "arena_master_start_fight",[(assign,"$arena_bet_team",2)]],
##  [anyone|plyr,"arena_master_select_team", [(ge,"$_num_teams",4)], "The yellow team. They will be victorious.",
##   "arena_master_start_fight",[(assign,"$arena_bet_team",3)]],
##  [anyone,"arena_master_bet_placed", [], "That's good. Let me record that. If you win, you'll get {reg5} denars.", "arena_master_start_fight",
##   [(store_mul,"$arena_win_amount", "$arena_bet_amount", "$_num_teams"),
##    (party_get_slot, ":player_odds", "$g_encountered_party", slot_town_player_odds),
##    (val_sub, "$arena_win_amount", "$arena_bet_amount"),
##    (val_mul, "$arena_win_amount", ":player_odds"),
##    (val_div, "$arena_win_amount", 1000),
##    (val_add, "$arena_win_amount", "$arena_bet_amount"),
##    (val_mul, "$arena_win_amount", 9),
##    (val_div, "$arena_win_amount", 10),
##    (assign, reg5, "$arena_win_amount"),
##    ]],
##
##  [anyone,"arena_master_start_fight", [], "Very well. The fight starts in a moment. Good luck.", "close_window",
##   [
##    (store_encountered_party,"$current_town"),
##    (party_get_slot, ":arena_scene","$current_town",slot_town_arena),
##    (modify_visitors_at_site,":arena_scene"),
##    (reset_visitors),
##
##    #Assemble participants
##    (assign, ":slot_no", 0),
##    (troop_set_slot, "trp_temp_array_a", ":slot_no", "trp_xerina"),
##    (val_add, ":slot_no", 1),
##    (troop_set_slot, "trp_temp_array_a", ":slot_no", "trp_dranton"),
##    (val_add, ":slot_no", 1),
##    (troop_set_slot, "trp_temp_array_a", ":slot_no", "trp_kradus"),
##    (val_add, ":slot_no", 1),
##    (try_for_range, reg(4), 0, 10),
##      (lt, ":slot_no", 48),
##      (troop_set_slot, "trp_temp_array_a", ":slot_no", "trp_regular_fighter"),
##      (val_add, ":slot_no", 1),
##    (try_end),
##    (try_for_range, reg(4), 0, 10),
##      (lt, ":slot_no", 48),
##      (troop_set_slot, "trp_temp_array_a", ":slot_no", "trp_veteran_fighter"),
##      (val_add, ":slot_no", 1),
##    (try_end),
##    (try_for_range, reg(4), 0, 10),
##      (lt, ":slot_no", 48),
##      (troop_set_slot, "trp_temp_array_a", ":slot_no", "trp_champion_fighter"),
##      (val_add, ":slot_no", 1),
##    (try_end),
##    (try_for_range, reg(4), 0, 5),
##      (lt, ":slot_no", 48),
##      (troop_set_slot, "trp_temp_array_a", ":slot_no", "trp_sword_sister"),
##      (val_add, ":slot_no", 1),
##    (try_end),
##    (try_for_range, reg(4), 0, 10),
##      (lt, ":slot_no", 48),
##      (troop_set_slot, "trp_temp_array_a", ":slot_no", "trp_hired_blade"),
##      (val_add, ":slot_no", 1),
##    (try_end),
##    (try_for_range, reg(4), 0, 10),
##      (lt, ":slot_no", 48),
##      (troop_set_slot, "trp_temp_array_a", ":slot_no", "trp_mercenary"),
##      (val_add, ":slot_no", 1),
##    (try_end),
##    (assign, "$pin_troop", "trp_temp_array_a"),
##    (call_script, "script_shuffle_troop_slots", 0, 48),
##
##    (try_for_range, reg(12), 0, 48),
##      (troop_set_slot, "trp_temp_array_b", reg(12),reg(12)), #Initialize temp_array_b such that temp_array_b[i] = i
##    (try_end),
##
##    (store_random_in_range, "$arena_player_team", 0, "$_num_teams"),
##    (try_for_range, ":i_team", 0, "$_num_teams"), # repeat for num_teams; reg(55) = cur_team
##      (assign, ":team_slots_start", ":i_team"),
##      (val_mul, ":team_slots_start", 8),
##      (assign, ":team_slots_end", ":team_slots_start"),
##      (val_add, ":team_slots_end", 8),
##      (assign, "$pin_troop", "trp_temp_array_b"),
##      (call_script, "script_shuffle_troop_slots", ":team_slots_start", ":team_slots_end"),
##      (assign, ":cur_slot", ":team_slots_start"),
##      (try_for_range, reg(6), 0, "$_team_size"), # repeat for team_size;
##        (troop_get_slot, ":cur_slot_troop", "trp_temp_array_a", ":cur_slot"),
##        (try_begin), #place player
##          (eq,"$arena_join_or_watch",0),
##          (eq, ":i_team", "$arena_player_team"),
##          (eq, reg(6), 0),
##          (assign, ":cur_slot_troop", "trp_player"),
##        (try_end),
##        (troop_get_slot, ":cur_entry_no", "trp_temp_array_b", ":cur_slot"),
##        (set_visitor,":cur_entry_no",":cur_slot_troop"),
##        (val_add, ":cur_slot", 1),
##      (try_end),
##    (try_end),
##
##    (try_begin),
##      (eq, "$arena_join_or_watch", 1),
##      (set_visitor, 33, "trp_player"),#entry point 51
##    (try_end),
##    (assign, "$arena_fight_won", 0),
##    (assign, "$arena_winner_team", -1),
##    (assign, "$waiting_for_arena_fight_result", 1),
##    (assign, "$g_mt_mode", abm_fight),
##    (party_get_slot, reg(6),"$current_town",slot_town_arena_melee_cur_tier),
##    (val_add,reg(6),1),
##    (val_mod,reg(6),3),
##    (party_set_slot, "$current_town",slot_town_arena_melee_cur_tier, reg(6)),
###    (set_jump_mission,"mt_arena_melee_fight"),
##    (party_get_slot, ":arena_mission_template", "$current_town", slot_town_arena_template),
##    (set_jump_mission, ":arena_mission_template"),
##    (party_get_slot, reg(7), "$current_town", slot_town_arena),
##    (jump_to_scene, reg(7)),
##    ]],



######################################################################################
  [trp_galeas,"start", [], "Hello {boy/girl}. If you have any prisoners, I will be happy to buy them from you.", "galeas_talk",[]],

  [trp_galeas|plyr,"galeas_talk",
   [[store_num_regular_prisoners,reg(0)],[ge,reg(0),1]],
   "Then you'd better bring your purse. I have got prisoners to sell.", "galeas_sell_prisoners",[]],
  [trp_galeas|plyr,"galeas_talk",[], "Not this time. Good-bye.", "close_window",[]],
  [trp_galeas,"galeas_sell_prisoners", [],
  "Let me see what you have...", "galeas_sell_prisoners_2",
   [[change_screen_trade_prisoners]]],
  [trp_galeas, "galeas_sell_prisoners_2", [], "You take more prisoners, bring them to me. I will pay well.", "close_window",[]],

##  [party_tpl|pt_refugees,"start", [], "We have been driven out of our homes because of this war.", "close_window",[(assign, "$g_leave_encounter",1)]],
##  [party_tpl|pt_farmers,"start", [], "We are just simple farmers.", "close_window",[(assign, "$g_leave_encounter",1)]],


# Random Quest related conversations
#  [trp_nobleman, "start", [],
#   "Who are you? What do you want? Be warned, we are fully armed and more than capable to defend ourselves. Go to your way now or you will regret it.", "nobleman_talk_1",
#   [(play_sound,"snd_encounter_nobleman")]],
#  [trp_nobleman|plyr, "nobleman_talk_1", [],
#   "I demand that you surrender to me.", "nobleman_talk_2",[]],
#  [trp_nobleman|plyr, "nobleman_talk_1", [],
#   "I am sorry sir. You may go.", "close_window",[(assign, "$g_leave_encounter",1)]],
#  [trp_nobleman, "nobleman_talk_2", [],
#   "Surrender to a puny peasant like you? Hah. Not likely.", "close_window",[[encounter_attack]]],
#
#  [trp_nobleman,"enemy_defeated", [], "Parley! I am of noble birth, and I ask for my right to surrender.", "nobleman_defeated_1",[]],
#  [trp_nobleman|plyr,"nobleman_defeated_1", [], "And I will grant you that. If you can be ransomed of course...", "nobleman_defeated_2",[]],
#  [trp_nobleman,"nobleman_defeated_2", [], "Oh, you need not worry about that. My family would pay a large ransom for me.", "nobleman_defeated_3",[]],
#  [trp_nobleman|plyr,"nobleman_defeated_3", [[str_store_troop_name,1,"$nobleman_quest_giver"]], "Hmm. {s1} will be happy about this... Then you are my prisoner.", "close_window",
#   [[assign,"$nobleman_quest_succeeded",1],[assign,"$nobleman_quest_nobleman_active",0]]],

# Prisoner Trains
##  [anyone,"start", [(eq,"$g_encountered_party_type",spt_prisoner_train)],
##   "What do you want?", "prisoner_train_talk",[]],
##
##  [anyone|plyr,"prisoner_train_talk", [],
##   "Set those prisoners free now!", "prisoner_train_talk_ultimatum",[]],
##  [anyone,"prisoner_train_talk_ultimatum", [],
##   "Or what? Are you going to attack us?", "prisoner_train_talk_ultimatum_2",[]],
##  [anyone|plyr,"prisoner_train_talk_ultimatum_2", [],
##   "Yes I will. Consider yourself warned!", "prisoner_train_talk_ultimatum_2a",[]],
##  [anyone,"prisoner_train_talk_ultimatum_2a", [],
##   "We'll see that.", "close_window",[
##    (call_script, "script_make_kingdom_hostile_to_player", "$g_encountered_party_faction", -3),
##    ]],
##
##  [anyone|plyr,"prisoner_train_talk_ultimatum_2", [],
##   "Attack you? Hell no! I just took pity on those poor souls.", "prisoner_train_talk_ultimatum_2b",[]],
##  [anyone,"prisoner_train_talk_ultimatum_2b", [],
##   "Find something else to take pity on.", "close_window",[(assign, "$g_leave_encounter",1)]],
##  [anyone|plyr,"prisoner_train_talk", [],
##   "Better watch those prisoners well. They may try to run away.", "prisoner_train_smalltalk",[]],
##  [anyone,"prisoner_train_smalltalk", [],
##   "Don't worry. They aren't going anywhere.", "close_window",[(assign, "$g_leave_encounter",1)]],



##  [anyone,"start", [(eq, "$g_encountered_party_type", spt_forager), (is_between, "$g_encountered_party_relation", -9, 1)],
##   "Hold it right there. Who are you?", "soldiers_interrogation",[(play_sound,"snd_encounter_vaegirs_neutral")]],
##  [anyone,"start", [(eq, "$g_encountered_party_type", spt_forager), (le, "$g_encountered_party_relation", -10)],
##   "You will not survive this!", "close_window",
##   [(store_relation, reg(5),"$g_encountered_party_faction"), (val_sub,reg(5),1), (set_relation,"$g_encountered_party_faction",0,reg(5)),(encounter_attack,0)]],
##  [anyone,"start", [(eq, "$g_encountered_party_type", spt_forager),(ge, "$g_encountered_party_relation", 1)],
##   "Our lands have been invaded. But we will drive them back.", "close_window",[(assign, "$g_leave_encounter",1),(play_sound,"snd_encounter_vaegirs_ally"),]],
##
##  [anyone,"start", [(eq, "$g_encountered_party_type", spt_scout),(is_between, "$g_encountered_party_relation", -9, 1)],
##   "Hold it right there. Who are you?", "soldiers_interrogation",[]],
##  [anyone,"start", [(eq, "$g_encountered_party_type", spt_scout),(le, "$g_encountered_party_relation", -10)],
##   "You deserve to die a thousand deaths!", "close_window",
##   [(store_relation, reg(5),"$g_encountered_party_faction"), (val_sub,reg(5),2), (set_relation,"$g_encountered_party_faction",0,reg(5)),(encounter_attack,0)]],
##  [anyone,"start", [(eq, "$g_encountered_party_type", spt_scout),(ge, "$g_encountered_party_relation", 1)],
##   "Venture deep into the enemy territory and find myself a caravan to raid. That's the way I will get rich.", "close_window",[(assign, "$g_leave_encounter",1)]],
##
##  [anyone,"start", [(this_or_next|eq, "$g_encountered_party_type", spt_patrol),(eq, "$g_encountered_party_type", spt_war_party),(is_between, "$g_encountered_party_relation", -9, 1)],
##   "Hold it right there. Who are you?", "soldiers_interrogation",[]],
##  [anyone,"start", [(this_or_next|eq, "$g_encountered_party_type", spt_patrol),(eq, "$g_encountered_party_type", spt_war_party),(le, "$g_encountered_party_relation", -10)],
##   "You will not survive this!", "close_window",
##   [(store_relation, reg(5),"$g_encountered_party_type"), (val_sub,reg(5),3), (set_relation,"$g_encountered_party_type",0,reg(5)),(encounter_attack,0)]],
##  [anyone,"start", [(this_or_next|eq, "$g_encountered_party_type", spt_patrol),(eq, "$g_encountered_party_type", spt_war_party),(ge, "$g_encountered_party_relation", 1)],
##   "Sooner or later, friend. Victory will belong to us.", "close_window",[(assign, "$g_leave_encounter",1)]],

#swadian parties
##  [anyone|plyr,"soldiers_interrogation", [], "I am {playername}.", "soldiers_interrogation_2",[]],
##  [anyone,"soldiers_interrogation_2", [], "What are you doing here?", "soldiers_interrogation_3",[]],
##  [anyone|plyr,"soldiers_interrogation_3", [], "I am carrying some merchandise.", "soldiers_interrogation_4",[]],
##  [anyone|plyr,"soldiers_interrogation_3", [], "I am just admiring the sights.", "soldiers_interrogation_4",[]],
##  [anyone,"soldiers_interrogation_4", [], "Hmm. All right. You may go now. But be careful. There is a war going on. The roads are not safe for travellers.", "close_window",[(assign, "$g_leave_encounter",1)]],





# Bandits
##  [party_tpl|pt_mountain_bandits,"start", [(this_or_next|eq, "$g_encountered_party_template", "pt_mountain_bandits"),(eq, "$g_encountered_party_template", "pt_forest_bandits"),
##                                           (eq,"$talk_context",tc_party_encounter),
##                                           (party_get_slot,":protected_until_hours", "$g_encountered_party",slot_party_ignore_player_until),
##                                           (store_current_hours,":cur_hours"),
##                                           (store_sub, ":protection_remaining",":protected_until_hours",":cur_hours"),
##                                           (ge, ":protection_remaining", 0)], "What do you want?\
## You want to pay us some more money?", "bandit_paid_talk",[]],
##
##  [anyone|plyr,"bandit_paid_talk", [], "Sorry to trouble you. I'll be on my way now.", "bandit_paid_talk_2a",[]],
##  [anyone,"bandit_paid_talk_2a", [], "Yeah. Stop fooling around and go make some money.\
## I want to see that purse full next time I see you.", "close_window",[(assign, "$g_leave_encounter",1)]],
##  [anyone|plyr,"bandit_paid_talk", [], "No. It's your turn to pay me this time.", "bandit_paid_talk_2b",[]],
##  [anyone,"bandit_paid_talk_2b", [], "What nonsense are you talking about? You want trouble? You got it.", "close_window",[
##       (party_set_slot,"$g_encountered_party",slot_party_ignore_player_until,0),
##       (party_ignore_player, "$g_encountered_party", 0),
##    ]],

# Ryan BEGIN
  [party_tpl|pt_mountain_bandits|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_forest_bandits|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_taiga_bandits|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_steppe_bandits|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_desert_bandits|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],

 ##Floris MTT begin
   [party_tpl|pt_mountain_bandits_r|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_forest_bandits_r|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_taiga_bandits_r|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_steppe_bandits_r|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_desert_bandits_r|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_mountain_bandits_e|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_forest_bandits_e|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_taiga_bandits_e|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_steppe_bandits_e|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
  [party_tpl|pt_desert_bandits_e|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker)],
   "{!}Warning: This line should never display.", "bandit_introduce",[]],
 ##Floris MTT end


  [anyone,"bandit_introduce", [
      (store_random_in_range, ":rand", 11, 15),
        (str_store_string, s11, "@I can smell a fat purse a mile away. Methinks yours could do with some lightening, eh?"),
        (str_store_string, s12, "@Why, it be another traveller, chance met upon the road! I should warn you, country here's a mite dangerous for a good {fellow/woman} like you. But for a small donation my boys and I'll make sure you get rightways to your destination, eh?"),
        (str_store_string, s13, "@Well well, look at this! You'd best start coughing up some silver, friend, or me and my boys'll have to break you."),
		(str_store_string, s14, "@There's a toll for passin' through this land, payable to us, so if you don't mind we'll just be collectin' our due from your purse..."),
        (str_store_string_reg, s5, ":rand"),
    ], "{s5}", "bandit_talk",[(play_sound,"snd_encounter_bandits")]],

  [anyone|plyr,"bandit_talk", [], "I'll give you nothing but cold steel, you scum!", "close_window",[[encounter_attack]]],
  [anyone|plyr,"bandit_talk", [], "There's no need to fight. I can pay for free passage.", "bandit_barter",[]],
  [anyone,"bandit_barter",
   [(store_relation, ":bandit_relation", "fac_player_faction", "$g_encountered_party_faction"),
    (ge, ":bandit_relation", -50),
    (store_troop_gold, ":total_value", "trp_player"),
    (troop_get_inventory_capacity, ":inv_size", "trp_player"),
    (try_for_range, ":i_slot", 0, ":inv_size"),
         (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
         (ge, ":item_id", 0),
         (try_begin),
           (is_between, ":item_id", trade_goods_begin, trade_goods_end),
           (store_item_value, ":item_value", ":item_id"),
           (val_add, ":total_value", ":item_value"),
         (try_end),
    (try_end),
    (store_div, "$bandit_tribute", ":total_value", 10), #10000 gold = excellent_target
    (val_max, "$bandit_tribute", 10),
    (assign, reg5, "$bandit_tribute")
    ], "Silver without blood, that's our favourite kind! Hmm, having a look at you, I reckon you could easily come up with {reg5} denars. Pay it, and we'll let you be on your way.", "bandit_barter_2",[]],
  [anyone|plyr,"bandit_barter_2", [[store_troop_gold,reg(2)],[ge,reg(2),"$bandit_tribute"],[assign,reg(5),"$bandit_tribute"]],
   "Very well, take it.", "bandit_barter_3a",[[troop_remove_gold, "trp_player","$bandit_tribute"]]],
  [anyone|plyr,"bandit_barter_2", [],
   "I don't have that much money with me", "bandit_barter_3b",[]],
  [anyone,"bandit_barter_3b", [],
   "That's too bad. I guess we'll just have to sell you into slavery. Take {him/her}, lads!", "close_window",[[encounter_attack]]],

  [anyone,"bandit_barter", [],
   "Hey, I've heard of you! You slaughter us freebooters like dogs, and now you expect us to let you go for a few stinking coins?\
 Forget it. You gave us no quarter, and you'll get none from us.", "close_window",[]],



  [anyone,"bandit_barter_3a", [], "Heh, that wasn't so hard, was it? All right, we'll let you go now. Be off.", "close_window",[
    (store_current_hours,":protected_until"),
    (val_add, ":protected_until", 72),
    (party_set_slot,"$g_encountered_party",slot_party_ignore_player_until,":protected_until"),
    (party_ignore_player, "$g_encountered_party", 72),
    (assign, "$g_leave_encounter",1)
    ]],


  [anyone,"start", [
				##Floris MTT begin
				(this_or_next|eq, "$g_encountered_party_template", "pt_mountain_bandits"),
				(this_or_next|eq, "$g_encountered_party_template", "pt_forest_bandits"),
				(this_or_next|eq, "$g_encountered_party_template", "pt_mountain_bandits_r"),
				(this_or_next|eq, "$g_encountered_party_template", "pt_forest_bandits_r"),
				(this_or_next|eq, "$g_encountered_party_template", "pt_mountain_bandits_e"),
				(eq, "$g_encountered_party_template", "pt_forest_bandits_e")
				##Floris MTT end
				],
   "Eh? What is it?", "bandit_meet",[]],

  [anyone|plyr,"bandit_meet", [], "Your luck has run out, wretch. Prepare to die!", "bandit_attack",
   [(store_relation, ":bandit_relation", "fac_player_faction", "$g_encountered_party_faction"),
    (val_sub, ":bandit_relation", 3),
    (val_max, ":bandit_relation", -100),
    (set_relation, "fac_player_faction", "$g_encountered_party_faction", ":bandit_relation"),
    (party_ignore_player, "$g_encountered_party", 0),
    (party_set_slot,"$g_encountered_party",slot_party_ignore_player_until, 0),
    ]],

  [anyone,"bandit_attack", [
      (store_random_in_range, ":rand", 11, 15),
        (str_store_string, s11, "@Another fool come to throw {him/her}self on my weapon, eh? Fine, let's fight!"),
        (str_store_string, s12, "@We're not afraid of you, {sirrah/wench}. Time to bust some heads!"),
        (str_store_string, s13, "@That was a mistake. Now I'm going to have to make your death long and painful."),
        (str_store_string, s14, "@Brave words. Let's see you back them up with deeds, cur!"),
        (str_store_string_reg, s5, ":rand"),
      ], "{s5}", "close_window",[]],

  [anyone|plyr,"bandit_meet", [], "Never mind, I have no business with you.", "close_window",[(assign, "$g_leave_encounter", 1)]],
# Ryan END



  [party_tpl|pt_rescued_prisoners,"start", [(eq,"$talk_context",tc_party_encounter)], "Do you want us to follow you?", "disbanded_troop_ask",[]],
  [anyone|plyr,"disbanded_troop_ask", [], "Yes. Let us ride together.", "disbanded_troop_join",[]],
  [anyone|plyr,"disbanded_troop_ask", [], "No. Not at this time.", "close_window",[(assign, "$g_leave_encounter",1)]],
  [anyone,"disbanded_troop_join", [[neg|party_can_join]], "It does not appear that you have room for us, {m'lord/m'lady}.", "close_window",[(assign, "$g_leave_encounter",1)]],
  [anyone,"disbanded_troop_join", [], "We are at your command.", "close_window",[[party_join],(assign, "$g_leave_encounter",1)]],

  [party_tpl|pt_enemy,"start", [(eq,"$talk_context",tc_party_encounter)], "You will not capture me again. Not this time.", "enemy_talk_1",[]],
  [party_tpl|pt_enemy|plyr,"enemy_talk_1", [], "You don't have a chance against me. Give up.", "enemy_talk_2",[]],
  [party_tpl|pt_enemy,"enemy_talk_2", [], "I will give up when you are dead!", "close_window",[[encounter_attack]]],


######################################
# ROUTED WARRIORS
######################################

  [party_tpl|pt_routed_warriors, "start", [(eq,"$talk_context",tc_party_encounter)],
   "I beg you, please leave us alone.", "party_encounter_routed_agents_are_caught",
   []],

  [party_tpl|pt_routed_warriors|plyr, "party_encounter_routed_agents_are_caught", [],
   "Do you think you can run away from me? You will be my prisoner or die!", "party_encounter_routed_agents_are_caught2",
   []],

  [party_tpl|pt_routed_warriors|plyr,"party_encounter_routed_agents_are_caught", [],
   "Ok. We'll leave you in peace for this time, do not face with us again.", "close_window", [(assign, "$g_leave_encounter",1)]],

  [party_tpl|pt_routed_warriors, "party_encounter_routed_agents_are_caught2",
   [
     #(store_party_size_wo_prisoners, ":routed_party_size", "$g_encountered_party"),
     #(store_party_size_wo_prisoners, ":main_party_size", "p_main_party"),

    # calculate power of routed party
    (assign, ":routed_party_power", 0),
    (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_troop_id, ":stack_troop", "$g_encountered_party", ":i_stack"),
      (store_character_level, ":troop_level", ":stack_troop"),
      (try_begin),
        (troop_is_mounted, ":stack_troop"),
        (val_add, ":troop_level", 5),
      (try_end),
      (party_stack_get_size, ":stack_size", "$g_encountered_party", ":i_stack"),
      (val_mul, ":troop_level", ":stack_size"),
      (val_add, ":routed_party_power", ":troop_level"),
    (try_end),

    # calculate power of our party
    (assign, ":main_party_power", 0),
    (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
      (store_character_level, ":troop_level", ":stack_troop"),
      (try_begin),
        (troop_is_mounted, ":stack_troop"),
        (val_add, ":troop_level", 5),
      (try_end),
      (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
      (val_mul, ":troop_level", ":stack_size"),
      (val_add, ":main_party_power", ":troop_level"),
    (try_end),

    (store_div, ":main_party_power_divided_by_5", ":main_party_power", 5),

    #find num attached parties to routed warriors
    (party_get_num_attached_parties, ":num_attached_parties", "$g_encountered_party"),

    (this_or_next|gt, ":num_attached_parties", 0), #always fight
    (ge, ":routed_party_power", ":main_party_power_divided_by_5"),
    ],
   "Haven't you got any mercy? Ok, we will fight you to the last man!", "close_window",
   []],

  [party_tpl|pt_routed_warriors, "party_encounter_routed_agents_are_caught2",
    [
      #(store_party_size_wo_prisoners, ":routed_party_size", "$g_encountered_party"),
      #(store_party_size_wo_prisoners, ":main_party_size", "p_main_party"),

      # calculate power of routed party
      (assign, ":routed_party_population", 0),
      (assign, ":routed_party_power", 0),
      (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "$g_encountered_party", ":i_stack"),
        (store_character_level, ":troop_level", ":stack_troop"),
        (try_begin),
          (troop_is_mounted, ":stack_troop"),
          (val_add, ":troop_level", 5),
        (try_end),
        (party_stack_get_size, ":stack_size", "$g_encountered_party", ":i_stack"),
        (val_mul, ":troop_level", ":stack_size"),
        (val_add, ":routed_party_power", ":troop_level"),
        (val_add, ":routed_party_population", ":stack_size"),
      (try_end),

      # calculate power of our party
      (assign, ":main_party_power", 0),
      (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
        (store_character_level, ":troop_level", ":stack_troop"),
        (try_begin),
          (troop_is_mounted, ":stack_troop"),
          (val_add, ":troop_level", 5),
        (try_end),
        (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
        (val_mul, ":troop_level", ":stack_size"),
        (val_add, ":main_party_power", ":troop_level"),
      (try_end),

      (store_div, ":main_party_power_divided_by_5", ":main_party_power", 5),
      (lt, ":routed_party_power", ":main_party_power_divided_by_5"),

      (store_party_size_wo_prisoners, ":routed_party_size", "$g_encountered_party"),
      (assign, reg3, ":routed_party_size"),

      (try_begin),
        (gt, ":routed_party_population", 1),
        (str_store_string, s1, "str_we_resign"),
      (else_try),
        (str_store_string, s1, "str_i_resign"),
      (try_end),
    ],
    "{s1}", "close_window",
    [(assign,"$g_enemy_surrenders", 1),
     (call_script, "script_party_wound_all_members", "$g_encountered_party"),
     (call_script, "script_party_copy", "p_total_enemy_casualties", "$g_encountered_party"),
     #(change_screen_exchange_with_party, "$g_encountered_party"),
     ]],

  #[party_tpl|pt_routed_warriors,"close_window_anythink_else", [],
  # "Anythink else.", "close_window", [(assign, "$g_leave_encounter",1)]],


# Ryan BEGIN
  [anyone,"sell_prisoner_outlaws", [[store_troop_kind_count,0,"trp_bandit_e_looter"],[ge,reg(0),1],[assign,reg(1),reg(0)],[val_mul,reg(1),10],[val_mul,reg(2),reg(0)],[val_mul,reg(2),10]],
   "Hmmm. 10 denars for each looter makes {reg1} denars for all {reg0} of them.", "sell_prisoner_outlaws",
   [[call_script, "script_troop_add_gold", "trp_player", reg(1)],[add_xp_to_troop,reg(2)],[remove_member_from_party,"trp_bandit_e_looter"]]],
  [anyone,"sell_prisoner_outlaws", [[store_troop_kind_count,0,"trp_bandit_e_bandit"],[ge,reg(0),1],[assign,reg(1),reg(0)],[val_mul,reg(1),20],[assign,reg(2),reg(0)],[val_mul,reg(2),20]],
   "Let me see. You've brought {reg0} bandits, so 20 denars for each comes up to {reg1} denars.", "sell_prisoner_outlaws",
   [[call_script, "script_troop_add_gold", "trp_player", reg(1)],[add_xp_to_troop,reg(2)],[remove_member_from_party,"trp_bandit_e_bandit"]]],
  [anyone,"sell_prisoner_outlaws", [[store_troop_kind_count,0,"trp_bandit_e_brigand"],[ge,reg(0),1],[assign,reg(1),reg(0)],[val_mul,reg(1),30],[assign,reg(2),reg(0)],[val_mul,reg(2),30]],
   "Well well, you've captured {reg0} brigands. Each one is worth 30 denars, so I'll give you {reg1} for them in total.", "sell_prisoner_outlaws",
   [[call_script, "script_troop_add_gold", "trp_player", reg(1)],[add_xp_to_troop,reg(2)],[remove_member_from_party,"trp_bandit_e_brigand"]]],
  [anyone,"sell_prisoner_outlaws", [], "I suppose that'll be all, then.", "close_window",[]],
# Ryan END

  [anyone|plyr,"prisoner_chat", [], "Do not try running away or trying something stupid. I will be watching you.", "prisoner_chat_2",[]],
  [anyone,"prisoner_chat_2", [], "No, I swear I won't.", "close_window",[]],


  [anyone,"start", [(party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
                    (this_or_next|is_between,"$g_talk_troop",weapon_merchants_begin,weapon_merchants_end),
                    (this_or_next|is_between,"$g_talk_troop",armor_merchants_begin, armor_merchants_end),
                    (             is_between,"$g_talk_troop",horse_merchants_begin, horse_merchants_end),
					##diplomacy start+
					#Replace "your lordship" with "your highness" if appropriate.
					(call_script,"script_dplmc_print_subordinate_says_sir_madame_to_s0"),
					(try_begin),
						(le, reg0, 2),
						(str_store_string, s0, "str_dplmc_my_lordlady"),
						(call_script, "script_dplmc_store_troop_is_female",  "trp_player"),
						(neq, reg0, 1),
						(str_store_string, s0, "@your lordship"),
					(try_end),
                    ],
   "Greetings, {s0}. How can I serve you today?", "town_merchant_talk",[]],#change {your lordship/my lady} to {s0}
   ##diplomacy end+

  [anyone,"start", [(this_or_next|is_between,"$g_talk_troop",weapon_merchants_begin,weapon_merchants_end),
                    (this_or_next|is_between,"$g_talk_troop",armor_merchants_begin, armor_merchants_end),
                    (             is_between,"$g_talk_troop",horse_merchants_begin, horse_merchants_end)], "Good day. What can I do for you?", "town_merchant_talk",[]],

  [anyone|plyr,"town_merchant_talk", [(is_between,"$g_talk_troop",weapon_merchants_begin,weapon_merchants_end)],
   "I want to buy a new weapon. Show me your wares.", "trade_requested_weapons",[]],
  [anyone|plyr,"town_merchant_talk", [(is_between,"$g_talk_troop",armor_merchants_begin,armor_merchants_end)],
   "I am looking for some equipment. Show me what you have.", "trade_requested_armor",[]],
  [anyone|plyr,"town_merchant_talk", [(is_between,"$g_talk_troop",horse_merchants_begin,horse_merchants_end)],
   "I am thinking of buying a horse.", "trade_requested_horse",[]],

##diplomacy start+ change to use script_dplmc_print_subordinate_says_sir_madame_to_s0
  [anyone,"trade_requested_weapons", [(call_script,"script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "Ah, yes {s0}. These arms are the best you'll find anywhere.", "merchant_trade",[[change_screen_trade]]],
  [anyone,"trade_requested_armor", [(call_script,"script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "Of course, {s0}. You won't find better quality armour than these in all Calradia.", "merchant_trade",[[change_screen_trade]]],
  [anyone,"trade_requested_horse", [(call_script,"script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "You have a fine eye for horses, {s0}. You won't find better beasts than these anywhere else.", "merchant_trade",[[change_screen_trade]]],
##diplomacy end+

  [anyone,"merchant_trade", [], "Anything else?", "town_merchant_talk",[]],
  [anyone|plyr,"town_merchant_talk", [], "Tell me. What are people talking about these days?", "merchant_gossip",[]],
  [anyone,"merchant_gossip", [], "Well, nothing new lately. Prices, weather, the war, the same old things.", "town_merchant_talk",[]],
  [anyone|plyr,"town_merchant_talk", [], "Good-bye.", "close_window",[]],




##  [anyone,"start", [(eq, "$talk_context", 0),
##                    (is_between,"$g_talk_troop",walkers_begin, walkers_end),
##                    (eq, "$sneaked_into_town",1),
##                     ], "Stay away beggar!", "close_window",[]],

  [anyone,"start", [(eq, "$talk_context", 0),
                    (is_between,"$g_talk_troop",walkers_begin, walkers_end),
                    (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
                     ], "My {lord/lady}?", "town_dweller_talk",[(assign, "$welfare_inquired",0),(assign, "$rumors_inquired",0),(assign, "$info_inquired",0)]],

  [anyone,"start", [(eq, "$talk_context", 0),
                    (is_between,"$g_talk_troop",walkers_begin, walkers_end),
					##diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} as appropriate
					(call_script,"script_dplmc_print_subordinate_says_sir_madame_to_s0"),
                     ], "Good day, {s0}.", "town_dweller_talk",[(assign, "$welfare_inquired", 0),(assign, "$rumors_inquired",0),(assign, "$info_inquired",0)]],
                    ##diplomacy end+
  [anyone|plyr,"town_dweller_talk", [(check_quest_active, "qst_hunt_down_fugitive"),
                                     (neg|check_quest_concluded, "qst_hunt_down_fugitive"),
                                      (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
                                      (quest_get_slot, ":quest_target_dna", "qst_hunt_down_fugitive", slot_quest_target_dna),
                                      (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
                                      (str_store_string, s4, s50),
                                      ],
   "I am looking for a man by the name of {s4}. I was told he may be hiding here.", "town_dweller_ask_fugitive",[]],
  ##diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} as appropriate
  [anyone ,"town_dweller_ask_fugitive", #[],
   [(call_script,"script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
   "Strangers come and go to our village, {s0}. If he is hiding here, you will surely find him if you look around.", "close_window",[]],
  ##diplomacy end+

# Ryan BEGIN
  [anyone|plyr,"town_dweller_talk",
   [
     (eq, 1, 0),
     (check_quest_active, "qst_meet_spy_in_enemy_town"),
     (neg|check_quest_succeeded, "qst_meet_spy_in_enemy_town"),
     (quest_slot_eq, "qst_meet_spy_in_enemy_town", slot_quest_target_center, "$current_town"),
     (str_store_item_name,s5,"$spy_item_worn"),
     ],
   "Pardon me, but is that a {s5} you're wearing?", "town_dweller_quest_meet_spy_in_enemy_town_ask_item",
   [
     ]],
  [anyone, "town_dweller_quest_meet_spy_in_enemy_town_ask_item", [
     (str_store_item_name,s5,"$spy_item_worn"),

     (try_begin),
     (troop_has_item_equipped,"$g_talk_troop","$spy_item_worn"),
     (str_store_string,s6,"@A {s5}? Well... Yes, I suppose it is. What a strange thing to ask."),
     (else_try),
     (str_store_string,s6,"@Eh? No, it most certainly is not a {s5}. I'd start questioning my eyesight if I were you."),
     (try_end),
  ],
   "{s6}", "town_dweller_talk",[]],

  [anyone|plyr|repeat_for_100,"town_dweller_talk",
   [
     (store_repeat_object,":object"),
     (lt,":object",4), # repeat only 4 times

     (check_quest_active, "qst_meet_spy_in_enemy_town"),
     (neg|check_quest_succeeded, "qst_meet_spy_in_enemy_town"),
     (quest_slot_eq, "qst_meet_spy_in_enemy_town", slot_quest_target_center, "$current_town"),

     (store_add,":string",":object","str_secret_sign_1"),
     (str_store_string, s4, ":string"),
     ],
   "{s4}", "town_dweller_quest_meet_spy_in_enemy_town",
   [
     (store_repeat_object,":object"),
     (assign, "$temp", ":object"),
     ]],

  [anyone ,"town_dweller_quest_meet_spy_in_enemy_town",
   [
     (call_script, "script_agent_get_town_walker_details", "$g_talk_agent"),
     (assign, ":walker_type", reg0),
     (eq, ":walker_type", walkert_spy),
     (quest_get_slot, ":secret_sign", "qst_meet_spy_in_enemy_town", slot_quest_target_amount),
     (val_sub, ":secret_sign", secret_signs_begin),
     (eq, ":secret_sign", "$temp"),
     (store_add, ":countersign", ":secret_sign", countersigns_begin),
     (str_store_string, s4, ":countersign"),
     ],
   "{s4}", "town_dweller_quest_meet_spy_in_enemy_town_know",[]],

  [anyone, "town_dweller_quest_meet_spy_in_enemy_town", [],
   "Eh? What kind of gibberish is that?", "town_dweller_quest_meet_spy_in_enemy_town_dont_know",[]],

  [anyone|plyr, "town_dweller_quest_meet_spy_in_enemy_town_dont_know", [],
   "Never mind.", "close_window",[]],

  [anyone|plyr, "town_dweller_quest_meet_spy_in_enemy_town_know", [
     (quest_get_slot, ":quest_giver", "qst_meet_spy_in_enemy_town", slot_quest_giver_troop),
     (str_store_troop_name, s4, ":quest_giver"),
  ],
   "{s4} sent me to collect your reports. Do you have them with you?", "town_dweller_quest_meet_spy_in_enemy_town_chat",[]],

  [anyone, "town_dweller_quest_meet_spy_in_enemy_town_chat", [
     (quest_get_slot, ":quest_giver", "qst_meet_spy_in_enemy_town", slot_quest_giver_troop),
     (str_store_troop_name, s4, ":quest_giver"),
  ],
   "I've been expecting you. Here they are, make sure they reach {s4} intact and without delay.", "town_dweller_quest_meet_spy_in_enemy_town_chat_2",[
     (call_script, "script_succeed_quest", "qst_meet_spy_in_enemy_town"),
     (call_script, "script_center_remove_walker_type_from_walkers", "$current_town", walkert_spy),
   ]],

  [anyone|plyr, "town_dweller_quest_meet_spy_in_enemy_town_chat_2", [],
   "Farewell.", "close_window",
   [
     ]],
# Ryan END

  [anyone|plyr,"town_dweller_talk", [(party_slot_eq, "$current_town", slot_party_type, spt_village),
                                     (eq, "$info_inquired", 0)], "What can you tell me about this village?", "town_dweller_ask_info",[(assign, "$info_inquired", 1)]],
  [anyone|plyr,"town_dweller_talk", [(party_slot_eq, "$current_town", slot_party_type, spt_town),
                                     (eq, "$info_inquired", 0)], "What can you tell me about this town?", "town_dweller_ask_info",[(assign, "$info_inquired", 1)]],


  [anyone,"town_dweller_ask_info", [(str_store_party_name, s5, "$current_town"),
                                    (assign, reg4, 0),
                                    (try_begin),
                                      (party_slot_eq, "$current_town", slot_party_type, spt_town),
                                      (assign, reg4, 1),
                                    (try_end),
									#diplomacy start+
									#replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
									(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
                                    (str_store_string, s6, "@This is the {reg4?town:village} of {s5}, {s0}."),
									##diplomacy end+
                                    (str_clear, s10),
                                    (try_begin),
                                      (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
                                      (str_store_string, s10, "@{s6} Our {reg4?town:village} and the surrounding lands belong to you of course, my {lord/lady}."),
                                    (else_try),
                                      (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
                                      (ge, ":town_lord", 0),
                                      (str_store_troop_name, s7, ":town_lord"),
                                      (store_troop_faction, ":town_lord_faction", ":town_lord"),
                                      (str_store_faction_name, s8, ":town_lord_faction"),
                                      (str_store_string, s10, "@{s6} Our {reg4?town:village} and the surrounding lands belong to {s7} of the {s8}."),
                                    (try_end),
                                    (str_clear, s5),
                                    (assign, ":number_of_goods", 0),
                                    (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
                                      #(store_sub, ":cur_good_slot", ":cur_good", trade_goods_begin),
                                      #(val_add, ":cur_good_slot", slot_town_trade_good_productions_begin),
                                      #(party_get_slot, ":production", "$g_encountered_party", ":cur_good_slot"),

                                      (call_script, "script_center_get_production", "$g_encountered_party", ":cur_good"),
                                      (assign, ":production", reg0),
                                      (ge, ":production", 20),

                                      (str_store_item_name, s3, ":cur_good"),
                                      (try_begin),
                                        (eq, ":number_of_goods", 0),
                                        (str_store_string, s5, s3),
                                      (else_try),
                                        (eq, ":number_of_goods", 1),
                                        (str_store_string, s5, "@{s3} and {s5}"),
                                      (else_try),
                                        (str_store_string, s5, "@{!}{s3}, {s5}"),
                                      (try_end),
                                      (val_add, ":number_of_goods", 1),
                                    (try_end),
									(try_begin),
										(gt, ":number_of_goods", 0),
										(assign, reg20, 1),
									(else_try),
										(assign, reg20, 0),
									(try_end),

                                    (str_store_string, s11, "@{reg20?We mostly produce {s5} here:We don't produce much here these days}.\
 If you would like to learn more, you can speak with our {reg4?guildmaster:village elder}. He is nearby, right over there."),
                                    ],
   "{s10} {s11}", "close_window",[]],

  [anyone|plyr,"town_dweller_talk", [(party_slot_eq, "$current_town", slot_party_type, spt_village),
                                     (eq, "$welfare_inquired", 0)], "How is life here?", "town_dweller_ask_situation",[(assign, "$welfare_inquired", 1)]],
  [anyone|plyr,"town_dweller_talk", [(party_slot_eq, "$current_town", slot_party_type, spt_town),
                                     (eq, "$welfare_inquired", 0)], "How is life here?", "town_dweller_ask_situation",[(assign, "$welfare_inquired", 1)]],


  [anyone,"town_dweller_ask_situation", [(call_script, "script_agent_get_town_walker_details", "$g_talk_agent"),
                                         (assign, ":walker_type", reg0),
                                         (eq, ":walker_type", walkert_needs_money),
										 #diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
										 (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
										 #diplomacy end+
                                         (party_slot_eq, "$current_town", slot_party_type, spt_village)],
   #diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
   "Disaster has struck my family, {s0}. We have no land of our own, and the others have no money to pay for our labor, or even to help us. My poor children lie at home hungry and sick. I don't know what we'll do.", "town_dweller_poor",[]],
   #diplomacy end+
  [anyone,"town_dweller_ask_situation", [(call_script, "script_agent_get_town_walker_details", "$g_talk_agent"),
                                         (assign, ":walker_type", reg0),
										 #diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
										 (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
										 #diplomacy end+
                                         (eq, ":walker_type", walkert_needs_money)],
   #diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
   "My life is miserable, {s0}. I haven't been able to find a job for months, and my poor children go to bed hungry each night.\
 My neighbours are too poor themselves to help me.", "town_dweller_poor",[]],
   #diplomacy end+
  [anyone|plyr,"town_dweller_poor", [(store_troop_gold, ":gold", "trp_player"),
                                     (ge, ":gold", 300),
                                     ],
   "Then take these 300 denars. I hope this will help you and your family.", "town_dweller_poor_paid",
   [(troop_remove_gold, "trp_player", 300),
    ]],

  [anyone|plyr,"town_dweller_poor", [],
   "Then clearly you must travel somewhere else, or learn another trade.", "town_dweller_poor_not_paid",[]],

  [anyone,"town_dweller_poor_not_paid", [], "Yes {sir/madam}. I will do as you say.", "close_window",[]],

  [anyone,"town_dweller_poor_paid", [], "{My lord/My good lady}. \
 You are so good and generous. I will tell everyone how you helped us.", "close_window",
   [(call_script, "script_change_player_relation_with_center", "$g_encountered_party", 1),
    (call_script, "script_agent_get_town_walker_details", "$g_talk_agent"),
    (assign, ":walker_no", reg2),
    (call_script, "script_center_set_walker_to_type", "$g_encountered_party", ":walker_no", walkert_needs_money_helped),
    ]],

  [anyone,"town_dweller_ask_situation", [(call_script, "script_agent_get_town_walker_details", "$g_talk_agent"),
                                         (assign, ":walker_type", reg0),
                                         (eq, ":walker_type", walkert_needs_money_helped),
										 #diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
										 (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
										 #diplomacy end+
                                         ],
   #diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
   "Thank you for your kindness {s0}. With your help our lives will be better. I will pray for you everyday.", "close_window",[]],
   #diplomacy end+
  [anyone,"town_dweller_ask_situation", [(neg|party_slot_ge, "$current_town", slot_town_prosperity, 30),
  #diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
  (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
   "Times are hard, {s0}. We work hard all day and yet we go to sleep hungry most nights.", "town_dweller_talk",[]],
   ##diplomacy end+

  [anyone,"town_dweller_ask_situation", [(neg|party_slot_ge, "$current_town", slot_town_prosperity, 70),#],
   #diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
   (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
   "Times are hard, {s0}. But we must count our blessings.", "town_dweller_talk",[]],
   #diplomacy end+
  [anyone,"town_dweller_ask_situation",
  ##diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
  [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
   "We are not doing too badly {s0}. We must count our blessings.", "town_dweller_talk",[]],
  ##diplomacy end+

  [anyone|plyr,"town_dweller_talk", [], "What is your trade?", "town_dweller_ask_trade",[]],

  [anyone,"town_dweller_ask_trade", [
  (call_script, "script_town_walker_occupation_string_to_s14", "$g_talk_agent"),
  ],
   "{s14}", "town_dweller_talk",[]],



  [anyone|plyr,"town_dweller_talk", [(eq, "$rumors_inquired", 0)], "What is the latest rumor around here?", "town_dweller_ask_rumor",[(assign, "$rumors_inquired", 1)]],
  ##diplomacy start+ The player's persuasive abilities can coax a rumor from the less friendly.
  ##OLD:
  #[anyone,"town_dweller_ask_rumor", [(neg|party_slot_ge, "$current_town", slot_center_player_relation, -5)], "I don't know anything that would be of interest to you.", "town_dweller_talk",[]],
  ##NEW:
  [anyone,"town_dweller_ask_rumor", [
  (store_skill_level, reg0, "skl_persuasion", "trp_player"),
  (store_sub, reg0, -5, reg0),
  (neg|party_slot_ge, "$current_town", slot_center_player_relation, reg0),
  ],
  "I don't know anything that would be of interest to you.", "town_dweller_talk",[]],
  ##diplomacy end+

  [anyone,"town_dweller_ask_rumor", [(store_mul, ":rumor_id", "$current_town", 197),
                                     (val_add,  ":rumor_id", "$g_talk_agent"),
                                     (call_script, "script_get_rumor_to_s61", ":rumor_id"),
                                     (gt, reg0, 0)], "{s61}", "town_dweller_talk",[]],

  [anyone,"town_dweller_ask_rumor", [], "I haven't heard anything interesting lately.", "town_dweller_talk",[]],

  [anyone|plyr,"town_dweller_talk", [], "[Leave]", "close_window",[]],

  [anyone,"start", [(eq, "$talk_context", 0),
                    (is_between,"$g_talk_troop",regular_troops_begin, regular_troops_end),
                    (party_slot_eq,"$current_town",slot_town_lord, "trp_player"),
					#diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
   				    (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
                     ], "Yes {s0}?", "player_castle_guard_talk",[]],#diplomacy end+ 
  [anyone|plyr,"player_castle_guard_talk", [], "How goes the watch, soldier?", "player_castle_guard_talk_2",[]],
  #diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
  [anyone,"player_castle_guard_talk_2", [], "All is quiet {s0}. Nothing to report.", "player_castle_guard_talk_3",[]],
  #diplomacy end+
  [anyone|plyr,"player_castle_guard_talk_3", [], "Good. Keep your eyes open.", "close_window",[]],


  [anyone,"start", [(eq, "$talk_context", 0),
                    (is_between,"$g_talk_troop",regular_troops_begin, regular_troops_end),
                    (is_between,"$g_encountered_party_faction",kingdoms_begin, kingdoms_end),
                    (eq, "$players_kingdom", "$g_encountered_party_faction"),
                    (troop_slot_ge, "trp_player", slot_troop_renown, 100),
                    (str_store_party_name, s10, "$current_town"),
					#diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
   				    (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
                     ], "Good day, {s0}. Always an honor to have you here in {s10}.", "close_window",[]],
					#diplomacy end+

  [anyone,"start", [(eq, "$talk_context", 0),
                    (is_between,"$g_talk_troop",regular_troops_begin, regular_troops_end),
                    (is_between,"$g_encountered_party_faction",kingdoms_begin, kingdoms_end),
                     ], "Mind your manners within the walls and we'll have no trouble.", "close_window",[]],

  [anyone,"start", [(eq, "$talk_context", tc_court_talk),
                    (is_between,"$g_talk_troop",regular_troops_begin, regular_troops_end),
                    (is_between,"$g_encountered_party_faction",kingdoms_begin, kingdoms_end),
                    (party_slot_eq,"$current_town",slot_town_lord, "trp_player"),
					#diplomacy start+ replace {my lord/my lady} with {your highness} if appropriate
					(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
                     ], "Your orders, {s0}?", "hall_guard_talk",[]],
					#diplomacy end+

  [anyone,"start", [(eq, "$talk_context", tc_court_talk),
                    (is_between,"$g_talk_troop",regular_troops_begin, regular_troops_end),
                    (is_between,"$g_encountered_party_faction",kingdoms_begin, kingdoms_end),
					#diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
   				    (call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
                     ], "We are not supposed to talk while on guard, {s0}.", "close_window",[]],
                    #diplomacy end+
  [anyone|plyr,"hall_guard_talk", [], "Stay on duty and let me know if anyone comes to see me.", "hall_guard_duty",[]],
  #diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
  [anyone,"hall_guard_duty", [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "Yes, {s0}. As you wish.", "close_window",[]],
  #diplomacy end+

  [anyone|plyr,"hall_guard_talk", [
  (eq, 1, 0),
  ], "I want you to arrest this man immediately!", "hall_guard_arrest",[]],
  #diplomacy start+ replace {sir/madame} with {my lord/my lady} or {your highness} if appropriate
  [anyone,"hall_guard_arrest", [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "Who do you want arrested {s0}?", "hall_guard_arrest_2",[]],
  #diplomacy end+
  [anyone|plyr,"hall_guard_arrest_2", [], "Ah, never mind my high spirits lads.", "close_window",[]],
  [anyone|plyr,"hall_guard_arrest_2", [], "Forget it. I will find another way to deal with this.", "close_window",[]],

  [anyone,"enemy_defeated", [], "Arggh! I hate this.", "close_window",[]],

  [anyone,"party_relieved", [], "Thank you for helping us against those bastards.", "close_window",[]],

  [anyone,"start", [(eq,"$talk_context", tc_party_encounter),(store_encountered_party, reg(5)),(party_get_template_id,reg(7),reg(5)),
				##Floris MTT begin
				(this_or_next|eq,reg(7),"pt_sea_raiders"),
				(this_or_next|eq,reg(7),"pt_sea_raiders_r"),
				(eq,reg(7),"pt_sea_raiders_e")],
				##Floris MTT end
   "I will drink from your skull!", "battle_reason_stated",[(play_sound,"snd_encounter_sea_raiders")]],

######################################
# GENERIC MEMBER CHAT
######################################
##diplomacy start+ replace instances of {sir/madam} with {my lord/my lady} or {your highness} if appropriate,
#using s0 and script_dplmc_print_subordinate_says_sir_madame_to_s0"
  [anyone,"member_chat", [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "Your orders {s0}?", "regular_member_talk",[]],
  [anyone|plyr,"regular_member_talk", [], "Tell me about yourself", "view_regular_char_requested",[]],
  [anyone,"view_regular_char_requested", [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "Aye {s0}. Let me tell you all there is to know about me.", "do_regular_member_view_char",[[change_screen_view_character]]],
##diplomacy end+
  [anyone,"do_regular_member_view_char", [], "Anything else?", "regular_member_talk",[]],


##Floris: Reenabled as savegame compatability was dropped-
# Custom Troops begin
  [anyone|plyr,"regular_member_talk", [(is_between,"$g_talk_troop",customizable_troops_begin, customizable_troops_end),], "I'd like to select your equipment.", "customize_troop_equipment_requested",[]],
  [anyone,"customize_troop_equipment_requested", [], "Aye {sir/madam}. Here is all the gear we have currently equipped. Your inventory will show the gear that you can assign to us.", "finish_custom_troop",[(call_script, "script_start_customizing", "$g_talk_troop")]],
  [anyone,"finish_custom_troop", [], "Very good {sir/madam}. I will put on the new gear now.", "finish_custom_response",[]],
  [anyone|plyr,"finish_custom_response", [], "Carry on.", "close_window",[(call_script, "script_finish_customizing", "$g_talk_troop")]],
# Custom Troops end
##

###diplomacy start+
#Allow viewing (but not changing) of the equipment of the troops you are leading.
#Code credit to rubik's Custom Commander, with minor string changes.
## CC view regular's equipment
  [anyone|plyr,"regular_member_talk", [],
   "Let me see your equipment.", "dplmc_view_regular_inventory", []
  ],
  [anyone,"dplmc_view_regular_inventory",
    [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),], "Very well {s0}, here is what I am using...", "dplmc_do_view_regular_inventory",#Use {s0} instead of {sir/madam}
    [
      (call_script, "script_dplmc_copy_inventory", "$g_player_troop", "trp_temp_array_a"),
      (call_script, "script_dplmc_copy_inventory", "$g_talk_troop", "trp_temp_array_b"),

      (try_for_range, ":i_slot", 0, 10),
        (troop_get_inventory_slot, ":item", "trp_temp_array_b", ":i_slot"),
        (gt, ":item", -1),
        (troop_get_inventory_slot_modifier, ":imod", "trp_temp_array_b", ":i_slot"),
        (troop_add_item,"trp_temp_array_b", ":item", ":imod"),
        (troop_set_inventory_slot, "trp_temp_array_b", ":i_slot", -1),
      (try_end),

      (change_screen_loot, "trp_temp_array_b"),
    ]],
  [anyone,"dplmc_do_view_regular_inventory", [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
   "Is that satisfactory, {s0}?", "dplmc_do_view_regular_inventory_2", []#Use {s0} instead of {sir/madam}
  ],
  [anyone|plyr,"dplmc_do_view_regular_inventory_2", 
    [
      (call_script, "script_dplmc_copy_inventory", "trp_temp_array_a", "$g_player_troop"),
    ],
   "Indeed.", "do_regular_member_view_char", []
  ],
## CC view regular's equipment
##diplomacy end+

  [anyone|plyr,"regular_member_talk", [], "Nothing. Keep moving.", "close_window",[]],





######################################
# GENERIC PARTY ENCOUNTER
######################################

  [anyone,"start", [(eq,"$talk_context",tc_party_encounter),
                    (gt,"$encountered_party_hostile",0),
                    (encountered_party_is_attacker),
                    ],
   "You have no chance against us. Surrender now or we will kill you all...", "party_encounter_hostile_attacker",
   [(try_begin),
				##Floris MTT begin
      (this_or_next|eq,"$g_encountered_party_template","pt_steppe_bandits"),
      (this_or_next|eq,"$g_encountered_party_template","pt_steppe_bandits_r"),
      (eq,"$g_encountered_party_template","pt_steppe_bandits_e"),
      (play_sound, "snd_encounter_steppe_bandits"),
				##Floris MTT end
    (try_end)]],
#  [anyone|plyr,"party_encounter_hostile_attacker", [
#                    ],
#   "I will pay you 1000 denars if you just let us go.", "close_window", []],
  [anyone|plyr,"party_encounter_hostile_attacker", [
                    ],
   "We will fight you to the end!", "close_window", []],
  [anyone|plyr,"party_encounter_hostile_attacker", [
                    ],
   "Don't attack! We surrender.", "close_window", [(assign,"$g_player_surrenders",1)]],

  [anyone,"start", [(eq,"$talk_context",tc_party_encounter),
                    (neg|encountered_party_is_attacker),
                    ],
   "What do you want?", "party_encounter_hostile_defender",
   []],

  [anyone|plyr,"party_encounter_hostile_defender", [],
   "Surrender or die!", "party_encounter_hostile_ultimatum_surrender", [

       ]],

#post 0907 changes begin
  [anyone,"party_encounter_hostile_ultimatum_surrender", [],
   "{s43}", "close_window", [
       (call_script, "script_lord_comment_to_s43", "$g_talk_troop", "str_lord_challenged_default"),
	 
##Floris - Bugfix for DPLMC patrols 
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_patrol),
	   (store_relation,":rel", "$g_encountered_party_faction","fac_player_supporters_faction"),
		(try_begin),
		  (gt, ":rel", 0),
		  (val_sub, ":rel", 10),
		(try_end),
		(val_sub, ":rel", 5),
		(call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":rel"),
	### Troop commentaries changes begin
		(call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
	### Troop commentaries changes end
##Floris - Bugfix end	   
       ]],
#post 0907 changes end

  [anyone|plyr,"party_encounter_hostile_defender", [],
   "Nothing. We'll leave you in peace.", "close_window", [(assign, "$g_leave_encounter",1)]],








  [anyone|auto_proceed, "start",
  [
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    (check_quest_active, "qst_collect_men"),
    #(neq, "$talk_context", tc_tavern_talk),
    #(neq, "$talk_context", tc_back_alley),
    (eq, "$talk_context", tc_merchants_house),
  ],
  "{!}.", "merchant_end", []],

  [anyone, "merchant_end", [],
  "Heh! I must really be in a tight spot, to place my hopes in a passing stranger. However, something about you tells me that my trust is not misplaced. Now, go see if you can round up some volunteers.", "close_window", []],

  [anyone, "start",
  [
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    (eq, "$talk_context", tc_merchants_house),
    (check_quest_active, "qst_save_town_from_bandits"),

    (store_div, ":number_of_civilian_loses_div_2", "$number_of_civilian_loses", 2),

    (try_begin),
      (eq, "$g_killed_first_bandit", 1),
      (store_add, ":player_success", "$number_of_bandits_killed_by_player", 1),
    (else_try),
      (store_add, ":player_success", "$number_of_bandits_killed_by_player", 0),
    (try_end),

    (val_sub, ":player_success", ":number_of_civilian_loses_div_2"),
    (val_max, ":player_success", 0),

    (call_script, "script_change_player_relation_with_center", "$g_starting_town", ":player_success"),

    (try_begin),
      (eq, "$g_killed_first_bandit", 1),
      (gt, "$number_of_bandits_killed_by_player", 2),
      (str_store_string, s3, "str_you_fought_well_at_town_fight_survived"),
      (troop_add_gold, "trp_player", 200),
    (else_try),
      (eq, "$g_killed_first_bandit", 1),
      (gt, "$number_of_bandits_killed_by_player", 0),
      (str_store_string, s3, "str_you_fought_normal_at_town_fight_survived"),
      (troop_add_gold, "trp_player", 200),
    (else_try),
      (eq, "$g_killed_first_bandit", 1),
      (eq, "$number_of_bandits_killed_by_player", 0),
      (str_store_string, s3, "str_you_fought_bad_at_town_fight_survived"),
      (troop_add_gold, "trp_player", 100),
    (else_try),
      (eq, "$g_killed_first_bandit", 0),
      (ge, "$number_of_bandits_killed_by_player", 2),
      (str_store_string, s3, "str_you_fought_well_at_town_fight"),
      (troop_add_gold, "trp_player", 100),
    (else_try),
      (str_store_string, s3, "str_you_wounded_at_town_fight"),
      (troop_add_gold, "trp_player", 100),
    (try_end),

    (try_begin),
      (ge, "$number_of_civilian_loses", 1),
      (assign, reg0, "$number_of_civilian_loses"),
      (str_store_string, s2, "str_unfortunately_reg0_civilians_wounded_during_fight_more"),
    (else_try),
      (eq, "$number_of_civilian_loses", 1),
      (assign, reg0, "$number_of_civilian_loses"),
      (str_store_string, s2, "str_unfortunately_reg0_civilians_wounded_during_fight"),
    (else_try),
      (str_store_string, s2, "str_also_one_another_good_news_is_any_civilians_did_not_wounded_during_fight"),
    (try_end),

    (call_script, "script_succeed_quest", "qst_save_town_from_bandits"),
    (call_script, "script_end_quest", "qst_save_town_from_bandits"),
  ],
  "{s3}{s2}", "merchant_quest_4e",
  []],

  [anyone|plyr,"merchant_quest_4e",
  [
    (try_begin),
      (eq, "$g_killed_first_bandit", 1),
      (gt, "$number_of_bandits_killed_by_player", 2),
      (str_store_string, s1, "str_you_fought_well_at_town_fight_survived_answer"),
    (else_try),
      (eq, "$g_killed_first_bandit", 1),
      (gt, "$number_of_bandits_killed_by_player", 0),
      (str_store_string, s1, "str_you_fought_normal_at_town_fight_survived_answer"),
    (else_try),
      (eq, "$g_killed_first_bandit", 1),
      (eq, "$number_of_bandits_killed_by_player", 0),
      (str_store_string, s1, "str_you_fought_bad_at_town_fight_survived_answer"),
    (else_try),
      (eq, "$g_killed_first_bandit", 0),
      (ge, "$number_of_bandits_killed_by_player", 2),
      (str_store_string, s1, "str_you_fought_well_at_town_fight_answer"),
    (else_try),
      (str_store_string, s1, "str_you_wounded_at_town_fight_answer"),
    (try_end),
  ],
  "{s1}", "merchant_finale",
  [
    (assign, "$dialog_with_merchant_ended", 1),
  ]],

  #[anyone|auto_proceed, "start",
  #[
  #  (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
  #  (eq, "$talk_context", tc_merchants_house),
  #  (check_quest_finished, "qst_save_town_from_bandits"),
  #],
  #"{!}.", "merchant_all_quest_completed",
  #[
  #]],


  [anyone|plyr,"merchant_quest_4e",
  [
  ],
  "The Heavens alone grant us victory.", "merchant_finale",
[  (assign, "$dialog_with_merchant_ended", 1),
  ]],

  [anyone|plyr,"merchant_quest_4e",
  [],
  "I'm glad to see that you're alive, too.", "merchant_finale",
  [
    (assign, "$dialog_with_merchant_ended", 1),
  ]],

  [anyone,"merchant_finale", [
  (faction_get_slot, ":faction_leader", "$g_encountered_party_faction", slot_faction_leader),
  (str_store_troop_name, s5, ":faction_leader"),
  ],
  "Yes, yes... Now, a couple of my boys have the watch captain pinned down in a back room, with a knife at his throat. I''ll need to go drag him before {s5} and explain what this breach of the peace is all about. You don't need to be part of that, though. I'll tell you what -- if all goes well, I'll meet you in the tavern again shortly, and let you know how it all came out. If you don't see me in the tavern, but instead see my head on a spike over the city gate, I'll assume you know enough to stay out of town for a while and forget this whole episode ever happened. So -- hopefully we'll meet again!", "close_window",
[
(assign, "$g_do_one_more_meeting_with_merchant", 2),
# (assign, "$g_do_one_more_meeting_with_merchant", 1), no need to this, do not open this line, it is already assigning while leaving mission.
# (jump_to_menu, "mnu_town"),
# (finish_mission, 0),
]],



  [anyone, "start",
  [
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    (eq, "$talk_context", tc_merchants_house),
    (neg|check_quest_finished, "qst_collect_men"),
    (eq, "$current_startup_quest_phase", 1),

    (try_begin),
      (eq, "$g_killed_first_bandit", 1),
      (str_store_string, s1, "str_are_you_all_right"),
    (else_try),
      (str_store_string, s1, "str_you_are_awake"),
    (try_end),
  ],
  "{s1}", "merchant_quest_1_prologue_1",
  []],

  [anyone,"merchant_quest_1_prologue_1",
  [
  ],
  "We've always had brigands in the hills, driven to banditry by war, debt, or love of violence. Recently, however, they've been getting bolder -- leaving their camps in the wild and venturing into town, looking for unwary prey. The watch commander tells us it's because of all the fighting on the frontiers -- fewer men to keep an eye on the streets -- but I'm not sure what to make of that. It seems to me that the most logical explanation is that these bandits have an ally inside the walls, who helps them enter unnoticed and helps them identify particularly tempting targets... Last week, you see, they took my brother.", "merchant_quest_1_prologue_2",
  []],

  [anyone,"merchant_quest_1_prologue_2",
  [],
  "I don't know what my brother was thinking -- a lad from a prominent house, out alone after dark in times like these... Well, I suppose you were too, but you're a stranger here, and didn't know how bad things have become. He had no such excuse. But he's family, so what can you do? If you don't protect your kin, then people will start thinking that you can't protect your investements, either, and I can't have that... No doubt the gang will soon send word about a ransom, but I don't care to pay it.", "merchant_quest_1_prologue_3",[]],


  [anyone,"merchant_quest_1_prologue_3",
  [],
  "So here's my proposition. You look like you've had a bit of experience with a blade -- and more importantly, you must have a bit of fire in your belly, or you wouldn't be coming to Calradia to seek your fortune. So here's what I'm asking you to do: gather a small party, track down these bandits to their lair, teach them a lesson they won't forget, and get my brother back safe. In return, you'll earn my lasting gratitude and a bit of silver. What do you say?", "merchant_quest_1a",[]],

  [anyone|plyr,"merchant_quest_1a",
  [
  ],
  "I am interested.", "merchant_quest_1b",[]],

  [anyone|plyr,"merchant_quest_1a",
  [
  ],
  "I am not interested, have more important business to do.", "close_window",
  [
    (assign, "$dialog_with_merchant_ended", 1),
  ]],
  
  ##diplomacy start+ Allow skipping the tutorial.
  [anyone|plyr,"merchant_quest_1a",
  [
     (ge, "$cheat_mode", 1),
  ],
  "{!}[CHEAT] I have played this before, and would prefer to skip the tutorial.", "dplmc_devel_merchant_quest_skip",
  []],
  
  [anyone,"dplmc_devel_merchant_quest_skip",
  [],
  "{!}Okay.  I'll just give you the reward, and we can assume that all of this already happened.", "close_window",
  [
	#Setup quest 1: recruit 5 men
	(troop_add_gold, "trp_player", 100),
    (str_store_troop_name, s9, "$g_talk_troop"),
    (str_store_party_name, s1, "$g_starting_town"),
    (str_store_string, s2, "str_start_up_quest_message_1"),
	(call_script, "script_start_quest", "qst_collect_men", "$g_talk_troop"),
	(party_get_position, pos1, "$current_town"),
	#Finish quest 1
	(call_script, "script_succeed_quest", "qst_collect_men"),
	(call_script, "script_end_quest", "qst_collect_men"),
	#Setup quest 2: find location of brother
	(str_store_party_name, s9, "$current_town"),
	(str_store_string, s2, "str_start_up_quest_message_2"),
	(call_script, "script_start_quest", "qst_learn_where_merchant_brother_is", "$g_talk_troop"),
	#Finish quest 2
	(call_script, "script_succeed_quest", "qst_learn_where_merchant_brother_is"),
	(call_script, "script_end_quest", "qst_learn_where_merchant_brother_is"),
	#Setup quest 3: rescue brother 
	(str_store_troop_name, s10, "$g_talk_troop"),
	(str_store_string, s2, "str_find_the_lair_near_s9_and_free_the_brother_of_the_prominent_s10_merchant"),
	(call_script, "script_start_quest", "qst_save_relative_of_merchant", "$g_talk_troop"),
	#Finish quest 3
	(assign, "$relative_of_merchant_is_found", 1),
	(call_script, "script_succeed_quest", "qst_save_relative_of_merchant"),
	(call_script, "script_finish_quest", "qst_save_relative_of_merchant", 100),
	(troop_add_gold, "trp_player", 200),
	#Setup quest 4: fight bandits
	(str_store_party_name_link, s9, "$g_starting_town"),
	(str_store_string, s2, "str_save_town_from_bandits"),
	(call_script, "script_start_quest", "qst_save_town_from_bandits", "$g_talk_troop"),
	#Finish quest 4
	(assign, "$current_startup_quest_phase", 4),
	(call_script, "script_change_player_relation_with_center", "$g_starting_town", 1),
	(troop_add_gold, "trp_player", 200),
    (call_script, "script_succeed_quest", "qst_save_town_from_bandits"),
    (call_script, "script_end_quest", "qst_save_town_from_bandits"),
	#So he'll reappear in the tavern (unless you don't immediately speak with him)
	(assign, "$dialog_with_merchant_ended", 1),
	(assign, "$g_do_one_more_meeting_with_merchant", 1),
	#Fix a subsequent-dialog bug if you speak with him again in his house at the start
	(neg|is_between, "$g_encountered_party_faction", npc_kingdoms_begin, npc_kingdoms_end),
	(store_faction_of_party, "$g_encountered_party_faction", "$g_starting_town"),
  ]],
  ##diplomacy end+

  [anyone,"merchant_quest_1b",
  [
  ],
  "You won't be able to do this by yourself, though. If you try and take on the whole gang singlehandedly, the hunter will become the hunted, I'll warrant. You'll first want to round up a group of volunteers. There's always a few lads in the villages around here, looking for a bit of work that's more interesting than tilling the soil or hauling water. They'll follow you if you pay. So... Take this purse of 100 denars. Consider it an advance on your reward. Go round to the villages, and use the money to hire some help. I'll reckon that you need at least five men to take on these bandits.", "merchant_quest_1c",
  [
    (call_script, "script_troop_add_gold", "trp_player", 100),

    (str_store_troop_name, s9, "$g_talk_troop"),
    (str_store_party_name, s1, "$g_starting_town"),
    (str_store_string, s2, "str_start_up_quest_message_1"),

    (call_script, "script_start_quest", "qst_collect_men", "$g_talk_troop"),

    (party_get_position, pos1, "$current_town"),
  ]],

  [anyone|plyr,"merchant_quest_1c",
  [
  ],
  "Very good, sir. I'll go collect some men from around the villages.", "merchant_quest_1d",[]],

  [anyone,"merchant_quest_1d",
  [
    (str_store_party_name, s1, "$current_town"),
  ],
  "Good. You can find me again in the tavern here in {s1} after you've got your group together. Then we'll speak about what we do next.", "close_window",
  [
    (assign, "$dialog_with_merchant_ended", 1),
  ]],

## Floris - STAT Dialogs 
##Town Specialists - Monk, Merchant

  [anyone, "start", [
					(this_or_next|is_between,"$g_talk_troop",town_specialist_begin,town_specialist_end),
					(this_or_next|is_between,"$g_talk_troop",village_specialist_begin,village_specialist_end),
					(is_between,"$g_talk_troop",castle_specialist_begin,castle_specialist_end),
                    (party_get_slot, ":economy_troop", "$current_town", slot_center_specialist_type),
                    (party_get_slot, ":economy_amount", "$current_town", slot_center_specialist_amount),
                    (gt, ":economy_amount", 0),
                    (store_sub, reg3, ":economy_amount", 1),
                    (store_sub, reg4, reg3, 1),
                    (call_script, "script_game_get_join_cost", ":economy_troop"),
                    (assign, ":join_cost", reg0),
                    (store_mul, reg5, ":economy_amount", reg0),
                    (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
                    (val_min, ":economy_amount", ":free_capacity"),
                    (store_troop_gold, ":cur_gold", "trp_player"),
                    (try_begin),
						(gt, ":join_cost", 0),
						(val_div, ":cur_gold", ":join_cost"),
						(val_min, ":economy_amount", ":cur_gold"),
                    (try_end),
                    (assign, "$temp", ":economy_amount"),
					(try_begin),
						(eq, "$g_talk_troop", "trp_skill_merchant"),
						(str_store_string, s17,
							"@Do you have a need for merchants, {sir/madam}?\
 {reg3?Me and {reg4?{reg3} of my mates:one of my mates} are:I am} looking for a master.\
 We'll join you for {reg5} denars."),
					(else_try),
						(eq, "$g_talk_troop", "trp_skill_monk"),
						(str_store_string, s17,
							"@Do you have a need for monks, {sir/madam}?\
 {reg3?Me and {reg4?{reg3} of my mates:one of my mates} are:I am} looking for a master.\
 We'll join you for {reg5} denars."),
					(else_try),
						(str_store_string, s17,
							"@Do you have a need for troops, {sir/madam}?\
 {reg3?Me and {reg4?{reg3} of my mates:one of my mates} are:I am} looking for a master.\
 We'll join you for {reg5} denars."),
					(try_end),
                    ],
   "{s17}", "economy_troops_talk", []],  

  [anyone, "start", [
  #(is_between,"$g_talk_troop",town_specialists_begin,town_specialists_end),
  ],
   "Anything else, {sir/madam}?", "economy_after_recruited", []],

  [anyone|plyr, "economy_after_recruited", [],
   "Make your preparations. We'll be moving at dawn.", "economy_after_recruited_2", []],
  [anyone|plyr, "economy_after_recruited", [],
   "Take your time. We'll be staying in this town for a while.", "economy_after_recruited_2", []], 
   
     [anyone|plyr, "economy_after_recruited_2", [],
   "Of course, master.", "close_window", []], 
 
  [anyone|plyr, "economy_troops_talk", [(try_begin),     #More Mercaneries Tavern
                                          (party_get_slot, ":economy_troop", "$current_town", slot_center_specialist_type),
                                          (eq, "$g_talk_troop", ":economy_troop"),                     
                                          (party_get_slot, ":economy_amount", "$current_town", slot_center_specialist_amount),
                                          (try_end),
                                          (eq, ":economy_amount", "$temp"),
                                          (call_script, "script_game_get_join_cost", ":economy_troop"),
                                          (store_mul, reg5, "$temp", reg0), #Tavern End
                                          ],
   "All right. I will hire you. Here is {reg5} denars.", "economy_talk_hire", []],

  [anyone, "economy_talk_hire", [(store_random_in_range, ":rand", 0, 4),
                                          (try_begin),
                                            (eq, ":rand", 0),
                                            (gt, "$temp", 1),
                                            (str_store_string, s17,
                                             "@You chose well, {sir/madam}. My lads know how to keep their word and earn their pay."),
                                          (else_try),
                                            (eq, ":rand", 1),
											(eq, "$g_talk_troop", "trp_skill_merchant"),											
                                            (str_store_string, s17,
                                             "@Well done, {sir/madam}. Keep the money and wine coming our way, and there's no deal in Calradia you cant make."),
                                          (else_try),
                                            (eq, ":rand", 2), 
											(eq, "$g_talk_troop", "trp_skill_merchant"),
                                            (str_store_string, s17,
                                             "@We are at your service, {sir/madam}. Point us in the direction of a market, and we'll do the rest."),
                                          (else_try),
											(eq, "$g_talk_troop", "trp_skill_merchant"),
                                            (str_store_string, s17,
                                             "@You wont find better merchants in all of Calradia."),
											(else_try),
												(str_store_string, s17,
                                             "@You won't regret this."),
                                          (try_end),],
   "{s17}", "close_window", [
                                          (try_begin),
                                          (party_get_slot, ":economy_troop", "$current_town", slot_center_specialist_type),
                                          (eq, "$g_talk_troop", ":economy_troop"),                     
                                          (assign, ":slot", slot_center_specialist_amount),
                                          (try_end),
                                          (call_script, "script_game_get_join_cost", ":economy_troop"),
                                          (store_mul, ":total_cost", "$temp", reg0),
                                          (troop_remove_gold, "trp_player", ":total_cost"),
                                          (party_add_members, "p_main_party", ":economy_troop", "$temp"),
										  (party_set_slot, "$current_town", ":slot", 0),
                                          ]],

  [anyone|plyr, "economy_troops_talk", [(eq, "$temp", 0),
                                          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
                                          (ge, ":free_capacity", 1)],
   "That sounds good. But I can't afford to hire any more men right now.", "economy_cant_lead", []],
  
  [anyone, "economy_cant_lead", 
  [(eq, "$g_talk_troop", "trp_skill_merchant"),], "That's a pity. Well, {reg3?we will:I will} be looking for deals around here for a while,\
 if you reconsider our business proposal.", "close_window", []],
 
  [anyone, "economy_cant_lead", [], "Maybe another time then.", "close_window", []],
  
  [anyone|plyr, "economy_troops_talk", [(eq, "$temp", 0),
                                          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
                                          (eq, ":free_capacity", 0)],
   "That sounds good. But I can't lead any more men right now.", "economy_cant_lead", []],


  [anyone|plyr, "economy_troops_talk", [],
   "Sorry. I don't need any other men right now.", "close_window", []],
 
 
  #[anyone, "merchant_all_quest_completed", 
  #[
  #],
  #"TODO-STARTUP : You can leave now.", "close_window",
  #[
  #]],

  [anyone,"start", [], "Surrender or die. Make your choice", "battle_reason_stated",[]],
  [anyone|plyr,"battle_reason_stated", [], "I am not afraid of you. I will fight.", "close_window",[[encounter_attack]]],

  [anyone,"start", [], "Hello. What can I do for you?", "free",[]],
  [anyone|plyr,"free", [[neg|in_meta_mission]], "Tell me about yourself", "view_char_requested",[]],
  [anyone,"view_char_requested", [], "Very well, listen to this...", "view_char",[[change_screen_view_character]]],
  [anyone,"view_char", [], "Anything else?", "free",[]],

  [anyone|plyr,"end", [], "[Done]", "close_window",[]],

  [anyone|plyr,"start", [], "Drop your weapons and surrender if you want to live", "threaten_1",[]],
  [anyone,"threaten_1", [], "We will fight you first", "end",[[encounter_attack]]],

#  [anyone|plyr,"free", [[partner_is_mercmaster]], "I need to hire some mercenaries.", "mercenaries_requested",[]],
#  [anyone,"mercenaries_requested", [], "I have the toughest fighters in all Calradia.", "buy_mercenaries",[[change_screen_buy_mercenaries]]],
#  [anyone,"buy_mercenaries", [], "Anything else?", "free",[]],

#  [anyone|plyr,"free", [[partner_is_recruitable]], "I need a capable sergeant like yourself. How much do you ask to work for me?", "employ_mercenary_requested",[]],
#  [anyone,"employ_mercenary_requested", [[store_mercenary_price,0],[store_mercenary_wage,1]], "I want {reg0} denars now and {reg1} denars as monthly payment.", "employ_mercenary_2",[]],
#  [anyone|plyr,"employ_mercenary_2", [], "I see I need to think of this.", "employ_mercenary_giveup",[]],
#  [anyone|plyr,"employ_mercenary_2", [[neg|hero_can_join]], "I don't have any more room in my party right now. I will talk to you again later.", "employ_mercenary_giveup",[]],
#  [anyone|plyr,"employ_mercenary_2", [[player_gold_ge,reg(0)],[hero_can_join]], "That's fine. Here's the {reg0} denars. From now on you work for me.", "employ_mercenary_commit",[[troop_remove_gold, "trp_player",reg(0)],[recruit_mercenary]]],
#  [anyone,"employ_mercenary_giveup", [], "Suits me.", "free",[]],
#  [anyone,"employ_mercenary_commit", [], "You got yourself the best fighter in the land.", "end",[]],


  [anyone,"member_direct_campaign", [], "Yes, {my lord/my lady}. Which message do you wish to send to the vassals?", "member_direct_campaign_choice",
  []],



  [anyone|plyr,"member_direct_campaign_choice",
   [
#     (eq, "$g_talk_troop_faction", "$players_kingdom"),
	 (this_or_next|neg|faction_slot_ge, "$players_kingdom", slot_faction_marshall, active_npcs_begin),
		(eq, "$players_kingdom", "fac_player_supporters_faction"),
     (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
		(faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_feast),
     ],
   "I want to start a new campaign. Let us assemble the army here.", "member_direct_campaign_call_to_arms_verify",
   [
     (faction_get_slot, ":old_marshall", "$players_kingdom", slot_faction_marshall),
     (try_begin),
        (ge, ":old_marshall", 0),
		(troop_get_slot, ":old_marshall_party", ":old_marshall", slot_troop_leaded_party),
        (party_is_active, ":old_marshall_party"),
        (party_set_marshall, ":old_marshall_party", 0),
     (try_end),

    (faction_set_slot, "$players_kingdom", slot_faction_marshall, "trp_player"),
   ]],

  [anyone|plyr,"member_direct_campaign_choice",
   [
#     (eq, "$g_talk_troop_faction", "$players_kingdom"),
     (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_feast),
     ],
   "I want to end the campaign and let everyone return home.", "member_give_order_disband_army_verify", []],

  [anyone|plyr,"member_direct_campaign_choice",
   [
#     (eq, "$g_talk_troop_faction", "$players_kingdom"),
     (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_feast),
	 (check_quest_active, "qst_organize_feast"),
	 (quest_get_slot, ":venue", "qst_organize_feast", slot_quest_target_center),
	 (store_faction_of_party, ":venue_faction", ":venue"),
	 (eq, ":venue_faction", "$players_kingdom"),
	 (str_store_party_name, s4, ":venue"),
     ],
   "I wish to invite the vassals of the realm to a feast at {s4}.", "member_give_order_invite_feast_verify", []],




  [anyone|plyr,"member_direct_campaign_choice",
   [
     ],
   "Never mind", "member_pretalk",
   []],




  [anyone,"member_give_order_invite_feast_verify", [],
   "You wish to invite the lords of the realm to a feast?", "member_give_order_invite_feast_verify_2",[]],

  [anyone|plyr,"member_give_order_invite_feast_verify_2", [], "Yes. It is time for us to strengthen the bonds that bring us together.", "member_give_order_invite_feast",[]],
  [anyone|plyr,"member_give_order_invite_feast_verify_2", [], "On second thought, this is perhaps not the time.", "member_pretalk",[]],

  [anyone,"member_give_order_invite_feast",
   [
	 (quest_get_slot, ":venue", "qst_organize_feast", slot_quest_target_center),
     (str_store_party_name, s4, ":venue"),
   ],
   "All right then. I shall dispatch messengers informing the lords of the realm of your feast at {s4}.", "member_pretalk",
   [
	 (quest_get_slot, ":venue", "qst_organize_feast", slot_quest_target_center),

	 (assign, "$player_marshal_ai_state", sfai_feast),
	 (assign, "$player_marshal_ai_object", ":venue"),
     (call_script, "script_decide_faction_ai", "$players_kingdom"),
	 (assign, "$g_recalculate_ais", 1),
	 (str_store_party_name, s4, ":venue"),

     ]],





  [anyone,"member_direct_campaign_call_to_arms_verify", [],
   "You wish to summon all lords for a new campaign?", "member_give_order_call_to_arms_verify_2",[]],

  [anyone|plyr,"member_give_order_call_to_arms_verify_2", [], "Yes. We must gather all our forces before we march on the enemy.", "member_give_order_call_to_arms",[]],
  [anyone|plyr,"member_give_order_call_to_arms_verify_2", [], "On second thought, it won't be necessary to summon everyone.", "member_pretalk",[]],

  [anyone,"member_give_order_call_to_arms",
   [],
   "All right then. I will send messengers and tell everyone to come here.", "member_pretalk",
   [
	 (assign, "$player_marshal_ai_state", sfai_gathering_army),
	 (assign, "$player_marshal_ai_object", "p_main_party"),
     (call_script, "script_decide_faction_ai", "$players_kingdom"),
	 (assign, "$g_recalculate_ais", 1),
     ]],


  [anyone,"member_give_order_disband_army_verify", [],
   "You want to end the current campaign and release all lords from duty?", "member_give_order_disband_army_2",[]],

  [anyone|plyr,"member_give_order_disband_army_2", [], "Yes. We no longer need all our forces here.", "member_give_order_disband_army",[]],
  [anyone|plyr,"member_give_order_disband_army_2", [], "On second thought, it will be better to stay together for now.", "member_pretalk",[]],

  [anyone,"member_give_order_disband_army",
   [],
   "All right. I will let everyone know that they are released from duty.", "member_pretalk",
   [
	 (assign, "$player_marshal_ai_state", sfai_default),
	 (assign, "$player_marshal_ai_object", -1),
     (call_script, "script_decide_faction_ai", "$players_kingdom"),
	 (assign, "$g_recalculate_ais", 1),

     ]],


  [anyone,"mayor_wealth_comparison_1",[

  (assign, ":wealthiest_center", "$g_encountered_party"),
  (assign, ":poorer_centers", 0),
  (assign, ":richer_centers", 0),

  (party_get_slot, ":wealthiest_center_wealth", "$g_encountered_party", slot_town_prosperity),
  (party_get_slot, ":mayor_center_wealth", "$g_encountered_party", slot_town_prosperity),

  (try_for_range, ":other_center", towns_begin, towns_end),
	(neq, ":other_center", "$g_encountered_party"),
	(party_get_slot, ":other_center_wealth", ":other_center", slot_town_prosperity),
	(try_begin),
		(gt, ":other_center_wealth", ":wealthiest_center_wealth"),
		(val_add, ":richer_centers", 1),
		(assign, ":wealthiest_center", ":other_center"),
		(assign, ":wealthiest_center_wealth", ":other_center_wealth"),
    (else_try),
		(gt, ":other_center_wealth", ":mayor_center_wealth"),
		(val_add, ":richer_centers", 1),
    (else_try),
		(val_add, ":poorer_centers", 1),
    (try_end),
  (try_end),

  (assign, reg4, ":richer_centers"),
  (assign, reg5, ":poorer_centers"),
  (str_store_party_name, s5, "$g_encountered_party"),
  (str_store_party_name, s4, ":wealthiest_center"),
	
  ], "Overall, the wealthiest town in Calradia is known to be {s4}. Here in {s5}, we are poorer than {reg4} towns, and richer than {reg5}.", "mayor_wealth_comparison_2",[
  ]],
  #Production of this town
  #Production of the hinterland
  #Volume of trade

  [anyone,"mayor_wealth_comparison_2",[

  (assign, ":wealthiest_center", "$g_encountered_party"),
  (assign, ":poorer_centers", 0),
  (assign, ":richer_centers", 0),

  (assign, ":mayor_town_production", 0),
  (try_for_range, ":item_kind_id", trade_goods_begin, trade_goods_end),
	(call_script, "script_center_get_production", "$g_encountered_party", ":item_kind_id"),
	(val_add, ":mayor_town_production", reg0),
  (try_end),
  (assign, ":wealthiest_town_production", ":mayor_town_production"),

  (try_begin),
	(ge, "$cheat_mode", 1),
	(assign, reg4, ":mayor_town_production"),
	(str_store_party_name, s4, "$g_encountered_party"),
	(display_message, "@{!}DEBUG -- Total production for {s4}: {reg4}"),
  (try_end),


  (try_for_range, ":other_center", towns_begin, towns_end),
	(neq, ":other_center", "$g_encountered_party"),
	(assign, ":other_town_production", 0),
	(try_for_range, ":item_kind_id", trade_goods_begin, trade_goods_end),
		(call_script, "script_center_get_production", ":other_center", ":item_kind_id"),
		(val_add, ":other_town_production", reg0),
	(try_end),
	(try_begin),
		(ge, "$cheat_mode", 1),
		(assign, reg4, ":other_town_production"),
		(str_store_party_name, s4, ":other_center"),
		(display_message, "@{!}DEBUG -- Total production for {s4}: {reg4}"),
	(try_end),

	(try_begin),
		(gt, ":other_town_production", ":wealthiest_town_production"),
		(val_add, ":richer_centers", 1),
		(assign, ":wealthiest_center", ":other_center"),
		(assign, ":wealthiest_town_production", ":other_town_production"),
    (else_try),
		(gt, ":other_town_production", ":mayor_town_production"),
		(val_add, ":richer_centers", 1),
    (else_try),
		(val_add, ":poorer_centers", 1),
    (try_end),
  (try_end),

  (assign, reg4, ":richer_centers"),
  (assign, reg5, ":poorer_centers"),
  (str_store_party_name, s5, "$g_encountered_party"),
  (str_store_party_name, s4, ":wealthiest_center"),

  ], "In terms of local industry, the most productive town in Calradia is known to be {s4}. Here in {s5}, we produce less than {reg4} towns, and produce more than {reg5}. Production is of course affected by the supply of raw materials, as well as by the overall prosperity of the town.", "mayor_wealth_comparison_3",[
  ]],

  [anyone,"mayor_wealth_comparison_3",[

  (assign, ":wealthiest_center", "$g_encountered_party"),
  (assign, ":poorer_centers", 0),
  (assign, ":richer_centers", 0),

  (try_for_range, ":town", towns_begin, towns_end),
	(party_set_slot, ":town", slot_party_temp_slot_1, 0),
  (try_end),

  (try_for_range, ":village", villages_begin, villages_end),
	(assign, ":village_good_production", 0),
	(try_for_range, ":item_kind_id", trade_goods_begin, trade_goods_end),
		(call_script, "script_center_get_production", ":village", ":item_kind_id"),
		(val_add, ":village_good_production", reg0),
	(try_end),
	(party_get_slot, ":market_town", ":village", slot_village_market_town),
	(party_get_slot, ":market_center_production", ":market_town", slot_party_temp_slot_1),
	(val_add, ":market_center_production", ":village_good_production"),
	(party_set_slot, ":market_town", slot_party_temp_slot_1, ":market_center_production"),
  (try_end),


  (party_get_slot, ":mayor_town_production", "$g_encountered_party", slot_party_temp_slot_1),
  (assign, ":wealthiest_town_production", ":mayor_town_production"),

  (try_begin),
	(ge, "$cheat_mode", 1),
	(assign, reg4, ":mayor_town_production"),
	(str_store_party_name, s4, "$g_encountered_party"),
	(display_message, "@{!}DEBUG -- Total rural production for {s4} region: {reg4}"),
  (try_end),


  (try_for_range, ":other_center", towns_begin, towns_end),
	(neq, ":other_center", "$g_encountered_party"),
	(party_get_slot, ":other_town_production", ":other_center", slot_party_temp_slot_1),

	(try_begin),
		(ge, "$cheat_mode", 1),
		(assign, reg4, ":other_town_production"),
		(str_store_party_name, s4, ":other_center"),
		(display_message, "@{!}DEBUG -- Total rural production for {s4} region: {reg4}"),
	(try_end),

	(try_begin),
		(gt, ":other_town_production", ":wealthiest_town_production"),
		(val_add, ":richer_centers", 1),
		(assign, ":wealthiest_center", ":other_center"),
		(assign, ":wealthiest_town_production", ":other_town_production"),
    (else_try),
		(gt, ":other_town_production", ":mayor_town_production"),
		(val_add, ":richer_centers", 1),
    (else_try),
		(val_add, ":poorer_centers", 1),
    (try_end),
  (try_end),

  (assign, reg4, ":richer_centers"),
  (assign, reg5, ":poorer_centers"),
  (str_store_party_name, s5, "$g_encountered_party"),
  (str_store_party_name, s4, ":wealthiest_center"),

  ], "In terms of the output of the surrounding villages, the town of {s4} is the richest in Calradia. Here in {s5}, the villages produce less than the hinterland around {reg4} towns, and produce more than {reg5}. The wealth of a town's hinterland, of course, is heavily dependent on the tides of war. Looting and pillage, and shifts in territory, can make a major impact.", "mayor_wealth_comparison_4",[
  ]],


  [anyone,"mayor_wealth_comparison_4",[

  (assign, ":wealthiest_center", "$g_encountered_party"),
  (assign, ":poorer_centers", 0),
  (assign, ":richer_centers", 0),

  (try_for_range, ":town", towns_begin, towns_end),
	(party_set_slot, ":town", slot_party_temp_slot_1, 0),
  (try_end),

  (try_for_range, ":log_entry_iterator", 0, "$num_log_entries"),
	(store_sub, ":log_entry_no", "$num_log_entries", ":log_entry_iterator"),
    (troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_party_traded),

    (troop_get_slot, ":event_time",            "trp_log_array_entry_time",              ":log_entry_no"),
	(store_current_hours, ":cur_hour"),
	(store_sub, ":hours_ago", ":cur_hour", ":event_time"),
	(lt, ":hours_ago", 1344),

    (troop_get_slot, ":origin",    "trp_log_array_center_object",          ":log_entry_no"),
	(is_between, ":origin", towns_begin, towns_end), #exclude village trading here

    (troop_get_slot, ":destination",    "trp_log_array_troop_object",          ":log_entry_no"),
	(party_get_slot, ":num_visits", ":destination", slot_party_temp_slot_1),
	(val_add, ":num_visits", 1),
	(party_set_slot, ":destination", slot_party_temp_slot_1, ":num_visits"),
  (try_end),

  (party_get_slot, ":mayor_town_production", "$g_encountered_party", slot_party_temp_slot_1),
  (assign, ":wealthiest_town_production", ":mayor_town_production"),

  (try_begin),
	(ge, "$cheat_mode", 1),
	(assign, reg4, ":mayor_town_production"),
	(str_store_party_name, s4, "$g_encountered_party"),
	(display_message, "@{!}DEBUG -- Total trade for {s4}: {reg4}"),
  (try_end),


  (try_for_range, ":other_center", towns_begin, towns_end),
	(neq, ":other_center", "$g_encountered_party"),
	(party_get_slot, ":other_town_production", ":other_center", slot_party_temp_slot_1),

	(try_begin),
		(ge, "$cheat_mode", 1),
		(assign, reg4, ":other_town_production"),
		(str_store_party_name, s4, ":other_center"),
		(display_message, "@{!}DEBUG -- Total trade for {s4}: {reg4}"),
	(try_end),

	(try_begin),
		(gt, ":other_town_production", ":wealthiest_town_production"),
		(val_add, ":richer_centers", 1),
		(assign, ":wealthiest_center", ":other_center"),
		(assign, ":wealthiest_town_production", ":other_town_production"),
    (else_try),
		(gt, ":other_town_production", ":mayor_town_production"),
		(val_add, ":richer_centers", 1),
    (else_try),
		(val_add, ":poorer_centers", 1),
    (try_end),
  (try_end),

  (assign, reg4, ":richer_centers"),
  (assign, reg5, ":poorer_centers"),
  (str_store_party_name, s5, "$g_encountered_party"),
  (str_store_party_name, s4, ":wealthiest_center"),

  ], "In terms of trade, the town of {s4} is believed to have received the most visits from caravans over the past few months. Here in {s5}, we are less visited than {reg4} towns, and more visited than {reg5}. ", "mayor_wealth_comparison_5",[
  ]],


  [anyone,"mayor_wealth_comparison_5",[

  (assign, ":wealthiest_center", "$g_encountered_party"),
  (assign, ":poorer_centers", 0),
  (assign, ":richer_centers", 0),

  (try_for_range, ":town", towns_begin, towns_end),
	(party_set_slot, ":town", slot_party_temp_slot_1, 0),
  (try_end),

  (try_for_range, ":log_entry_iterator", 0, "$num_log_entries"),
	(store_sub, ":log_entry_no", "$num_log_entries", ":log_entry_iterator"),
    (troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_traveller_attacked),

    (troop_get_slot, ":event_time",            "trp_log_array_entry_time",              ":log_entry_no"),
	(store_current_hours, ":cur_hour"),
	(store_sub, ":hours_ago", ":cur_hour", ":event_time"),
	(lt, ":hours_ago", 1344),

    (troop_get_slot, ":origin",    "trp_log_array_center_object",          ":log_entry_no"),
    (troop_get_slot, ":destination",    "trp_log_array_troop_object",          ":log_entry_no"),

	(try_begin),
		(is_between, ":destination", towns_begin, towns_end),
		(party_get_slot, ":num_attacks", ":destination", slot_party_temp_slot_1),
		(val_add, ":num_attacks", 1),
		(party_set_slot, ":destination", slot_party_temp_slot_1, ":num_attacks"),
	(try_end),

	(try_begin),
		(is_between, ":origin", towns_begin, towns_end),
		(party_get_slot, ":num_attacks", ":origin", slot_party_temp_slot_1),
		(val_add, ":num_attacks", 1),
		(party_set_slot, ":origin", slot_party_temp_slot_1, ":num_attacks"),
	(try_end),
  (try_end),

  (party_get_slot, ":mayor_town_production", "$g_encountered_party", slot_party_temp_slot_1),
  (assign, ":wealthiest_town_production", ":mayor_town_production"),

  (try_begin),
	(ge, "$cheat_mode", 1),
	(assign, reg4, ":mayor_town_production"),
	(str_store_party_name, s4, "$g_encountered_party"),
	(display_message, "@{!}DEBUG -- Total attacks for {s4}: {reg4}"),
  (try_end),


  (try_for_range, ":other_center", towns_begin, towns_end),
	(neq, ":other_center", "$g_encountered_party"),
	(party_get_slot, ":other_town_production", ":other_center", slot_party_temp_slot_1),

	(try_begin),
		(ge, "$cheat_mode", 1),
		(assign, reg4, ":other_town_production"),
		(str_store_party_name, s4, ":other_center"),
		(display_message, "@{!}DEBUG -- Total attacks for {s4}: {reg4}"),
	(try_end),

	(try_begin),
		(gt, ":other_town_production", ":wealthiest_town_production"),
		(val_add, ":richer_centers", 1),
		(assign, ":wealthiest_center", ":other_center"),
		(assign, ":wealthiest_town_production", ":other_town_production"),
    (else_try),
		(gt, ":other_town_production", ":mayor_town_production"),
		(val_add, ":richer_centers", 1),
    (else_try),
		(val_add, ":poorer_centers", 1),
    (try_end),
  (try_end),

  (assign, reg4, ":richer_centers"),
  (assign, reg5, ":poorer_centers"),
  (str_store_party_name, s5, "$g_encountered_party"),
  (str_store_party_name, s4, ":wealthiest_center"),

  ], "In terms of attacks on travellers, the town of {s4} is believed to be the most dangerous. Here in {s5}, we are less afflicted by bandits and raiders than {reg4} towns, and more afflicted than {reg5}. ", "mayor_pretalk",[
  ]],

	##diplomacy start+
	#Imported Floris dialog options letting you rebel directly from your liege by
	#leaving his kingdom and refusing to hand over your fiefs.
	## Floris - Rebellion Option  
	  [anyone|plyr ,"lord_ask_leave_service_verify_again", [
		##altered the condition block
		(neg|troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop"),
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_spouse, "trp_player"),
		(neg|faction_slot_eq, "$g_talk_troop_faction", slot_faction_leader, "trp_player"),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$g_talk_troop_faction"),
		(lt, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		
		(assign, ":has_walled_center", walled_centers_end),
		(try_for_range, ":center_no", walled_centers_begin, ":has_walled_center"),
			(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
			(assign, ":has_walled_center", ":center_no"),
		(try_end),
		(is_between, ":has_walled_center", walled_centers_begin, walled_centers_end),
		
	  ], "I have no intention of losing my lands, {s65}.", "dplmc_lord_ask_leave_service_rebellion",[]],
	  
	   [anyone,"dplmc_lord_ask_leave_service_rebellion", [
		(ge, "$g_talk_troop_relation", 15)],
		"Hrmph. Now do not be hasty with such words, {playername}. I deserve more respect than that, I think. Those lands belong to me and my heirs as you swore. If you continue down this route you will do me great offense, and there is no need for this to come to blows.",
			"dplmc_lord_ask_leave_service_rebellion_verify",[]],

	  [anyone,"dplmc_lord_ask_leave_service_rebellion", [
	  ],
	  "You've grown rash, {playername}. Your oath binds you to me and you govern what you do at my will. Think about what it is you are saying, as it is far from wise and will end poorly for you. You'd do well to reconsider.",
		"dplmc_lord_ask_leave_service_rebellion_verify",[]],

	   [anyone|plyr ,"dplmc_lord_ask_leave_service_rebellion_verify", [], "You are right, {s65}. The lands are yours, but still I must go.", "lord_ask_leave_service_3",[]],
	   
	   [anyone|plyr ,"dplmc_lord_ask_leave_service_rebellion_verify", [], "My blood and sweat earned those lands, not yours. They are mine.", "dplmc_lord_ask_leave_rebellion_confirm",[
	   ##diplomacy start+
		#The relation change with the liege is exacerbated by the number of fiefs
		#lost.  The "-10" figure is the previous relation hit for defecting; this now
		#scales up with the number of centers taken.
		(assign, ":relation_change", 0),
		(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
			(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
			(val_add, ":relation_change", -10),
		(try_end),
		
		#Defecting from a supposedly-beloved lord causes a greater hit to honor than if
		#the defection isn't so out-of-the-blue.
		(store_add, ":honor_change", "$g_talk_troop_relation", 5),
		(val_div, ":honor_change", -10),
		(val_min, ":honor_change", 0),
		#Defecting during a time of war is more dishonorable than defecting during a time
		#of peace.
		(try_begin),
			(assign, ":is_war", 0),
			(try_for_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
				(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
				(neq, ":faction_no", "$g_talk_troop_faction"),
				(store_relation, ":reln", ":faction_no", "$g_talk_troop_faction"),
				(lt, ":reln", 0),
				(assign, ":is_war", 1),
			(try_end),
			(gt, ":is_war", 0),
			(val_add, ":honor_change", -5),
		(try_end),
		#The baseline change is -10.  The greatest possible is -25 (100 relation with the king, and at war).
		(val_sub, ":honor_change", 10),
		
		#If the player was insufficiently recognized for his service, the honor loss
		#is lower.  (This will further modify the reaction of some lords.)
		(call_script, "script_dplmc_center_point_calc", "$g_talk_troop_faction", "trp_player", "$g_talk_troop", 3),
		(assign, ":avg_renown_per_center_point", reg0),
		(assign, ":player_center_points", reg1),
		(assign, ":king_center_points", reg2),
		(troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
		(troop_get_slot, ":king_renown", "$g_talk_troop", slot_troop_renown),
		(assign, ":fief_unfairness", 0),#0 = no justification on basis of unfairness, 1 = justified by unfairness

		(try_begin),
			(eq, ":player_center_points", 0),
			#Unfair if the player has no fiefs and at least 3/4 of average renown per center point
			(try_begin),
				(store_mul, reg0, ":avg_renown_per_center_point", 3),
				(val_div, reg0, 4),
				(ge, ":player_renown", reg0),
				(assign, ":fief_unfairness", 1),
				(val_add, ":honor_change", 5),
			(try_end),
		(else_try),
			#Unfair if the player's (renown / center points) is more than 5/4 the average
			(gt, ":player_center_points", 0),
			(store_div, ":player_renown_per_point", ":player_renown", ":player_center_points"),
			(store_mul, reg0, ":avg_renown_per_center_point", 5),
			(val_div, reg0, 4),
			#player is insufficiently rewarded for his renown
			(ge, ":player_renown_per_point", reg0),
			(assign, ":fief_unfairness", 1),
			(val_add, ":honor_change", 5),
		(else_try),
			#Unfair if the player's renown per center point is more than 5/4 that of the king,
			#and not less than 3/4 of the faction average
			(store_mul, reg0, ":avg_renown_per_center_point", 3),
			(val_div, reg0, 4),
			(ge, ":player_renown_per_point", reg0),
			
			(store_mul, reg0, ":king_renown", 5),
			(val_div, reg0, 4),
			(gt, ":king_center_points", 0),
			(val_div, reg0, ":king_center_points"),
			#player is insufficiently rewarded for his renown
			(ge, ":player_renown_per_point", reg0),
			(assign, ":fief_unfairness", 1),
		(try_end),
		
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", ":relation_change"),
		(val_min, ":honor_change", -10),#In any event there will be some level of honor loss.
		(call_script, "script_change_player_honor", ":honor_change"),
			
		#If the player's departure is not justified by some other cause (such as
		#not being granted the rights to a fief that he had conquered, which Martial lords
		#would be sympathetic to at least in principle), he takes a general relations hit.
		(try_for_range, ":troop_no", heroes_begin, heroes_end),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(neq, ":troop_no", "$g_talk_troop"),
			(neq, ":troop_no", active_npcs_including_player_begin),
			(store_troop_faction, ":faction_no", ":troop_no"),
			(eq, ":faction_no", "$g_talk_troop_faction"),
			
			#Calculate the relationship penalty, if any
			(assign, ":relation_penalty", 0),
			
			#Relevant factors are:
			#The troop's relation with the player, the troop's relation with his liege,
			#the troop's primary reputation, and whether the troop has the tmt_honest
			#morality subtype (which despite its name is primarily related to keeping
			#bargains), and whether this defection is causing the troop to lose any fiefs.
			(call_script, "script_troop_get_player_relation", ":troop_no"),
			(assign, ":troop_player_relation", reg0),
			
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", "$g_talk_troop"),
			(assign, ":troop_king_relation", reg0),
			
			(troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
			(call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_honest),
			(assign, ":honest_val", reg0),
			
			(assign, ":fiefs_lost", 0),
			(try_for_range, ":village_no", villages_begin, villages_end),
				(party_slot_eq, ":village_no", slot_town_lord, ":troop_no"),
				(party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),
				(ge, ":bound_center", 1),
				(party_slot_eq, ":bound_center", slot_town_lord, "trp_player"),
				(val_add, ":fiefs_lost", 1),
			(try_end),
			
			#Modify for relationship with liege
			(try_begin),
				(this_or_next|ge, ":honest_val", 1),
				(this_or_next|eq, ":reputation", lrep_upstanding),
					(eq, ":reputation", lrep_moralist),			
				(ge, ":troop_king_relation", 5),
				(val_sub, ":relation_penalty", 1),
			(else_try),
				(this_or_next|lt, ":honest_val", 0),
				(this_or_next|eq, ":reputation", lrep_debauched),
				(this_or_next|eq, ":reputation", lrep_roguish),
					(eq, ":reputation", lrep_ambitious),
				(ge, ":troop_king_relation", 25),
				(val_sub, ":relation_penalty", 1),
			(else_try),
				(ge, ":troop_king_relation", 15),
				(val_sub, ":relation_penalty", 1),
			(try_end),
			
			#Those who like the king more than the player will take his side,
			#if they met the above relation threshold.
			(try_begin),
				(lt, ":relation_penalty", 0),
				(ge, ":troop_king_relation", ":troop_player_relation"),
				(val_sub, ":relation_penalty", 1),
			(try_end),
					
			#Lords who would consider the rebellion more justified if the player was "under-fiefed"
			#(some will only care if they liked the player; others have a more general sense of fairness).
			(try_begin),
				(ge, ":fief_unfairness", 1),
				(try_begin),
					(ge, ":honest_val", 0),
					(neq, ":reputation", lrep_debauched),
					(neq, ":reputation", lrep_selfrighteous),
					(neq, ":reputation", lrep_quarrelsome),			
					(neq, ":reputation", lrep_cunning),
					(neq, ":reputation", lrep_ambitious),
					(ge, ":troop_player_relation", 0),
					(val_add, ":relation_penalty", ":fief_unfairness"),
				(else_try),
					(ge, ":troop_player_relation", 20),
					(val_add, ":relation_penalty", ":fief_unfairness"),
				(try_end),
			(try_end),
			
			#Subtract a penalty for lost fiefs
			(try_begin),
				(ge, ":fiefs_lost", 1),
				#apply -2 times fiefs lost
				(this_or_next|eq, ":reputation", lrep_custodian),
				(this_or_next|eq, ":reputation", lrep_ambitious),
				(this_or_next|eq, ":reputation", lrep_quarrelsome),
				(this_or_next|eq, ":reputation", lrep_selfrighteous),
				(this_or_next|eq, ":reputation", lrep_cunning),
				(this_or_next|eq, ":reputation", lrep_debauched),
					(eq, ":reputation", lrep_martial),
				(val_sub, ":relation_penalty", ":fiefs_lost"),
				(val_sub, ":relation_penalty", ":fiefs_lost"),
			(else_try),
				(ge, ":fiefs_lost", 1),
				#apply -1 times fiefs lost
				(neg|ge, ":reputation", lrep_conventional),
				(neq, ":reputation", lrep_goodnatured),
				(val_sub, ":relation_penalty", ":fiefs_lost"),
			(try_end),
			
			#Apply a non-zero (and non-positive) penalty
			(lt, ":relation_penalty", 0),
			(call_script, "script_change_player_relation_with_troop", ":troop_no", ":relation_penalty"),
		(try_end),
		##diplomacy end+
		]],
		
	   [anyone, "dplmc_lord_ask_leave_rebellion_confirm", [
		(ge, "$g_talk_troop_relation", 25)],
		"You disappoint me greatly, {playername}. You may have once had my confidence, but this is beyond reason. Do not doubt that I will defend my house's honor from your insult. This is war between us.", "dplmc_lord_ask_leave_rebellion_confirm_final", [
		(call_script, "script_player_leave_faction", 0), #"1" would mean give back fiefs
		(call_script, "script_activate_player_faction", "trp_player"),]],
		
	   [anyone, "dplmc_lord_ask_leave_rebellion_confirm", [
	   ], "I should have seen your treachery coming. I must be growing soft to have been fool enough to miss your schemes. No matter. Your time will yet come, {playername}. Justice is switftest on a field of battle.", "dplmc_lord_ask_leave_rebellion_confirm_final", [
		(call_script, "script_player_leave_faction", 0), #"1" would mean give back fiefs
		(call_script, "script_activate_player_faction", "trp_player")]],
		
	   [anyone|plyr, "dplmc_lord_ask_leave_rebellion_confirm_final", [
	   ], "I hold you in no ill-esteem, {s65}. I do only what is just.", "dplmc_lord_ask_leave_rebellion_end", []],
	   [anyone|plyr, "dplmc_lord_ask_leave_rebellion_confirm_final", [
	   ], "We all do what we must. Good bye.", "dplmc_lord_ask_leave_rebellion_end", []],
	   [anyone|plyr, "dplmc_lord_ask_leave_rebellion_confirm_final", [
	   ], "Then I await the day we meet in battle.", "dplmc_lord_ask_leave_rebellion_end", []],
	   
	   [anyone, "dplmc_lord_ask_leave_rebellion_end", [
		(ge, "$g_talk_troop_relation", 25),
		(str_store_faction_name, s1, "$g_talk_troop_faction")
		], 
		"This is a dark day, {playername}. It will be marked and rued throughout the {s1}. Your treachery will not be soon forgotten. It would be best if you left quickly.", "close_window", [
		(assign, "$g_leave_encounter", 1)]],
		
	   [anyone, "dplmc_lord_ask_leave_rebellion_end", [
	   ], "You are not the same {man/woman} I took as my vassal, {playername}. Be gone from my sight before I end this now.", "close_window", [(assign, "$g_leave_encounter", 1)]],
	## Floris - Rebellion Option
	##diplomacy end+
  
  
  [anyone|plyr,"free", [[in_meta_mission]], " Good-bye.", "close_window",[]],
  [anyone|plyr,"free", [[neg|in_meta_mission]], " [Leave]", "close_window",[]],
#  [anyone,"free", [], "NO MATCHING SENTENCE!", "close_window",[]],

#LAZERAS MODIFIED  {Top Tier Troops Recruit}
###########################################################################
   [anyone,
      "event_triggered",
      [
         (store_conversation_troop,"$g_talk_troop"),
         #(is_between,"$g_talk_troop", additional_heroes_begin, additional_heroes_end),
                        (eq, "$g_talk_troop", reg20),
         (eq, "$g_upgrade_talk", 1),
                        (troop_get_type, reg65, "trp_player"),
                        (str_store_string,s65,"@{reg65?my Lady:my Lord}"),
                        (str_store_troop_name,s21,reg21),
      ],
      "Yes, {s65}?",
      "upgrade_talk",
      []
   ],
       [anyone|plyr,
      "upgrade_talk",
      [],
      "I have seen you fight well in battles, soldier.",
      "upgrade_talk_1",
      []
   ],
        [anyone,
      "upgrade_talk_1",
      [
      ],
      "I only do my duty to {s65}, sire.",
      "upgrade_talk_2",
      []
         ],
         [anyone|plyr,
      "upgrade_talk_2",
      [],
      "And well, too. The only time I've heard someone with such skills in battle, it has been in sagas. You are a hero!",
      "upgrade_talk_3a",
      []
         ],         
         [anyone|plyr,
      "upgrade_talk_2",
      [],
      "I just wanted you to know that I take notice in such skills in battle. Now fall back in line!",
      "upgrade_talk_3b",
      []
         ],
   [anyone,
      "upgrade_talk_3a",
      [
      ],
      "You honour me with your words. I will do my utter best to honour them.",
      "upgrade_talk_4a",
      []
         ],
         [anyone|plyr,
      "upgrade_talk_4a",
      [],
      "From now on you shall be remembered as a {s21}",
      "upgrade_talk_5",
      []
         ],
   [anyone,
      "upgrade_talk_5",
      [
                    (call_script,"script_upgrade_troop_to_hero", reg20, reg21),
      ],
      "I will defend my new title to my death, and I will not let you down. I promise you this; The blood on my steel will never dry!",
      "close_window",
      []
         ],         
   [anyone,
      "upgrade_talk_3b",
      [
      ],
      "Yes, {s65}",
      "close_window",
      []
   ],
 ##Moved down from above where it is commented out  
  [anyone, "event_triggered", [
                     ],
   "{!}Sorry -- just talking to myself [ERROR- {s51}]", "close_window", [
       ]],
#LAZERAS MODIFIED  {Top Tier Troops Recruit}

## Floris - Rebellion Option  						Disabled and replaced with the Altered version of Diplomacy 3.32+ by zParzifal // see slightly above Lazeras Top Tier Troops Recruit

#   [anyone|plyr ,"lord_ask_leave_service_verify_again", [], "I have no intention of losing my lands, {s65}.", "lord_ask_leave_service_rebellion",[]],
#   [anyone,"lord_ask_leave_service_rebellion", [(ge, "$g_talk_troop_relation", 15)], "Hrmph.\
# Now do not be hasty with such words, {playername}. I deserve more respect than that, I think. Those lands belong to me and my heirs as you swore.\
# If you continue down this route you will do me great offense, and there is no need for this to come to blows.", "lord_ask_leave_service_rebellion_verify",[]],
#  [anyone,"lord_ask_leave_service_rebellion", [], "You've grown rash, {playername}. Your oath binds you to me and you govern what you do at my will.\
# Think about what it is you are saying, as it is far from wise and will end poorly for you. You'd do well to reconsider.", "lord_ask_leave_service_rebellion_verify",[]],   
#   [anyone|plyr ,"lord_ask_leave_service_rebellion_verify", [], "You are right, {s65}. The lands are yours, but still I must go.", "lord_ask_leave_service_3",[]],
#   [anyone|plyr ,"lord_ask_leave_service_rebellion_verify", [], "My blood and sweat earned those lands, not yours. They are mine.", "lord_ask_leave_rebellion_confirm",[
#    (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -10),(call_script, "script_change_player_honor", -10)]],
#   [anyone, "lord_ask_leave_rebellion_confirm", [(ge, "$g_talk_troop_relation", 25)], "You disappoint me greatly, {playername}.\
# You may have once had my confidence, but this is beyond reason. Do not doubt that I will defend my house's honor from your insult.\
# This is war between us.", "lord_ask_leave_rebellion_confirm_final", [(call_script, "script_player_leave_faction", 0), #"1" would mean give back fiefs
#    (call_script, "script_activate_player_faction", "trp_player"),]],
#   [anyone, "lord_ask_leave_rebellion_confirm", [], "I should have seen your treachery coming. I must be growing soft to have been fool enough to miss your schemes.\
# No matter. Your time will yet come, {playername}. Justice is switftest on a field of battle.", "lord_ask_leave_rebellion_confirm_final", [
#    (call_script, "script_player_leave_faction", 0), #"1" would mean give back fiefs
#    (call_script, "script_activate_player_faction", "trp_player")]],
#   [anyone|plyr, "lord_ask_leave_rebellion_confirm_final", [], "I hold you in no ill-esteem, {s65}. I do only what is just.", "lord_ask_leave_rebellion_end", []],
#   [anyone|plyr, "lord_ask_leave_rebellion_confirm_final", [], "We all do what we must. Good bye.", "lord_ask_leave_rebellion_end", []],
#   [anyone|plyr, "lord_ask_leave_rebellion_confirm_final", [], "Then I await the day we meet in battle.", "lord_ask_leave_rebellion_end", []],
#   [anyone, "lord_ask_leave_rebellion_end", [(ge, "$g_talk_troop_relation", 25),(str_store_faction_name, s1, "$g_talk_troop_faction")], 
#     "This is a dark day, {playername}. It will be marked and rued throughout the {s1}. Your treachery will not be soon forgotten. It would be best if you left quickly.", "close_window", [(assign, "$g_leave_encounter", 1)]],
#   [anyone, "lord_ask_leave_rebellion_end", [], "You are not the same {man/woman} I took as my vassal, {playername}. Be gone from my sight before I end this now.", "close_window", [(assign, "$g_leave_encounter", 1)]],
## Floris - Rebellion Option  

## Floris - Trade with Merchant Caravans
  [anyone|plyr,"merchant_talk", [], "I'd like to see your wares.", "merchant_trade_request",[]],  
  [anyone, "merchant_trade_request", [(lt,"$g_encountered_party_relation",0)],
    "You must be joking! The crown would not take kindly to us trading with the likes of you.", "merchant_trade_deny",[]],
  [anyone, "merchant_trade_request", [(neq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
    (store_party_size_wo_prisoners,":size", "p_main_party"),(this_or_next|lt, ":size", 60),(neg|troop_slot_ge, "trp_player", slot_troop_renown, 200)],
    "My wares? Sorry {sir/ma'am}, I haven't the time to unload the caravan. Deadlines to keep.", "merchant_trade_deny",[]],  	
  [anyone, "merchant_trade_request", [],
    "Certainly. Give me and my men a moment to make a proper presentation.", "merchant_trade_completed",
	[(call_script, "script_trade_with_travelling_merchant", begin, 1)]],
  [anyone,"merchant_trade_completed", [], "Anything else?", "merchant_trade_completed_2",[]],
  [anyone,"merchant_trade_completed_2", [], "Anything else?", "merchant_talk", [(call_script, "script_trade_with_travelling_merchant", end)]], #To allow for delay in returning gear
  [anyone|plyr, "merchant_trade_deny", [], "You refuse me? How dare you, peddler!", "merchant_trade_force", []],
  [anyone|plyr, "merchant_trade_deny", [(ge,"$g_encountered_party_relation",0)], "Most unfortunate. I had planned to part with good coin.", "merchant_trade_rethink", []],
  [anyone|plyr, "merchant_trade_deny", [(ge,"$g_encountered_party_relation",0)], "Understood, but there was another thing.", "merchant_pretalk", []],
  [anyone|plyr, "merchant_trade_deny", [(ge,"$g_encountered_party_relation",0)], "Very well. Good journey. [Leave]", "close_window", [(assign, "$g_leave_encounter",1)]], 
  [anyone|plyr, "merchant_trade_deny", [(lt,"$g_encountered_party_relation",0)], "Best scurry on your way then, lest some bandits appear. [Leave]", "close_window", [(assign, "$g_leave_encounter",1)]], 
  [anyone, "merchant_trade_rethink", [(store_skill_level, ":skill", "skl_persuasion", "trp_player"),(store_random_in_range, ":rand", 0, 10),(val_add, ":skill", ":rand"),(gt, ":skill", 10)], 
    "Well, we could be persuaded to stop, but only for a moment", "merchant_trade_completed",
	[(call_script, "script_trade_with_travelling_merchant", begin, 2)]],
  [anyone, "merchant_trade_rethink", [], "We really must be getting on our way.", "merchant_talk",[]],
  [anyone, "merchant_trade_force", [(lt,"$g_encountered_party_relation",10),(str_store_faction_name, s1, "$g_encountered_party_faction")], 
    "Tough words from one unloved by the {s1}. We've no time for this.", "merchant_trade_force_2", []],
  [anyone, "merchant_trade_force", [], "Settle down, {man/woman}. It's just business.", "merchant_trade_force_2", []],
  [anyone|plyr, "merchant_trade_force_2", [], "Then I will take what I wish from your corpses.", "merchant_attack", [(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -10)]],
  [anyone|plyr, "merchant_trade_force_2", [], "Show me your wares or I will show you my steel. Now!", "merchant_trade_rethink_2", [(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3)]],
  [anyone|plyr, "merchant_trade_force_2", [], "Get out of my sight, peddler. [Leave]", "close_window", [(assign, "$g_leave_encounter",1)]],
  [anyone, "merchant_trade_rethink_2", [(lt,"$g_encountered_party_relation",0)], "Be quick about it, knave.", "merchant_trade_completed",
    [(call_script, "script_trade_with_travelling_merchant", begin, 5)]],  
  [anyone, "merchant_trade_rethink_2", [], "Hrmph. Our apologies mi{lord/lady}. Right away.", "merchant_trade_completed",
    [(call_script, "script_trade_with_travelling_merchant", begin, 4)]],
## Floris - Trade with Merchant Caravans 

## Zaitenko's Reinforcement Script
# Reinforcements
  [party_tpl|pt_reinforcements,"start", [(eq,"$talk_context",tc_party_encounter),
                                         (party_get_slot, ":ai_object", "$g_encountered_party", slot_party_ai_object),
                                         (str_store_party_name,s21,":ai_object"),
                                         (str_store_party_name, s20, "$g_encountered_party")],
   "Who goes there? We are {s20}.\ We're on our way to {s21}.", "reinforcements_intro",[]],
  [anyone|plyr, "reinforcements_intro", [], "I am {playername}. I'm just passing by.", "close_window",[]],
  [anyone|plyr, "reinforcements_intro", [], "I am {playername}. And I'm here to stop you from reaching your destination!.", "reinforcement_hostile",[]],
  [party_tpl|pt_reinforcements,"reinforcement_hostile", [(faction_get_slot, ":faction_leader", "$g_encountered_party_faction",slot_faction_leader),
                                                         (str_store_troop_name, s9, ":faction_leader"),],
                                                         "What!? We are under the protection of {s9}!\ Be certain he will take vengance!", "reinforcements_attack",[]],
  [anyone|plyr, "reinforcements_attack", [], "Fine let him! I will kill him after I've dealt with you!", "close_window",[(call_script, "script_make_kingdom_hostile_to_player", "$g_encountered_party_faction", -1),
                                                                                                                          (encounter_attack,0)]],
  [anyone|plyr, "reinforcements_attack", [], "Allright, go! But you have not seen the last of me!", "close_window",[]],
##
####################################################################################################################################
# LAV MODIFICATIONS START (COMPANIONS OVERSEER MOD)
####################################################################################################################################
  [anyone, "lco_conversation_end", [(troop_is_hero,"$g_lco_target"),(assign,"$g_lco_operation",lco_run_presentation)], "Nice to know you are not forgetting me!", "close_window", [(change_screen_return)]],
  [anyone, "lco_conversation_end", [(assign,"$g_lco_operation",lco_run_presentation)], "It's a honor to serve you, {sir/my lady}!", "close_window", [(change_screen_return)]],
####################################################################################################################################
# LAV MODIFICATIONS END (COMPANIONS OVERSEER MOD)
####################################################################################################################################
 ##Caba - new cheats
  [anyone|plyr,"regular_member_talk", [(ge, "$cheat_mode", 1)], "CHEAT: Upgrade One Member", "do_regular_member_view_char",[
    (assign, ":stack", -1),
    (party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
    (try_for_range, ":i", 0, ":num_of_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i"),
        (eq, ":stack_troop", "$g_talk_troop"),    
        (assign, ":stack", ":i"),
        (assign, ":num_of_stacks", 0),
    (try_end),
    (neq, ":stack", -1),
    (call_script, "script_game_get_upgrade_xp", "$g_talk_troop"),
    (party_add_xp_to_stack, "p_main_party", ":stack", reg0),
   ]],
  [anyone|plyr,"regular_member_talk", [(ge, "$cheat_mode", 1)], "CHEAT: Upgrade Full Stack", "do_regular_member_view_char",[
    (assign, ":stack", -1),
    (party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
    (try_for_range, ":i", 0, ":num_of_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i"),
        (eq, ":stack_troop", "$g_talk_troop"),    
        (assign, ":stack", ":i"),
        (assign, ":num_of_stacks", 0),
    (try_end),
    (neq, ":stack", -1),
    (call_script, "script_game_get_upgrade_xp", "$g_talk_troop"),
    (party_stack_get_size, reg1, "p_main_party", ":stack"),
    (val_mul, reg0, reg1),
    (party_add_xp_to_stack, "p_main_party", ":stack", reg0),
   ]],
  ##Caba new cheats end

]
