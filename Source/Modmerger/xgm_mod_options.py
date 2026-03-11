from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
#import string

from xgm_mod_options_header import *

############################################################################
## 0) overlay id (put something unique; used as dict keys in save/load options from a file via WSE; added by Caba'drin May 2012)
## 1) overlay type (defined in xgm_mod_options_header)
## 2) overlay type specific parameters (e.g. for number box, it can be lower/upper range, for cbobox, it would be the cbo items etc)
##    a) xgm_ov_numberbox : lower_bound(inclusive), upper_bound(exclusive). e.g. [0,101] for range of values from 0-100
##    b) xgm_ov_combolabel/xgm_ov_combobutton  : list of combo items. e.g. ["option1", "option2", "option3"]
##    c) xgm_ov_slider : lower_bound(inclusive), upper_bound(exclusive). e.g. [0,101] for range of values from 0-100
##    d) xgm_ov_checkbox : not used fttb. just leave empty. e.g. []
## 3) text label
## 4) reserved for text label flags
## 5) description (shown on mouse-over; added by Caba'drin April 2012)
## 6) reserved for description flags
## 7) initialization op block.  Used for updating the overlay values from game values. Must assign the desired value to reg1.
## 8) update op block.  Used for updating game values from overlay values. The overlay value is in reg1.
## 9) optional. reserved for option page id. unused for now. leave out for options using general page.
############################################################################

