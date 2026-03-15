from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
#And here start the party templates. Please note that the minimum is the same as in native, while the maximum is twice native.
	("none"								,"none"								,icon_people_gray_knight																			,0		,fac_commoners		,merchant_personality			,[]),
	("rescued_prisoners"				,"Rescued Prisoners"				,icon_people_gray_knight																			,0		,fac_commoners		,merchant_personality			,[]),
	("enemy"							,"Enemy"							,icon_people_gray_knight																			,0		,fac_undeads		,merchant_personality			,[]),
	("hero_party"						,"Hero Party"						,icon_people_gray_knight																			,0		,fac_commoners		,merchant_personality			,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_people_vaegir_knight,0,fac_neutral,merchant_personality,[]),
	("village_defenders"				,"Village Defenders"				,icon_people_peasant																				,0		,fac_commoners		,merchant_personality			,[(trp_mercenary_n_farmer,10,40),(trp_woman_n_peasant,0,8)]),
	("village_defenders_r"				,"Village Defenders"				,icon_people_peasant																				,0		,fac_commoners		,merchant_personality			,[(trp_mercenary_r_farmer,10,40),(trp_woman_r_peasant,0,8)]),
	("village_defenders_e"				,"Village Defenders"				,icon_people_peasant																				,0		,fac_commoners		,merchant_personality			,[(trp_mercenary_e_farmer,10,40),(trp_woman_e_peasant,0,8)]),

	("cattle_herd"						,"Cattle Herd"						,icon_people_cattle|carries_goods(10)																,0		,fac_neutral		,merchant_personality			,[(trp_cattle,80,120)]),

##	("vaegir_nobleman"					,"Vaegir Nobleman"					,icon_people_vaegir_knight|carries_goods(10)|pf_quest_party											,0		,fac_commoners		,merchant_personality			,[(trp_nobleman,1,1),(:vaegir_voevoda,2,12),(:vaegir_posadnik,4,24)]),
##	("swadian_nobleman"					,"Swadian Nobleman"					,icon_people_gray_knight|carries_goods(10)|pf_quest_party											,0		,fac_commoners		,merchant_personality			,[(trp_nobleman,1,1),(:swadian_chevalier_banneret,2,12),(:swadian_chevalier,4,24)]),
##	("peasant"							,"Peasant"							,icon_people_peasant																				,0		,fac_commoners		,merchant_personality			,[(:mercenary_farmer,1,12),(:woman_peasant,0,14)]),

## CC
#	("black_khergit_raiders"			,"Black Khergit Raiders"			,icon_people_khergit_horseman_b|carries_goods(2)													,0		,fac_black_khergits	,bandit_personality				,[(trp_khergit_e_mandugai,2,40),(trp_khergit_e_cherbi,6,28),(trp_bandit_e_black_khergit_horseman,10,20)]),
#	("dark_hunters"						,"Dark Hunters"						,icon_people_gray_knight																			,0		,fac_dark_knights	,soldier_personality			,[(trp_dark_knight,4,22),(trp_dark_sniper,10,20),(trp_dark_hunter,13,25)]),
##

##Bandits
	#Native
	("looters"							,"Looters"							,icon_people_axeman|carries_goods(8)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_n_looter,6,45)]),#Diplomacy 3.2 # 3-90
	("manhunters"						,"Manhunters"						,icon_people_gray_knight																			,0		,fac_manhunters		,soldier_personality			,[(trp_bandit_n_manhunter,18,40)]), # 9-80
	("forest_bandits"					,"Forest Bandits"					,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_n_forest,8,52)]), # 4-104
	("taiga_bandits"					,"Tundra Bandits"					,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_n_taiga,8,58)]), # 4-116
	("steppe_bandits"					,"Steppe Bandits"					,icon_people_khergit|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_n_steppe,8,58)]), # 4-115
	("sea_raiders"						,"Sea Raiders"						,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_n_sea_raider,10,50)]), # 5-100
	("mountain_bandits"					,"Mountain Bandits"					,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_n_mountain,8,60)]), # 4-120
	("desert_bandits"					,"Desert Bandits"					,icon_people_vaegir_knight|carries_goods(2)															,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_n_desert,8,58)]), # 4-116
	#Reworked
	("looters_r"						,"Looters"							,icon_people_axeman|carries_goods(8)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_r_looter,6,45)]),#Diplomacy 3.2 # 3-90
	("manhunters_r"						,"Manhunters"						,icon_people_gray_knight																			,0		,fac_manhunters		,soldier_personality			,[(trp_bandit_r_manhunter,18,40)]), # 9-80
	("forest_bandits_r"					,"Forest Bandits"					,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_r_forest,8,52)]), # 4-104
	("taiga_bandits_r"					,"Tundra Bandits"					,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_r_taiga,8,58)]), # 4-116
	("steppe_bandits_r"					,"Steppe Bandits"					,icon_people_khergit|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_r_steppe,8,58)]), # 4-116
	("sea_raiders_r"					,"Sea Raiders"						,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_r_sea_raider,10,50)]), # 5-100
	("mountain_bandits_r"				,"Mountain Bandits"					,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_r_mountain,8,60)]), # 4-120
	("desert_bandits_r"					,"Desert Bandits"					,icon_people_vaegir_knight|carries_goods(2)															,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_r_desert,8,58)]), # 4-116
	#Expanded
	("looters_e"						,"Looters"							,icon_people_axeman|carries_goods(8)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_e_looter,6,45)]),#Diplomacy 3.2 # 3-90
	("manhunters_e"						,"Manhunters"						,icon_people_gray_knight																			,0		,fac_manhunters		,soldier_personality			,[(trp_bandit_e_manhunter,18,40)]), # 9-80
	("forest_bandits_e"					,"Forest Bandits"					,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_e_forest,8,52)]), # 4-104
	("taiga_bandits_e"					,"Tundra Bandits"					,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_e_taiga,8,58)]), # 4-116
	("steppe_bandits_e"					,"Steppe Bandits"					,icon_people_khergit|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_e_steppe,8,58)]), # 4-116
	("sea_raiders_e"					,"Sea Raiders"						,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_e_sea_raider,10,50)]), # 5-100
	("mountain_bandits_e"				,"Mountain Bandits"					,icon_people_axeman|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_e_mountain,8,60)]), # 4-120
	("desert_bandits_e"					,"Desert Bandits"					,icon_people_vaegir_knight|carries_goods(2)															,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_e_desert,8,58)]), # 4-116

	("deserters"						,"Deserters"						,icon_people_vaegir_knight|carries_goods(3)															,0		,fac_deserters		,bandit_personality				,[]),