mod_options = [  
  # ("sync", xgm_ov_checkbox, [], "Sync Mod Options:", 0, ##OPTION REQUIRED, UNCHANGED, for save/load options from a file via WSE; added by Caba'drin May 2012
	  # "Ticked, "+mod_name+" mod options will be stored and syncronized for a common set of options across many games. If the box was un-ticked, ticking it will cause any options sync'd from another playthrough to be loaded into this game.^^Unticked, the options set here will only apply to this playthrough and will need to be re-configured for a new game.", 0,
	  # [(assign, reg1, "$g_mod_options_sync"),],
	  # [(assign, "$g_mod_options_sync", reg1),
	   # (try_begin),
	        # (eq, "$g_mod_options_sync", 1),
			# (try_begin),		  
				# (eq, "$g_is_quick_battle", 1),
				# (presentation_set_duration, 0),
			# (try_end),
			# (start_presentation, "prsnt_mod_option"),
	   # (try_end),
	  # ],
	# ),	
	
	("general_title_bar", xgm_ov_title, [], "General Options", tf_center_justify|tf_with_outline),
	
	## WINDYPLAINS+ ## - Ported over fast travel pause options from Silverstag.
	# ("floris_ft_force_pause", xgm_ov_checkbox, [], "Pause at hostiles during fast travel:", 0,
		# "Ticked, while fast-travelling (Ctrl-Space), the game will automatically pause when your party detects a hostile party. Unticked, as in Native, the game will NOT pause.", 0,
		# [(assign, reg1, "$g_ft_force_pause"),],
		# [(assign, "$g_ft_force_pause", reg1),],),

	("floris_ft_force_pause", xgm_ov_combobutton, ["- Disabled -", "Any Enemy", "Actual Threats"], "Pause during fast travel for:", 0,
		"Ticked, while fast-travelling (Ctrl-Space), the game will automatically pause when your party detects a hostile party. Unticked, as in Native, the game will NOT pause.", 0,
		[(assign, reg1, "$g_ft_force_pause"),],
		[(assign, "$g_ft_force_pause", reg1),],),
	## WINDYPLAINS- ##
	
	("pbod_bodyguard", xgm_ov_checkbox, [], "Enable Bodyguards in Towns/Villages:", 0,
		"Bodyguards allows your companions to serve as your character's bodyguards in town and village scenes. The number of bodyguards depends on your character's leadership and renown.", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_bodyguard),],
		[(party_set_slot, "p_main_party", slot_party_pref_bodyguard, reg1),],),	 
	
	("floris_fow", xgm_ov_checkbox, [], "Enable Fog of War:", 0,
		"Ticked, locations you have not visited are hidden on the world map until you are in seeing range. Unticked, as in Native, the full map is revealed at game start.", 0,
		[(assign, reg1, "$g_fog"),],
		[(assign, "$g_fog", reg1),
		(try_begin),(neq, "$g_is_quick_battle", 1),(call_script, "script_initialize_fog"),(try_end),],),
	   
	
	("display_title_bar", xgm_ov_title, [], "Display", tf_center_justify|tf_with_outline),
	
	("cc_minimap_show", xgm_ov_checkbox, [], "Show battle minimap:", 0,
		"Ticked, a minimap/radar will always be in the upper right hand corner of your screen. Unticked, no map unless you hit Backspace.", 0,
		[(assign, reg1, "$g_show_minimap"),],
		[(assign, "$g_show_minimap", reg1),],),

	("cc_minimap_size", xgm_ov_numberbox, [60, 111], "Size of battle minimap (%):", 0,
		"Sets the size of the minimap, if it is activated above.", 0,
		[(assign, reg1, "$g_minimap_ratio"),],
		[(assign, "$g_minimap_ratio", reg1),],),
	  
	("cc_hp_bars_ally", xgm_ov_checkbox, [], "Show health bars of ally troops:", 0,
		"Ticked, you will see health bars at the distance set above. Unticked, no health bars on allies.", 0,
		[(assign, reg1, "$g_hp_bar_ally"),],
		[(assign, "$g_hp_bar_ally", reg1),],),

	("cc_hp_bars_enemy", xgm_ov_checkbox, [], "Show health bars of enemy troops:", 0,
		"Ticked, you will see health bars at the distance set above. Unticked, no health bars on enemies.", 0,
		[(assign, reg1, "$g_hp_bar_enemy"),],
		[(assign,"$g_hp_bar_enemy", reg1),],),
	
	("cc_hp_bars_dist", xgm_ov_numberbox, [3,81], "Distance limit for showing HP bars:", 0,
		"Sets how far away you'll see hit point/health status bars for troops and when they disappear, if you have them activated below.", 0,
		[(assign, reg1, "$g_hp_bar_dis_limit"),],
		[(assign, "$g_hp_bar_dis_limit", reg1),],),

	("cc_report_shot_dist", xgm_ov_checkbox, [], "Report shot distance:", 0,
		"Ticked, the scrolling battle text display will list how far each of your bow/crossbow shots goes. Unticked, this is not displayed.", 0,
		[(assign, reg1, "$g_report_shot_distance"),],
		[(assign, "$g_report_shot_distance", reg1),],),

	("cc_report_xp_prof", xgm_ov_checkbox, [], "Report extra XP & Wpn Prof:", 0,
		"One receives extra weapon proficiencies and XP points due to Intelligence. Ticked, the scrolling battle text display will notify you of these extra points. Unticked, this is not displayed.", 0,
		[(assign, reg1, "$g_report_extra_xp_and_wpt"),],
		[(assign, "$g_report_extra_xp_and_wpt", reg1),],),
	
	("floris_date", xgm_ov_checkbox, [], "Disable Time of Day:", 0,
		"Ticked, as in Native. Unticked, the date also shows the time of day/hour.", 0,
		[(assign, reg1, "$g_date"),],
		[(assign, "$g_date", reg1),],),

	
	("combat_title_bar", xgm_ov_title, [], "Combat", tf_center_justify|tf_with_outline),
	
	("pbod_battle_size", xgm_ov_numberbox, [30,max_battle_size + 1], "Record Battle Size as set in Options:", 0,
		"Record the Battle Size you have set in the normal Game Options screen so the Pre-Battle Deployment (choose your troops) option works correctly.", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_prebattle_battle_size),
		(val_clamp, reg1, 30, max_battle_size + 1),
		(party_set_slot, "p_main_party", slot_party_prebattle_battle_size, reg1),],
		[(val_clamp, reg1, 30, max_battle_size + 1),
		(party_set_slot, "p_main_party", slot_party_prebattle_battle_size, reg1),],),
	
	("pbod_bc_continue", xgm_ov_checkbox, [], "Enable Battle Continuation:", 0,
		"Battle Continuation allows your troops to continue fighting after you are knocked out.", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_bc_continue),],
		[(party_set_slot, "p_main_party", slot_party_pref_bc_continue, reg1),],),

	("pbod_bc_charge_ko", xgm_ov_combobutton, ["- Disabled -", "Charge All", "Formations AI"], "Batt. Cont., Charge after KO:", 0,
		"If Battle Continuation is active, you can select what your troops will do after you get knocked out: Disabled has them continue their previous orders; Charge all will give everyone a charge order; Formations AI (if active for the AI) will allow the new AI to take over for you.", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_bc_charge_ko),],
		[(party_set_slot, "p_main_party", slot_party_pref_bc_charge_ko, reg1),],),

	("cc_reinforcement", xgm_ov_numberbox, [2,101], "Reinforcement waves:", 0,
		"Allows you to increase or decrease the number of reinforcements that occur prior to the battle round ending.", 0,
		[(assign, reg1, "$g_reinforcement_stage"),],
		[(assign, "$g_reinforcement_stage", reg1),],),

	("cc_battle_speed", xgm_ov_numberbox, [1,6], "Speed of battles on the map:", 0,
		"Adjusts how fast auto-calculated battles between the AI go. The slower, the greater chance you can get to them from a distance, but it also slows down the pace of the game.", 0,
		[(assign, reg1, "$g_speed_ai_battles"),],
		[(assign, "$g_speed_ai_battles", reg1),],),

	("pbod_formations", xgm_ov_combobutton, ["- Disabled -", "Formations AI", "Native AI, w/Formations"], "Formations Battle AI:", 0,
		"Select your prefered Battle AI: Disabled is Native AI; Formations AI both allows the AI to use formations and changes their battle decision-making; Native AI w/Formations is Native AI but carries out the Native AI with basic formations. (Only active in field battles.)", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_formations),],
		[(party_set_slot, "p_main_party", slot_party_pref_formations, reg1),],),
	  
	("pbod_siege_charge", xgm_ov_checkbox, [], "Disable charge on belfry reaching wall:", 0,
		"Unticked, as Native, when the belfry (siege tower) reaches a wall, the player's attacking force will automatically charge. Ticked and the charge order will not be automatically given.", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_siege_charge),],
		[(party_set_slot, "p_main_party", slot_party_pref_siege_charge, reg1),],),

	("pbod_div_dehorse", xgm_ov_combobutton, [s0, s1, s2, s3, s4, s5, s6, s7, s8, "- Disabled -"], 
		"Reassign De-horsed Cavalry to:", 0,
		"Mounted bots, once their horse dies, can be re-assinged to a division of your choosing. If active, AI bots will be reassigned to infantry. (Only active in field battles.)", 0,
		[
			(try_for_range, ":i", 0, 9),
				(str_store_class_name, ":i", ":i"),
			(try_end),
			(party_get_slot, reg1, "p_main_party", slot_party_pref_div_dehorse),
		],
		[(party_set_slot, "p_main_party", slot_party_pref_div_dehorse, reg1),],),
	   
	("pbod_div_no_ammo", xgm_ov_combobutton, [s0, s1, s2, s3, s4, s5, s6, s7, s8, "- Disabled -"], 
		"Reassign No-Ammo Archers to:", 0,
		"Foot archer bots, once out of ammo, can be re-assinged to a division of your choosing. If active, AI bots will be reassigned to infantry. (Only active in field battles.)", 0,
		[
			(try_for_range, ":i", 0, 9),
				(str_store_class_name, ":i", ":i"),
			(try_end),
			(party_get_slot, reg1, "p_main_party", slot_party_pref_div_no_ammo),
		],
		[(party_set_slot, "p_main_party", slot_party_pref_div_no_ammo, reg1),],),
		
	("pbod_ally_division", xgm_ov_checkbox, [], "Keep allies in the basic 3 divisions:", 0,
		"Ticked, troops of ally parties under your command will not be assigned to your customized divisions, but to the default infantry, archer, and cavalry divisions. Unticked, as in Native, any ally troops under your command will be re-assigned to the same divisions as your troops of the same type.", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_ally_division),],
		[(party_set_slot, "p_main_party", slot_party_pref_ally_division, reg1),],),	 
	
	("pbod_spo_brace", xgm_ov_checkbox, [], "Enable AI Spear Bracing:", 0,
		"Enabling AI Special Orders allows the AI teams to use volley fire (crossbows), skirmish mode (bow-users), and spear-bracing (polearm infantry). (Only active in field battles.)", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_spo_brace),],
		[(party_set_slot, "p_main_party", slot_party_pref_spo_brace, reg1),],),

	("pbod_spo_skirmish", xgm_ov_checkbox, [], "Enable AI Skirmishing:", 0,
		"Enabling AI Special Orders allows the AI teams to use volley fire (crossbows), skirmish mode (bow-users), and spear-bracing (polearm infantry). (Only active in field battles.)", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_spo_skirmish),],
		[(party_set_slot, "p_main_party", slot_party_pref_spo_skirmish, reg1),],),

	("pbod_spo_volley", xgm_ov_checkbox, [], "Enable AI Volley Fire:", 0,
		"Enabling AI Special Orders allows the AI teams to use volley fire (crossbows), skirmish mode (bow-users), and spear-bracing (polearm infantry). (Only active in field battles.)", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_spo_volley),],
		[(party_set_slot, "p_main_party", slot_party_pref_spo_volley, reg1),],),

	("pbod_wu_lance", xgm_ov_checkbox, [], "Use NPC Lancer Fix:", 0,
		"Weapon Use Fix for Lancers will force mounted bots with lances to use them unless they are surrounded by enemies. (Only active in field battles.)", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_wu_lance),],
		[(party_set_slot, "p_main_party", slot_party_pref_wu_lance, reg1),],),
		
	("pbod_wu_harcher", xgm_ov_checkbox, [], "Use NPC Horse Archer Fix:", 0,
		"Weapon Use Fix for Horse Archers will force mounted bots with bows to use them until they run out of ammo. (Only active in field battles.)", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_wu_harcher),],
		[(party_set_slot, "p_main_party", slot_party_pref_wu_harcher, reg1),],),
		
	("pbod_wu_spear", xgm_ov_checkbox, [], "Use NPC Spear/Polearm Fix:", 0,
		"Weapon Use Fix for Spear/Polearms will force infantry bots with polearms to use them unless they are surrounded by enemies. (Only active in field battles.)", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_wu_spear),],
		[(party_set_slot, "p_main_party", slot_party_pref_wu_spear, reg1),],),
		
	("pbod_dmg_tweaks", xgm_ov_checkbox, [], "Use Pike/Horse Damage Tweaks:", 0,
		"Damage tweaks will give a flat boost to damage from spears to horses, and charge damage from horses to infantry, in an attempt to compensate for poor AI use of polearms and charges. (Only active in field battles.)", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_dmg_tweaks),],
		[(party_set_slot, "p_main_party", slot_party_pref_dmg_tweaks, reg1),],), 
	
	# ("pbod_spo_pavise", xgm_ov_checkbox, [], "Enable AI Deploy Pavise Shields:", 0,
		# "Enabling AI Special Orders allows the AI teams to use volley fire and pavise deployment (crossbows), skirmish mode (bow-users), and spear-bracing (polearm infantry). (Only active in field battles.)", 0,
		# [(party_get_slot, reg1, "p_main_party", slot_party_pref_spo_pavise),],
		# [(party_set_slot, "p_main_party", slot_party_pref_spo_pavise, reg1),],),
	
    ("cc_morale_food", xgm_ov_numberbox, [0,100], "Morale threshold for consuming food^twice the speed as much as normal:", 0,
		"Sets the morale level below which your troops will need to eat twice as much food to stay happy. If your party's morale is below this value, the speed of consuming food will be twice as much as normal, and the bonus to party morale of all food will also be doubled. Set it very low to essentially disable this 'difficulty enhancement.'", 0,
		[(assign, reg1, "$g_morale_threshold"),],
		[(assign, "$g_morale_threshold", reg1),],),

	("diplo_terrain_adv", xgm_ov_checkbox, [], "Terrain advantage in Autocalc battles:", 0,
		"Ticked, autocalculated battles give advantage to factions on their home terrain. Unticked, as in Native and auto-battles are only based on party size and troop levels.", 0,
		[(store_add, reg1, "$g_dplmc_terrain_advantage", 1),],
		[(store_sub, "$g_dplmc_terrain_advantage", reg1, 1),],),

	("XX_encumbrance", xgm_ov_checkbox, [], "Skill penalty from encumbrance:", 0,
		"Ticked, you and your companions receive penalties to athletics, riding and horsearchery from heavy armor. Unticked, it is as in Native.", 0,
		[(assign, reg1, "$g_encumbrance_penalty"),],
		[(assign, "$g_encumbrance_penalty", reg1),],),
		
	("pbod_wp_prof_decrease", xgm_ov_checkbox, [], "Enable ranged penalty from weather:", 0,
		"The Weather Proficiency Penalties lowers the ranged weapons proficiencies of all troops while in battle in heavy fog, rain/snow, or at night to reflect the poor conditions for archery.", 0,
		[(party_get_slot, reg1, "p_main_party", slot_party_pref_wp_prof_decrease),],
		[(party_set_slot, "p_main_party", slot_party_pref_wp_prof_decrease, reg1),],),	 
		
	("diplo_horse_speed", xgm_ov_checkbox, [], "Disable horse speed scaling:", 0,
		"Ticked, it is as in Native. UN-ticked, the more injured a horse, the slower it goes.", 0,
		[(assign, reg1, "$g_dplmc_horse_speed"),],
		[(assign, "$g_dplmc_horse_speed", reg1),],),
		
	("XX_drowning", xgm_ov_checkbox, [], "Allow drowning in missions:", 0,
		"Ticked, you can drown if you are under water for a length of time. Unticked, it is as in Native and you can walk at the bottom of a lake for ages.", 0,
		[(assign, reg1, "$drowning"),],
		[(assign, "$drowning", reg1),],),
  	
	
	("diplomacy_title_bar", xgm_ov_title, [], "Diplomacy", tf_center_justify|tf_with_outline),
	
	("diplo_exile", xgm_ov_combobutton, ["- Disabled -", "Enabled", "Frequent"], "Lords returning from exile:", 0,
		"Allows exiled lords to be pardoned after a time and rejoin a faction to prevent 'lord-drain' in the late game.", 0,
		[(store_add, reg1, "$g_dplmc_lord_recycling", 1),],
		[(store_sub, "$g_dplmc_lord_recycling", reg1, 1),],),
		
	("diplo_change_ai", xgm_ov_combobutton, ["- Disabled -", "Low", "Medium", "High/Experimental"], "Diplomacy AI changes:", 0,
		"Difficulty setting. The higher the setting, the more difficult for the player.", 0,
		[(store_add, reg1, "$g_dplmc_ai_changes", 1),],
		[(store_sub, "$g_dplmc_ai_changes", reg1, 1),],),
		
	("diplo_change_econ", xgm_ov_combobutton, ["- Disabled -", "Low", "Medium", "High/Experimental"], "Diplomacy economic changes:", 0,
		"Difficulty setting. The higher the setting, the more difficult for the player.", 0,
		[(store_add, reg1, "$g_dplmc_gold_changes", 1)],
		[(store_sub, "$g_dplmc_gold_changes", reg1, 1),],),
		
	("diplo_prejudice", xgm_ov_combobutton, ["- Disabled -", "Default", "High"], "Anti-woman prejudice level:", 0,
		"Disabled levels the playing-field for female player characters. Default as in Native. High increases the sexism/anti-woman prejudice of the medieval setting for female player characters.", 0,
		[
			(try_begin),
				(this_or_next|eq, "$g_disable_condescending_comments", 2),
				(eq, "$g_disable_condescending_comments", 3),
				(assign, reg1, 0),
			(else_try),
				(this_or_next|eq, "$g_disable_condescending_comments", -1),
				(eq, "$g_disable_condescending_comments", -2),
				(assign, reg1, 2),
			(else_try),
				(assign, reg1, 1),
			(try_end),
		],
		[
			(try_begin),
				(eq, reg1, 0),
				(assign, "$g_disable_condescending_comments", 2),
			(else_try),
				(eq, reg1, 2),
				(assign, "$g_disable_condescending_comments", -2),
			(else_try),
				(assign, "$g_disable_condescending_comments", 0),
			(try_end),
		],),

	
	("tournament_title_bar", xgm_ov_title, [], "Tournaments", tf_center_justify|tf_with_outline),
	
	("tpe_toggle", xgm_ov_checkbox, [], "Enable Tournament Enhancements:", 0,
		"Ticked, the enhanced tournament system is active. Unticked, tournaments are as in Native.", 0,
		[(assign, reg1, "$g_wp_tpe_active"),],
		[
			(assign, "$g_wp_tpe_active", reg1),
			(try_begin),
				(eq, "$g_wp_tpe_active", 0),
				(assign, "$tpe_quests_active", 0),
				(assign, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_OFF),
			(else_try),
				(assign, "$tpe_quests_active", 1),
				(assign, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_MEDIUM),
			(try_end),
		],),
	 
	("tpe_reactions", xgm_ov_combobutton, ["- Disabled -", "Low Reaction", "Medium Reaction", "High Reaction"], "Tournament Quests:", 0,
		"Set to disabled this will prevent tournament invitation quests from appearing.^^Each 'reaction' level will adjust how much is changed by you attending a tournament or failing to attend.^^There is a negative relation penalty for failing to attend tournaments you are invited to on the 'High Reaction' setting.", 0,
		[(assign, reg1, "$tpe_quest_reactions")],
		[
			(assign, "$tpe_quest_reactions", reg1),
			(try_begin),
				(eq, "$tpe_quest_reactions", TPE_QUEST_REACTIONS_OFF),
				(assign, "$tpe_quests_active", 0),
			(else_try),
				(assign, "$tpe_quests_active", 1),
			(try_end),
		],),
	
	("tpe_shortcuts", xgm_ov_combobutton, ["- Disabled -", "Options Panel", "Design Panel", "Information"], "TPE Setting Shortcuts:", 0,
		"Select any of the presentations on this menu and you'll immediately jump to that panel for configuring up tournament settings.", 0,
		[(assign, reg1, 0)],
		[
			(try_begin),
				(eq, reg1, 1),
				(neq, "$g_is_quick_battle", 1), # Not using a custom battle.
				## Options Panel
				(change_screen_return),
				(assign, "$g_wp_tpe_troop", "trp_player"),
				(troop_set_slot, "trp_tpe_presobj", tpe_options_display_mode, wp_tpe_combat_settings),
				(assign, "$return_presentation", "prsnt_mod_option"),
				(start_presentation, "prsnt_tournament_options_panel"),
			(else_try),
				(eq, reg1, 2),
				(neq, "$g_is_quick_battle", 1), # Not using a custom battle.
				## Design Panel
				(change_screen_return),
				(assign, "$tournament_town", "p_town_1"), # Just picking a default.
				(assign, "$return_presentation", "prsnt_mod_option"),
				(start_presentation, "prsnt_tpe_design_settings"),
			(else_try),
				(eq, reg1, 3),
				(neq, "$g_is_quick_battle", 1), # Not using a custom battle.
				## Help Panel
				(change_screen_return),
				(troop_set_slot, tci_objects, tci_val_information_mode, 0),
				(assign, "$return_presentation", "prsnt_mod_option"),
				(start_presentation, "prsnt_tpe_credits"),
			(try_end),
		],),
	
	
	("weather_title_bar", xgm_ov_title, [], "Weather", tf_center_justify|tf_with_outline),
	
	("cc_weather_rain", xgm_ov_numberbox, [0,101], "Probability of rain/snow (%):", 0,
		"Can set the likelihood of precipitation in battles.", 0,
		[(assign, reg1, "$g_rand_rain_limit"),],
		[(assign, "$g_rand_rain_limit", reg1),],),

	("cc_weather_cloud", xgm_ov_numberbox, [0,101], "Cloud amount:", 0,
		"Sets the cloud cover on the map and in battles, which increases the likelihood of rain/snow.", 0,
		[(get_global_cloud_amount, reg1),],
		[(set_global_cloud_amount, reg1),],),

	("cc_weather_fog", xgm_ov_numberbox, [0,101], "Fog strength:", 0,
		"Sets fog strength on the map and in battles.", 0,
		[(get_global_haze_amount, reg1),],
		[(set_global_haze_amount, reg1),],),	
	
	
	("cheats_title_bar", xgm_ov_title, [], "Cheats", tf_center_justify|tf_with_outline),
	
	("pbod_npc_complaints", xgm_ov_checkbox, [], "Disable Companions' complaints:", 0,
		"Disabling NPC Complaints will mute your companion's complaints about each other or your decisions. It will not remove the consequences of their opinions, however.", 0,
		[(assign, reg1, "$disable_npc_complaints"),],
		[(assign, "$disable_npc_complaints", reg1),],),

	("pbod_cheat_mode", xgm_ov_checkbox, [], "Enable the cheat menu:", 0,
		"The cheat/debug mode activates debug messages as well as the 'cheatmenu' in your Camp Menu and additional options under Reports.", 0,
		[(assign, reg1, "$cheat_mode"),],
		[(assign, "$cheat_mode", reg1),],),	

	("option_bandit_heroes", xgm_ov_checkbox, [], "Enable Bandit Heroes:", 0,
		"When checked, bandit heroes will randomly spawn on the map gathering other bandits of the same type to them to form a larger party.", 0,
		[(assign, reg1, "$enable_bandit_heroes"),],
		[(assign, "$enable_bandit_heroes", reg1),],),	

	("limit_bandit_heroes", xgm_ov_numberbox, [1, 16], "Limit Bandit Hero Allies:", 0,
		"This number directly limits how many additional bandit parties may accompany an active bandit hero.", 0,
		[(assign, reg1, "$bandit_hero_limiter"),],
		[(assign, "$bandit_hero_limiter", reg1),],),
	  	 	
]


# TODO: add option pages here


# collation of all *_mod_options.py from active mods
# import and merge related variables from all {active_mod}_mod_options.py for all active mods
try:
    from modmerger_options import options, mods_active
    from modmerger import mod_get_process_order, mod_is_active
    from util_common import add_objects
    modcomp_name = "mod_options"
    var_list = ["mod_options",]
    
    #from modmerger import modmerge
    #modmerge(var_set)

    mod_process_order = mod_get_process_order(modcomp_name)
    
    vars_to_import= ["mod_options"]
    
    for x in mod_process_order:
        if(mod_is_active(x) and x <> "xgm_mod_options"): # must exclude this file since we are using this file as base
            try:
                #mergefn_name = "modmerge_%s"%(modcomp_name)
                target_module_name = "%s_%s"%(x,modcomp_name)
                
                _temp = __import__( target_module_name , globals(), locals(), vars_to_import,-1)
                logger.info("Merging objects for component \"%s\" from mod \"%s\"..."%(modcomp_name,x))

                add_objects(mod_options, _temp.mod_options) # import from target module.

                # TODO: collect option pages

            except ImportError:
                errstring = "Failed importing for component \"%s\" for mod \"%s\"." % (modcomp_name, x)
                logger.debug(errstring)
        else:
            errstring = "Mod \"%s\" not active for Component \"%s\"." % (x, modcomp_name)
            logger.debug(errstring)