##Merchant Caravan
	#Native
	("merchant_caravan"					,"Merchant Caravan"					,icon_people_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party					,0		,fac_commoners		,escorted_merchant_personality	,[(trp_caravan_master,1,1),(trp_mercenary_n_page,4,32),(trp_mercenary_n_soldner,1,10),(trp_mercenary_n_ritter,0,4),(trp_mercenary_n_ritter,0,4)]),
	("troublesome_bandits"				,"Troublesome Bandits"				,icon_people_axeman|carries_goods(9)|pf_quest_party													,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_n_bandit,28,55)]), # 14-110
	("bandits_awaiting_ransom"			,"Bandits Awaiting Ransom"			,icon_people_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party							,0		,fac_neutral		,bandit_personality				,[(trp_bandit_n_bandit,40,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]), # 24-116
	#Reworked
	("merchant_caravan_r"				,"Merchant Caravan"					,icon_people_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party					,0		,fac_commoners		,escorted_merchant_personality	,[(trp_caravan_master,1,1),(trp_mercenary_r_halberdier,4,32),(trp_mercenary_r_armbrust_soldner,1,10),(trp_mercenary_r_reichslandser,0,4),(trp_mercenary_r_ritter,0,4)]),
	("troublesome_bandits_r"			,"Troublesome Bandits"				,icon_people_axeman|carries_goods(9)|pf_quest_party													,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_r_bandit,28,55)]), # 14-110
	("bandits_awaiting_ransom_r"		,"Bandits Awaiting Ransom"			,icon_people_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party							,0		,fac_neutral		,bandit_personality				,[(trp_bandit_r_bandit,40,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]), # 24-116
	#Expanded
	("merchant_caravan_e"				,"Merchant Caravan"					,icon_people_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party					,0		,fac_commoners		,escorted_merchant_personality	,[(trp_caravan_master,1,1),(trp_mercenary_e_volksheer,4,32),(trp_mercenary_e_armbrust_komtur,1,10),(trp_mercenary_e_reichslandser,0,4),(trp_mercenary_e_ritter,0,4)]),
	("troublesome_bandits_e"			,"Troublesome Bandits"				,icon_people_axeman|carries_goods(9)|pf_quest_party													,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_e_bandit,28,55)]), # 14-110
	("bandits_awaiting_ransom_e"		,"Bandits Awaiting Ransom"			,icon_people_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party							,0		,fac_neutral		,bandit_personality				,[(trp_bandit_e_bandit,40,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]), # 24-116

	("kidnapped_girl"					,"Kidnapped Girl"					,icon_people_woman|pf_quest_party																	,0		,fac_neutral		,merchant_personality			,[(trp_kidnapped_girl,1,1)]),

	#Native
	("village_farmers"					,"Village Farmers"					,icon_people_peasant|pf_civilian																	,0		,fac_innocents		,merchant_personality			,[(trp_mercenary_n_farmer,5,20),(trp_woman_n_peasant,3,16)]),
	("spy_partners"						,"Unremarkable Travellers"			,icon_people_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party						,0		,fac_neutral		,merchant_personality			,[(trp_spy_partner,1,1),(trp_mercenary_n_soldner,2,8),(trp_mercenary_n_soldner,2,8),(trp_mercenary_n_ritter,1,4),(trp_mercenary_n_komtur,0,2)]),
	("runaway_serfs"					,"Runaway Serfs"					,icon_people_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party							,0		,fac_neutral		,merchant_personality			,[(trp_mercenary_n_farmer,5,20),(trp_woman_n_peasant,3,16)]),
	#Reworked
	("village_farmers_r"				,"Village Farmers"					,icon_people_peasant|pf_civilian																	,0		,fac_innocents		,merchant_personality			,[(trp_mercenary_r_farmer,5,20),(trp_woman_r_peasant,3,16)]),
	("spy_partners_r"					,"Unremarkable Travellers"			,icon_people_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party						,0		,fac_neutral		,merchant_personality			,[(trp_spy_partner,1,1),(trp_mercenary_r_brabanzon,2,8),(trp_mercenary_r_armbrust_komtur,2,8),(trp_mercenary_r_reichslandser,1,4),(trp_mercenary_r_armbrust_komtur,0,2)]),
	("runaway_serfs_r"					,"Runaway Serfs"					,icon_people_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party							,0		,fac_neutral		,merchant_personality			,[(trp_mercenary_r_farmer,5,20),(trp_woman_r_peasant,3,16)]),
	#Expanded
	("village_farmers_e"				,"Village Farmers"					,icon_people_peasant|pf_civilian																	,0		,fac_innocents		,merchant_personality			,[(trp_mercenary_e_farmer,5,20),(trp_woman_e_peasant,3,16)]),
	("spy_partners_e"					,"Unremarkable Travellers"			,icon_people_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party						,0		,fac_neutral		,merchant_personality			,[(trp_spy_partner,1,1),(trp_mercenary_e_ritterbroeder,2,8),(trp_mercenary_e_armbrust_komtur,2,8),(trp_mercenary_e_reichslandser,1,4),(trp_mercenary_e_doppelsoldner,0,2)]),
	("runaway_serfs_e"					,"Runaway Serfs"					,icon_people_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party							,0		,fac_neutral		,merchant_personality			,[(trp_mercenary_e_farmer,5,20),(trp_woman_e_peasant,3,16)]),

	("spy"								,"Ordinary Townsman"				,icon_people_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party						,0		,fac_neutral		,merchant_personality			,[(trp_spy,1,1)]),
	("sacrificed_messenger"				,"Sacrificed Messenger"				,icon_people_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party						,0		,fac_neutral		,merchant_personality			,[]),
##	("conspirator"						,"Conspirators"						,icon_people_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party						,0		,fac_neutral		,merchant_personality			,[(trp_conspirator,3,8)]),
##	("conspirator_leader"				,"Conspirator Leader"				,icon_people_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party						,0		,fac_neutral		,merchant_personality			,[(trp_conspirator_leader,1,1)]),
##	("peasant_rebels"					,"Peasant Rebels"					,icon_people_peasant																				,0		,fac_peasant_rebels	,bandit_personality				,[(trp_peasant_rebel,33,194)]),
##	("noble_refugees"					,"Noble Refugees"					,icon_people_gray_knight|carries_goods(12)|pf_quest_party											,0		,fac_noble_refugees	,merchant_personality			,[(trp_noble_refugee,3,10),(trp_noble_refugee_woman,5,14)]),

	("forager_party"					,"Foraging Party"					,icon_people_gray_knight|carries_goods(5)|pf_show_faction											,0		,fac_commoners		,merchant_personality			,[]),
	("scout_party"						,"Scouts"							,icon_people_gray_knight|carries_goods(1)|pf_show_faction											,0		,fac_commoners		,bandit_personality				,[]),
	("patrol_party"						,"Patrol"							,icon_people_gray_knight|carries_goods(2)|pf_show_faction											,0		,fac_commoners		,soldier_personality			,[]),
##	("war_party"						,"War Party"						,icon_people_gray_knight|carries_goods(3)															,0		,fac_commoners		,soldier_personality			,[]),
	("messenger_party"					,"Messenger"						,icon_people_gray_knight|pf_show_faction															,0		,fac_commoners		,merchant_personality			,[]),
	("raider_party"						,"Raiders"							,icon_people_gray_knight|carries_goods(16)|pf_quest_party											,0		,fac_commoners		,bandit_personality				,[]),

	#Native
	("raider_captives"					,"Raider Captives"					,0																									,0		,fac_commoners		,0								,[(trp_woman_n_peasant,6,60,pmf_is_prisoner)]),
	("kingdom_caravan_party"			,"Caravan"							,icon_people_mule|carries_goods(25)|pf_show_faction													,0		,fac_commoners		,merchant_personality			,[(trp_caravan_master,1,1),(trp_mercenary_n_page,10,40),(trp_mercenary_n_soldner,2,20),(trp_mercenary_n_soldner,0,10),(trp_mercenary_n_ritter,0,10)]),
	#Reworked
	("raider_captives_r"				,"Raider Captives"					,0																									,0		,fac_commoners		,0								,[(trp_woman_r_peasant,6,60,pmf_is_prisoner)]),
	("kingdom_caravan_party_r"			,"Caravan"							,icon_people_mule|carries_goods(25)|pf_show_faction													,0		,fac_commoners		,merchant_personality			,[(trp_caravan_master,1,1),(trp_mercenary_r_halberdier,10,40),(trp_mercenary_r_armbrust_komtur,2,20),(trp_mercenary_r_brabanzon,0,10),(trp_mercenary_r_ritter,0,10)]),
	#Expanded
	("raider_captives_e"				,"Raider Captives"					,0																									,0		,fac_commoners		,0								,[(trp_woman_e_peasant,6,60,pmf_is_prisoner)]),
	("kingdom_caravan_party_e"			,"Caravan"							,icon_people_mule|carries_goods(25)|pf_show_faction													,0		,fac_commoners		,merchant_personality			,[(trp_caravan_master,1,1),(trp_mercenary_e_volksheer,10,40),(trp_mercenary_e_armbrust_komtur,2,20),(trp_mercenary_e_soldner,0,10),(trp_mercenary_e_ritter,0,10)]),

	("prisoner_train_party"				,"Prisoner Train"					,icon_people_gray_knight|carries_goods(5)|pf_show_faction											,0		,fac_commoners		,merchant_personality			,[]),
##Floris addon seatrade
	#Native
	("sea_traders"						,"Royal Traders"					,icon_ship|pf_is_ship|carries_goods(50)|pf_show_faction												,0		,fac_commoners		,merchant_personality			,[(trp_caravan_master,1,1),(trp_mercenary_n_armbrust_soldner,20,40),(trp_mercenary_n_soldner,5,30),(trp_mercenary_n_komtur,5,10),(trp_mercenary_n_komtur_ritter,5,10)]),
	#Reworked
	("sea_traders_r"					,"Royal Traders"					,icon_ship|pf_is_ship|carries_goods(50)|pf_show_faction												,0		,fac_commoners		,merchant_personality			,[(trp_caravan_master,1,1),(trp_mercenary_r_burger,20,40),(trp_mercenary_r_armbrust_soldner,5,30),(trp_mercenary_r_doppelsoldner,5,10),(trp_mercenary_r_burgmann,5,10)]),
	#Expanded
	("sea_traders_e"					,"Royal Traders"					,icon_ship|pf_is_ship|carries_goods(50)|pf_show_faction												,0		,fac_commoners		,merchant_personality			,[(trp_caravan_master,1,1),(trp_mercenary_e_brabanzon,20,40),(trp_mercenary_e_armbrust_komtur,5,30),(trp_mercenary_e_kreuzritter,5,10),(trp_mercenary_e_burgmann,5,10)]),

	("ship"								,"Ship"								,icon_ship|pf_is_ship|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction	,0		,fac_commoners		,merchant_personality			,[(trp_sea_captain,1,1)]),
##Floris addon seatrade end  
	#Native
	("default_prisoners"				,"Default Prisoners"				,0																									,0		,fac_commoners		,0								,[(trp_bandit_n_bandit,5,20,pmf_is_prisoner)]),
	#Reworked
	("default_prisoners_r"				,"Default Prisoners"				,0																									,0		,fac_commoners		,0								,[(trp_bandit_r_bandit,5,20,pmf_is_prisoner)]),
	#Expanded
	("default_prisoners_e"				,"Default Prisoners"				,0																									,0		,fac_commoners		,0								,[(trp_bandit_e_bandit,5,20,pmf_is_prisoner)]),

	("routed_warriors"					,"Routed Enemies"					,icon_people_vaegir_knight																			,0		,fac_commoners		,soldier_personality			,[]),


# Caravans
	#Native
	("center_reinforcements"			,"Reinforcements"					,icon_people_axeman|carries_goods(16)																,0		,fac_commoners		,soldier_personality			,[(trp_mercenary_n_townsman,5,60),(trp_mercenary_n_page,2,14),(trp_mercenary_n_armbrust_soldner,1,14),(trp_mercenary_n_ritter,1,6),(trp_mercenary_n_komtur_ritter,0,3),(trp_mercenary_n_komtur,0,3)]),
	#Reworked
	("center_reinforcements_r"			,"Reinforcements"					,icon_people_axeman|carries_goods(16)																,0		,fac_commoners		,soldier_personality			,[(trp_mercenary_r_townsman,5,60),(trp_mercenary_r_page,2,14),(trp_mercenary_r_armbrust_soldner,1,14),(trp_mercenary_r_ritter,1,6),(trp_mercenary_r_komtur_ritter,0,3),(trp_mercenary_r_doppelsoldner,0,3)]),
	#Expanded
	("center_reinforcements_e"			,"Reinforcements"					,icon_people_axeman|carries_goods(16)																,0		,fac_commoners		,soldier_personality			,[(trp_mercenary_e_townsman,5,60),(trp_mercenary_e_page,2,14),(trp_mercenary_e_armbrust_komtur,1,14),(trp_mercenary_e_ritter,1,6),(trp_mercenary_e_kreuzritter,0,3),(trp_mercenary_e_komtur,0,3)]),

	("kingdom_hero_party"				,"War Party"						,icon_people_flagbearer_a|pf_show_faction|pf_default_behavior										,0		,fac_commoners		,soldier_personality			,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

##Native
#Swadia
	("kingdom_1_reinforcements_a"	,"{!}kingdom_1_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_farmer,0,5),(trp_swadian_n_peasant,5,13),(trp_swadian_n_militia,1,3),(trp_swadian_n_militia,1,3),(trp_swadian_n_page,0,2),(trp_swadian_n_archer_militia,0,2)]),
	("kingdom_1_reinforcements_b"	,"{!}kingdom_1_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_townsman,0,5),(trp_swadian_n_peasant,5,13),(trp_swadian_n_militia,1,3),(trp_swadian_n_militia,1,3),(trp_swadian_n_page,0,2),(trp_swadian_n_archer_militia,0,2)]),
	("kingdom_1_reinforcements_c"	,"{!}kingdom_1_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_n_huntress,0,1),(trp_swadian_n_page,1,2),(trp_swadian_n_page,1,2),(trp_swadian_n_ecuyer,0,1),(trp_swadian_n_ecuyer,0,1),(trp_swadian_n_chevalier,0,1)]),
	("kingdom_1_reinforcements_d"	,"{!}kingdom_1_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_armbrust_soldner,0,1),(trp_swadian_n_archer_militia,1,2),(trp_swadian_n_longbowman,1,2),(trp_swadian_n_longbowman,0,1),(trp_swadian_n_jock,0,1),(trp_swadian_n_selfbow_archer,0,1)]),
	("kingdom_1_reinforcements_e"	,"{!}kingdom_1_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_ritter,0,1),(trp_swadian_n_page,1,2),(trp_swadian_n_jacobite,1,2),(trp_swadian_n_jacobite,0,1),(trp_swadian_n_jock,0,1),(trp_swadian_n_jock,0,1)]),
	("kingdom_1_reinforcements_f"	,"{!}kingdom_1_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_swadian_n_chevalier,1,3),(trp_swadian_n_selfbow_archer,1,3),(trp_swadian_n_chevalier,1,2),(trp_swadian_n_selfbow_archer,0,2),(trp_swadian_n_chevalier,0,1),(trp_swadian_n_selfbow_archer,0,1)]),
#Vaegir
	("kingdom_2_reinforcements_a"	,"{!}kingdom_2_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_farmer,0,5),(trp_vaegir_n_kholop,5,13),(trp_vaegir_n_otrok,1,3),(trp_vaegir_n_otrok,1,3),(trp_vaegir_n_kazak,0,2),(trp_vaegir_n_kmet,0,2)]),
	("kingdom_2_reinforcements_b"	,"{!}kingdom_2_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_townsman,0,5),(trp_vaegir_n_kholop,5,13),(trp_vaegir_n_otrok,1,3),(trp_vaegir_n_otrok,1,3),(trp_vaegir_n_kmet,0,2),(trp_vaegir_n_kmet,0,2)]),
	("kingdom_2_reinforcements_c"	,"{!}kingdom_2_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_page,0,1),(trp_vaegir_n_kmet,1,2),(trp_vaegir_n_kmet,1,2),(trp_vaegir_n_zalstrelshik,0,1),(trp_vaegir_n_zalstrelshik,0,1),(trp_vaegir_n_druzhinnik_veteran,0,1)]),
	("kingdom_2_reinforcements_d"	,"{!}kingdom_2_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_woman_n_huntress,0,1),(trp_vaegir_n_kazak,1,2),(trp_vaegir_n_yesaul,1,2),(trp_vaegir_n_plastun,0,1),(trp_vaegir_n_pansirniy_kazan,0,1),(trp_vaegir_n_luchnik,0,1)]),
	("kingdom_2_reinforcements_e"	,"{!}kingdom_2_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_woman_n_maiden,0,1),(trp_vaegir_n_kmet,1,2),(trp_vaegir_n_yesaul,1,2),(trp_vaegir_n_plastun,0,1),(trp_vaegir_n_luchnik,0,1),(trp_vaegir_n_druzhinnik_veteran,0,1)]),
	("kingdom_2_reinforcements_f"	,"{!}kingdom_2_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_vaegir_n_pansirniy_kazan,1,3),(trp_vaegir_n_luchnik,1,3),(trp_vaegir_n_pansirniy_kazan,1,2),(trp_vaegir_n_luchnik,0,2),(trp_vaegir_n_pansirniy_kazan,0,1),(trp_vaegir_n_druzhinnik_veteran,0,1)]),
#Khergit
	("kingdom_3_reinforcements_a"	,"{!}kingdom_3_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_farmer,0,5),(trp_khergit_n_tariachin,3,9),(trp_khergit_n_qarbughaci,1,3),(trp_khergit_n_qarbughaci,1,3),(trp_khergit_n_morici,1,4),(trp_khergit_n_morici,1,4)]),
	("kingdom_3_reinforcements_b"	,"{!}kingdom_3_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_townsman,0,5),(trp_khergit_n_tariachin,3,9),(trp_khergit_n_qarbughaci,1,3),(trp_khergit_n_qarbughaci,1,3),(trp_khergit_n_morici,1,4),(trp_khergit_n_morici,1,4)]),
	("kingdom_3_reinforcements_c"	,"{!}kingdom_3_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_n_maiden,0,1),(trp_khergit_n_morici,1,2),(trp_khergit_n_morici,1,2),(trp_khergit_n_kipchak,0,1),(trp_khergit_n_kipchak,1,2),(trp_khergit_n_borjigin,0,1)]),
	("kingdom_3_reinforcements_d"	,"{!}kingdom_3_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_page,0,1),(trp_khergit_n_morici,1,2),(trp_khergit_n_qubuci,1,2),(trp_khergit_n_qubuci,0,1),(trp_khergit_n_borjigin,0,1),(trp_khergit_n_borjigin,0,1)]),
	("kingdom_3_reinforcements_e"	,"{!}kingdom_3_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_woman_n_maiden,0,1),(trp_khergit_n_morici,1,2),(trp_khergit_n_qubuci,1,2),(trp_khergit_n_qubuci,1,0),(trp_khergit_n_borjigin,0,1),(trp_khergit_n_borjigin,0,1)]),
	("kingdom_3_reinforcements_f"	,"{!}kingdom_3_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_khergit_n_borjigin,1,3),(trp_khergit_n_borjigin,1,3),(trp_khergit_n_borjigin,1,2),(trp_khergit_n_borjigin,0,2),(trp_khergit_n_borjigin,0,1),(trp_khergit_n_borjigin,0,1)]),
#Nord
	("kingdom_4_reinforcements_a"	,"{!}kingdom_4_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_farmer,0,5),(trp_nord_n_bondi,2,5),(trp_nord_n_gesith,3,7),(trp_nord_n_huskarl,3,7),(trp_nord_n_bogmadur,1,2),(trp_nord_n_gridman,1,2)]),
	("kingdom_4_reinforcements_b"	,"{!}kingdom_4_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_townsman,0,5),(trp_nord_n_bondi,2,5),(trp_nord_n_gesith,3,7),(trp_nord_n_huskarl,3,7),(trp_nord_n_bogmadur,1,2),(trp_nord_n_gridman,1,2)]),
	("kingdom_4_reinforcements_c"	,"{!}kingdom_4_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_page,0,1),(trp_nord_n_bogmadur,1,2),(trp_nord_n_vigamadr,1,2),(trp_nord_n_vigamadr,0,1),(trp_nord_n_bogsveigir,0,1),(trp_nord_n_skjadsveinn,0,1)]),
	("kingdom_4_reinforcements_d"	,"{!}kingdom_4_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_woman_n_huntress,0,1),(trp_nord_n_bogmadur,1,2),(trp_nord_n_bogsveigir,1,2),(trp_nord_n_vigamadr,0,1),(trp_nord_n_skjadsveinn,0,1),(trp_nord_n_skjadsveinn,0,1)]),
	("kingdom_4_reinforcements_e"	,"{!}kingdom_4_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_ritter,0,1),(trp_nord_n_gridman,1,2),(trp_nord_n_bogsveigir,1,2),(trp_nord_n_vigamadr,0,1),(trp_nord_n_skjadsveinn,0,1),(trp_nord_n_skjadsveinn,0,1)]),
	("kingdom_4_reinforcements_f"	,"{!}kingdom_4_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_nord_n_skjadsveinn,1,3),(trp_nord_n_skjadsveinn,1,3),(trp_nord_n_husbondi,1,2),(trp_nord_n_husbondi,0,2),(trp_nord_n_husbondi,0,1),(trp_nord_n_husbondi,0,1)]),
#Rhodok
	("kingdom_5_reinforcements_a"	,"{!}kingdom_5_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_farmer,0,5),(trp_rhodok_n_cittadino,4,9),(trp_rhodok_n_novizio,2,5),(trp_rhodok_n_recluta_balestriere,2,5),(trp_rhodok_n_milizia,1,2),(trp_rhodok_n_milizia_balestriere,1,2)]),
	("kingdom_5_reinforcements_b"	,"{!}kingdom_5_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_townsman,0,5),(trp_rhodok_n_cittadino,4,9),(trp_rhodok_n_novizio,2,5),(trp_rhodok_n_recluta_balestriere,2,5),(trp_rhodok_n_milizia_balestriere,1,2),(trp_rhodok_n_milizia,1,2)]),
	("kingdom_5_reinforcements_c"	,"{!}kingdom_5_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_armbrust_soldner,0,1),(trp_rhodok_n_milizia,1,2),(trp_rhodok_n_balestriere,1,2),(trp_rhodok_n_fante,0,1),(trp_rhodok_n_fante,0,1),(trp_rhodok_n_veterano,0,1)]),
	("kingdom_5_reinforcements_d"	,"{!}kingdom_5_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_page,0,1),(trp_rhodok_n_milizia_balestriere,1,2),(trp_rhodok_n_fante,1,2),(trp_rhodok_n_fante,0,1),(trp_rhodok_n_balestriere,0,1),(trp_rhodok_n_veterano,0,1)]),
	("kingdom_5_reinforcements_e"	,"{!}kingdom_5_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_woman_n_maiden,0,1),(trp_rhodok_e_fante,1,2),(trp_rhodok_n_balestriere,1,2),(trp_rhodok_n_fante,0,1),(trp_rhodok_n_fante,0,1),(trp_rhodok_n_veterano,0,1)]),
	("kingdom_5_reinforcements_f"	,"{!}kingdom_5_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_rhodok_n_veterano,1,3),(trp_rhodok_n_balestriere_veterano,1,3),(trp_rhodok_n_veterano,1,2),(trp_rhodok_n_balestriere_veterano,0,2),(trp_rhodok_n_veterano,0,1),(trp_rhodok_n_balestriere_veterano,0,1)]), 
#Sarranid
	("kingdom_6_reinforcements_a"	,"{!}kingdom_6_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_farmer,0,5),(trp_sarranid_n_millet,5,13),(trp_sarranid_n_ajam,1,3),(trp_sarranid_n_ajam,1,3),(trp_sarranid_n_cemaat,0,2),(trp_sarranid_n_jebelus,0,2)]),
	("kingdom_6_reinforcements_b"	,"{!}kingdom_6_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_townsman,0,5),(trp_sarranid_n_millet,5,13),(trp_sarranid_n_ajam,1,3),(trp_sarranid_n_ajam,1,3),(trp_sarranid_n_cemaat,0,2),(trp_sarranid_n_jebelus,0,2)]),
	("kingdom_6_reinforcements_c"	,"{!}kingdom_6_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_n_huntress,0,1),(trp_sarranid_n_cemaat,1,2),(trp_sarranid_n_jebelus,1,2),(trp_sarranid_n_garip,0,1),(trp_sarranid_n_garip,0,1),(trp_sarranid_e_terkes_serdengecti,0,1)]),
	("kingdom_6_reinforcements_d"	,"{!}kingdom_6_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_page,0,1),(trp_sarranid_n_cemaat,1,2),(trp_sarranid_n_timariot,1,2),(trp_sarranid_n_yerliyya,0,1),(trp_sarranid_n_yeniceri,0,1),(trp_sarranid_n_yeniceri,0,1)]),
	("kingdom_6_reinforcements_e"	,"{!}kingdom_6_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_ritter,0,1),(trp_sarranid_n_jebelus,1,2),(trp_sarranid_n_yerliyya,1,2),(trp_sarranid_n_garip,0,1),(trp_sarranid_n_yeniceri,0,1),(trp_sarranid_n_uluteci,0,1)]),
	("kingdom_6_reinforcements_f"	,"{!}kingdom_6_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_sarranid_n_kapikula,1,3),(trp_sarranid_n_uluteci,1,3),(trp_sarranid_n_kapikula,1,2),(trp_sarranid_n_uluteci,0,2),(trp_sarranid_n_kapikula,0,1),(trp_sarranid_n_uluteci,0,1)]),
#Player Faction: Custom troops
	("kingdom_7_reinforcements_a"	,"{!}kingdom_7_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_farmer,0,5),(trp_custom_n_recruit,5,13),(trp_custom_n_militia,1,3),(trp_custom_n_militia,1,3),(trp_custom_n_guard,0,2),(trp_custom_n_page,0,2)]),
	("kingdom_7_reinforcements_b"	,"{!}kingdom_7_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_townsman,0,2),(trp_custom_n_recruit,5,9),(trp_custom_n_militia,1,3),(trp_custom_n_militia,1,3),(trp_custom_n_page,0,2),(trp_custom_n_guard,0,2)]),
	("kingdom_7_reinforcements_c"	,"{!}kingdom_7_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_n_huntress,0,1),(trp_custom_n_guard,1,2),(trp_custom_n_swordman,1,2),(trp_custom_n_archer,0,1),(trp_custom_n_knight,0,1),(trp_custom_n_expert_archer,0,1)]),
	("kingdom_7_reinforcements_d"	,"{!}kingdom_7_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_armbrust_soldner,0,1),(trp_custom_n_page,1,2),(trp_custom_n_swordman,1,2),(trp_custom_n_archer,0,1),(trp_custom_n_swordmaster,0,1),(trp_custom_n_expert_archer,0,1)]),
	("kingdom_7_reinforcements_e"	,"{!}kingdom_7_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_n_ritter,0,1),(trp_custom_n_guard,1,2),(trp_custom_n_squire,1,2),(trp_mercenary_n_soldner,0,1),(trp_custom_n_swordmaster,0,1),(trp_custom_n_expert_archer,0,1)]),
	("kingdom_7_reinforcements_f"	,"{!}kingdom_7_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_custom_n_knight,1,3),(trp_custom_n_expert_archer,1,3),(trp_mercenary_n_komtur,1,2),(trp_mercenary_n_komtur,0,2),(trp_woman_n_swob_ridder,0,1),(trp_woman_n_swob_ridder,0,1)]),
##Reworked
#Swadia
	("kingdom_1_reinforcements_a_r"	,"{!}kingdom_1_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_farmer,0,5),(trp_swadian_r_peasant,5,13),(trp_swadian_r_militia,1,3),(trp_swadian_r_peasant_archer,1,3),(trp_swadian_r_page,0,2),(trp_swadian_r_sergeant_at_arms,0,2)]),
	("kingdom_1_reinforcements_b_r"	,"{!}kingdom_1_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_townsman,0,5),(trp_swadian_r_peasant,5,13),(trp_swadian_r_militia,1,3),(trp_swadian_r_peasant_archer,1,3),(trp_swadian_r_sergeant_at_arms,0,2),(trp_swadian_r_archer_militia,0,2)]),
	("kingdom_1_reinforcements_c_r"	,"{!}kingdom_1_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_r_huntress,0,1),(trp_swadian_r_sergeant_at_arms,1,2),(trp_swadian_r_page,1,2),(trp_swadian_r_piquier,0,1),(trp_swadian_r_ecuyer,0,1),(trp_swadian_r_chevalier,0,1)]),
	("kingdom_1_reinforcements_d_r"	,"{!}kingdom_1_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_burger,0,1),(trp_swadian_r_archer_militia,1,2),(trp_swadian_r_longbowman,1,2),(trp_swadian_r_longbowman,0,1),(trp_swadian_r_jock,0,1),(trp_swadian_r_selfbow_archer,0,1)]),
	("kingdom_1_reinforcements_e_r"	,"{!}kingdom_1_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_reichslandser,0,1),(trp_swadian_r_sergeant_at_arms,1,2),(trp_swadian_r_jacobite,1,2),(trp_swadian_r_hobilar,0,1),(trp_swadian_r_jock,0,1),(trp_swadian_r_jock,0,1)]),
	("kingdom_1_reinforcements_f_r"	,"{!}kingdom_1_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_swadian_r_chevalier,1,3),(trp_swadian_r_selfbow_archer,1,3),(trp_swadian_r_chevalier_banneret,1,2),(trp_swadian_r_selfbow_archer,0,2),(trp_swadian_r_chevalier_banneret,0,1),(trp_swadian_r_selfbow_archer,0,1)]),
#Vaegir
	("kingdom_2_reinforcements_a_r"	,"{!}kingdom_2_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_farmer,0,5),(trp_vaegir_r_kholop,5,13),(trp_vaegir_r_otrok,1,3),(trp_vaegir_r_pasynok,1,3),(trp_vaegir_r_kazak,0,2),(trp_vaegir_r_kmet,0,2)]),
	("kingdom_2_reinforcements_b_r"	,"{!}kingdom_2_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_townsman,0,5),(trp_vaegir_r_kholop,5,13),(trp_vaegir_r_otrok,1,3),(trp_vaegir_r_pasynok,1,3),(trp_vaegir_r_grid,0,2),(trp_vaegir_r_kmet,0,2)]),
	("kingdom_2_reinforcements_c_r"	,"{!}kingdom_2_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_halberdier,0,1),(trp_vaegir_r_kmet,1,2),(trp_vaegir_r_grid,1,2),(trp_vaegir_r_zalstrelshik,0,1),(trp_vaegir_r_mladshiy_druzhinnik,0,1),(trp_vaegir_r_druzhinnik_veteran,0,1)]),
	("kingdom_2_reinforcements_d_r"	,"{!}kingdom_2_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_woman_r_stedinger,0,1),(trp_vaegir_r_kazak,1,2),(trp_vaegir_r_yesaul,1,2),(trp_vaegir_r_plastun,0,1),(trp_vaegir_r_ataman,0,1),(trp_vaegir_r_luchnik,0,1)]),
	("kingdom_2_reinforcements_e_r"	,"{!}kingdom_2_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_woman_r_mounted_markswoman,0,1),(trp_vaegir_r_grid,1,2),(trp_vaegir_r_ratnik,1,2),(trp_vaegir_r_mladshiy_druzhinnik,0,1),(trp_vaegir_r_luchnik,0,1),(trp_vaegir_r_druzhinnik_veteran,0,1)]),
	("kingdom_2_reinforcements_f_r"	,"{!}kingdom_2_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_vaegir_r_ataman,1,3),(trp_vaegir_r_luchnik,1,3),(trp_vaegir_r_luchnik,1,2),(trp_vaegir_r_metkiy_luchnik,0,2),(trp_vaegir_r_ataman,0,1),(trp_vaegir_r_metkiy_luchnik,0,1)]),
#Khergit
	("kingdom_3_reinforcements_a_r"	,"{!}kingdom_3_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_farmer,0,5),(trp_khergit_r_tariachin,3,9),(trp_khergit_r_tsereg,1,3),(trp_khergit_r_qarbughaci,1,3),(trp_khergit_r_morici,1,4),(trp_khergit_r_asud,1,4)]),
	("kingdom_3_reinforcements_b_r"	,"{!}kingdom_3_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_townsman,0,5),(trp_khergit_r_tariachin,3,9),(trp_khergit_r_tsereg,1,3),(trp_khergit_r_qarbughaci,1,3),(trp_khergit_r_asud,1,4),(trp_khergit_r_abaci,1,4)]),
	("kingdom_3_reinforcements_c_r"	,"{!}kingdom_3_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_r_mounted_markswoman,0,1),(trp_khergit_r_morici,1,2),(trp_khergit_r_asud,1,2),(trp_khergit_r_kipchak,0,1),(trp_khergit_r_quaqli,1,2),(trp_khergit_r_khevtuul,0,1)]),
	("kingdom_3_reinforcements_d_r"	,"{!}kingdom_3_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_page,0,1),(trp_khergit_r_abaci,1,2),(trp_khergit_r_aqala_asud,1,2),(trp_khergit_r_teriguci,0,1),(trp_khergit_r_aqala_teriguci,0,1),(trp_khergit_r_borjigin,0,1)]),
	("kingdom_3_reinforcements_e_r"	,"{!}kingdom_3_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_woman_r_truus_te_paard,0,1),(trp_khergit_r_asud,1,2),(trp_khergit_r_aqala_asud,1,2),(trp_khergit_r_aqala_asud,1,0),(trp_khergit_r_khevtuul,0,1),(trp_khergit_r_aqala_teriguci,0,1)]),
	("kingdom_3_reinforcements_f_r"	,"{!}kingdom_3_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_khergit_r_khevtuul,1,3),(trp_khergit_r_borjigin,1,3),(trp_khergit_r_khevtuul,1,2),(trp_khergit_r_borjigin,0,2),(trp_khergit_r_keshig,0,1),(trp_khergit_r_borjigin,0,1)]),
#Nord
	("kingdom_4_reinforcements_a_r"	,"{!}kingdom_4_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_farmer,0,5),(trp_nord_r_bondi,2,5),(trp_nord_r_berserkr,3,7),(trp_nord_r_huskarl,3,7),(trp_nord_r_kertilsveinr,1,2),(trp_nord_r_gesith,1,2)]),
	("kingdom_4_reinforcements_b_r"	,"{!}kingdom_4_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_townsman,0,5),(trp_nord_r_bondi,2,5),(trp_nord_r_berserkr,3,7),(trp_nord_r_huskarl,3,7),(trp_nord_r_gesith,1,2),(trp_nord_r_gridman,1,2)]),
	("kingdom_4_reinforcements_c_r"	,"{!}kingdom_4_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_halberdier,0,1),(trp_nord_r_gesith,1,2),(trp_nord_r_vikingr,1,2),(trp_nord_r_vikingr,0,1),(trp_nord_r_vigamadr,0,1),(trp_nord_r_heahgerefa,0,1)]),
	("kingdom_4_reinforcements_d_r"	,"{!}kingdom_4_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_woman_r_huntress,0,1),(trp_nord_r_gesith,1,2),(trp_nord_r_bogsveigir,1,2),(trp_nord_r_innaesmaen,0,1),(trp_nord_r_kappi,0,1),(trp_nord_r_skjadsveinn,0,1)]),
	("kingdom_4_reinforcements_e_r"	,"{!}kingdom_4_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_reichslandser,0,1),(trp_nord_r_gesith,1,2),(trp_nord_r_hermadur,1,2),(trp_nord_r_innaesmaen,0,1),(trp_nord_r_heahgerefa,0,1),(trp_nord_r_kappi,0,1)]),
	("kingdom_4_reinforcements_f_r"	,"{!}kingdom_4_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_nord_r_skjadsveinn,1,3),(trp_nord_r_skjadsveinn,1,3),(trp_nord_r_skjadsveinn,1,2),(trp_nord_r_husbondi,0,2),(trp_nord_r_skjadsveinn,0,1),(trp_nord_r_husbondi,0,1)]),
#Rhodok
	("kingdom_5_reinforcements_a_r"	,"{!}kingdom_5_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_farmer,0,5),(trp_rhodok_r_cittadino,4,9),(trp_rhodok_r_novizio,2,5),(trp_rhodok_r_recluta,2,5),(trp_rhodok_r_lanciere_a_cavallo,1,2),(trp_rhodok_r_recluta_balestriere,1,2)]),
	("kingdom_5_reinforcements_b_r"	,"{!}kingdom_5_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_townsman,0,5),(trp_rhodok_r_cittadino,4,9),(trp_rhodok_r_novizio,2,5),(trp_rhodok_r_recluta,2,5),(trp_rhodok_r_recluta_balestriere,1,2),(trp_rhodok_r_lanciere,1,2)]),
	("kingdom_5_reinforcements_c_r"	,"{!}kingdom_5_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_armbrust_miliz,0,1),(trp_rhodok_r_lanciere,1,2),(trp_rhodok_r_balestriere,1,2),(trp_rhodok_r_lanciere_veterano,0,1),(trp_rhodok_r_lanza_spezzata,0,1),(trp_rhodok_r_picchiere_veterano,0,1)]),
	("kingdom_5_reinforcements_d_r"	,"{!}kingdom_5_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_halberdier,0,1),(trp_rhodok_r_recluta_balestriere,1,2),(trp_rhodok_r_lanza_spezzata,1,2),(trp_rhodok_r_fante,0,1),(trp_rhodok_r_balestriere,0,1),(trp_rhodok_r_picchiere_veterano,0,1)]),
	("kingdom_5_reinforcements_e_r"	,"{!}kingdom_5_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_woman_r_kriegerin,0,1),(trp_rhodok_r_fante,1,2),(trp_rhodok_r_balestriere_leggero,1,2),(trp_rhodok_r_lanciere_veterano,0,1),(trp_rhodok_r_lanza_spezzata,0,1),(trp_rhodok_r_picchiere_veterano,0,1)]),
	("kingdom_5_reinforcements_f_r"	,"{!}kingdom_5_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_rhodok_r_picchiere_veterano,1,3),(trp_rhodok_r_balestriere_d_assedio,1,3),(trp_rhodok_r_picchiere_veterano,1,2),(trp_rhodok_r_capitano_d_assedio,0,2),(trp_rhodok_r_picchiere_veterano,0,1),(trp_rhodok_r_capitano_d_assedio,0,1)]), 
#Sarranid
	("kingdom_6_reinforcements_a_r"	,"{!}kingdom_6_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_farmer,0,5),(trp_sarranid_r_millet,5,13),(trp_sarranid_r_ajam,1,3),(trp_sarranid_r_oglan,1,3),(trp_sarranid_r_azab,0,2),(trp_sarranid_r_jebelus,0,2)]),
	("kingdom_6_reinforcements_b_r"	,"{!}kingdom_6_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_townsman,0,5),(trp_sarranid_r_millet,5,13),(trp_sarranid_r_ajam,1,3),(trp_sarranid_r_oglan,1,3),(trp_sarranid_r_cemaat,0,2),(trp_sarranid_r_jebelus,0,2)]),
	("kingdom_6_reinforcements_c_r"	,"{!}kingdom_6_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_r_stedinger,0,1),(trp_sarranid_r_azab,1,2),(trp_sarranid_r_jebelus,1,2),(trp_sarranid_r_badw,0,1),(trp_sarranid_r_garip,0,1),(trp_sarranid_r_yerliyya,0,1)]),
	("kingdom_6_reinforcements_d_r"	,"{!}kingdom_6_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_halberdier,0,1),(trp_sarranid_r_cemaat,1,2),(trp_sarranid_r_al_haqa,1,2),(trp_sarranid_r_kapikulu_savari,0,1),(trp_sarranid_r_kapikula,0,1),(trp_sarranid_r_yerliyya,0,1)]),
	("kingdom_6_reinforcements_e_r"	,"{!}kingdom_6_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_ritter,0,1),(trp_sarranid_r_jebelus,1,2),(trp_sarranid_r_kapikulu_savari,1,2),(trp_sarranid_r_garip,0,1),(trp_sarranid_r_yerliyya,0,1),(trp_sarranid_r_uluteci,0,1)]),
	("kingdom_6_reinforcements_f_r"	,"{!}kingdom_6_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_sarranid_r_kapikula,1,3),(trp_sarranid_r_uluteci,1,3),(trp_sarranid_r_yeniceri,1,2),(trp_sarranid_r_uluteci,0,2),(trp_sarranid_r_yeniceri,0,1),(trp_sarranid_r_uluteci,0,1)]),
#Player Faction: Custom troops
	("kingdom_7_reinforcements_a_r"	,"{!}kingdom_7_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_farmer,0,5),(trp_custom_r_recruit,5,13),(trp_custom_r_militia,1,3),(trp_custom_r_hunter,1,3),(trp_custom_r_guard,0,2),(trp_custom_r_page,0,2)]),
	("kingdom_7_reinforcements_b_r"	,"{!}kingdom_7_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_townsman,0,2),(trp_custom_r_recruit,5,9),(trp_custom_r_militia,1,3),(trp_custom_r_hunter,1,3),(trp_custom_r_page,0,2),(trp_custom_r_woodsman,0,2)]),
	("kingdom_7_reinforcements_c_r"	,"{!}kingdom_7_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_r_huntress,0,1),(trp_custom_r_guard,1,2),(trp_custom_r_swordman,1,2),(trp_custom_r_archer,0,1),(trp_custom_r_knight,0,1),(trp_custom_r_frontline_skirmisher,0,1)]),
	("kingdom_7_reinforcements_d_r"	,"{!}kingdom_7_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_burger,0,1),(trp_custom_r_page,1,2),(trp_custom_r_spearman,1,2),(trp_custom_r_skirmisher,0,1),(trp_custom_r_swordmaster,0,1),(trp_custom_r_expert_archer,0,1)]),
	("kingdom_7_reinforcements_e_r"	,"{!}kingdom_7_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_r_reichslandser,0,1),(trp_custom_r_woodsman,1,2),(trp_custom_r_squire,1,2),(trp_mercenary_r_armbrust_soldner,0,1),(trp_custom_r_swordmaster,0,1),(trp_custom_r_expert_archer,0,1)]),
	("kingdom_7_reinforcements_f_r"	,"{!}kingdom_7_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_custom_r_knight,1,3),(trp_custom_r_expert_archer,1,3),(trp_mercenary_r_doppelsoldner,1,2),(trp_mercenary_r_burgmann,0,2),(trp_woman_r_swob_ridder,0,1),(trp_woman_r_amazon,0,1)]),
##Expanded
#Swadia
	("kingdom_1_reinforcements_a_e"	,"{!}kingdom_1_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_farmer,0,5),(trp_swadian_e_peasant,5,13),(trp_swadian_e_militia,1,3),(trp_swadian_e_peasant_archer,1,3),(trp_swadian_e_page,0,2),(trp_swadian_e_sergeant_at_arms,0,2)]),
	("kingdom_1_reinforcements_b_e"	,"{!}kingdom_1_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_townsman,0,5),(trp_swadian_e_peasant,5,13),(trp_swadian_e_militia,1,3),(trp_swadian_e_peasant_archer,1,3),(trp_swadian_e_vougier,0,2),(trp_swadian_e_archer_militia,0,2)]),
	("kingdom_1_reinforcements_c_e"	,"{!}kingdom_1_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_e_huntress,0,1),(trp_swadian_e_vougier,1,2),(trp_swadian_e_page,1,2),(trp_swadian_e_piquier,0,1),(trp_swadian_e_ecuyer,0,1),(trp_swadian_e_hobilar,0,1)]),
	("kingdom_1_reinforcements_d_e"	,"{!}kingdom_1_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_brabanzon,0,1),(trp_swadian_e_archer_militia,1,2),(trp_swadian_e_longbowman,1,2),(trp_swadian_e_tracker,0,1),(trp_swadian_e_sheriff,0,1),(trp_swadian_e_skirmisher,0,1)]),
	("kingdom_1_reinforcements_e_e"	,"{!}kingdom_1_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_reichslandser,0,1),(trp_swadian_e_sergeant_at_arms,1,2),(trp_swadian_e_jacobite,1,2),(trp_swadian_e_guard,0,1),(trp_swadian_e_jock,0,1),(trp_swadian_e_man_at_arms,0,1)]),
	("kingdom_1_reinforcements_f_e"	,"{!}kingdom_1_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_swadian_e_chevalier,1,3),(trp_swadian_e_selfbow_archer,1,3),(trp_swadian_e_chevalier_banneret,1,2),(trp_swadian_e_yeoman_archer,0,2),(trp_swadian_e_baron_mineures,0,1),(trp_swadian_e_retinue_longbowman,0,1)]),
#Vaegir
	("kingdom_2_reinforcements_a_e"	,"{!}kingdom_2_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_farmer,0,5),(trp_vaegir_e_kholop,5,13),(trp_vaegir_e_otrok,1,3),(trp_vaegir_e_pasynok,1,3),(trp_vaegir_e_kazak,0,2),(trp_vaegir_e_kmet,0,2)]),
	("kingdom_2_reinforcements_b_e"	,"{!}kingdom_2_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_townsman,0,5),(trp_vaegir_e_kholop,5,13),(trp_vaegir_e_otrok,1,3),(trp_vaegir_e_pasynok,1,3),(trp_vaegir_e_grid,0,2),(trp_vaegir_e_kmet,0,2)]),
	("kingdom_2_reinforcements_c_e"	,"{!}kingdom_2_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_volksheer,0,1),(trp_vaegir_e_kmet,1,2),(trp_vaegir_e_grid,1,2),(trp_vaegir_e_zalstrelshik,0,1),(trp_vaegir_e_poztoma_druzhinaik,0,1),(trp_vaegir_e_druzhinnik_veteran,0,1)]),
	("kingdom_2_reinforcements_d_e"	,"{!}kingdom_2_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_woman_e_stedinger,0,1),(trp_vaegir_e_kazak,1,2),(trp_vaegir_e_yesaul,1,2),(trp_vaegir_e_plastun,0,1),(trp_vaegir_e_ataman,0,1),(trp_vaegir_e_golova,0,1)]),
	("kingdom_2_reinforcements_e_e"	,"{!}kingdom_2_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_woman_e_beritten_jungfrau,0,1),(trp_vaegir_e_grid,1,2),(trp_vaegir_e_ratnik,1,2),(trp_vaegir_e_mladshiy_druzhinnik,0,1),(trp_vaegir_e_posadnik,0,1),(trp_vaegir_e_druzhinnik,0,1)]),
	("kingdom_2_reinforcements_f_e"	,"{!}kingdom_2_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_vaegir_e_pansirniy_kazan,1,3),(trp_vaegir_e_luchnik,1,3),(trp_vaegir_e_vityas,1,2),(trp_vaegir_e_metkiy_luchnik,0,2),(trp_vaegir_e_bogatyr,0,1),(trp_vaegir_e_sokoliniy_glaz,0,1)]),
#Khergit
	("kingdom_3_reinforcements_a_e"	,"{!}kingdom_3_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_farmer,0,5),(trp_khergit_e_tariachin,3,9),(trp_khergit_e_tsereg,1,3),(trp_khergit_e_qarbughaci,1,3),(trp_khergit_e_morici,1,4),(trp_khergit_e_surcin,1,4)]),
	("kingdom_3_reinforcements_b_e"	,"{!}kingdom_3_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_townsman,0,5),(trp_khergit_e_tariachin,3,9),(trp_khergit_e_tsereg,1,3),(trp_khergit_e_qarbughaci,1,3),(trp_khergit_e_asud,1,4),(trp_khergit_e_abaci,1,4)]),
	("kingdom_3_reinforcements_c_e"	,"{!}kingdom_3_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_e_mounted_markswoman,0,1),(trp_khergit_e_morici,1,2),(trp_khergit_e_asud,1,2),(trp_khergit_e_yabagharu_morici,0,1),(trp_khergit_e_quaqli,1,2),(trp_khergit_e_torguu,0,1)]),
	("kingdom_3_reinforcements_d_e"	,"{!}kingdom_3_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_page,0,1),(trp_khergit_e_abaci,1,2),(trp_khergit_e_aqala_surcin,1,2),(trp_khergit_e_teriguci,0,1),(trp_khergit_e_aqala_teriguci,0,1),(trp_khergit_e_numyn_ad,0,1)]),
	("kingdom_3_reinforcements_e_e"	,"{!}kingdom_3_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_woman_e_truus_te_paard,0,1),(trp_khergit_e_surcin,1,2),(trp_khergit_e_aqala_asud,1,2),(trp_khergit_e_aqala_surcin,1,0),(trp_khergit_e_khevtuul,0,1),(trp_khergit_e_aqala_teriguci,0,1)]),
	("kingdom_3_reinforcements_f_e"	,"{!}kingdom_3_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_khergit_e_torguu,1,3),(trp_khergit_e_borjigin,1,3),(trp_khergit_e_khorchen,1,2),(trp_khergit_e_aqata_borjigin,0,2),(trp_khergit_e_cherbi,0,1),(trp_khergit_e_mandugai,0,1)]),
#Nord
	("kingdom_4_reinforcements_a_e"	,"{!}kingdom_4_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_farmer,0,5),(trp_nord_e_bondi,2,5),(trp_nord_e_berserkr,3,7),(trp_nord_e_huskarl,3,7),(trp_nord_e_kertilsveinr,1,2),(trp_nord_e_gesith,1,2)]),
	("kingdom_4_reinforcements_b_e"	,"{!}kingdom_4_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_townsman,0,5),(trp_nord_e_bondi,2,5),(trp_nord_e_berserkr,3,7),(trp_nord_e_huskarl,3,7),(trp_nord_e_bogmadur,1,2),(trp_nord_e_gridman,1,2)]),
	("kingdom_4_reinforcements_c_e"	,"{!}kingdom_4_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_volksheer,0,1),(trp_nord_e_bogmadur,1,2),(trp_nord_e_ascoman,1,2),(trp_nord_e_vikingr,0,1),(trp_nord_e_einhleyping,0,1),(trp_nord_e_lausaman,0,1)]),
	("kingdom_4_reinforcements_d_e"	,"{!}kingdom_4_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_woman_e_huntress,0,1),(trp_nord_e_bogmadur,1,2),(trp_nord_e_bogsveigir,1,2),(trp_nord_e_innaesmaen,0,1),(trp_nord_e_kappi,0,1),(trp_nord_e_heimthegi,0,1)]),
	("kingdom_4_reinforcements_e_e"	,"{!}kingdom_4_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_reichslandser,0,1),(trp_nord_e_gesith,1,2),(trp_nord_e_hermadur,1,2),(trp_nord_e_innaesmaen,0,1),(trp_nord_e_heahgerefa,0,1),(trp_nord_e_himthige,0,1)]),
	("kingdom_4_reinforcements_f_e"	,"{!}kingdom_4_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_nord_e_hirdman,1,3),(trp_nord_e_skjadsveinn,1,3),(trp_nord_e_skutilsveinr,1,2),(trp_nord_e_husbondi,0,2),(trp_nord_e_aetheling,0,1),(trp_nord_e_vaeringi,0,1)]),
#Rhodok
	("kingdom_5_reinforcements_a_e"	,"{!}kingdom_5_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_farmer,0,5),(trp_rhodok_e_cittadino,4,9),(trp_rhodok_e_novizio,2,5),(trp_rhodok_e_recluta,2,5),(trp_rhodok_e_milizia,1,2),(trp_rhodok_e_milizia_balestriere,1,2)]),
	("kingdom_5_reinforcements_b_e"	,"{!}kingdom_5_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_townsman,0,5),(trp_rhodok_e_cittadino,4,9),(trp_rhodok_e_novizio,2,5),(trp_rhodok_e_recluta,2,5),(trp_rhodok_e_recluta_balestriere,1,2),(trp_rhodok_e_lanciere,1,2)]),
	("kingdom_5_reinforcements_c_e"	,"{!}kingdom_5_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_armbrust_soldner,0,1),(trp_rhodok_e_lanciere,1,2),(trp_rhodok_e_balestriere,1,2),(trp_rhodok_e_lanciere_veterano,0,1),(trp_rhodok_e_lanciere_a_cavallo,0,1),(trp_rhodok_e_guardia,0,1)]),
	("kingdom_5_reinforcements_d_e"	,"{!}kingdom_5_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_halberdier,0,1),(trp_rhodok_e_milizia_balestriere,1,2),(trp_rhodok_e_lanza_spezzata,1,2),(trp_rhodok_e_fante,0,1),(trp_rhodok_e_balestriere,0,1),(trp_rhodok_e_provisionato,0,1)]),
	("kingdom_5_reinforcements_e_e"	,"{!}kingdom_5_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_woman_e_kriegerin,0,1),(trp_rhodok_e_fante,1,2),(trp_rhodok_e_balestriere_leggero,1,2),(trp_rhodok_e_lanciere_veterano,0,1),(trp_rhodok_e_lanciere_a_cavallo,0,1),(trp_rhodok_e_picchiere_veterano,0,1)]),
	("kingdom_5_reinforcements_f_e"	,"{!}kingdom_5_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_rhodok_e_veterano,1,3),(trp_rhodok_e_balestriere_d_assedio,1,3),(trp_rhodok_e_capitano_di_ventura,1,2),(trp_rhodok_e_capitano_d_assedio,0,2),(trp_rhodok_e_condottiero,0,1),(trp_rhodok_e_condottiero_d_assedio,0,1)]), 
#Sarranid
	("kingdom_6_reinforcements_a_e"	,"{!}kingdom_6_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_farmer,0,5),(trp_sarranid_e_millet,5,13),(trp_sarranid_e_ajam,1,3),(trp_sarranid_e_oglan,1,3),(trp_sarranid_e_azab,0,2),(trp_sarranid_e_jebelus,0,2)]),
	("kingdom_6_reinforcements_b_e"	,"{!}kingdom_6_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_townsman,0,5),(trp_sarranid_e_millet,5,13),(trp_sarranid_e_ajam,1,3),(trp_sarranid_e_oglan,1,3),(trp_sarranid_e_cemaat,0,2),(trp_sarranid_e_ghulam,0,2)]),
	("kingdom_6_reinforcements_c_e"	,"{!}kingdom_6_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_e_hospitaller,0,1),(trp_sarranid_e_azab,1,2),(trp_sarranid_e_ghulam,1,2),(trp_sarranid_e_serdengecti,0,1),(trp_sarranid_e_tabardariyya,0,1),(trp_sarranid_e_terkes_serdengecti,0,1)]),
	("kingdom_6_reinforcements_d_e"	,"{!}kingdom_6_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_halberdier,0,1),(trp_sarranid_e_cemaat,1,2),(trp_sarranid_e_al_haqa,1,2),(trp_sarranid_e_yerliyya,0,1),(trp_sarranid_e_yeniceri,0,1),(trp_sarranid_e_beylik,0,1)]),
	("kingdom_6_reinforcements_e_e"	,"{!}kingdom_6_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_ritter,0,1),(trp_sarranid_e_jebelus,1,2),(trp_sarranid_e_kapikulu_savari,1,2),(trp_sarranid_e_garip,0,1),(trp_sarranid_e_beylik,0,1),(trp_sarranid_e_uluteci,0,1)]),
	("kingdom_6_reinforcements_f_e"	,"{!}kingdom_6_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_sarranid_e_kapikula,1,3),(trp_sarranid_e_akinci,1,3),(trp_sarranid_e_memluk,1,2),(trp_sarranid_e_sipahi,0,2),(trp_sarranid_e_hasham,0,1),(trp_sarranid_e_iqta_dar,0,1)]),
#Player Faction: Custom troops
	("kingdom_7_reinforcements_a_e"	,"{!}kingdom_7_reinforcements_a"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_farmer,0,5),(trp_custom_e_recruit,5,13),(trp_custom_e_militia,1,3),(trp_custom_e_hunter,1,3),(trp_custom_e_guard,0,2),(trp_custom_e_page,0,2)]),
	("kingdom_7_reinforcements_b_e"	,"{!}kingdom_7_reinforcements_b"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_townsman,0,2),(trp_custom_e_recruit,5,9),(trp_custom_e_militia,1,3),(trp_custom_e_hunter,1,3),(trp_custom_e_page,0,2),(trp_custom_e_woodsman,0,2)]),
	("kingdom_7_reinforcements_c_e"	,"{!}kingdom_7_reinforcements_c"		,0																									,0		,fac_commoners		,0								,[(trp_woman_e_huntress,0,1),(trp_custom_e_guard,1,2),(trp_custom_e_swordman,1,2),(trp_custom_e_archer,0,1),(trp_custom_e_knight,0,1),(trp_custom_e_frontline_skirmisher,0,1)]),
	("kingdom_7_reinforcements_d_e"	,"{!}kingdom_7_reinforcements_d"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_brabanzon,0,1),(trp_custom_e_page,1,2),(trp_custom_e_spearman,1,2),(trp_custom_e_skirmisher,0,1),(trp_custom_e_swordmaster,0,1),(trp_custom_e_horse_archer,0,1)]),
	("kingdom_7_reinforcements_e_e"	,"{!}kingdom_7_reinforcements_e"		,0																									,0		,fac_commoners		,0								,[(trp_mercenary_e_reichslandser,0,1),(trp_custom_e_woodsman,1,2),(trp_custom_e_squire,1,2),(trp_mercenary_e_armbrust_komtur,0,1),(trp_custom_e_spearmaster,0,1),(trp_custom_e_expert_archer,0,1)]),
	("kingdom_7_reinforcements_f_e"	,"{!}kingdom_7_reinforcements_f"		,0																									,0		,fac_commoners		,0								,[(trp_custom_e_heavy_knight,1,3),(trp_custom_e_heavy_horse_archer,1,3),(trp_mercenary_e_grosskomtur,1,2),(trp_mercenary_e_landsknecht,0,2),(trp_woman_e_kenau,0,1),(trp_woman_e_walkure,0,1)]),


# Bandit Lairs
	#Native
	("steppe_bandit_lair"			,"Steppe Bandit Lair"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_n_steppe,15,116)]),
	("taiga_bandit_lair"			,"Tundra Bandit Lair"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_n_taiga,15,116)]),
	("desert_bandit_lair"			,"Desert Bandit Lair"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_n_desert,15,116)]),
	("forest_bandit_lair"			,"Forest Bandit Camp"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_n_forest,15,116)]),
	("mountain_bandit_lair"			,"Mountain Bandit Hideout"				,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_n_mountain,15,116)]),
	("sea_raider_lair"				,"Sea Raider Landing"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_n_sea_raider,15,100)]),
	("looter_lair"					,"Kidnappers' Hideout"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_n_looter,15,50)]),
	("bandit_lair_templates_end"	,"{!}bandit_lair_templates_end"			,icon_people_axeman|carries_goods(2)|pf_is_static													,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_n_sea_raider,15,100)]),
	("leaded_looters"				,"Band of robbers"						,icon_people_axeman|carries_goods(8)|pf_quest_party													,0		,fac_neutral		,bandit_personality				,[(trp_looter_leader,1,1),(trp_bandit_n_looter,3,6)]),
	#Reworked
	("steppe_bandit_lair_r"			,"Steppe Bandit Lair"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_r_steppe,15,116)]),
	("taiga_bandit_lair_r"			,"Tundra Bandit Lair"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_r_taiga,15,116)]),
	("desert_bandit_lair_r"			,"Desert Bandit Lair"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_r_desert,15,116)]),
	("forest_bandit_lair_r"			,"Forest Bandit Camp"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_r_forest,15,116)]),
	("mountain_bandit_lair_r"		,"Mountain Bandit Hideout"				,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_r_mountain,15,116)]),
	("sea_raider_lair_r"			,"Sea Raider Landing"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_r_sea_raider,15,100)]),
	("looter_lair_r"				,"Kidnappers' Hideout"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_r_looter,15,50)]),
	("bandit_lair_templates_end_r"	,"{!}bandit_lair_templates_end"			,icon_people_axeman|carries_goods(2)|pf_is_static													,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_r_sea_raider,15,100)]),
	("leaded_looters_r"				,"Band of robbers"						,icon_people_axeman|carries_goods(8)|pf_quest_party													,0		,fac_neutral		,bandit_personality				,[(trp_looter_leader,1,1),(trp_bandit_r_looter,3,6)]),
	#Expanded
	("steppe_bandit_lair_e"			,"Steppe Bandit Lair"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_e_steppe,15,116)]),
	("taiga_bandit_lair_e"			,"Tundra Bandit Lair"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_e_taiga,15,116)]),
	("desert_bandit_lair_e"			,"Desert Bandit Lair"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_e_desert,15,116)]),
	("forest_bandit_lair_e"			,"Forest Bandit Camp"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_e_forest,15,116)]),
	("mountain_bandit_lair_e"		,"Mountain Bandit Hideout"				,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_e_mountain,15,116)]),
	("sea_raider_lair_e"			,"Sea Raider Landing"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_e_sea_raider,15,100)]),
	("looter_lair_e"				,"Kidnappers' Hideout"					,icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders									,0		,fac_neutral		,bandit_personality				,[(trp_bandit_e_looter,15,50)]),
	("bandit_lair_templates_end_e"	,"{!}bandit_lair_templates_end"			,icon_people_axeman|carries_goods(2)|pf_is_static													,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_e_sea_raider,15,100)]),
	("leaded_looters_e"				,"Band of robbers"						,icon_people_axeman|carries_goods(8)|pf_quest_party													,0		,fac_neutral		,bandit_personality				,[(trp_looter_leader,1,1),(trp_bandit_e_looter,3,6)]),

   ##diplomacy begin
	("dplmc_spouse"					,"Your spouse"							,icon_people_woman|pf_civilian|pf_show_faction														,0		,fac_neutral		,merchant_personality			,[]),
	#Native
	("dplmc_gift_caravan"			,"Your Caravan"							,icon_people_mule|carries_goods(25)|pf_show_faction													,0		,fac_commoners		,escorted_merchant_personality	,[(trp_caravan_master,1,1),(trp_mercenary_n_page,4,32),(trp_mercenary_n_ritter,1,10),(trp_mercenary_n_komtur_ritter,0,4),(trp_mercenary_n_komtur,0,4)]),
	#Reworked
	("dplmc_gift_caravan_r"			,"Your Caravan"							,icon_people_mule|carries_goods(25)|pf_show_faction													,0		,fac_commoners		,escorted_merchant_personality	,[(trp_caravan_master,1,1),(trp_mercenary_r_page,4,32),(trp_mercenary_r_ritter,1,10),(trp_mercenary_r_komtur_ritter,0,4),(trp_mercenary_r_doppelsoldner,0,4)]),
	#Expanded
	("dplmc_gift_caravan_e"			,"Your Caravan"							,icon_people_mule|carries_goods(25)|pf_show_faction													,0		,fac_commoners		,escorted_merchant_personality	,[(trp_caravan_master,1,1),(trp_mercenary_e_page,4,32),(trp_mercenary_e_ritter,1,10),(trp_mercenary_e_komtur_ritter,0,4),(trp_mercenary_e_kreuzritter,0,4)]),
#recruiter kit begin
	("dplmc_recruiter"				,"Recruiter"							,icon_people_gray_knight|pf_show_faction															,0		,fac_neutral		,merchant_personality			,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
   ##diplomacy end

#TEMPERED  ENTRENCHMENT PARTY
	("entrench"						,"Entrenchment"							,icon_camp_entrench_last|pf_is_static|pf_always_visible|pf_no_label									,0		,fac_neutral		,bandit_personality				,[]),   

## Zaitenko's Reinforcement Script
	("reinforcements"				,"Reinforcements"						,icon_people_axeman|pf_show_faction																	,0		,fac_commoners		,soldier_personality			,[]),
##
#wulf
	#Native
	("sea_raiders_ships"			,"Sea Raiders"							,icon_ship|pf_is_ship|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_n_sea_raider,50,100)]),
	#Reworked
	("sea_raiders_ships_r"			,"Sea Raiders"							,icon_ship|pf_is_ship|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_r_sea_raider,50,100)]),
	#Expanded
	("sea_raiders_ships_e"			,"Sea Raiders"							,icon_ship|pf_is_ship|carries_goods(2)																,0		,fac_outlaws		,bandit_personality				,[(trp_bandit_e_sea_raider,50,100)]),
#wulf end
##Floris MTT end
]