except:
    raise
# collation end

# At this point, mod_options will contain the list of all mod_options specified.



## utility functions

from util_wrappers import *

# helper wrapper to access mod_options
class ModOptionWrapper(BaseWrapper):

    def __init__(self, _data):
        # verify _data
        if( not isinstance(_data,TupleType) or (len(_data)<2)):
            raise ValueError("ItemSetWrapper: Wrapped must be a tuple.")
        BaseWrapper.__init__(self,_data)
        
        
    def GetId(self):
        return self.data[0]

    def GetType(self):
        return self.data[1]

    def GetParameters(self):
        if len(self.data) >2: 
            return self.data[2]
        return None

    def GetParameter(self, i):
        if len(self.data) >2: 
            return self.data[2][i]
        return None

    def GetTextLabel(self):
        if len(self.data) >3: 
            return self.data[3]
        return None

    def GetTextLabelFlags(self):
        if len(self.data) >4: 
            return self.data[4]
        return None

    def GetDescription(self):
        if len(self.data) >5: 
            return self.data[5]
        return None

    def GetDescriptionFlags(self):
        if len(self.data) >6: 
            return self.data[6]
        return None

    def GetInitializeBlock(self):
        if len(self.data) >7: 
            return OpBlockWrapper(self.data[7])
        return None

    def GetUpdateBlock(self):
        if len(self.data) >8: 
            return OpBlockWrapper(self.data[8])
        return None

    def GetHeight(self):
        if self.GetType() == xgm_ov_line:
            return xgm_mod_options_line_height
        elif self.GetType() in [xgm_ov_checkbox, xgm_ov_numberbox, xgm_ov_combolabel, xgm_ov_combobutton, xgm_ov_title]:
            return xgm_mod_options_property_height        
        return 0 # no other types supported

## class ModOptionWrapper
	


# this function will compute the total height required for a list of mod_options.
def mod_options_get_total_height(_mod_options = mod_options):
    height = 0
    for x in _mod_options:
        aModOption = ModOptionWrapper(x)
        height += aModOption.GetHeight()	
    # for x in _mod_options:
    return height;    
## mod_options_get_total_height	
