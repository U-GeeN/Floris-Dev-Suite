#####Floris Notes#####
# I've used items from the following sources:
# - 15th century weapons v1.1 by Shredzorz
# - 19 Warhorses v1.0 by Lor Dric, with some items by Saregona
# - Battlefield Priests for Calradia v1.0, by Yamabusi
# - Brytenwalda v3.3.2, by the Brytenwalda Team
# - Coloured Lances Project v1.0 by CounterPoint391
# - Crusader Heraldry OSP v0.1 by CounterPoint391
# - Eastern Armor OSP v1.0 by Njunja
# - Frell's Khazak Armor Pack v1.0 by Frell
# - Half Cataphracts v2.0 by wanderer949
# - Highlander Model Pack v1.0 by Yamabusi
# - Long Caparisoned Horses v2.0 by wanderer949
# - More Horses v5.0 by wanderer949
# - More Warhorses v2.0 by wanderer949
# - Narf's items, from Magus Mod v1.7 by Oddball_E8
# - Narf's Rus Armour Pack v1.2 by Narf
# - Narf's Transitional Armour Pack v1.3 by narf
# - Native Warband v1.143 by TaleWorlds
# - Norman Helmets Pack v1.1 by Sayd Uthman
# - Oakeshott Sword Pack v0.2 by CounterPoint391
# - OSP Dungeon-Labyrinth-parts and Magnus-Hammer v1.0
# - OSP Helmets v0.2 by Dindi, items by Luigi, Njiekovic[, Ursca, Ubberdorc, Mirathei, Raz., The Pope, TRC and Dindi
# - OSP Indo-Persian Armor Pack v1.2 by drakharios
# - OSP Indo-Persian Armor II v1.0 by drakharios
# - OSP Indo-Persian Shields v1.0 by drakharios
# - OSP Item Variants v1.6 by thick1988
# - OSP Spak Items v2.0 by Spak
# - OSP Weapons v1.0 by Bismarck, items by The Pope, Luigi, James and RR_Raptor65
# - Reworked Armors OSP v1.6, by Kovas
# - Silver Wolf Resource Pack v6.0 by Silverwolf
# - Smiley Stuff OSP v1.0 by SendMeSmile
# - The Wild Wind v0.14 by Shredzorz
# - The Chocolat Box v1.01, compilated by beezarandy, items by Faradon, Narf, Raptor65, talak, Dejawolf and Maw
# - Viking Model Pack v2010 by Dejawolf
# - Warband Horses v4.0 by Lor Dric
#
# The total number of items:
# Minimal + Expanded = Total
# Tutorial:					 15 +    0 =   15
# Horse Meat:				  1 +    0 =    1
# Practice and arena items:	 56 +    0 =   56
# Books:					 16 +    0 =   16
# Quest Items:				  3 +    0 =    3
# Animals:					 15 +    0 =   15
# Horses
#	Normal:					 13 +   82 =   95
#	War:					 16 +   90 =  106
# Weapons
#	Axes	
#		One-handed:			 18 +    7 =   25
#		Two-handed:			 19 +    2 =   21
#	Blunt
#		One-handed:			 19 +   14 =   33
#		Two-handed:			  9 +    6 =   15
#	Polearms
#		Two-handed:			 36 +   47 =   83
#		Lances:				 12 +   19 =   32
#	Swords
#		One-handed:			 42 +   40 =   82
#		Two-handed:			 19 +   20 =   39
#	Ranged
#		Ammunition:			 16 +    5 =   21
#		Bows & Crossbows:	 19 +   20 =   39
#		Throwing Weapons:	 18 +    8 =   26
# Armors
#	Armor:					 80 +  244 =  324
#	Cloths:					 39 +   60 =   99
#	Dresses:				 27 +   18 =   45
#	Footwear:				 59 +    0 =   59
#	Handgear:				 29 +    7 =   36
#	Headgear (civilian):	 37 +   36 =   73
#	Headgear (war):			 53 +  203 =  256
#	Shields:				 66 +   62 =  128
#							__________________+
# Total items				752 +  990 = 1742
#
######################

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none				= 0
imodbits_horse_basic		= imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn|imodbit_timid ## CC
imodbits_cloth				= imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor				= imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate				= imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm			= imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield				= imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword				= imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high			= imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe				= imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace				= imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick				= imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow				= imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow			= imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile			= imodbit_bent | imodbit_large_bag
imodbits_thrown				= imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy	= imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good			= imodbit_spirited|imodbit_heavy
imodbits_good				= imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad				= imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

## CC
missile_distance_trigger	= [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter_agent"),
      
      (eq, "$g_report_shot_distance", 1),
      (get_player_agent_no, ":player_agent"),
      (try_begin),
        (eq, ":shooter_agent", ":player_agent"),
        (agent_get_position, pos2, ":shooter_agent"),
        (agent_get_horse, ":horse_agent", ":player_agent"),
        (try_begin),
          (gt, ":horse_agent", -1),
          (position_move_z, pos2, 220),
        (else_try),
          (position_move_z, pos2, 150),
        (try_end),
        (get_distance_between_positions, ":distance", pos1, pos2),
        (store_div, reg61, ":distance", 100),
        (store_mod, reg62, ":distance", 100),
        (try_begin),
          (lt, reg62, 10),
          (str_store_string, s1, "@{reg61}.0{reg62}"),
        (else_try),
          (str_store_string, s1, "@{reg61}.{reg62}"),
        (try_end),
        (display_message, "@Shot distance: {s1} meters.", 0xCCCCCC),
      (try_end),
    ])]
## CC

items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

##Tutorial items - 15
#Minimal - 15
["tutorial_spear", "Spear", [("we_swa_spear_boar",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["tutorial_club", "Club", [("tutorial_club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["tutorial_battle_axe", "Battle Axe", [("tutorial_battle_axe",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["tutorial_arrows","Arrows", [("we_pla_arrow",0),("we_pla_arrow_flying",ixmesh_flying_ammo),("we_pla_quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile,missile_distance_trigger],
["tutorial_bolts","Bolts", [("we_rho_bolt",0),("we_rho_bolt_flying",ixmesh_flying_ammo),("we_rho_bolt_bag", ixmesh_carry),("we_rho_bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile,missile_distance_trigger],
["tutorial_short_bow", "Short Bow", [("we_swa_bow_practice",0),("we_swa_bow_practice_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
["tutorial_crossbow", "Crossbow", [("we_rho_crossbow_hunting",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
["tutorial_throwing_daggers", "Throwing Daggers", [("we_vae_sword_throw_daggers",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile,missile_distance_trigger],
["tutorial_saddle_horse", "Saddle Horse", [("ho_swa_saddle_black",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["tutorial_shield", "Kite Shield", [("tutorial_shield",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
["tutorial_staff_no_attack","Staff", [("we_sar_spear_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
["tutorial_staff","Staff", [("we_sar_spear_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
["tutorial_sword", "Sword", [("tutorial_sword",0),("tutorial_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
["tutorial_axe", "Axe", [("tutorial_axe",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#Horse meat? - 1
#Minimal - 1
["horse_meat","Horse Meat", [("trade_cattle_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|abundance(50)|food_quality(30)|max_ammo(40),imodbits_none,[],[fac_kingdom_3]],
# Items before this point are hardwired and their order should not be changed!

##Practice and arena items - 56
#Minimum - 56
#Practice Weapons - 6
["practice_axe", "Practice Axe", [("practice_axe",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
["practice_lance","Practice Lance", [("we_swa_spear_lance_jousting",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(15,blunt),imodbits_none],
["practice_staff","Practice Staff", [("we_sar_spear_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
["practice_sword_heavy","Heavy Practice Sword", [("practice_sword_heavy",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword, 21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
#Practice Ranged Weapons - 11
["practice_arrows","Practice Arrows", [("practice_arrows",0),("we_pla_arrow_flying",ixmesh_flying_ammo),("practice_arrows_quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile,missile_distance_trigger],
["practice_arrows_10_amount","Practice Arrows", [("we_pla_arrow",0),("we_pla_arrow_flying",ixmesh_flying_ammo),("we_pla_quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile,missile_distance_trigger],
["practice_arrows_100_amount","Practice Arrows", [("we_pla_arrow",0),("we_pla_arrow_flying",ixmesh_flying_ammo),("we_pla_quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile,missile_distance_trigger],
["practice_bolts","Practice Bolts", [("we_rho_bolt",0),("we_rho_bolt_flying",ixmesh_flying_ammo),("we_rho_bolt_bag", ixmesh_carry),("we_rho_bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_missile,missile_distance_trigger],
["practice_bolts_9_amount","Practice Bolts", [("we_rho_bolt",0),("we_rho_bolt_flying",ixmesh_flying_ammo),("we_rho_bolt_bag", ixmesh_carry),("we_rho_bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile,missile_distance_trigger],
["practice_bow","Practice Bow", [("we_nor_bow_hunting",0), ("we_nor_bow_hunting_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
["practice_crossbow", "Practice Crossbow", [("we_rho_crossbow_hunting",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,blunt)|max_ammo(1),imodbits_crossbow],
["practice_javelin", "Practice Javelins", [("we_sar_spear_javelin",0),("we_sar_spear_javelin_quiver", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown,missile_distance_trigger],
["practice_javelin_melee", "practice_javelin_melee", [("we_sar_spear_javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
["practice_throwing_daggers", "Throwing Daggers", [("we_vae_sword_throw_daggers",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown,missile_distance_trigger],
["practice_throwing_daggers_100_amount", "Throwing Daggers", [("we_vae_sword_throw_daggers",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown,missile_distance_trigger],
#Practice Defence - 3
["practice_boots", "Practice Boots", [("bo_rho_t3_highlander",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],
["practice_horse","Practice Horse", [("ho_swa_saddle_black",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
["practice_shield","Practice Shield", [("practice_shield",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
#Arena Weapons - 4
["arena_axe", "Axe", [("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
["arena_sword", "Sword", [("arena_sword_one_handed",0),("arena_sword_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 243 , weight(1.5)|spd_rtng(99) | weapon_length(95)|swing_damage(22 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
["arena_sword_two_handed",  "Two Handed Sword", [("arena_sword_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 670 , weight(2.75)|spd_rtng(93) | weapon_length(110)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
["arena_lance","Lance", [("arena_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],
#Arena Shields - 4
["arena_shield_red", "Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_blue", "Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_green", "Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_yellow", "Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
#Arena Armor - 10
["arena_armor_white", "Arena Armor White", [("arena_armor_white",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("arena_armor_red",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_blue", "Arena Armor Blue", [("arena_armor_blue",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_green", "Arena Armor Green", [("arena_armor_green",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_yellow", "Arena Armor Yellow", [("arena_armor_yellow",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_tunic_white", "Arena Tunic White ", [("arena_tunic_white",0)], itp_type_body_armor |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("arena_tunic_red",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_blue", "Arena Tunic Blue", [("arena_tunic_blue",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_green", "Arena Tunic Green", [("arena_tunic_green",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_yellow", "Arena Tunic Yellow", [("arena_tunic_yellow",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
#Arena Helmets - 18
["arena_helmet_red", "Arena Helmet Red", [("arena_helmet_red",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_blue", "Arena Helmet Blue", [("arena_helmet_blue",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_green", "Arena Helmet Green", [("arena_helmet_green",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_yellow", "Arena Helmet Yellow", [("arena_helmet_yellow",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_white", "Steppe Helmet White", [("steppe_helmet_white",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_red", "Steppe Helmet Red", [("steppe_helmet_red",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_blue", "Steppe Helmet Blue", [("steppe_helmet_blue",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_green", "Steppe Helmet Green", [("steppe_helmet_green",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_yellow", "Steppe Helmet Yellow", [("steppe_helmet_yellow",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["tourney_helm_white", "White Tourney Helm", [("tourney_helm_white",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_red", "Red Tourney Helmet", [("tourney_helm_red",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_blue", "Blue Tourney Helmet", [("tourney_helm_blue",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_green", "Green Tourney Helmet", [("tourney_helm_green",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_yellow", "Yellow Tourney Helmet", [("tourney_helm_yellow",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_red", "Red Arena Turban", [("he_sar_t3_rabati_d",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_blue", "Blue Arena Turban", [("he_sar_t3_rabati_e",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_green", "Green Arena Turban", [("he_sar_t3_rabati_f",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_yellow", "Yellow Arena Turban", [("he_sar_t3_rabati_c",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],

##Books - 16
# A treatise on The Method of Mechanical Theorems Archimedes
#This book must be at the beginning of readable books
#Minimal - 13
["book_tactics","De Re Militari", [("bk_book_01",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
["book_persuasion","Rhetorica ad Herennium", [("bk_book_02",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
["book_leadership","The Life of Alixenus the Great", [("bk_book_03",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
["book_intelligence","Essays on Logic", [("bk_book_04",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
["book_trade","A Treatise on the Value of Things", [("bk_book_05",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
["book_weapon_mastery", "On the Art of Fighting with Swords", [("bk_book_06",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
["book_engineering","Method of Mechanical Theorems", [("bk_book_07",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
["book_necronomicon","Necronomicon", [("bk_book_15",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
["book_bible","Holy Bible", [("bk_book_16",0)], itp_type_book, 0, 4500,weight(2)|abundance(100),imodbits_none],
["book_prisoner_management","Ramun's Note", [("bk_book_11",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
#Reference books
["book_spotting_reference","Scientia Servandi", [("bk_book_12",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
["book_first_aid_reference","Primo Auxilium", [("bk_book_13",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
["book_pathfinding_reference","Lore of Calradia", [("bk_book_14",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
#Minimal - 3
["book_wound_treatment_reference","The Book of Healing", [("bk_book_08",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
["book_training_reference","Manual of Arms", [("bk_book_09",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
["book_surgery_reference","The Great Book of Surgery", [("bk_book_10",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
["book_trade_ledger","Merchant's Ledger", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none], ## Floris - caba
##

##other trade goods (first one is spice)
#Minimal - 34
["trade_spice","Spice", [("trade_spice",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbit_fine|imodbit_large_bag|imodbit_exquisite],
["trade_salt","Salt", [("trade_salt",0)], itp_merchandise|itp_type_goods, 0, 255,weight(50)|abundance(120),imodbit_fine|imodbit_large_bag],
["trade_oil","Oil", [("trade_oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 450,weight(50)|abundance(60)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["trade_pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbit_cracked|imodbit_crude|imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_rough|imodbit_sturdy],
["trade_raw_flax","Flax Bundle", [("trade_raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbit_fine|imodbit_exquisite],
["trade_linen","Linen", [("trade_linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_sturdy],
["trade_wool","Wool", [("trade_wool",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbit_fine|imodbit_exquisite],
["trade_wool_cloth","Wool Cloth", [("trade_wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_sturdy],
["trade_raw_silk","Raw Silk", [("trade_raw_silk",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbit_fine|imodbit_exquisite],
["trade_raw_dyes","Dyes", [("trade_raw_dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork],
["trade_velvet","Velvet", [("trade_velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork],
["trade_iron","Iron", [("trade_iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbit_rusty|imodbit_poor|imodbit_well_made|imodbit_tempered|imodbit_hardened],
["trade_tools","Tools", [("trade_tools",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbit_rusty|imodbit_crude|imodbit_old|imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_sturdy|imodbit_hardened],
["trade_raw_leather","Hides", [("trade_raw_leather",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbit_fine|imodbit_exquisite|imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick],
["trade_leatherwork","Leatherwork", [("trade_leatherwork",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_masterwork|imodbit_tattered|imodbit_ragged|imodbit_rough|imodbit_sturdy|imodbit_thick],
["trade_raw_date_fruit","Date Fruit", [("trade_raw_date_fruit",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbit_cheap|imodbit_fine|imodbit_exquisite],
["trade_furs","Furs", [("trade_furs",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbit_cheap|imodbit_fine|imodbit_exquisite|imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick],
["trade_wine","Wine", [("trade_wine",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 220,weight(30)|abundance(60)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_strong],
["trade_ale","Ale", [("trade_ale",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 120,weight(30)|abundance(70)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite|imodbit_strong|imodbit_lordly],
["trade_smoked_fish","Smoked Fish", [("trade_smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["trade_cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["trade_honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(30),imodbit_cheap|imodbit_fine|imodbit_exquisite],
["trade_sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(10)|abundance(110)|food_quality(40)|max_ammo(40),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["trade_cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(15)|abundance(110)|food_quality(40)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_exquisite],
["trade_dried_meat","Dried Meat", [("trade_dried_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["trade_apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(20)|abundance(110)|food_quality(40)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_exquisite],
["trade_raw_grapes","Grapes", [("trade_raw_grapes",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbit_cheap|imodbit_fine|imodbit_exquisite], #x2 for wine
["trade_raw_olives","Olives", [("trade_raw_olives",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbit_cheap|imodbit_fine|imodbit_exquisite], #x3 for oil
["trade_grain","Grain", [("trade_grain",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 30,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_exquisite|imodbit_large_bag],
["trade_cattle_meat","Beef", [("trade_cattle_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(100)|food_quality(80)|max_ammo(50),imodbits_none],
["trade_bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
["trade_chicken","Chicken", [("trade_chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
["trade_pork","Pork", [("trade_pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
["trade_butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbit_cheap|imodbit_fine|imodbit_well_made|imodbit_exquisite],
#Dummy items for Mercantilism Mod by keinplan84m - 20 ##Included for future savegame compatibility or sub-mod-ability; change trade_good constants and re-add itp_merchandise if used
["trade_dummy01","Dummy item 1", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy02","Dummy item 2", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy03","Dummy item 3", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy04","Dummy item 4", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy05","Dummy item 5", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy06","Dummy item 6", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy07","Dummy item 7", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy08","Dummy item 8", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy09","Dummy item 9", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy10","Dummy item 10", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy11","Dummy item 11", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy12","Dummy item 12", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy13","Dummy item 13", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy14","Dummy item 14", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy15","Dummy item 15", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy16","Dummy item 16", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy17","Dummy item 17", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy18","Dummy item 18", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy19","Dummy item 19", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
["trade_dummy20","Dummy item 20", [("trade_spice",0)], itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none], #itp_merchandise|
##

#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

### Quest Items - 3
["siege_supply","Supplies", [("trade_ale",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
["quest_wine","Wine", [("trade_wine",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
["quest_ale","Ale", [("trade_ale",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],
###

### Animals - 15
#Minimal - 15
["an_gen_boar","Wild Boar", [("an_gen_boar",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(15)|difficulty(11)|horse_speed(30)|horse_maneuver(20)|horse_charge(200)|horse_scale(55),imodbits_horse_basic],
["an_gen_chicken","Chicken", [("an_gen_chicken",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(7)|difficulty(11)|horse_speed(7)|horse_maneuver(65)|horse_charge(10)|horse_scale(27),imodbits_horse_basic],
["an_gen_cowblackwhite","Black-White Cow", [("an_gen_cowblackwhite",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(10)|difficulty(11)|horse_speed(25)|horse_maneuver(20)|horse_charge(50)|horse_scale(100),imodbits_horse_basic],
["an_gen_cowbrown","Brown Cow", [("an_gen_cowbrown",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(10)|difficulty(11)|horse_speed(25)|horse_maneuver(20)|horse_charge(50)|horse_scale(100),imodbits_horse_basic],
["an_gen_cowbrownwhite","Brown-White Cow", [("an_gen_cowbrownwhite",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(10)|difficulty(11)|horse_speed(25)|horse_maneuver(20)|horse_charge(50)|horse_scale(100),imodbits_horse_basic],
["an_gen_cowwhite","White Cow", [("an_gen_cowwhite",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(10)|difficulty(11)|horse_speed(25)|horse_maneuver(20)|horse_charge(50)|horse_scale(100),imodbits_horse_basic],
["an_gen_deerfemale","Female Deer", [("an_gen_deerfemale",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(12)|difficulty(11)|horse_speed(45)|horse_maneuver(34)|horse_charge(40)|horse_scale(90),imodbits_horse_basic],
["an_gen_deermale","Male Deer", [("an_gen_deermale",0)], itp_type_horse,0,1411,abundance(40)|hit_points(2000)|body_armor(15)|difficulty(11)|horse_speed(50)|horse_maneuver(32)|horse_charge(200)|horse_scale(100),imodbits_horse_basic],
["an_gen_deeryoung","Young Deer", [("an_gen_deeryoung",0)], itp_type_horse,0,1411,abundance(40)|hit_points(70)|body_armor(5)|difficulty(11)|horse_speed(40)|horse_maneuver(37)|horse_charge(20)|horse_scale(55),imodbits_horse_basic],
["an_gen_donkeywild","Wild Donkey", [("an_gen_donkeywild",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(10)|difficulty(11)|horse_speed(30)|horse_maneuver(20)|horse_charge(50)|horse_scale(65),imodbits_horse_basic],
["an_gen_goatbrown","Brown Goat", [("an_gen_goatbrown",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(8)|difficulty(11)|horse_speed(40)|horse_maneuver(30)|horse_charge(20)|horse_scale(55),imodbits_horse_basic],
["an_gen_goatwhite","White Goat", [("an_gen_goatwhite",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(8)|difficulty(11)|horse_speed(40)|horse_maneuver(30)|horse_charge(20)|horse_scale(55),imodbits_horse_basic],
["an_gen_pig","Pig", [("an_gen_pig",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(15)|difficulty(11)|horse_speed(30)|horse_maneuver(20)|horse_charge(20)|horse_scale(45),imodbits_horse_basic],
["an_gen_sheep","Sheep", [("an_gen_sheep",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(5)|difficulty(11)|horse_speed(26)|horse_maneuver(50)|horse_charge(9)|horse_scale(62),imodbits_horse_basic],
["an_gen_wolf","Wolf", [("an_gen_wolf",0)], itp_type_horse,0,1411,abundance(40)|hit_points(180)|body_armor(10)|difficulty(11)|horse_speed(40)|horse_maneuver(40)|horse_charge(100)|horse_scale(55),imodbits_horse_basic],
###

### Horses - 200

##Normal Horses - 95
#Swadia - 14
#Minimal - 2
["ho_swa_saddle_black","Saddle Horse", [("ho_swa_saddle_black",0)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic, [], [fac_kingdom_1,fac_player_faction]],
["ho_swa_destrier_black","Black Destrier", [("ho_swa_destrier_black",0)], itp_merchandise|itp_type_horse, 0, 811,abundance(100)|hit_points(155)|body_armor(18)|difficulty(3)|horse_speed(42)|horse_maneuver(45)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion,[],[fac_kingdom_1,fac_player_faction]],
#Vaegir - 15
#Minimal - 2
["ho_vae_saddle_feather","Feather Saddle Horse", [("ho_vae_saddle_feather",0)], itp_merchandise|itp_type_horse, 0, 250,abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(45)|horse_charge(11)|horse_scale(104),imodbits_horse_basic, [], [fac_kingdom_2,fac_player_faction]],
["ho_vae_rus_brown","Brown Vaegir Horse",[("ho_vae_rus_brown",0)], itp_merchandise|itp_type_horse,0,594,abundance(100)|hit_points(150)|body_armor(20)|difficulty(2)|horse_speed(40)|horse_maneuver(40)|horse_charge(8)|horse_scale(108),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_2,fac_player_faction]],
#Khergit - 14
#Minimal - 2
["ho_khe_saddle_coloured","Coloured Saddle Horse", [("ho_khe_saddle_coloured",0)], itp_merchandise|itp_type_horse, 0, 230,abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(44)|horse_maneuver(45)|horse_charge(10)|horse_scale(104),imodbits_horse_basic, [], [fac_kingdom_3,fac_player_faction]],
["ho_khe_steppe_brownpainted","Brown Painted Steppe Horse", [("ho_khe_steppe_brownpainted",0)], itp_merchandise|itp_type_horse, 0, 198,abundance(100)|hit_points(120)|body_armor(11)|difficulty(2)|horse_speed(41)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3,fac_player_faction]],
#Nord - 14
#Minimal - 2
["ho_nor_mule","Mule", [("ho_nor_mule",0)], itp_merchandise|itp_type_horse, 0, 260,abundance(70)|hit_points(120)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(98),imodbits_horse_basic|imodbit_champion,[],[fac_kingdom_4,fac_player_faction]],
["ho_nor_courser_greysteel","Steel Grey Courser", [("ho_nor_courser_greysteel",0)], itp_merchandise|itp_type_horse, 0, 589,abundance(100)|hit_points(110)|body_armor(12)|difficulty(2)|horse_speed(50)|horse_maneuver(42)|horse_charge(12)|horse_scale(106),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_4,fac_player_faction]],
#Rhodok - 16
#Minimal - 2
["ho_rho_donkey_brown","Brown Donkey", [("ho_rho_donkey_brown",0)], itp_merchandise|itp_type_horse, 0, 90,abundance(90)|hit_points(100)|body_armor(6)|difficulty(1)|horse_speed(36)|horse_maneuver(39)|horse_charge(9)|horse_scale(90),imodbits_horse_basic|imodbit_champion,[],[fac_kingdom_5,fac_player_faction]],
["ho_rho_rouncy_brown","Brown Rouncey", [("ho_rho_rouncy_brown",0)], itp_merchandise|itp_type_horse, 0, 245,abundance(100)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(46)|horse_maneuver(43)|horse_charge(10)|horse_scale(104),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_5,fac_player_faction]],
#Sarranid - 16
#Minimal - 2
["ho_sar_camel_bactrian","Bactrian Camel", [("ho_sar_camel_bactrian",0)], itp_merchandise|itp_type_horse, 0, 500,abundance(40)|hit_points(140)|body_armor(12)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(8)|horse_scale(106),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6,fac_player_faction]],
["ho_sar_arab_dun","Dun Desert Horse", [("ho_sar_arab_dun",0)], itp_merchandise|itp_type_horse, 0, 689,abundance(100)|hit_points(120)|body_armor(9)|difficulty(3)|horse_speed(45)|horse_maneuver(54)|horse_charge(16)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6,fac_player_faction]],
#Player Faction - 6
#Minimal - 1
["ho_pla_sumpter_white","White Sumpter Horse", [("ho_pla_sumpter_white",0)], itp_merchandise|itp_type_horse, 0, 134,abundance(100)|hit_points(100)|body_armor(14)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic,[],[fac_player_faction]],

##War Horses - 105
#Swadia - 16
#Minimal - 2
["ho_swa_war_royal","Royal Warhorse", [("ho_swa_war_royal",0)], itp_merchandise|itp_type_horse, 0, 1230,abundance(50)|hit_points(155)|body_armor(41)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["ho_swa_charger_long","Long Barded Charger", [("ho_swa_charger_long",0)], itp_merchandise|itp_type_horse, 0, 1951,abundance(40)|hit_points(165)|body_armor(60)|difficulty(4)|horse_speed(37)|horse_maneuver(43)|horse_charge(34)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
#Vaegir - 15
#Minimal - 2
["ho_vae_war_leathered","Leathered Warhorse", [("ho_vae_war_leathered",0)], itp_merchandise|itp_type_horse, 0, 1240,abundance(50)|hit_points(155)|body_armor(41)|difficulty(4)|horse_speed(41)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_2]],
["ho_vae_charger_leathered","Leathered Charger", [("ho_vae_charger_leathered",0)], itp_merchandise|itp_type_horse,0,1804,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion,[],[fac_kingdom_2]],
#Khergit - 15
#Minimal - 2
["ho_khe_war_brass","Brass Warhorse", [("ho_khe_war_brass",0)], itp_merchandise|itp_type_horse, 0, 1236,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(42)|horse_maneuver(41)|horse_charge(27)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3]],
["ho_khe_charger_steppe","Steppe Charger", [("ho_khe_charger_steppe",0)], itp_merchandise|itp_type_horse, 0, 1818,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(41)|horse_maneuver(43)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3]],
#Nord - 14
#Minimal - 2
["ho_nor_war_blue","Blue Warhorse", [("ho_nor_war_blue",0)], itp_merchandise|itp_type_horse, 0, 1193,abundance(50)|hit_points(155)|body_armor(39)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_4]],
["ho_nor_charger_lamellar","Lamellar Charger", [("ho_nor_charger_lamellar",0)], itp_merchandise|itp_type_horse, 0, 1789,abundance(40)|hit_points(170)|body_armor(56)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion,[],[fac_kingdom_4]],
#Rhodok - 14
#Minimal - 2
["ho_rho_war_chain","Chain Warhorse", [("ho_rho_war_chain",0)], itp_merchandise|itp_type_horse, 0, 1255,abundance(50)|hit_points(165)|body_armor(41)|difficulty(4)|horse_speed(40)|horse_maneuver(40)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_5]],
["ho_rho_charger_chain","Chain Charger", [("ho_rho_charger_chain",0)], itp_merchandise|itp_type_horse, 0, 1852,abundance(40)|hit_points(165)|body_armor(59)|difficulty(4)|horse_speed(39)|horse_maneuver(43)|horse_charge(33)|horse_scale(112),imodbits_horse_basic|imodbit_champion,[],[fac_kingdom_5]],
#Sarranid - 15
#Minimal - 2
["ho_sar_war_golden","Golden Warhorse", [("ho_sar_war_golden",0)], itp_merchandise|itp_type_horse, 0, 1233,abundance(50)|hit_points(155)|body_armor(40)|difficulty(4)|horse_speed(41)|horse_maneuver(43)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
["ho_sar_charger_sarranid","Sarranid Charger", [("ho_sar_charger_sarranid",0)], itp_merchandise|itp_type_horse, 0, 1875,abundance(40)|hit_points(165)|body_armor(59)|difficulty(4)|horse_speed(40)|horse_maneuver(42)|horse_charge(33)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
#Player Faction - 17
#Minimal - 4
["ho_pla_charger_highlander","Highlander Charger", [("ho_pla_charger_highlander",0)], itp_merchandise|itp_type_horse, 0, 1837,abundance(40)|hit_points(170)|body_armor(57)|difficulty(4)|horse_speed(39)|horse_maneuver(43)|horse_charge(33)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_player_faction]],
["ho_pla_charger_plated","Iron Plated Charger", [("ho_pla_charger_plated",0)], itp_merchandise|itp_type_horse, 0, 1847,abundance(40)|hit_points(165)|body_armor(59)|difficulty(4)|horse_speed(40)|horse_maneuver(43)|horse_charge(33)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_player_faction]],
["ho_pla_elephant_battle","Battle Elephant", [("ho_pla_elephant_battle",0)], itp_merchandise|itp_type_horse, 0, 30000,abundance(1)|hit_points(300)|body_armor(40)|difficulty(6)|horse_speed(30)|horse_maneuver(20)|horse_charge(250)|horse_scale(130),imodbits_horse_basic|imodbit_champion, [], [fac_player_faction]],
["ho_pla_war_gerulfingen","Gerulfingen Warhorse", [("ho_pla_war_gerulfingen",0)], itp_merchandise|itp_type_horse, 0, 1216,abundance(10)|hit_points(170)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_player_faction]],
###

#### Weapons

###Axes - 45

##One-handed - 25
#Swadia - 2
#Minimal - 2
["we_swa_axe_hatchet", "Hatchet", [("we_swa_axe_hatchet",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,13,weight(2)|abundance(100)|difficulty(0)|spd_rtng(97)|weapon_length(60)|swing_damage(23,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_1]],
["we_swa_axe_swadian", "Swadian Axe", [("we_swa_axe_swadian",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,84,weight(1.75)|abundance(80)|difficulty(8)|spd_rtng(95)|weapon_length(60)|swing_damage(31,cut)|thrust_damage(0,pierce),imodbits_sword_high,[],[fac_kingdom_1]],
#Vaegir - 2
#Minimal - 2
["we_vae_axe_onehanded", "One Handed Axe", [("we_vae_axe_onehanded",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,21,weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(92)|weapon_length(71)|swing_damage(25,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_2]],
["we_vae_axe_vaegir", "Vaegir Axe", [("we_vae_axe_vaegir",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,78,weight(2)|abundance(80)|difficulty(8)|spd_rtng(93)|weapon_length(70)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_sword_high,[],[fac_kingdom_2]],
#Khergit - 2
#Minimal - 2
["we_khe_axe_steppe", "Steppe Axe", [("we_khe_axe_steppe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,19,weight(1.75)|abundance(100)|difficulty(0)|spd_rtng(90)|weapon_length(72)|swing_damage(25,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_3]],
["we_khe_axe_khergit", "Khergit Axe", [("we_khe_axe_khergit",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,85,weight(2)|abundance(80)|difficulty(8)|spd_rtng(93)|weapon_length(65)|swing_damage(31,cut)|thrust_damage(0,pierce),imodbits_sword_high,[],[fac_kingdom_3]],
#Nord - 7
#Minimal - 5
["we_nor_axe_jomsviking", "Jomsviking Axe", [("we_nor_axe_jomsviking",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,20,weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(90)|weapon_length(50)|swing_damage(24,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_4]],
["we_nor_axe_danox", "Danox", [("we_nor_axe_danox",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,79,weight(1.5)|abundance(80)|difficulty(8)|spd_rtng(99)|weapon_length(60)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_4]],
["we_nor_axe_haloygox", "Haloygox", [("we_nor_axe_haloygox",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,184,weight(1.5)|abundance(70)|difficulty(8)|spd_rtng(98)|weapon_length(61)|swing_damage(34,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_4,fac_player_faction]],
["we_nor_axe_breithofudox", "Breithofudox", [("we_nor_axe_breithofudox",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,263,weight(1.5)|abundance(60)|difficulty(9)|spd_rtng(97)|weapon_length(60)|swing_damage(37,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_4]],
["we_nor_axe_trondrox", "Trondrox", [("we_nor_axe_trondrox",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,553,weight(1.5)|abundance(50)|difficulty(0)|spd_rtng(97)|weapon_length(61)|swing_damage(40,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_4]],
#Rhodok - 6
#Minimal - 2
["we_rho_axe_pick", "Pickaxe", [("we_rho_axe_pick",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,11,weight(3)|abundance(100)|difficulty(0)|spd_rtng(99)|weapon_length(70)|swing_damage(19,pierce)|thrust_damage(0,pierce),imodbits_pick,[],[fac_kingdom_5]],
["we_rho_axe_pick_military", "Military Pick", [("we_rho_axe_pick_military",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,95,weight(1.5)|abundance(80)|difficulty(8)|spd_rtng(97)|weapon_length(70)|swing_damage(31,pierce)|thrust_damage(0,pierce),imodbits_pick,[],[fac_kingdom_5]],
#Sarranid - 4
#Minimal - 3
["we_sar_axe_onehanded", "Desert Axe", [("we_sar_axe_onehanded",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,27,weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(91)|weapon_length(76)|swing_damage(24,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_6]],
["we_sar_axe_battle", "Iron Battle Axe", [("we_sar_axe_battle",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,97,weight(1.75)|abundance(80)|difficulty(8)|spd_rtng(90)|weapon_length(71)|swing_damage(31,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_6]],
["we_sar_axe_wariron", "Iron War Axe", [("we_sar_axe_wariron",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,283,weight(1.75)|abundance(70)|difficulty(10)|spd_rtng(90)|weapon_length(71)|swing_damage(38,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_6]],
#Player Faction - 2
#Minimal - 2
["we_pla_axe_battleshort", "Short Battle Axe", [("we_pla_axe_battleshort",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip,78,weight(2)|abundance(80)|difficulty(8)|spd_rtng(92)|weapon_length(70)|swing_damage(31,cut)|thrust_damage(20,pierce),imodbits_sword_high,[],[fac_player_faction]],
["we_pla_axe_battle", "Battle Axe", [("we_pla_axe_battle",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip,260,weight(2.5)|abundance(70)|difficulty(9)|spd_rtng(91)|weapon_length(80)|swing_damage(36,cut)|thrust_damage(21,pierce),imodbits_sword_high,[],[fac_player_faction]],

##Two-handed - 21
#Swadia - 3
#Minimal - 3
["we_swa_axe_voulge", "Voulge", [("we_swa_axe_voulge",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,129,weight(4.5)|abundance(100)|difficulty(8)|spd_rtng(87)|weapon_length(119)|swing_damage(35,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_1,fac_player_faction]],
["we_swa_axe_voulgeshort", "Shortened Voulge", [("we_swa_axe_voulgeshort",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,228,weight(4.5)|abundance(80)|difficulty(9)|spd_rtng(92)|weapon_length(100)|swing_damage(45,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_1]],
["we_swa_axe_voulgelong", "Long Voulge", [("we_swa_axe_voulgelong",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,389,weight(3.0)|abundance(70)|difficulty(12)|spd_rtng(88)|weapon_length(175)|swing_damage(40,cut)|thrust_damage(18,pierce),imodbits_axe,[],[fac_kingdom_1]],
#Vaegir - 4
#Minimal - 4
["we_vae_axe_bardiche", "Bardiche", [("we_vae_axe_bardiche",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,291,weight(4.5)|abundance(70)|difficulty(9)|spd_rtng(91)|weapon_length(102)|swing_damage(47,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_2]],
["we_vae_axe_bardichelong", "Long Bardiche", [("we_vae_axe_bardichelong",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,390,weight(4.5)|abundance(60)|difficulty(13)|spd_rtng(89)|weapon_length(140)|swing_damage(48,cut)|thrust_damage(17,pierce),imodbits_axe,[],[fac_kingdom_2,fac_player_faction]],
["we_vae_axe_bardichegreat", "Great Bardiche", [("we_vae_axe_bardichegreat",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,617,weight(4.5)|abundance(60)|difficulty(10)|spd_rtng(89)|weapon_length(116)|swing_damage(50,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_2]],
["we_vae_axe_bardichegreatlong", "Great Long Bardiche", [("we_vae_axe_bardichegreatlong",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,660,weight(5.0)|abundance(60)|difficulty(14)|spd_rtng(88)|weapon_length(155)|swing_damage(50,cut)|thrust_damage(17,pierce),imodbits_axe,[],[fac_kingdom_2]],
#Khergit - 1
#Minimal - 1
["we_khe_axe_voulge", "Khergit Voulge", [("we_khe_axe_voulge",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,410,weight(4.5)|abundance(60)|difficulty(13)|spd_rtng(89)|weapon_length(190)|swing_damage(48,cut)|thrust_damage(17,pierce),imodbits_axe,[],[fac_kingdom_3,fac_player_faction]],
#Nord - 8
#Minimal - 6
["we_nor_axe_hedmarkox_tveirhendr", "Tveirhendr Hedmarkox", [("we_nor_axe_hedmarkox_tveirhendr",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,92,weight(4.5)|abundance(100)|difficulty(8)|spd_rtng(95)|weapon_length(100)|swing_damage(38,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_4]],
["we_nor_axe_danox_tveirhendr", "Tveirhendr Danox", [("we_nor_axe_danox_tveirhendr",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,168,weight(4.5)|abundance(80)|difficulty(8)|spd_rtng(95)|weapon_length(100)|swing_damage(41,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_4]],
["we_nor_axe_nordic", "Nordic Great Axe", [("we_nor_axe_nordic",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,271,weight(4.5)|abundance(70)|difficulty(9)|spd_rtng(94)|weapon_length(100)|swing_damage(43,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_4]],
["we_nor_axe_danelong", "Long Dane Axe", [("we_nor_axe_danelong",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise,itc_staff|itcf_carry_axe_back,390,weight(4.5)|abundance(70)|difficulty(9)|spd_rtng(93)|weapon_length(155)|swing_damage(46,cut)|thrust_damage(19,blunt),imodbits_axe,[],[fac_kingdom_4]], 
	["we_nor_axe_danelong_alt", "Long Dane Axe", [("we_nor_axe_danelong",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,390,weight(4.5)|abundance(70)|difficulty(9)|spd_rtng(88)|weapon_length(155)|swing_damage(46,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_4]],
["we_nor_axe_beardedlight", "Light Bearded Axe", [("we_nor_axe_beardedlight",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,510,weight(4.5)|abundance(60)|difficulty(10)|spd_rtng(92)|weapon_length(120)|swing_damage(50,cut)|thrust_damage(18,blunt),imodbits_axe,[],[fac_kingdom_4]], 
	["we_nor_axe_beardedlight_alt", "Light Bearded Axe", [("we_nor_axe_beardedlight",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,510,weight(4.5)|abundance(60)|difficulty(11)|spd_rtng(87)|weapon_length(120)|swing_damage(50,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_4]],
["we_nor_axe_bearded", "Bearded Axe", [("we_nor_axe_bearded",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,660,weight(4.5)|abundance(50)|difficulty(12)|spd_rtng(91)|weapon_length(140)|swing_damage(54,cut)|thrust_damage(19, blunt),imodbits_axe,[],[fac_kingdom_4]], 
	["we_nor_axe_bearded_alt", "Bearded Axe", [("we_nor_axe_bearded",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,660,weight(4.5)|abundance(50)|difficulty(12)|spd_rtng(85)|weapon_length(140)|swing_damage(54,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_4]],
#Rhodok - 1
#Minimal - 1
["we_rho_axe_knight", "Knights Axe", [("we_rho_axe_knight",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_back,100,weight(4.5)|abundance(90)|difficulty(8)|spd_rtng(95)|weapon_length(110)|swing_damage(38,cut)|thrust_damage(25,pierce),imodbits_sword_high,[],[fac_kingdom_5]],
#Sarranid
#Minimal - 2
["we_sar_axe_war", "Sarranid War Axe", [("we_sar_axe_war",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,380,weight(3.0)|abundance(70)|difficulty(9)|spd_rtng(90)|weapon_length(90)|swing_damage(46,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_6]],
["we_sar_axe_battletwo", "Sarranid Battle Axe", [("we_sar_axe_battletwo",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,490,weight(3.0)|abundance(60)|difficulty(10)|spd_rtng(89)|weapon_length(95)|swing_damage(49,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_6]],
#Player Faction - 2
#Minimal - 2
["we_pla_axe_twohanded", "Two Handed War Axe", [("we_pla_axe_twohanded",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,280,weight(4.5)|abundance(80)|difficulty(9)|spd_rtng(96)|weapon_length(92)|swing_damage(44,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_player_faction]],
["we_pla_axe_great", "Great Axe", [("we_pla_axe_great",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,316,weight(4.5)|abundance(70)|difficulty(9)|spd_rtng(94)|weapon_length(96)|swing_damage(47,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_player_faction]],

###Blunt Weapons - 48

##One-handed - 33
#General - 2
#Minimal - 2
["we_gen_blunt_torch", "Torch", [("we_gen_blunt_torch",0)], itp_type_one_handed_wpn|itp_primary,itc_scimitar,11,weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none, [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),])]],
["we_gen_blunt_keys", "Ring of Keys", [("we_gen_blunt_keys",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar, 240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ], 
#Swadia - 4
#Minimal - 2
["we_swa_blunt_club", "Swadian Club", [("we_swa_blunt_club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,11,weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(98)|weapon_length(70)|swing_damage(20,blunt)|thrust_damage(0,pierce),imodbits_none,[],[fac_kingdom_1]],
["we_swa_blunt_morningstar", "Swadian Morningstar", [("we_swa_blunt_morningstar",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,305,weight(4.5)|difficulty(13)|spd_rtng(89)|weapon_length(86)|swing_damage(36,pierce)|thrust_damage(0,pierce),imodbits_mace,[],[fac_kingdom_1]],
#Vaegir - 12
#Minimal - 6
["we_vae_blunt_club", "Vaegir Club", [("we_vae_blunt_club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,11,weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(98)|weapon_length(70)|swing_damage(20,blunt)|thrust_damage(0,pierce),imodbits_none,[],[fac_kingdom_2]],
["we_vae_blunt_hammer", "Hammer", [("we_vae_blunt_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar,30,weight(2)|difficulty(0)|spd_rtng(98)|weapon_length(60)|swing_damage(24,blunt)|thrust_damage(0,pierce),imodbits_mace,[],[fac_kingdom_2,fac_player_faction]],
["we_vae_blunt_hammerthick", "Thick Hammer", [("we_vae_blunt_hammerthick",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,109,weight(2.3)|difficulty(8)|spd_rtng(92)|weapon_length(70)|swing_damage(28,blunt)|thrust_damage(0,pierce),imodbits_mace,[],[fac_kingdom_2]],
["we_vae_blunt_hammersleek", "Sleek Hammer", [("we_vae_blunt_hammersleek",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,185,weight(2.3)|difficulty(8)|spd_rtng(93)|weapon_length(70)|swing_damage(29,blunt)|thrust_damage(0,pierce),imodbits_mace,[],[fac_kingdom_2]],
["we_vae_blunt_hammerempirewar", "Empire War Hammer", [("we_vae_blunt_hammerempirewar",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,232, weight(3)|difficulty(9)|spd_rtng(90)|weapon_length(75)|swing_damage(30,blunt)|thrust_damage(0,pierce),imodbits_mace,[],[fac_kingdom_2]],
["we_vae_blunt_hammermilitary", "Military Hammer", [("we_vae_blunt_hammermilitary",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,317,weight(2)|difficulty(10)|spd_rtng(95)|weapon_length(70)|swing_damage(31,blunt)|thrust_damage(0,pierce),imodbits_mace,[],[fac_kingdom_2]],
#Khergit - 1
#Minimal - 1
["we_khe_blunt_club", "Khergit Club", [("we_khe_blunt_club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,11,weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(98)|weapon_length(70)|swing_damage(20,blunt)|thrust_damage(0,pierce),imodbits_none,[],[fac_kingdom_3]],
#Nord - 1
#Minimal - 1
["we_nor_blunt_stick", "Wooden Stick", [("we_nor_blunt_stick",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,4,weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(99)|weapon_length(63)|swing_damage(13,blunt)|thrust_damage(0,pierce),imodbits_none,[],[fac_kingdom_4,fac_player_faction]],
#Rhodok - 1
#Minimal - 1
["we_rho_blunt_club", "Rhodok Club", [("we_rho_blunt_club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,11,weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(98)|weapon_length(70)|swing_damage(20,blunt)|thrust_damage(0,pierce),imodbits_none,[],[fac_kingdom_5]],
#Sarranid - 10
#Minimal - 4
["we_sar_blunt_club", "Sarranid Club", [("we_sar_blunt_club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,11,weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(98)|weapon_length(70)|swing_damage(20,blunt)|thrust_damage(0,pierce),imodbits_none,[],[fac_kingdom_6]],
["we_sar_blunt_maceiron", "Iron Mace", [("we_sar_blunt_maceiron",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,113,weight(2.0)|abundance(90)|difficulty(0)|spd_rtng(99)|weapon_length(73)|swing_damage(22,blunt)|thrust_damage(0,pierce),imodbits_mace,[],[fac_kingdom_6,fac_player_faction]],
["we_sar_blunt_maceflanged", "Flanged Mace", [("we_sar_blunt_maceflanged",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,222,weight(3.5)|abundance(80)|difficulty(7)|spd_rtng(103)|weapon_length(70)|swing_damage(24,blunt)|thrust_damage(0,pierce),imodbits_mace,[],[fac_kingdom_6]],
["we_sar_blunt_macespiked", "Spiked Mace", [("we_sar_blunt_macespiked",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,281,weight(3.5)|abundance(70)|difficulty(8)|spd_rtng(98)|weapon_length(70)|swing_damage(28,blunt)|thrust_damage(0,pierce),imodbits_pick,[],[fac_kingdom_6]],
#Player Faction - 2
#Minimal - 2
["we_pla_blunt_morningstar_mercenary", "Mercenary Morningstar", [("we_pla_blunt_morningstar_mercenary",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,275,weight(3.5)|abundance(70)|difficulty(8)|spd_rtng(98)|weapon_length(60)|swing_damage(28,blunt)|thrust_damage(0,pierce),imodbits_pick,[],[fac_player_faction]],
["we_pla_blunt_morningstar_squared", "Squared Mace", [("we_pla_blunt_morningstar_squared",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,284,weight(3.5)|abundance(70)|difficulty(8)|spd_rtng(98)|weapon_length(70)|swing_damage(28,blunt)|thrust_damage(0,pierce),imodbits_pick,[],[fac_player_faction]],

##Two-handed - 15
#Swadia - 2
#Minimal - 1
["we_swa_blunt_club_long", "Long Spiked Club", [("we_swa_blunt_club_long",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,264,weight(2.5)|abundance(80)|difficulty(9)|spd_rtng(96)|weapon_length(126)|swing_damage(23,pierce)|thrust_damage(20,blunt),imodbits_mace,[],[fac_kingdom_1]],
#Vaegir - 6
#Minimal - 3
["we_vae_blunt_maul", "Maul", [("we_vae_blunt_maul",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,97,weight(6)|difficulty(11)|spd_rtng(83)|weapon_length(79)|swing_damage(36,blunt)|thrust_damage(0,pierce),imodbits_mace,[],[fac_kingdom_2,fac_player_faction]],
["we_vae_blunt_sledgehammer", "Sledgehammer", [("we_vae_blunt_sledgehammer",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,101,weight(7)|difficulty(12)|spd_rtng(81)| weapon_length(82)|swing_damage(39,blunt)|thrust_damage(0,pierce),imodbits_mace,[],[fac_kingdom_2]],
["we_vae_blunt_greathammer", "Great Hammer", [("we_vae_blunt_greathammer",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,290,weight(9)|difficulty(14)|spd_rtng(79)|weapon_length(75)|swing_damage(45,blunt)|thrust_damage(0 ,  pierce),imodbits_mace,[],[fac_kingdom_2]],
#Khergit - 0
#Minimal - 0
#Nord - 0
#Minimal - 0
#Rhodok - 0
#Minimal - 0
#Sarranid - 2
#Minimal - 3
["we_sar_blunt_maceknobbedlong", "Long Hafted Knobbed Mace", [("we_sar_blunt_maceknobbedlong",0)], itp_type_polearm| itp_can_knock_down|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,324,weight(2.5)|abundance(70)|difficulty(10)|spd_rtng(95)|weapon_length(133)|swing_damage(26,blunt)|thrust_damage(23,blunt),imodbits_mace,[],[fac_kingdom_6]],
["we_sar_blunt_macespikedlong", "Long Hafted Spiked Mace", [("we_sar_blunt_macespikedlong",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,390,weight(2.5)|abundance(70)|difficulty(10)|spd_rtng(94)|weapon_length(140)|swing_damage(28,blunt)|thrust_damage(24,blunt),imodbits_mace,[],[fac_kingdom_6]],
["we_sar_blunt_mace_ironlong", "Long Iron Mace", [("we_sar_blunt_mace_ironlong",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,470,weight(4.5)|abundance(80)|difficulty(10)|spd_rtng(90)|weapon_length(95)|swing_damage(35,blunt)|thrust_damage(22,blunt),imodbits_mace,[],[fac_kingdom_6,fac_player_faction]],
#Player Faction - 3
#Minimal - 2
["we_pla_blunt_goedendag", "Goedendag", [("we_pla_blunt_goedendag",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back,200,weight(2.5)|abundance(90)|difficulty(9)|spd_rtng(95)|weapon_length(117)|swing_damage(24,blunt)|thrust_damage(20,pierce),imodbits_mace,[],[fac_player_faction]],
["we_pla_blunt_becdecorbin", "Bec de Corbin", [("we_pla_blunt_becdecorbin",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear,125,weight(6.0)|difficulty(8)|spd_rtng(81)|weapon_length(120)|swing_damage(38,blunt)|thrust_damage(38,pierce),imodbits_polearm,[],[fac_player_faction]],

###Polearms - 115

##Two-handed - 83
#Swadia - 7
#Minimal - 4
["we_swa_spear_boar", "Boar Spear", [("we_swa_spear_boar",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,76,weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(90)|weapon_length(157)|swing_damage(26,cut)|thrust_damage(23,pierce),imodbits_polearm,[],[fac_kingdom_1]],
["we_swa_spear_glaive_small","Small Glaive",[("we_swa_spear_glaive_small",0)],itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,245,weight(2.5)|abundance(80)|difficulty(9)|spd_rtng(82)|weapon_length(163)|swing_damage(31,cut)|thrust_damage(28,pierce),imodbits_polearm,[],[fac_kingdom_1]],
["we_swa_spear_glaive","Glaive",[("we_swa_spear_glaive",0)],itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,270,weight(2.25)|abundance(70)|difficulty(10)|spd_rtng(80)|weapon_length(170)|swing_damage(34,cut)|thrust_damage(29,pierce),imodbits_polearm,[],[fac_kingdom_1]],
["we_swa_spear_bill_english", "English Bill", [("we_swa_spear_bill_english",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,541,weight(5.5)|abundance(60)|difficulty(12)|spd_rtng(75)|weapon_length(182)|swing_damage(44,cut)|thrust_damage(32,pierce),imodbits_polearm,[],[fac_kingdom_1]],
#Vaegir - 9
#Minimal - 4
["we_vae_spear_scythe", "Scythe", [("we_vae_spear_scythe",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,43,weight(3)|abundance(100)|difficulty(0)|spd_rtng(79)|weapon_length(182)|swing_damage(19,cut)|thrust_damage(14,pierce),imodbits_polearm,[],[fac_kingdom_2]],
["we_vae_spear_scythe_military", "Military Scythe", [("we_vae_spear_scythe_military",0),("we_vae_spear_scythe_military_bad",imodbits_bad)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,155,weight(2.5)|abundance(80)|difficulty(11)|spd_rtng(90)|weapon_length(155)|swing_damage(36,cut)|thrust_damage(25,pierce),imodbits_polearm,[],[fac_kingdom_2]],
["we_vae_spear_scythe_shortened", "Shortened Military Scythe", [("we_vae_spear_scythe_shortened",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,364,weight(3.0)|abundance(70)|difficulty(11)|spd_rtng(90)|weapon_length(112)|swing_damage(45,cut)|thrust_damage(0,pierce),imodbits_sword_high,[],[fac_kingdom_2]],
["we_vae_spear_polehammer", "Vaegir Polehammer", [("we_vae_spear_polehammer",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,549,weight(7)|abundance(60)|difficulty(15)|spd_rtng(71)|weapon_length(160)|swing_damage(46,blunt)|thrust_damage(20,pierce),imodbits_polearm,[],[fac_kingdom_2]],
#Khergit - 14
#Minimal - 6
["we_khe_spear_staff", "Khergit Staff", [("we_khe_spear_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,40,weight(1.5)|abundance(120)|difficulty(0)|spd_rtng(100)|weapon_length(130)|swing_damage(18,blunt)|thrust_damage(19,blunt),imodbits_polearm,[],[fac_kingdom_3]],
["we_khe_spear_bamboolong", "Bamboo Long Spear", [("we_khe_spear_bamboolong",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,76,weight(1.5)|abundance(90)|difficulty(0)|spd_rtng(85)|weapon_length(140)|swing_damage(20,cut)|thrust_damage(26,pierce),imodbits_polearm,[],[fac_kingdom_3]],
["we_khe_spear_nagita", "Nagita", [("we_khe_spear_nagita",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,185,weight(2.75)|abundance(80)|difficulty(11)|spd_rtng(95)|weapon_length(135)|swing_damage(37,cut)|thrust_damage(20,pierce),imodbits_polearm,[],[fac_kingdom_3]],
["we_khe_spear_viper", "Viper Spear", [("we_khe_spear_viper",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,240,weight(2.75)|abundance(70)|difficulty(8)|spd_rtng(90)|weapon_length(110)|swing_damage(14,blunt)|thrust_damage(30,pierce),imodbits_polearm,[],[fac_kingdom_3]],
["we_khe_spear_haftedblade", "Hafted Blade", [("we_khe_spear_haftedblade",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,350,weight(3.25)|abundance(60)|difficulty(11)|spd_rtng(93)|weapon_length(153)|swing_damage(39,cut)|thrust_damage(19,pierce),imodbits_polearm,[],[fac_kingdom_3]],
["we_khe_spear_nagitakhergit", "Khergit Nagita", [("we_khe_spear_nagitakhergit",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,502,weight(5)|abundance(50)|difficulty(12)|spd_rtng(60)|weapon_length(250)|swing_damage(43,cut)|thrust_damage(20,pierce),imodbits_polearm,[],[fac_kingdom_3]],
#Nord - 13
#Minimal - 6
["we_nor_spear_sviar", "Sviar", [("we_nor_spear_sviar",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,53,weight(2)|abundance(100)|difficulty(0)|spd_rtng(102)|weapon_length(120)|swing_damage(19,blunt)|thrust_damage(25,pierce),imodbits_polearm,[],[fac_kingdom_4]],
["we_nor_spear_svia", "Svia", [("we_nor_spear_svia",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,82,weight(2.25)|abundance(90)|difficulty(0)|spd_rtng(93)|weapon_length(130)|swing_damage(20,blunt)|thrust_damage(26,pierce),imodbits_polearm,[],[fac_kingdom_4]],
["we_nor_spear_hoggkesja", "Hoggkesja", [("we_nor_spear_hoggkesja",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,137,weight(2.5)|abundance(80)|difficulty(7)|spd_rtng(95)|weapon_length(140)|swing_damage(20,blunt)|thrust_damage(27, pierce),imodbits_polearm,[],[fac_kingdom_4]],
["we_nor_spear_krokaspjott_kastad", "Kastad Krokaspjott", [("we_nor_spear_krokaspjott_kastad",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,230,weight(2.75)|abundance(70)|difficulty(8)|spd_rtng(90)|weapon_length(170)|swing_damage(19,blunt)|thrust_damage(29,pierce),imodbits_polearm,[],[fac_kingdom_4]],
["we_nor_spear_hoggspjott_langr", "Langr Hoggspjott", [("we_nor_spear_hoggspjott_langr",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,369,weight(2.5)|abundance(60)|difficulty(9)|spd_rtng(90)|weapon_length(180)|swing_damage(19,blunt)|thrust_damage(33,pierce),imodbits_polearm,[],[fac_kingdom_4]],
["we_nor_spear_spjotkesja", "Spjotkesja", [("we_nor_spear_spjotkesja",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,450,weight(2.5)|abundance(50)|difficulty(10)|spd_rtng(87)|weapon_length(200)|swing_damage(18,blunt)|thrust_damage(35,pierce),imodbits_polearm,[],[fac_kingdom_4]],
#Rhodok - 16
#Minimal - 6
["we_rho_spear_fork_pitch", "Pitch Fork", [("we_rho_spear_fork_pitch",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff,19,weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(83)| weapon_length(154)|swing_damage(0,blunt)|thrust_damage(18,pierce),imodbits_polearm,[],[fac_kingdom_5]],
["we_rho_spear_fork_military", "Military Fork", [("we_rho_spear_fork_military",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff,153,weight(4.5)|abundance(80)|difficulty(0)|spd_rtng(88)|weapon_length(135)|swing_damage(0,blunt)|thrust_damage(23,pierce),imodbits_polearm,[],[fac_kingdom_5]],
["we_rho_spear_fork_battle", "Battle Fork", [("we_rho_spear_fork_battle",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff,282,weight(4.5)|abundance(70)|difficulty(0)|spd_rtng(87)|weapon_length(142)|swing_damage(0,blunt)|thrust_damage(24,pierce),imodbits_polearm,[],[fac_kingdom_5]],
["we_rho_spear_mountain", "Mountain Spear", [("we_rho_spear_mountain",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,310,weight(2.6)|abundance(60)|difficulty(7)|spd_rtng(93)|weapon_length(156)|swing_damage(10,cut)|thrust_damage(27,pierce),imodbits_polearm,[],[fac_kingdom_5]],
["we_rho_spear_large", "Large Spear", [("we_rho_spear_large",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,420,weight(3.5)|abundance(50)|difficulty(9)|spd_rtng(87)|weapon_length(200)|swing_damage(25,cut)|thrust_damage(34,pierce),imodbits_polearm,[],[fac_kingdom_5]],
["we_rho_spear_phalanx", "Phalanx Pike", [("we_rho_spear_phalanx",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,775,weight(4)|abundance(40)|difficulty(11)|spd_rtng(80)|weapon_length(300)|swing_damage(20,cut)|thrust_damage(40,pierce),imodbits_polearm,[],[fac_kingdom_5]],
#Sarranid - 6
#Minimal - 3
["we_sar_spear_staff", "Staff", [("we_sar_spear_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,36,weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(100)|weapon_length(130)|swing_damage(18,blunt)|thrust_damage(19,blunt),imodbits_polearm,[],[fac_kingdom_6]],
["we_sar_spear_staff_quarter", "Quarter Staff", [("we_sar_spear_staff_quarter",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,60,weight(2)|abundance(100)|difficulty(0)|spd_rtng(104)|weapon_length(140)|swing_damage(20,blunt)|thrust_damage(20,blunt),imodbits_polearm,[],[fac_kingdom_6]],
["we_sar_spear_staff_iron", "Iron Staff", [("we_sar_spear_staff_iron",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary, itc_staff|itcf_carry_sword_back,202,weight(2)|abundance(90)|difficulty(0)|spd_rtng(97)|weapon_length(140)|swing_damage(25,blunt)|thrust_damage(26,blunt),imodbits_polearm,[],[fac_kingdom_6]],
["we_sar_spear_pikestrong", "Strong Desert Pike", [("we_sar_spear_pikestrong",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,371,weight(2.6)|abundance(80)|difficulty(8)|spd_rtng(88)|weapon_length(170)|swing_damage(0,cut)|thrust_damage(31,pierce),imodbits_polearm,[],[fac_kingdom_6]],
#Player Faction - 18
#Minimal - 7
["we_pla_spear_crook_shepperd", "Shepherd Crook", [("we_pla_spear_crook_shepperd",0)],itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,10,weight(3)|abundance(100)|difficulty(0)|spd_rtng(90)|weapon_length(150)|swing_damage(15,blunt)|thrust_damage(10,blunt),imodbits_polearm,[],[fac_player_faction]],
["we_pla_spear_staff_bishop", "Bishop Staff", [("we_pla_spear_staff_bishop",0)],itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,370,weight(3)|abundance(10)|difficulty(7)|spd_rtng(100)|weapon_length(180)|swing_damage(30,blunt)|thrust_damage(20,blunt),imodbits_polearm,[],[fac_player_faction]],
["we_pla_spear_halberd", "Halberd", [("we_pla_spear_halberd",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,233,weight(4.6)|abundance(80)|difficulty(11)|spd_rtng(81)|weapon_length(150)|swing_damage(35,cut)|thrust_damage(30,pierce),imodbits_polearm,[],[fac_player_faction]],
["we_pla_spear_halberd_dark", "Dark Halberd", [("we_pla_spear_halberd_dark",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,585,weight(4.8)|abundance(60)|difficulty(13)|spd_rtng(79)|weapon_length(160)|swing_damage(45,cut)|thrust_damage(40,pierce),imodbits_polearm,[],[fac_player_faction]],
["we_pla_spear_halberd_elite", "Elite Halberd", [("we_pla_spear_halberd_elite",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,610,weight(5.1)|abundance(60)|difficulty(13)|spd_rtng(74)|weapon_length(180)|swing_damage(45,cut)|thrust_damage(36,pierce),imodbits_polearm,[],[fac_player_faction]],
["we_pla_spear_halberd_bearded", "Bearded Halberd", [("we_pla_spear_halberd_bearded",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,607,weight(5.5)|abundance(60)|difficulty(13)|spd_rtng(61)|weapon_length(200)|swing_damage(44,cut)|thrust_damage(36,pierce),imodbits_polearm,[],[fac_player_faction]],
["we_pla_spear_halberd_long", "Long Halberd", [("we_pla_spear_halberd_long",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,455,weight(5.2)|abundance(70)|difficulty(12)|spd_rtng(75)|weapon_length(220)|swing_damage(42,cut)|thrust_damage(36,pierce),imodbits_polearm,[],[fac_player_faction]],

##Lances - 32
#Swadia - 12
#Minimal - 4
["we_swa_spear_lance_jousting", "Jousting Lance", [("we_swa_spear_lance_jousting",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,158,weight(5)|abundance(100)|difficulty(8)|spd_rtng(61)|weapon_length(240)|swing_damage(0,cut)|thrust_damage(17,blunt),imodbits_polearm,[],[fac_kingdom_1]],
["we_swa_spear_lance_light", "Light Lance", [("we_swa_spear_lance_light",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,180,weight(2.5)|abundance(80)|difficulty(9)|spd_rtng(85)|weapon_length(175)|swing_damage(16,blunt)|thrust_damage(27,pierce),imodbits_polearm,[],[fac_kingdom_1]],
["we_swa_spear_lance_heavy", "Heavy Lance", [("we_swa_spear_lance_heavy",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,360,weight(2.75)|abundance(70)|difficulty(10)|spd_rtng(75)|weapon_length(190)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_polearm,[],[fac_kingdom_1]],
["we_swa_spear_lance_great", "Great Lance", [("we_swa_spear_lance_great",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,410,weight(5)|abundance(60)|difficulty(11)|spd_rtng(55)|weapon_length(240)|swing_damage(0,cut)|thrust_damage(21,pierce),imodbits_polearm,[],[fac_kingdom_1]],
#Vaegir - 3
#Minimal - 1
["we_vae_spear_lance", "Vaegir Lance", [("we_vae_spear_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,270,weight(2.5)|abundance(80)|difficulty(9)|spd_rtng(80)|weapon_length(180)|swing_damage(16,blunt)|thrust_damage(26,pierce),imodbits_polearm,[],[fac_kingdom_2]],
#Khergit - 7
#Minimal - 3
["we_khe_spear_lance", "Khergit Lance", [("we_khe_spear_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,240,weight(4)|abundance(80)|difficulty(9)|spd_rtng(55)|weapon_length(240)|swing_damage(19,blunt)|thrust_damage(20,pierce),imodbits_polearm,[],[fac_kingdom_3]],
["we_khe_spear_lanceflag_a", "Blue Flagged Khergit Lance", [("we_khe_spear_lanceflag_a",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,451,weight(4.1)|abundance(60)|difficulty(11)|spd_rtng(55)|weapon_length(240)|swing_damage(0,cut)|thrust_damage(21,pierce),imodbits_polearm,[],[fac_kingdom_3]],
["we_khe_spear_lancehook", "Hooked Lance", [("we_khe_spear_lancehook",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,551,weight(4.5)|abundance(60)|difficulty(12)|spd_rtng(55)|weapon_length(190)|swing_damage(20,cut)|thrust_damage(25,pierce),imodbits_polearm,[],[fac_kingdom_3]],
#Nord - 2
#Minimal - 1
["we_nor_spear_svia_langr", "Langr Svia", [("we_nor_spear_svia_langr",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,289,weight(2.5)|abundance(100)|difficulty(7)|spd_rtng(80)|weapon_length(200)|swing_damage(15,blunt)|thrust_damage(28,pierce),imodbits_polearm,[],[fac_kingdom_4]],
#Rhodok - 3
#Minimal - 1
["we_rho_spear_lance", "Rhodok Lance", [("we_rho_spear_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,565,weight(3.5)|abundance(80)|difficulty(9)|spd_rtng(91)|weapon_length(240)|swing_damage(18,blunt)|thrust_damage(30,pierce),imodbits_polearm,[],[fac_kingdom_5]],
#Sarranid - 4
#Minimal - 2
["we_sar_spear_desert", "Desert Lance", [("we_sar_spear_desert",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,191,weight(5)|abundance(100)|difficulty(8)|spd_rtng(68)|weapon_length(210)|swing_damage(13,blunt)|thrust_damage(19,pierce),imodbits_polearm,[],[fac_kingdom_6]],
["we_sar_spear_lance", "Sarranid Lance", [("we_sar_spear_lance",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,590,weight(6.5)|abundance(80)|difficulty(9)|spd_rtng(45)|weapon_length(320)|swing_damage(0,cut)|thrust_damage(28,pierce),imodbits_polearm,[],[fac_kingdom_6]],
#Player Faction - 1
#Minimal - 1
["we_pla_spear_lancegothic", "Gothic Lance", [("we_pla_spear_lancegothic",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,210,weight(5)|abundance(80)|difficulty(10)|spd_rtng(70)|weapon_length(200)|swing_damage(0,cut)|thrust_damage(20,pierce),imodbits_polearm,[],[fac_player_faction]],

###Swords - 121

###One-handed - 82
##Swadia - 10
#Minimal - 5
["we_swa_sword_clamshelldagger", "Clamshell Dagger", [("we_swa_sword_clamshelldagger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,45,weight(1)|abundance(100)|difficulty(0)|spd_rtng(99)|weapon_length(50)|swing_damage(17,cut)|thrust_damage(20,pierce),imodbits_sword_high,[],[fac_kingdom_1]],
["we_swa_sword_senlac", "Senlac Sword", [("we_swa_sword_senlac",0),("we_swa_scabbard_senlac", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,176,weight(1.7)|abundance(90)|difficulty(0)|spd_rtng(99)|weapon_length(95)|swing_damage(27,cut)|thrust_damage(22,pierce),imodbits_sword_high,[],[fac_kingdom_1]],
["we_swa_sword_clamshell", "Clamshell Sword", [("we_swa_sword_clamshell",0),("we_swa_scabbard_clamshell", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,444,weight(2)|abundance(70)|difficulty(8)|spd_rtng(99)|weapon_length(80)|swing_damage(31,cut)|thrust_damage(24,pierce),imodbits_sword_high,[],[fac_kingdom_1]],
["we_swa_sword_knight", "Knight Sword", [("we_swa_sword_knight",0),("we_swa_scabbard_knight", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,496,weight(1.6)|abundance(60)|difficulty(8)|spd_rtng(100)|weapon_length(95)|swing_damage(32,cut)|thrust_damage(24,pierce),imodbits_sword_high,[],[fac_kingdom_1]],
["we_swa_sword_lord", "Swadian Lord Sword", [("we_swa_sword_lord",0),("we_swa_scabbard_lord", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,612,weight(2.5)|abundance(40)|difficulty(9)|spd_rtng(94)|weapon_length(100)|swing_damage(34,cut)|thrust_damage(25,pierce),imodbits_sword_high,[],[fac_kingdom_1]],
##Vaegir - 9
#Minimal - 5
["we_vae_sword_sickle", "Sickle", [("we_vae_sword_sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,9,weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99)|weapon_length(40)|swing_damage(20,cut)|thrust_damage(0,pierce),imodbits_none,[],[fac_kingdom_2]],
["we_vae_sword_knife", "Knife", [("we_vae_sword_knife",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,33,weight(0.5)|abundance(100)|difficulty(0)|spd_rtng(110)|weapon_length(40)|swing_damage(21,cut)|thrust_damage(13,pierce),imodbits_sword,[],[fac_kingdom_2]],
["we_vae_sword_sickle_military", "Military Sickle", [("we_vae_sword_sickle_military",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,220,weight(1.0)|abundance(70)|difficulty(9)|spd_rtng(100)|weapon_length(75)|swing_damage(26,pierce)|thrust_damage(0,pierce),imodbits_axe,[],[fac_kingdom_2]],
["we_vae_sword_jarl", "Jarl Sword", [("we_vae_sword_jarl",0),("we_vae_scabbard_jarl", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,461,weight(1.5)|abundance(50)|difficulty(8)|spd_rtng(100)|weapon_length(95)|swing_damage(31,cut)|thrust_damage(24,pierce),imodbits_sword_high,[],[fac_kingdom_2]],
["we_vae_sword_cleaver_military", "Military Cleaver", [("we_vae_sword_cleaver_military",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,588,weight(1.5)|abundance(40)|difficulty(9)|spd_rtng(96)|weapon_length(95)|swing_damage(35,cut)|thrust_damage(0,pierce),imodbits_sword_high,[],[fac_kingdom_2]],
##Khergit - 11
#Minimal - 6
["we_khe_sword_dagger", "Khergit Dagger", [("we_khe_sword_dagger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,39,weight(1)|abundance(100)|difficulty(0)|spd_rtng(108)|weapon_length(41)|swing_damage(23,cut)|thrust_damage(14,pierce),imodbits_sword_high,[],[fac_kingdom_3]],
["we_khe_sword_executionerone", "Khergit Executioner", [("we_khe_sword_executionerone",0),("we_khe_scabbard_steppe", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,122,weight(1.5)|abundance(90)|difficulty(0)|spd_rtng(100)|weapon_length(90)|swing_damage(27,cut),imodbits_sword_high,[],[fac_kingdom_3]],
["we_khe_sword_nomad", "Nomad Sabre", [("we_khe_sword_nomad",0),("we_khe_scabbard_nomad", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,252,weight(1.25)|abundance(80)|difficulty(0)|spd_rtng(100)|weapon_length(97)|swing_damage(29,cut),imodbits_sword_high,[],[fac_kingdom_3]],
["we_khe_sword_khergit", "Khergit Sabre", [("we_khe_sword_khergit",0),("we_khe_scabbard_khergit", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,403,weight(1.5)|abundance(60)|difficulty(7)|spd_rtng(99)|weapon_length(97)|swing_damage(30,cut),imodbits_sword_high,[],[fac_kingdom_3]],
["we_khe_sword_steppe", "Steppe Sabre", [("we_khe_sword_steppe",0),("we_khe_scabbard_steppe", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,422,weight(1.5)|abundance(60)|difficulty(8)|spd_rtng(99)|weapon_length(98)|swing_damage(31,cut),imodbits_sword_high,[],[fac_kingdom_3]],
["we_khe_sword_broad", "Broad Sabre", [("we_khe_sword_broad",0),("we_khe_scabbard_broad", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,543,weight(1.75)|abundance(50)|difficulty(9)|spd_rtng(98)|weapon_length(96)|swing_damage(33,cut),imodbits_sword_high,[],[fac_kingdom_3]],
##Nord - 12
#Minimal - 6
["we_nor_sword_seax", "Seax", [("we_nor_sword_seax",0),("we_nor_scabbard_seax", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,43,weight(0.75)|abundance(100)|difficulty(0)|spd_rtng(108)|weapon_length(40)|swing_damage(24,cut)|thrust_damage(17,pierce),imodbits_sword_high,[],[fac_kingdom_4]],
["we_nor_sword_pict", "Pict Sword", [("we_nor_sword_pict",0),("we_nor_scabbard_pict", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,100,weight(1.5)|abundance(90)|difficulty(0)|spd_rtng(99)|weapon_length(90)|swing_damage(26,cut)|thrust_damage(19,pierce),imodbits_sword_high,[],[fac_kingdom_4]],
["we_nor_sword_angle", "Angle Longsword", [("we_nor_sword_angle",0),("we_nor_scabbard_angle", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,200,weight(1.5)|abundance(80)|difficulty(0)|spd_rtng(99)|weapon_length(95)|swing_damage(27,cut)|thrust_damage(19,pierce),imodbits_sword_high,[],[fac_kingdom_4]],
["we_nor_sword_nordic", "Nordic War Sword", [("we_nor_sword_nordic",0),("we_nor_scabbard_nordic", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,300,weight(1.5)|abundance(70)|difficulty(7)|spd_rtng(99)|weapon_length(95)|swing_damage(28,cut)|thrust_damage(20,pierce),imodbits_sword_high,[],[fac_kingdom_4]],
["we_nor_sword_saxon", "Saxon Sword", [("we_nor_sword_saxon",0),("we_nor_scabbard_saxon", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,400,weight(1.5)|abundance(60)|difficulty(8)|spd_rtng(99)|weapon_length(90)|swing_damage(29,cut)|thrust_damage(20,pierce),imodbits_sword_high,[],[fac_kingdom_4]],
["we_nor_sword_eurodino", "Eurodino Sword", [("we_nor_sword_eurodino",0),("we_nor_scabbard_eurodino", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,500,weight(1.5)|abundance(50)|difficulty(9)|spd_rtng(99)|weapon_length(95)|swing_damage(30,cut)|thrust_damage(21,pierce),imodbits_sword_high,[],[fac_kingdom_4]],
##Rhodok - 14
#Minimal - 6
["we_rho_sword_rondeldagger", "Rondel Dagger", [("we_rho_sword_rondeldagger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,40,weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(106)|weapon_length(47)|swing_damage(12,cut)|thrust_damage(22,pierce),imodbits_sword_high,[],[fac_kingdom_5]],
["we_rho_sword_short", "Rhodok Short Sword", [("we_rho_sword_short",0),("we_rho_scabbard_short", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,111,weight(1.5)|abundance(90)|difficulty(0)|spd_rtng(105)|weapon_length(60)|swing_damage(26,cut)|thrust_damage(21,pierce),imodbits_sword_high,[],[fac_kingdom_5]],
["we_rho_sword_squire", "Squire Sword", [("we_rho_sword_squire",0),("we_rho_scabbard_squire", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,163,weight(1.5)|abundance(80)|difficulty(7)|spd_rtng(100)|weapon_length(95)|swing_damage(29,cut)|thrust_damage(23,pierce),imodbits_sword_high,[],[fac_kingdom_5]],
["we_rho_sword_castellan", "Castellan Sword", [("we_rho_sword_castellan",0),("we_rho_scabbard_castellan", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,414,weight(1.6)|abundance(60)|difficulty(8)|spd_rtng(100)|weapon_length(95)|swing_damage(30,cut)|thrust_damage(23,pierce),imodbits_sword_high,[],[fac_kingdom_5]],
["we_rho_sword_estoc_small", "Small Estoc", [("we_rho_sword_estoc_small",0),("we_rho_scabbard_estoc_small", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,477,weight(1.5)|abundance(60)|difficulty(8)|spd_rtng(97)|weapon_length(100)|swing_damage(32,cut)|thrust_damage(24,pierce),imodbits_sword_high,[],[fac_kingdom_5]],
["we_rho_sword_general", "General Sword", [("we_rho_sword_general",0),("we_rho_scabbard_general", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,493,weight(2)|abundance(50)|difficulty(8)|spd_rtng(99)|weapon_length(100)|swing_damage(32,cut)|thrust_damage(24,pierce),imodbits_sword_high,[],[fac_kingdom_5]],
##Sarranid - 12
#Minimal - 6
["we_sar_sword_khyber", "Khyber Knife", [("we_sar_sword_khyber",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,30,weight(0.75)|abundance(100)|difficulty(0)|spd_rtng(108)|weapon_length(60)|swing_damage(20,cut)|thrust_damage(15,pierce),imodbits_sword,[],[fac_kingdom_6]],
["we_sar_sword_sarranid", "Sarranid Sword", [("we_sar_sword_sarranid",0),("we_sar_scabbard_sarranid", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,108,weight(1.5)|abundance(90)|difficulty(0)|spd_rtng(99)|weapon_length(97)|swing_damage(26,cut)|thrust_damage(19,pierce),imodbits_sword_high,[],[fac_kingdom_6]],
["we_sar_sword_arming", "Sarranid Arming Sword", [("we_sar_sword_arming",0),("we_sar_scabbard_arming", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,218,weight(1.5)|abundance(80)|difficulty(0)|spd_rtng(99)|weapon_length(97)|swing_damage(28,cut)|thrust_damage(19,pierce),imodbits_sword_high,[],[fac_kingdom_6]],
["we_sar_sword_cavalry", "Sarranid Cavalry Sword", [("we_sar_sword_cavalry",0),("we_sar_scabbard_cavalry", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,310,weight(1.5)|abundance(70)|difficulty(7)|spd_rtng(98)|weapon_length(105)|swing_damage(28,cut)|thrust_damage(19,pierce),imodbits_sword_high,[],[fac_kingdom_6]],
["we_sar_sword_scimitar", "Scimitar", [("we_sar_sword_scimitar",0),("we_sar_scabbard_scimitar", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,411,weight(1.5)|abundance(60)|difficulty(8)|spd_rtng(101)|weapon_length(97)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_sword_high,[],[fac_kingdom_6]],
["we_sar_sword_guard", "Sarranid Guard Sword", [("we_sar_sword_guard",0),("we_sar_scabbard_guard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,420,weight(1.5)|abundance(60)|difficulty(8)|spd_rtng(99)|weapon_length(97)|swing_damage(30,cut)|thrust_damage(20,pierce),imodbits_sword_high,[],[fac_kingdom_6]],
##Player Faction - 14
#Minimal - 8
["we_pla_sword_dagger", "Mercenary Dagger", [("we_pla_sword_dagger",0),("we_pla_scabbard_dagger",ixmesh_carry),("we_pla_sword_dagger",imodbits_good),("we_pla_scabbard_dagger",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,37,weight(0.75)|abundance(100)|difficulty(0)|spd_rtng(109)|weapon_length(47)|swing_damage(22,cut)|thrust_damage(19,pierce),imodbits_sword_high,[],[fac_player_faction]],
["we_pla_sword_strange", "Strange Sword", [("we_pla_sword_strange",0),("we_pla_scabbard_strange",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn,679,weight(2.0)|difficulty(9)|spd_rtng(108)|weapon_length(95)|swing_damage(32,cut)|thrust_damage(18,pierce),imodbits_sword,[],[fac_player_faction]],
["we_pla_sword_strange_short", "Strange Short Sword", [("we_pla_sword_strange_short",0),("we_pla_scabbard_strange_short",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn,321,weight(1.25)|difficulty(0)|spd_rtng(108)|weapon_length(65)|swing_damage(25,cut)|thrust_damage(19,pierce),imodbits_sword,[],[fac_player_faction]],
["we_pla_sword_reeve", "Reeve Sword", [("we_pla_sword_reeve",0),("we_pla_scabbard_reeve", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,106,weight(1.7)|abundance(90)|difficulty(0)|spd_rtng(99)|weapon_length(95)|swing_damage(26,cut)|thrust_damage(21,pierce),imodbits_sword_high,[],[fac_player_faction]],
["we_pla_sword_templar", "Templar Sword", [("we_pla_sword_templar",0),("we_pla_scabbard_templar", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,212,weight(1.7)|abundance(80)|difficulty(7)|spd_rtng(100)|weapon_length(95)|swing_damage(28,cut)|thrust_damage(22,pierce),imodbits_sword_high,[],[fac_player_faction]],
["we_pla_sword_gothic", "Gothic Sword", [("we_pla_sword_gothic",0),("we_pla_scabbard_gothic", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,306,weight(1.6)|abundance(70)|difficulty(7)|spd_rtng(101)|weapon_length(80)|swing_damage(29,cut)|thrust_damage(23,pierce),imodbits_sword_high,[],[fac_player_faction]],
["we_pla_sword_ritter", "Ritter Sword", [("we_pla_sword_ritter",0),("we_pla_scabbard_ritter", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,419,weight(1.9)|abundance(60)|difficulty(8)|spd_rtng(99)|weapon_length(95)|swing_damage(30,cut)|thrust_damage(23,pierce),imodbits_sword_high,[],[fac_player_faction]],
["we_pla_sword_hospitaller", "Hospitaller Sword", [("we_pla_sword_hospitaller",0),("we_pla_scabbard_hospitaller", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,458,weight(1.8)|abundance(60)|difficulty(8)|spd_rtng(100)|weapon_length(95)|swing_damage(31,cut)|thrust_damage(24,pierce),imodbits_sword_high,[],[fac_player_faction]],

###Two-handed - 39
##Swadia - 8
#Minimal - 4
["we_swa_sword_crusader", "Crusader Longsword", [("we_swa_sword_crusader",0),("we_swa_scabbard_crusader", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,250,weight(2)|abundance(100)|difficulty(9)|spd_rtng(97)|weapon_length(98)|swing_damage(33,cut)|thrust_damage(31,pierce),imodbits_sword_high,[],[fac_kingdom_1]],
["we_swa_sword_longenglish", "English Longsword", [("we_swa_sword_longenglish",0),("we_swa_scabbard_longenglish", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,415,weight(2)|abundance(90)|difficulty(10)|spd_rtng(99)| weapon_length(103)|swing_damage(37,cut)|thrust_damage(32,pierce),imodbits_sword_high,[],[fac_kingdom_1]],
["we_swa_sword_clamshell_claymore", "Clamshell Claymore", [("we_swa_sword_clamshell_claymore",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,1189,weight(2.75)|abundance(60)|difficulty(13)|spd_rtng(96)|weapon_length(120)|swing_damage(51,cut)|thrust_damage(33,pierce),imodbits_sword_high,[],[fac_kingdom_1]],
["we_swa_sword_twohanded_claymore", "Twohanded Claymore", [("we_swa_sword_twohanded_claymore",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,1261,weight(3)|abundance(60)|difficulty(13)|spd_rtng(94)|weapon_length(130)|swing_damage(52,cut)|thrust_damage(34,pierce),imodbits_sword_high,[],[fac_kingdom_1]],
##Vaegir - 2
#Minimal - 1
["we_vae_sword_cleaverwar", "War Cleaver", [("we_vae_sword_cleaverwar",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,620,weight(2.75)|abundance(80)|difficulty(11)|spd_rtng(93)|weapon_length(120)|swing_damage(45,cut)|thrust_damage(0,cut),imodbits_sword_high,[],[fac_kingdom_2]],
##Khergit - 4
#Minimal - 2
["we_khe_sword_sabre", "Two Handed Sabre", [("we_khe_sword_sabre",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,523,weight(2.75)|abundance(80)|difficulty(11)|spd_rtng(96)|weapon_length(120)|swing_damage(40,cut)|thrust_damage(0,pierce),imodbits_sword_high,[],[fac_kingdom_3]],
["we_khe_sword_sabredark", "Dark Two Handed Sabre", [("we_khe_sword_sabredark",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,604,weight(2.75)|abundance(80)|difficulty(11)|spd_rtng(96)|weapon_length(120)|swing_damage(44,cut)|thrust_damage(0,pierce),imodbits_sword_high,[],[fac_kingdom_3]],
##Nord - 3
#Minimal - 1
["we_nor_sword_danish_great", "Danish Greatsword", [("we_nor_sword_danish_great",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,589,weight(3)|abundance(80)|difficulty(11)|spd_rtng(96)|weapon_length(114)|swing_damage(42,cut)|thrust_damage(33, pierce),imodbits_sword_high,[],[fac_kingdom_4]],
##Rhodok - 8
#Minimal - 4
["we_rho_sword_estoc", "Estoc", [("we_rho_sword_estoc",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip,352,weight(2)|abundance(100)|difficulty(9)|spd_rtng(98)|weapon_length(100)|swing_damage(36,cut)|thrust_damage(26,pierce),imodbits_sword_high,[],[fac_kingdom_5]],
["we_rho_sword_estoc_empire", "Empire Estoc", [("we_rho_sword_estoc_empire",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,636,weight(2.25)|abundance(80)|difficulty(11)|spd_rtng(94)| weapon_length(120)|swing_damage(45,cut)|thrust_damage(29,pierce),imodbits_sword_high,[],[fac_kingdom_5]],
["we_rho_sword_great", "Greatsword", [("we_rho_sword_great",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,677,weight(2.7)|abundance(70)|difficulty(12)|spd_rtng(96)|weapon_length(120)|swing_damage(46,cut)|thrust_damage(31,pierce),imodbits_sword_high,[],[fac_kingdom_5]],
["we_rho_sword_great_long", "Long Greatsword", [("we_rho_sword_great_long",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,766,weight(3)|abundance(70)|difficulty(12)|spd_rtng(95)|weapon_length(130)|swing_damage(48,cut)|thrust_damage(32,pierce),imodbits_sword_high,[],[fac_kingdom_5]],
##Sarranid - 5
#Minimal - 2
["we_sar_sword_scimitarbastard", "Bastard Scimitar", [("we_sar_sword_scimitarbastard",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip,411,weight(1.8)|abundance(90)|difficulty(10)|spd_rtng(96)|weapon_length(100)|swing_damage(38,cut)|thrust_damage(27,pierce),imodbits_sword_high,[],[fac_kingdom_6]],
["we_sar_sword_scimitartwolarge", "Large Two-handed Scimitar", [("we_sar_sword_scimitartwolarge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,598,weight(2.75)|abundance(80)|difficulty(11)|spd_rtng(94)|weapon_length(110)|swing_damage(42,cut)|thrust_damage(29,pierce),imodbits_sword_high,[],[fac_kingdom_6,fac_player_faction]],
##Player Faction - 9
#Minimal - 5
["we_pla_sword_strange_great", "Strange Great Sword", [("we_pla_sword_strange_great",0),("we_pla_scabbard_strange_great",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn,920,weight(3.5)|difficulty(11)|spd_rtng(92)|weapon_length(125)|swing_damage(38,cut)|thrust_damage(0,pierce),imodbits_axe,[],[fac_player_faction]],
["we_pla_sword_grosser_messer", "Grosser Messer", [("we_pla_sword_grosser_messer",0),("we_pla_scabbard_grosser_messer", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,285,weight(2.0)|abundance(100)|difficulty(9)|spd_rtng(98)|weapon_length(93)|swing_damage(35,cut)|thrust_damage(24,pierce),imodbits_sword_high,[],[fac_player_faction]],
["we_pla_sword_zweilander", "Zweilander", [("we_pla_sword_zweilander",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,648,weight(3)|abundance(80)|difficulty(11)|spd_rtng(94)|weapon_length(130)|swing_damage(45,cut)|thrust_damage(30,pierce),imodbits_sword_high,[],[fac_player_faction]],
["we_pla_sword_zweilander_flaming", "Flaming Zweilander", [("we_pla_sword_zweilander_flaming",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,1133,weight(3.4)|abundance(60)|difficulty(13)|spd_rtng(92)|weapon_length(140)|swing_damage(50,cut)|thrust_damage(33,pierce),imodbits_sword_high,[],[fac_player_faction]],
["we_pla_sword_great_four", "Four Handed Greatsword", [("we_pla_sword_great_four",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,1252,weight(3)|abundance(60)|difficulty(13)|spd_rtng(92)|weapon_length(140)|swing_damage(52,cut)|thrust_damage(34,pierce),imodbits_sword_high,[],[fac_player_faction]],

###Ranged Weapons - 86

##Ammunition - 21
#Swadia - 2
#Minimal - 2
["we_swa_arrow_gromite","Gromite Arrows", [("we_swa_arrow_gromite",0),("we_swa_arrow_gromite_flying",ixmesh_flying_ammo),("we_swa_quiver_gromite", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,70,weight(3)|abundance(100)|weapon_length(91)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile,missile_distance_trigger,[fac_kingdom_1]],
["we_swa_arrow_steel","Steel Arrows", [("we_swa_arrow_steel",0),("we_swa_arrow_steel_flying",ixmesh_flying_ammo),("we_swa_quiver_steel", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,150,weight(3)|abundance(60)|weapon_length(91)|thrust_damage(2,pierce)|max_ammo(28),imodbits_missile,missile_distance_trigger,[fac_kingdom_1]],
#Vaegir - 2
#Minimal - 2
["we_vae_arrow_sharp","Sharp Arrows", [("we_vae_arrow_sharp",0),("we_vae_arrow_sharp_flying",ixmesh_flying_ammo),("we_vae_quiver_sharp", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,60,weight(3.5)|abundance(100)|weapon_length(91)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile,missile_distance_trigger,[fac_kingdom_2]],
["we_vae_arrow_imperial","Imperial Arrows", [("we_vae_arrow_imperial",0),("we_vae_arrow_imperial_flying",ixmesh_flying_ammo),("we_vae_quiver_imperial", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,130,weight(3.5)|abundance(60)|weapon_length(91)|thrust_damage(2,pierce)|max_ammo(28),imodbits_missile,missile_distance_trigger,[fac_kingdom_2]],
#Khergit - 7
#Minimal - 3
["we_khe_arrow_khergit","Khergit Arrows", [("we_khe_arrow_khergit",0),("we_khe_arrow_flying",ixmesh_flying_ammo),("we_khe_quiver_khergit", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,70,weight(2.5)|abundance(100)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile,missile_distance_trigger,[fac_kingdom_3]],
["we_khe_arrow_mongol","Mongol Arrows", [("we_khe_arrow_mongol",0),("we_khe_arrow_mongol_flying",ixmesh_flying_ammo),("we_khe_quiver_mongol", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,200,weight(3)|abundance(60)|weapon_length(95)|thrust_damage(2,pierce)|max_ammo(28),imodbits_missile,missile_distance_trigger,[fac_kingdom_3]],
["we_khe_arrow_mongol_piercing","Piercing Mongol Arrows", [("we_khe_arrow_mongol_piercing",0),("we_khe_arrow_mongol_piercing_flying",ixmesh_flying_ammo),("we_khe_quiver_mongol_piercing", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,410,weight(3.5)|abundance(30)|weapon_length(95)|thrust_damage(3,pierce)|max_ammo(26),imodbits_missile,missile_distance_trigger,[fac_kingdom_3]],
#Nord - 2
#Minimal - 2
["we_nor_arrow_bodkin","Bodkin Arrows", [("we_nor_arrow_bodkin",0),("we_nor_arrow_bodkin_flying",ixmesh_flying_ammo),("we_nor_quiver_bodkin", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,60,weight(3)|abundance(100)|weapon_length(91)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile,missile_distance_trigger,[fac_kingdom_4]],
["we_nor_arrow_barbed","Barbed Arrows", [("we_nor_arrow_barbed",0),("we_nor_arrow_barbed_flying",ixmesh_flying_ammo),("we_nor_quiver_barbed", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,160,weight(3)|abundance(60)|weapon_length(95)|thrust_damage(2,pierce)|max_ammo(28),imodbits_missile,missile_distance_trigger,[fac_kingdom_4]],
#Rhodok - 3
#Minimal - 3
["we_rho_bolt","Bolts", [("we_rho_bolt",0),("we_rho_bolt_flying",ixmesh_flying_ammo),("we_rho_bolt_bag", ixmesh_carry),("we_rho_bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical,64,weight(2.25)|abundance(100)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(29),imodbits_missile,missile_distance_trigger,[fac_kingdom_5,fac_player_faction]],
["we_rho_bolt_steel","Steel Bolts", [("we_rho_bolt",0),("we_rho_bolt_flying",ixmesh_flying_ammo),("we_rho_bolt_steel_bag", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical,210,weight(2.5)|abundance(60)|weapon_length(63)|thrust_damage(2,pierce)|max_ammo(27),imodbits_missile,missile_distance_trigger,[fac_kingdom_5,fac_player_faction]],
["we_rho_cartridges","Cartridges", [("we_rho_cartridges",0)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo,0,41,weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile,missile_distance_trigger],
#Sarranid - 3
#Minimal - 2
["we_sar_arrow_sarranid","Sarranid Arrows", [("we_sar_arrow_sarranid",0),("we_sar_arrow_sarranid_flying",ixmesh_flying_ammo),("we_sar_quiver_sarranid", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,75,weight(2.5)|abundance(100)|weapon_length(91)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile,missile_distance_trigger,[fac_kingdom_6]],
["we_sar_arrow_desert","Desert Arrows", [("we_sar_arrow_desert",0),("we_sar_arrow_desert_flying",ixmesh_flying_ammo),("we_sar_quiver_desert", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,180,weight(2.5)|abundance(50)|weapon_length(91)|thrust_damage(2,pierce)|max_ammo(28),imodbits_missile,missile_distance_trigger,[fac_kingdom_6]],
#Player Faction - 2
#Minimal - 2
["we_pla_arrow","Arrows", [("we_pla_arrow",0),("we_pla_arrow_flying",ixmesh_flying_ammo),("we_pla_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back,72,weight(3)|abundance(100)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile,missile_distance_trigger,[fac_player_faction]],
["we_pla_arrow_amazon","Amazon Arrows", [("we_pla_arrow_amazon",0),("we_pla_arrow_amazon_flying",ixmesh_flying_ammo),("we_pla_quiver_amazon", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right,190,weight(3)|abundance(60)|weapon_length(91)|thrust_damage(2,pierce)|max_ammo(28),imodbits_missile,missile_distance_trigger,[fac_player_faction]],

##Bows & Crossbows - 39
#Swadia - 6
#Minimal - 3
["we_swa_bow_practice", "Swadian Practice Bow", [("we_swa_bow_practice",0),("we_swa_bow_practice_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,49,weight(1)|abundance(120)|difficulty(0)|spd_rtng(93)|shoot_speed(54)|thrust_damage(18,cut)|accuracy(90),imodbits_bow,[],[fac_kingdom_1]],
["we_swa_bow_straight", "Straight Bow", [("we_swa_bow_straight",0),("we_swa_bow_straight_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,208,weight(1)|abundance(80)|difficulty(3)|spd_rtng(97)|shoot_speed(56)|thrust_damage(26,cut)|accuracy(90),imodbits_bow,[],[fac_kingdom_1]],
["we_swa_bow_long", "Longbow", [("we_swa_bow_long",0),("we_swa_bow_long_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back,719,weight(1.75)|abundance(60)|difficulty(5)|spd_rtng(81)|shoot_speed(58)|thrust_damage(33,pierce)|accuracy(90),imodbits_bow,[],[fac_kingdom_1]],
#Vaegir - 6
#Minimal - 3
["we_vae_bow_hunting", "Imperial Hunting Bow", [("we_vae_bow_hunting",0),("we_vae_bow_hunting_carry", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,233,weight(1.25)|abundance(90)|difficulty(2)|spd_rtng(96)|shoot_speed(56)|thrust_damage(27,cut)|accuracy(90),imodbits_bow,[],[fac_kingdom_2]],
["we_vae_bow_war", "War Bow", [("we_vae_bow_war",0),("we_vae_bow_war_carry", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,585,weight(1.25)|abundance(70)|difficulty(4)|spd_rtng(77)|shoot_speed(58)|thrust_damage(35,pierce)|accuracy(90),imodbit_cracked|imodbit_bent|imodbit_masterwork,[],[fac_kingdom_2]],
["we_vae_bow_imperial", "Imperial War Bow", [("we_vae_bow_imperial",0),("we_vae_bow_imperial_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,814,weight(1.25)|abundance(60)|difficulty(5)|spd_rtng(79)|shoot_speed(59)|thrust_damage(40,pierce)|accuracy(90),imodbit_cracked|imodbit_bent|imodbit_masterwork,[],[fac_kingdom_2]],
#Khergit - 10
#Minimal - 3
["we_khe_bow_practice", "Khergit Practice Bow", [("we_khe_bow_practice",0),("we_khe_bow_practice_case", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,50,weight(1.25)|abundance(120)|difficulty(0)|spd_rtng(93)|shoot_speed(55)|thrust_damage(18,cut)|accuracy(90),imodbits_bow,[],[fac_kingdom_3,fac_player_faction]],
["we_khe_bow_red", "Red Khergit Bow", [("we_khe_bow_red",0),("we_khe_case_red", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,250,weight(1.25)|abundance(80)|difficulty(2)|spd_rtng(93)|shoot_speed(56)|thrust_damage(25,cut)|accuracy(90),imodbits_bow,[],[fac_kingdom_3,fac_player_faction]],
["we_khe_bow_strong", "Strong Khergit Bow", [("we_khe_bow_strong",0),("we_khe_case_strong", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,750,weight(1.75)|abundance(60)|difficulty(4)|spd_rtng(93)|shoot_speed(57)|thrust_damage(32,pierce)|accuracy(90),imodbits_crossbow,[],[fac_kingdom_3]],
#Nord - 3
#Minimal - 2
["we_nor_bow_hunting", "Hunting Bow", [("we_nor_bow_hunting",0),("we_nor_bow_hunting_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back,120,weight(1)|abundance(90)|difficulty(0)|spd_rtng(120)|shoot_speed(52)|thrust_damage(19,cut)|accuracy(90),imodbits_bow,[],[fac_kingdom_4]],
["we_nor_bow", "Nord Bow", [("we_nor_bow",0),("we_nor_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back,220,weight(1)|abundance(80)|difficulty(1)|spd_rtng(120)|shoot_speed(52)|thrust_damage(23,pierce)|accuracy(90),imodbits_bow,[],[fac_kingdom_4]],
#Rhodok - 6
#Minimal - 3
["we_rho_crossbow_hunting", "Hunting Crossbow", [("we_rho_crossbow_hunting",0)], itp_type_crossbow|itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_crossbow|itcf_carry_crossbow_back,22,weight(2.25)|abundance(120)|difficulty(0)|spd_rtng(60)|shoot_speed(50)|thrust_damage(42,pierce)|max_ammo(1)|accuracy(90),imodbits_crossbow,[],[fac_kingdom_5,fac_player_faction]],
["we_rho_crossbow", "Crossbow", [("we_rho_crossbow",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,182,weight(3)|abundance(90)|difficulty(10)|spd_rtng(45)|shoot_speed(66)|thrust_damage(64,pierce)|max_ammo(1)|accuracy(90),imodbits_crossbow,[],[fac_kingdom_5,fac_player_faction]],
["we_rho_crossbow_siege", "Siege Crossbow", [("we_rho_crossbow_siege",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,683,weight(3.75)|abundance(70)|difficulty(14)|spd_rtng(35)|shoot_speed(70)|thrust_damage(87,pierce)|max_ammo(1)|accuracy(90),imodbits_crossbow,[],[fac_kingdom_5,fac_player_faction]],
#Sarranid - 6
#Minimal - 3
["we_sar_bow_practice", "Sarranid Practice Bow", [("we_sar_bow_practice",0),("we_sar_bow_practice_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,58,weight(1.25)|abundance(120)|difficulty(0)|spd_rtng(94)|shoot_speed(54)|thrust_damage(19,cut)|accuracy(90),imodbits_bow,[],[fac_kingdom_6]],
["we_sar_bow_leopard", "Leopard Bow", [("we_sar_bow_leopard",0),("we_sar_bow_leopard_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,233,weight(1.25)|abundance(90)|difficulty(2)|spd_rtng(96)|shoot_speed(56)|thrust_damage(27,cut)|accuracy(90),imodbits_bow,[],[fac_kingdom_6]],
["we_sar_bow_recurved", "Sarranid Recurved Bow", [("we_sar_bow_recurved",0),("we_sar_bow_recurved_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,421,weight(1.25)|abundance(80)|difficulty(3)|spd_rtng(75)|shoot_speed(57)|thrust_damage(30,pierce)|accuracy(90),imodbit_cracked|imodbit_bent|imodbit_masterwork,[],[fac_kingdom_6]],
#Player Faction - 2
#Minimal - 2
["we_pla_bow_amazon", "Amazon Bow", [("we_pla_bow_amazon",0),("we_pla_bow_amazon_case",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,750,weight(1.75)|abundance(60)|difficulty(4)|spd_rtng(93)|shoot_speed(57)|thrust_damage(32,pierce)|accuracy(90),imodbits_bow,[],[fac_player_faction]],
["we_pla_pistol_arquebus", "Arquebus",[("we_pla_pistol_arquebus",0)],itp_type_musket|itp_cant_reload_on_horseback|itp_primary|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,230,weight(4)|abundance(10)|difficulty(0)|spd_rtng(42)|shoot_speed(105)|thrust_damage(54,pierce)|max_ammo(1)|accuracy(80),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,0),(position_move_y, pos1,100),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])],[fac_player_faction]],
["we_pla_pistol_blunderbus", "Blunderbus",[("we_pla_pistol_blunderbus",0)],itp_type_musket|itp_cant_reload_on_horseback|itp_primary|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,450,weight(4.5)|abundance(10)|difficulty(0)|spd_rtng(42)|shoot_speed(98)|thrust_damage(63,pierce)|max_ammo(1)|accuracy(85),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,0),(position_move_y, pos1,72),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])],[fac_player_faction]],
["we_pla_pistol_matchlock", "Matchlock Rifle",[("we_pla_pistol_matchlock",0)],itp_type_musket|itp_cant_reload_on_horseback|itp_primary|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,680,weight(5)|abundance(10)|difficulty(0)|spd_rtng(40)|shoot_speed(114)|thrust_damage(72,pierce)|max_ammo(1)|accuracy(90),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,0),(position_move_y, pos1,107),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])],[fac_player_faction]],
["we_pla_pistol_flintlock_rifle", "Flintlock Rifle",[("we_pla_pistol_flintlock_rifle",0)],itp_type_musket|itp_cant_reload_on_horseback|itp_primary|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,1230,weight(5.5)|abundance(10)|difficulty(0)|spd_rtng(44)|shoot_speed(128)|thrust_damage(81,pierce)|max_ammo(1)|accuracy(95),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,0),(position_move_y, pos1,139),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])],[fac_player_faction]],
["we_pla_pistol_flintlock", "Flintlock Pistol", [("we_pla_pistol_flintlock",0),("we_pla_pistol_flintlock_good",imodbits_good)], itp_type_pistol|itp_primary|itp_secondary ,itcf_shoot_pistol|itcf_reload_pistol,230,weight(1.5)|abundance(10)|difficulty(0)|spd_rtng(64)|shoot_speed(89)|thrust_damage(50,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst,"psys_pistol_smoke", pos1, 15)])],[fac_player_faction]],

##Throwing weapons - 26
#Swadia - 5
#Minimal - 3
["we_swa_throw_stone", "Swadian Stones", [("we_swa_throw_stone",0)], itp_type_thrown|itp_primary,itcf_throw_stone,1,weight(4)|difficulty(0)|spd_rtng(97)|shoot_speed(30)|thrust_damage(11,blunt)|max_ammo(18)|weapon_length(8)|accuracy(80),imodbit_large_bag,[],[fac_kingdom_1]],
["we_swa_throw_darts", "Darts", [("we_swa_throw_darts",0),("we_swa_throw_darts_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 155 , weight(5)|difficulty(1)|abundance(100)|spd_rtng(95) | shoot_speed(28) | thrust_damage(22,pierce)|max_ammo(12)|weapon_length(32),imodbits_thrown,[],[fac_kingdom_1]],
["we_swa_throw_darts_war", "War Darts", [("we_swa_throw_darts_war",0),("we_swa_throw_darts_war_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 285 , weight(5)|difficulty(2)|abundance(80)|spd_rtng(93) | shoot_speed(27) | thrust_damage(25,pierce)|max_ammo(12)|weapon_length(45),imodbits_thrown,[],[fac_kingdom_1]],
#Vaegir - 5
#Minimal - 3
["we_vae_throw_snow", "Snow Balls", [("we_vae_throw_snow",0)], itp_type_thrown|itp_primary,itcf_throw_stone,1,weight(1)|difficulty(0)|spd_rtng(97)|shoot_speed(25)|thrust_damage(9,blunt)|max_ammo(18)|weapon_length(8)|accuracy(80),imodbit_large_bag,[],[fac_kingdom_2]],
["we_vae_sword_throw_knives","Throwing Knives",[("we_vae_sword_throw_knives",0)],itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife,76,weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(121)|difficulty(0)|shoot_speed(25)|thrust_damage(19,cut)|max_ammo(20)|weapon_length(0),imodbits_thrown,[],[fac_kingdom_2]],
["we_vae_sword_throw_daggers","Throwing Daggers",[("we_vae_sword_throw_daggers",0)],itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife,193,weight(3.5)|abundance(80)|difficulty(0)|spd_rtng(110)|difficulty(1)|shoot_speed(24)|thrust_damage(25,cut)|max_ammo(20)|weapon_length(0),imodbits_thrown,[],[fac_kingdom_2]],
#Khergit - 1
#Minimal - 1
["we_khe_throw_stone", "Khergit Stones", [("we_khe_throw_stone",0)], itp_type_thrown|itp_primary,itcf_throw_stone,1,weight(4)|difficulty(0)|spd_rtng(97)|shoot_speed(30)|thrust_damage(11,blunt)|max_ammo(18)|weapon_length(8)|accuracy(80),imodbit_large_bag,[],[fac_kingdom_1]],
#Nord - 10
#Minimal - 6
["we_nor_axe_throw_light", "Light Throwing Axes", [("we_nor_axe_throw_light",0)], itp_type_thrown|itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,100,weight(5)|abundance(100)|difficulty(1)|spd_rtng(99)|shoot_speed(18)|thrust_damage(31,cut)|max_ammo(10)|weapon_length(53),imodbits_thrown_minus_heavy,[],[fac_kingdom_4]],
	["we_nor_axe_throw_light_melee", "Light Throwing Axe", [("we_nor_axe_throw_light",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield,itc_scimitar,100,weight(1)|abundance(100)|difficulty(1)|spd_rtng(99)|weapon_length(53)|swing_damage(23,cut),imodbits_thrown_minus_heavy,[],[fac_kingdom_4]],
["we_nor_axe_throw_vendelox", "Vendelox Axes", [("we_nor_axe_throw_vendelox",0)], itp_type_thrown|itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,480,weight(5)|abundance(80)|difficulty(3)|spd_rtng(97)|shoot_speed(18)|thrust_damage(39,cut)|max_ammo(10)|weapon_length(50),imodbits_thrown_minus_heavy,[],[fac_kingdom_4]],
	["we_nor_axe_throw_vendelox_melee", "Vendelox Axe", [("we_nor_axe_throw_vendelox",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,480,weight(1)|abundance(80)|difficulty(3)|spd_rtng(97)|swing_damage(29,cut)|weapon_length(50),imodbits_thrown_minus_heavy,[],[fac_kingdom_4]],
["we_nor_axe_throw_mammen", "Mammen Axes", [("we_nor_axe_throw_mammen",0)], itp_type_thrown|itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,1570,weight(5)|abundance(50)|difficulty(5)|spd_rtng(95)|shoot_speed(18)|thrust_damage(47,cut)|max_ammo(10)|weapon_length(50),imodbits_thrown_minus_heavy,[],[fac_kingdom_4]],
	["we_nor_axe_throw_mammen_melee", "Mammen Axe", [("we_nor_axe_throw_mammen",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,1570,weight(1)|difficulty(5)|abundance(50)|spd_rtng(95)|swing_damage(35,cut)|weapon_length(50),imodbits_thrown_minus_heavy,[],[fac_kingdom_4]],
["we_nor_spear_kastspjottmidtaggir", "Kastspjott Midtaggir", [("we_nor_spear_kastspjottmidtaggir",0),("we_nor_quiver_kastspjottmidtaggir", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,200,weight(5)|abundance(100)|difficulty(1)|spd_rtng(95)|shoot_speed(25)|thrust_damage(30,pierce)|max_ammo(10)|weapon_length(100),imodbits_thrown,[],[fac_kingdom_4]],
	["we_nor_spear_kastspjottmidtaggir_melee", "Kastspjott Midtaggir", [("we_nor_spear_kastspjottmidtaggir",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,200,weight(1)|abundance(100)|difficulty(0)|spd_rtng(95)|weapon_length(100)|swing_damage(10,cut)|thrust_damage(12,pierce),imodbits_polearm,[],[fac_kingdom_4]],
["we_nor_spear_atgeirr", "Kastspjott Midtaggir", [("we_nor_spear_atgeirr",0),("we_nor_quiver_atgeirr", ixmesh_carry)], itp_type_thrown|itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,1000,weight(5)|abundance(40)|difficulty(4)|spd_rtng(99)|shoot_speed(25)|thrust_damage(51,pierce)|max_ammo(10)|weapon_length(90),imodbits_thrown,[],[fac_kingdom_4]],
	["we_nor_spear_atgeirr_melee", "Atgeirr", [("we_nor_spear_atgeirr",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,1000,weight(1)|abundance(40)|difficulty(3)|spd_rtng(99)|weapon_length(90)|swing_damage(21,cut)|thrust_damage(27,pierce),imodbits_polearm,[],[fac_kingdom_4]],
["we_nor_throw_stone", "Nord Stones", [("we_nor_throw_stone",0)], itp_type_thrown|itp_primary,itcf_throw_stone,1,weight(4)|difficulty(0)|spd_rtng(97)|shoot_speed(30)|thrust_damage(11,blunt)|max_ammo(18)|weapon_length(8)|accuracy(80),imodbit_large_bag,[],[fac_kingdom_1]],
#Rhodok - 1
#Minimal - 1
["we_rho_throw_stone", "Rhodok Stones", [("we_rho_throw_stone",0)], itp_type_thrown|itp_primary,itcf_throw_stone,1,weight(4)|difficulty(0)|spd_rtng(97)|shoot_speed(30)|thrust_damage(11,blunt)|max_ammo(18)|weapon_length(8)|accuracy(80),imodbit_large_bag,[],[fac_kingdom_1]],
#Sarranid - 4
#Minimal - 4
["we_sar_spear_javelin", "Javelins", [("we_sar_spear_javelin",0),("we_sar_spear_javelin_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 300, weight(5)|difficulty(1)|spd_rtng(91)|shoot_speed(25)|thrust_damage(34 ,  pierce)|max_ammo(10)|weapon_length(75),imodbits_thrown,[],[fac_kingdom_6]],
	["we_sar_spear_javelin_melee", "Javelin", [("we_sar_spear_javelin",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,300,weight(1)|difficulty(0)|spd_rtng(95)|swing_damage(12,cut)|thrust_damage(14,pierce)|weapon_length(75),imodbits_polearm,[],[fac_kingdom_6]],
["we_sar_spear_throwing_spears", "Throwing Spears", [("we_sar_spear_throwing_spears",0),("we_sar_spear_throwing_spears_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,525,weight(4)|difficulty(2)|spd_rtng(87)|shoot_speed(22)|thrust_damage(41,pierce)|max_ammo(10)|weapon_length(65),imodbits_thrown,[],[fac_kingdom_6]],
	["we_sar_spear_throwing_spear_melee", "Throwing Spear", [("we_sar_spear_throwing_spears",0),("we_sar_spear_throwing_spears_bag", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry,itc_staff,525,weight(1)|difficulty(1)|spd_rtng(91)|swing_damage(16,cut)|thrust_damage(20, pierce)|weapon_length(75),imodbits_thrown,[],[fac_kingdom_6]],
["we_sar_spear_jarid", "Jarids", [("we_sar_spear_jarid",0),("we_sar_spear_jarid_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,860,weight(4)|difficulty(3)|spd_rtng(89)|shoot_speed(24)|thrust_damage(48,pierce)|max_ammo(10)|weapon_length(65),imodbits_thrown,[],[fac_kingdom_6]],
	["we_sar_spear_jarid_melee", "Jarid", [("we_sar_spear_jarid",0),("we_sar_spear_jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_primary|itp_wooden_parry,itc_staff,860,weight(1)|difficulty(2)|spd_rtng(93)|swing_damage(18,cut)| thrust_damage(23,pierce)|weapon_length(65),imodbits_thrown,[],[fac_kingdom_6]],
["we_sar_throw_stone", "Sarranid Stones", [("we_sar_throw_stone",0)], itp_type_thrown|itp_primary,itcf_throw_stone,1,weight(4)|difficulty(0)|spd_rtng(97)|shoot_speed(30)|thrust_damage(11,blunt)|max_ammo(18)|weapon_length(8)|accuracy(80),imodbit_large_bag,[],[fac_kingdom_1]],
#Player Faction - 0
#Minimal - 0

####

#### Armors

###Armors - 324
##Swadia - 46
#Minimal - 11
["ar_swa_ban_scale_a", "Blue Scale Armor", [("ar_swa_ban_scale_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,50,weight(9)|abundance(10)|head_armor(0)|body_armor(18)|leg_armor(6)|difficulty(8),imodbits_armor,[],[fac_kingdom_1]],
["ar_swa_dip_coatplate_a", "Red Diplomatic Coat of Plates", [("ar_swa_dip_coatplate_a",0)], itp_unique|itp_type_body_armor|itp_covers_legs,0,2754,weight(20)|abundance(10)|head_armor(0)|body_armor(51)|leg_armor(16)|difficulty(0),imodbits_plate,[],[fac_kingdom_1]],
["ar_swa_t2_gambeson_a", "Red Gambeson", [("ar_swa_t2_gambeson_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,30,weight(8)|abundance(90)|head_armor(0)|body_armor(15)|leg_armor(4)|difficulty(7),imodbits_cloth,[],[fac_kingdom_1]],
["ar_swa_t3_hauberk_a", "Mail Hauberk", [("ar_swa_t3_hauberk_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,84,weight(12)|abundance(80)|head_armor(0)|body_armor(24)|leg_armor(7)|difficulty(8),imodbits_armor,[],[fac_kingdom_1]],
["ar_swa_t4_captain_a", "Swadian Yellow Surcoat", [("ar_swa_t4_captain_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,302, weight(14)|abundance(70)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_1]],
["ar_swa_t4_tabardmail_a", "Red Tabard over Mail", [("ar_swa_t4_tabardmail_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,254, weight(14)|abundance(70)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_1]],
["ar_swa_t5_mailsurcoat_a", "Mail with Red Surcoat", [("ar_swa_t5_mailsurcoat_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,810,weight(18)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(13)|difficulty(10),imodbits_armor,[],[fac_kingdom_1]],
["ar_swa_t6_coatplate_b", "Black Coat of Plates", [("ar_swa_t6_coatplate_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,2754,weight(20)|abundance(50)|head_armor(0)|body_armor(51)|leg_armor(16)|difficulty(12),imodbits_plate,[],[fac_kingdom_1]],
["ar_swa_t7_fullplate_a", "Full Plate Armor", [("ar_swa_t7_fullplate_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,7290,weight(24)|abundance(40)|head_armor(0)|body_armor(57)|leg_armor(17)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_1]],
["ar_swa_t7_fullplate_b", "Orange Full Plate Armor", [("ar_swa_t7_fullplate_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,7290,weight(24)|abundance(40)|head_armor(0)|body_armor(57)|leg_armor(17)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_1]],
["ar_swa_t7_fullplate_c", "Heavy Full Plate Armor", [("ar_swa_t7_fullplate_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,7953,weight(24)|abundance(40)|head_armor(0)|body_armor(58)|leg_armor(17)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_1]],
##Vaegir - 45
#Minimal - 10
["ar_vae_ban_tribal_a", "Tribal Scale Armor", [("ar_vae_ban_tribal_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,95,weight(12)|abundance(10)|head_armor(0)|body_armor(21)|leg_armor(9)|difficulty(8),imodbits_armor,[],[fac_kingdom_2]],
["ar_vae_t2_leather_a", "Green Leather Armor", [("ar_vae_t2_leather_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,34,weight(8)|abundance(90)|head_armor(0)|body_armor(17)|leg_armor(4)|difficulty(7),imodbits_cloth,[],[fac_kingdom_2]],
["ar_vae_t3_padded_a", "Blue Padded Leather", [("ar_vae_t3_padded_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,78,weight(11)|abundance(80)|head_armor(0)|body_armor(23)|leg_armor(7)|difficulty(8),imodbits_armor,[],[fac_kingdom_2]],
["ar_vae_t4_jerkin_a", "Leather Jerkin", [("ar_vae_t4_jerkin_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,202, weight(12)|abundance(70)|head_armor(0)|body_armor(31)|leg_armor(10)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_2]],
["ar_vae_t4_jerkin_b", "Red Leather Jerkin", [("ar_vae_t4_jerkin_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,202, weight(12)|abundance(70)|head_armor(0)|body_armor(31)|leg_armor(10)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_2]],
["ar_vae_t5_studded_a", "Green Plated Leather Armor", [("ar_vae_t5_studded_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,748,weight(17)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(11)|difficulty(10),imodbits_armor,[],[fac_kingdom_2]],
["ar_vae_t6_cuirbouilli_a", "Red Cuir Bouilli", [("ar_vae_t6_cuirbouilli_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,3078,weight(22)|abundance(50)|head_armor(0)|body_armor(53)|leg_armor(16)|difficulty(12),imodbits_plate,[],[fac_kingdom_2]],
["ar_vae_t7_elite_a", "Vaegir Yellow Elite Armor", [("ar_vae_t7_elite_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,6627,weight(23)|abundance(40)|head_armor(0)|body_armor(56)|leg_armor(17)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_2]],
["ar_vae_t7_elite_b", "Vaegir Green Elite Armor", [("ar_vae_t7_elite_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,5964,weight(22)|abundance(40)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_2]],
["ar_vae_t7_elite_c", "Vaegir Red Elite Armor", [("ar_vae_t7_elite_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,6627,weight(23)|abundance(40)|head_armor(0)|body_armor(56)|leg_armor(17)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_2]],
##Khergit - 45
#Minimal - 10
["ar_khe_ban_robe_a", "Khergit Black Robe", [("ar_khe_ban_robe_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,102,weight(11)|abundance(10)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(8),imodbits_armor,[],[fac_kingdom_3]],
["ar_khe_t2_armor_a", "Khergit Red Armor", [("ar_khe_t2_armor_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,32,weight(8)|abundance(90)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(7),imodbits_cloth,[],[fac_kingdom_3]],
["ar_khe_t3_steppe_a", "Green Steppe Armor", [("ar_khe_t3_steppe_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,66,weight(10)|abundance(80)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(8),imodbits_armor,[],[fac_kingdom_3]],
["ar_khe_t4_lamellar_a", "Khergit Brown Lamellar Armor", [("ar_khe_t4_lamellar_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,294, weight(13)|abundance(70)|head_armor(0)|body_armor(37)|leg_armor(7)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_3]],
["ar_khe_t4_lamellar_b", "Khergit Green Lamellar Armor", [("ar_khe_t4_lamellar_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,294, weight(13)|abundance(70)|head_armor(0)|body_armor(37)|leg_armor(7)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_3]],
["ar_khe_t5_guard_a", "Khergit Blue Guard Armor", [("ar_khe_t5_guard_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,996,weight(19)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(15)|difficulty(10),imodbits_armor,[],[fac_kingdom_3]],
["ar_khe_t6_tunic_a", "Khergit Red Tunic Armor", [("ar_khe_t6_tunic_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,2268,weight(20)|abundance(50)|head_armor(0)|body_armor(50)|leg_armor(14)|difficulty(12),imodbits_plate,[],[fac_kingdom_3]],
["ar_khe_t7_mongol_a", "Khergit Khan Elite Armor", [("ar_khe_t7_mongol_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,5301,weight(22)|abundance(40)|head_armor(0)|body_armor(55)|leg_armor(16)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_3]],
["ar_khe_t7_mongol_b", "Khergit Heavy Elite Armor", [("ar_khe_t7_mongol_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,5301,weight(22)|abundance(40)|head_armor(0)|body_armor(55)|leg_armor(16)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_3]],
["ar_khe_t7_mongol_c", "Khergit Lamellar Elite Armor", [("ar_khe_t7_mongol_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,4638,weight(21)|abundance(40)|head_armor(0)|body_armor(55)|leg_armor(15)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_3]],
##Nord - 45
#Minimal - 10
["ar_nor_ban_raider_a", "Blue Raider Hauberk", [("ar_nor_ban_raider_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,135,weight(15)|abundance(10)|head_armor(0)|body_armor(30)|leg_armor(11)|difficulty(8),imodbits_armor,[],[fac_kingdom_4]],
["ar_nor_t2_vikinglamellar_a", "Blue Viking Lamellar Armor", [("ar_nor_t2_vikinglamellar_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,36,weight(9)|abundance(90)|head_armor(0)|body_armor(18)|leg_armor(4)|difficulty(7),imodbits_armor,[],[fac_kingdom_4]],
["ar_nor_t3_furcoat_a", "Green Fur Coat of Armor", [("ar_nor_t3_furcoat_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,60,weight(10)|abundance(80)|head_armor(0)|body_armor(21)|leg_armor(6)|difficulty(8),imodbits_armor,[],[fac_kingdom_4]],
["ar_nor_t4_lightarmor_a", "Blue Nordic Light Armor", [("ar_nor_t4_lightarmor_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,222, weight(12)|abundance(70)|head_armor(0)|body_armor(33)|leg_armor(9)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_4]],
["ar_nor_t4_lightarmor_b", "Green Nordic Light Armor", [("ar_nor_t4_lightarmor_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,222, weight(12)|abundance(70)|head_armor(0)|body_armor(33)|leg_armor(9)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_4]],
["ar_nor_t5_byrnie_a", "Red Nordic Byrnie", [("ar_nor_t5_byrnie_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,655,weight(16)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(11)|difficulty(10),imodbits_armor,[],[fac_kingdom_4]],
["ar_nor_t6_mailshirt_a", "White Raven Nordic Mail Shirt", [("ar_nor_t6_mailshirt_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,2106,weight(20)|abundance(50)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(12),imodbits_plate,[],[fac_kingdom_4]],
["ar_nor_t7_vikingbyrnie_a", "Red Brown Viking Byrnie", [("ar_nor_t7_vikingbyrnie_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,3975,weight(21)|abundance(40)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_4]],
["ar_nor_t7_vikingbyrnie_b", "Blue White Viking Byrnie", [("ar_nor_t7_vikingbyrnie_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,3975,weight(21)|abundance(40)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_4]],
["ar_nor_t7_vikingbyrnie_c", "Blue Brown Viking Byrnie", [("ar_nor_t7_vikingbyrnie_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,3975,weight(21)|abundance(40)|head_armor(0)|body_armor(55)|leg_armor(14)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_4]],
##Rhodok - 45
#Minimal - 10
["ar_rho_ban_highlander_a","Brown Highlander Costume",[("ar_rho_ban_highlander_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,45,weight(8)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(6)|difficulty(7),imodbits_cloth,[],[fac_kingdom_5]],
["ar_rho_t2_ragged_a", "Leather Peasant Outfit", [("ar_rho_t2_ragged_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,40,weight(8)|abundance(90)|head_armor(0)|body_armor(18)|leg_armor(6)|difficulty(7),imodbits_cloth,[],[fac_kingdom_5]],
["ar_rho_t3_aketon_a", "Padded Leather Peasant Outfit", [("ar_rho_t3_aketon_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,84,weight(11)|abundance(80)|head_armor(0)|body_armor(23)|leg_armor(8)|difficulty(8),imodbits_armor,[],[fac_kingdom_5]],
["ar_rho_t4_mailshirt_a", "Yellow Peasant Mail Shirt", [("ar_rho_t4_mailshirt_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,270, weight(14)|abundance(70)|head_armor(0)|body_armor(35)|leg_armor(10)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_5]],
["ar_rho_t4_highlander_a", "Brown Highlander Armor", [("ar_rho_t4_highlander_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,222, weight(12)|abundance(70)|head_armor(0)|body_armor(33)|leg_armor(9)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_5]],
["ar_rho_t5_brigandine_a", "Red Brigandine", [("ar_rho_t5_brigandine_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,934,weight(19)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(13)|difficulty(10),imodbits_armor,[],[fac_kingdom_5]],
["ar_rho_t6_corrazina_a", "Green Corrazina", [("ar_rho_t6_corrazina_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,2592,weight(21)|abundance(50)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(12),imodbits_plate,[],[fac_kingdom_5]],
["ar_rho_t7_bnw_a", "Slashed Black and White Armour", [("ar_rho_t7_bnw_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,5301,weight(24)|abundance(40)|head_armor(0)|body_armor(55)|leg_armor(16)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_5]],
["ar_rho_t7_gothic_a", "Gothic Yellow Plate Armor", [("ar_rho_t7_gothic_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,6627,weight(23)|abundance(40)|head_armor(0)|body_armor(57)|leg_armor(16)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_5]],
["ar_rho_t7_milan_a", "Milanese Yellow Plate Armor", [("ar_rho_t7_milan_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,7290,weight(24)|abundance(40)|head_armor(0)|body_armor(57)|leg_armor(17)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_5]],
##Sarranid - 55
#Minimal - 15
["ar_sar_ban_skirmisher_a", "Brown Skirmisher Armor", [("ar_sar_ban_skirmisher_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,105,weight(11)|abundance(10)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(8),imodbits_armor,[],[fac_kingdom_6]],
["ar_sar_sla_t2_a", "Padded Leather Slaver Armor", [("ar_sar_sla_t2_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,59,weight(13)|abundance(10)|head_armor(0)|body_armor(26)|leg_armor(8)|difficulty(7),imodbits_cloth,[],[fac_kingdom_6]],
["ar_sar_sla_t3_a", "Leather Plated Slaver Armor", [("ar_sar_sla_t3_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,135,weight(13)|abundance(10)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(8),imodbits_armor,[],[fac_kingdom_6]],
["ar_sar_sla_t4_a", "Yellow Slaver Horn Armor", [("ar_sar_sla_t4_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,405,weight(16)|abundance(10)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(9),imodbits_plate,[],[fac_kingdom_6]],
["ar_sar_sla_t5_a", "Green Slaver Vij Armor", [("ar_sar_sla_t5_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,1337,weight(20)|abundance(10)|head_armor(0)|body_armor(51)|leg_armor(18)|difficulty(10),imodbits_plate,[],[fac_kingdom_6]],
["ar_sar_sla_t6_a", "Dark Slaver Maratha Mail", [("ar_sar_sla_t6_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,3645,weight(22)|abundance(10)|head_armor(0)|body_armor(55)|leg_armor(18)|difficulty(12),imodbits_plate,[],[fac_kingdom_6]],

["ar_sar_t2_quilted_a", "Light Green Quilted Vest", [("ar_sar_t2_quilted_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,36,weight(9)|abundance(90)|head_armor(0)|body_armor(17)|leg_armor(5)|difficulty(7),imodbits_cloth,[],[fac_kingdom_6]],
["ar_sar_t3_leather_a", "Yellow Sarranid Leather Armor", [("ar_sar_t3_leather_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,74,weight(10)|abundance(80)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(8),imodbits_armor,[],[fac_kingdom_6]],
["ar_sar_t4_cavrobe_a", "Yellow Cavalry Robe", [("ar_sar_t4_cavrobe_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,286, weight(14)|abundance(70)|head_armor(0)|body_armor(35)|leg_armor(11)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_6]],
["ar_sar_t4_chihal_a", "Patterned Chihal Robe", [("ar_sar_t4_chihal_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,275, weight(13)|abundance(70)|head_armor(0)|body_armor(36)|leg_armor(9)|difficulty(9) ,imodbits_armor,[],[fac_kingdom_6]],
["ar_sar_t5_mailshirt_a", "Orange Sarranid Mail Shirt", [("ar_sar_t5_mailshirt_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,838,weight(17)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(10),imodbits_armor,[],[fac_kingdom_6]],
["ar_sar_t6_chaintab_a", "Green Sarranid Chain Armor", [("ar_sar_t6_chaintab_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,2592,weight(20)|abundance(50)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(12),imodbits_plate,[],[fac_kingdom_6]],
["ar_sar_t7_fullplate_a", "Metal Sarranid Full Plate", [("ar_sar_t7_fullplate_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,5301,weight(22)|abundance(40)|head_armor(0)|body_armor(55)|leg_armor(16)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_6]],
["ar_sar_t7_fullplate_b", "Copper Sarranid Full Plate", [("ar_sar_t7_fullplate_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,7490,weight(23)|abundance(40)|head_armor(0)|body_armor(57)|leg_armor(17)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_6]],
["ar_sar_t7_fullplate_c", "Gold Sarranid Full Plate", [("ar_sar_t7_fullplate_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,7290,weight(24)|abundance(40)|head_armor(0)|body_armor(56)|leg_armor(18)|difficulty(14) ,imodbits_plate,[],[fac_kingdom_6]],
##Player Faction - 43
#Minimal - 14
["ar_pla_t2_tabard_a", "Black and White Tabard", [("ar_pla_t2_tabard_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,30,weight(8)|abundance(90)|head_armor(0)|body_armor(15)|leg_armor(4)|difficulty(7),imodbits_cloth,[],[fac_player_faction]],
["ar_pla_t3_tabard_a", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,90,weight(12)|abundance(80)|head_armor(0)|body_armor(25)|leg_armor(7)|difficulty(8),imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":agent_no", ":troop_no")])],[fac_player_faction]],
["ar_pla_t4_heraldic_a", "Heraldic Mail", [("heraldic_armor_new_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,286, weight(15)|abundance(70)|head_armor(0)|body_armor(35)|leg_armor(11)|difficulty(9) ,imodbits_armor,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])],[fac_player_faction]],
["ar_pla_t4_heraldic_b", "Short Heraldic Mail", [("heraldic_armor_new_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,254, weight(13)|abundance(70)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(9) ,imodbits_armor,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":agent_no", ":troop_no")])],[fac_player_faction]],
["ar_pla_t5_mailsurcoat_tableau", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,810,weight(18)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(13)|difficulty(10),imodbits_armor,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])],[fac_player_faction]],
["ar_pla_t5_mailsurcoat_a", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,810,weight(18)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(13)|difficulty(10),imodbits_armor,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])],[fac_player_faction]],
["ar_pla_t5_mailsurcoat_b", "Mail with Gerulfingen Surcoat", [("ar_pla_t5_mailsurcoat_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,810,weight(18)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(13)|difficulty(10),imodbits_armor,[],[fac_player_faction]],
["ar_pla_t6_heraldic_a", "Heraldic Heavy Mail and Plate", [("ar_pla_t6_heraldic_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,2430,weight(21)|abundance(50)|head_armor(0)|body_armor(51)|leg_armor(14)|difficulty(12),imodbits_plate,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_ar_pla_t6_heraldic", ":agent_no", ":troop_no")])],[fac_player_faction]],
["ar_pla_t7_knight_a", "Holy Roman Armor", [("ar_pla_t7_knight_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,7290,weight(24)|abundance(40)|head_armor(0)|body_armor(57)|leg_armor(17)|difficulty(14) ,imodbits_plate,[],[fac_player_faction]],
["ar_pla_t7_knight_b", "Danish Plate Armor", [("ar_pla_t7_knight_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,7290,weight(24)|abundance(40)|head_armor(0)|body_armor(57)|leg_armor(17)|difficulty(14) ,imodbits_plate,[],[fac_player_faction]],
["ar_pla_t7_knight_c", "Imperial Plate Armor", [("ar_pla_t7_knight_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,7953,weight(23)|abundance(40)|head_armor(0)|body_armor(56)|leg_armor(19)|difficulty(14) ,imodbits_plate,[],[fac_player_faction]],
["ar_pla_pri_bishop", "Bishop Habit", [("ar_pla_pri_bishop",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0,2430,weight(21)|abundance(10)|head_armor(0)|body_armor(51)|leg_armor(14)|difficulty(12),imodbits_plate,[],[fac_player_faction]],
["ar_pla_pri_captain", "Captain Armor", [("ar_pla_pri_captain",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0,270, weight(14)|abundance(10)|head_armor(0)|body_armor(35)|leg_armor(10)|difficulty(9) ,imodbits_armor,[],[fac_player_faction]],
["ar_pla_str_samurai", "Strange Armor", [("ar_pla_str_samurai",0)], itp_type_body_armor|itp_covers_legs,0,359,weight(18)|abundance(10)|head_armor(0)|body_armor(38)|leg_armor(12)|difficulty(9) ,imodbits_armor,[],[fac_player_faction]],

###Cloths - 99
##Swadia - 15
#Minimal - 5
["ar_swa_mer_outfit", "Swadian Merchant Outfit", [("ar_swa_mer_outfit",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,348,weight(4)|abundance(70)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["ar_swa_nob_outfit", "Green Swadian Noble Outfit", [("ar_swa_nob_outfit",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,700,weight(4)|abundance(50)|head_armor(0)|body_armor(25)|leg_armor(7)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["ar_swa_shi_linen", "White Linen Shirt", [("ar_swa_shi_linen",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,6,weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["ar_swa_sla_loin", "Brown Mountain Cloth", [("ar_swa_sla_loin",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,3,weight(4)|abundance(120)|head_armor(0)|body_armor(3)|leg_armor(1)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["ar_swa_tun_tabard", "Green Tabard", [("ar_swa_tun_tabard",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,15,weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
##Vaegir - 15
#Minimal - 5
["ar_vae_mer_jacket", "Leather Jacket", [("ar_vae_mer_jacket",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,305,weight(3)|abundance(70)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["ar_vae_nob_outfit", "Brown Vaegir Noble Outfit", [("ar_vae_nob_outfit",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,650,weight(4)|abundance(50)|head_armor(0)|body_armor(24)|leg_armor(6)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["ar_vae_shi_red", "Red Vaegir Shirt", [("ar_vae_shi_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,5,weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["ar_vae_sla_jacketgray", "Gray Jacket", [("ar_vae_sla_jacketgray",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,2,weight(1)|abundance(120)|head_armor(0)|body_armor(2)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["ar_vae_tun_red", "Red Vaegir Tunic", [("ar_vae_tun_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,13,weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(1)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
##Khergit - 15
#Minimal - 5
["ar_khe_mer_nomadvest", "Nomad Vest", [("ar_khe_mer_nomadvest",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0,360,weight(7)|abundance(70)|head_armor(0)|body_armor(17)|leg_armor(5)|difficulty(0) ,imodbits_cloth,[],[fac_kingdom_3]],
["ar_khe_nob_kazakhrobe", "Kazakh Robe", [("ar_khe_nob_kazakhrobe",0)], itp_merchandise|itp_type_body_armor|itp_civilian|itp_covers_legs|itp_civilian,0,590,weight(13)|abundance(50)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["ar_khe_shi_peltcoat", "Green Pelt Coat", [("ar_khe_shi_peltcoat",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 10, weight(2)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["ar_khe_sla_naked", "Khergit Slave Paint", [("ar_khe_sla_naked",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,1,weight(1)|abundance(120)|head_armor(0)|body_armor(1)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["ar_khe_tun_furcoat", "Brown Fur Coat", [("ar_khe_tun_furcoat",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,15,weight(6)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(3)|difficulty(0) ,imodbits_armor,[],[fac_kingdom_3]],
##Nord - 15
#Minimal - 5
["ar_nor_mer_tunic", "Merchant Tunic", [("ar_nor_mer_tunic",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0,373,weight(7)|abundance(70)|head_armor(0)|body_armor(13)|leg_armor(3)|difficulty(0) ,imodbits_cloth,[],[fac_kingdom_4]],
["ar_nor_nob_skjorta", "Black Skjorta", [("ar_nor_nob_skjorta",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,630,weight(4)|abundance(50)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["ar_nor_shi_skjortira", "White Linen Skjortira", [("ar_nor_shi_skjortira",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,7,weight(2)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["ar_nor_sla_trousers", "Blue Trousers", [("ar_nor_sla_trousers",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,2,weight(1)|abundance(120)|head_armor(0)|body_armor(2)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["ar_nor_tun_blue", "Blue Viking Tunic", [("ar_nor_tun_blue",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,12,weight(4)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
##Rhodok - 15
#Minimal - 5
["ar_rho_mer_highlandergreen","Green Highlander Merchant Costume", [("ar_rho_mer_highlandergreen",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,348,weight(3)|abundance(70)|head_armor(0)|body_armor(13)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["ar_rho_nob_robe","Rhodok Noble Robe",[("ar_rho_nob_robe",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,750,weight(4)|abundance(50)|head_armor(0)|body_armor(26)|leg_armor(8)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["ar_rho_shi_capegreen", "Tunic with Green Cape", [("ar_rho_shi_capegreen",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,6,weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth,[],[fac_kingdom_5]], 
["ar_rho_sla_tunic", "Light Green Mountain Cloth", [("ar_rho_sla_tunic",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,3,weight(4)|abundance(120)|head_armor(0)|body_armor(3)|leg_armor(1)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["ar_rho_tun_vest", "White Tunic with vest", [("ar_rho_tun_vest",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,14,weight(2)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
##Sarranid - 15
#Minimal - 5
["ar_sar_mer_ethiopian","Ethiopian Merchant Tunic", [("ar_sar_mer_ethiopian",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,316,weight(3)|abundance(70)|head_armor(0)|body_armor(13)|leg_armor(3)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["ar_sar_nob_maratha","Orange Maratha Tunic",[("ar_sar_nob_maratha",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,450,weight(4)|abundance(50)|head_armor(0)|body_armor(21)|leg_armor(4)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["ar_sar_shi_robe", "Striped Brown Worn Robe", [("ar_sar_shi_robe",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,7,weight(3)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(3)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["ar_sar_sla_naked", "Sarranid Slave Mark", [("ar_sar_sla_naked",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,1,weight(1)|abundance(120)|head_armor(0)|body_armor(1)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["ar_sar_tun_robeblack", "Black Worn Robe", [("ar_sar_tun_robeblack",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,14,weight(3)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(4)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
##Player Faction - 9
#Minimal - 9
["ar_pla_mer_highlanderbrown","Brown Highlander Merchant Costume",[("ar_pla_mer_highlanderbrown",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,355,weight(3)|abundance(70)|head_armor(0)|body_armor(13)|leg_armor(2)|difficulty(0),imodbits_armor,[],[fac_player_faction]],
["ar_pla_mer_leatherapron", "Leather Apron", [("ar_pla_mer_leatherapron",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,41,weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],
["ar_pla_mer_surgeon","Surgeon Clothing",[("ar_pla_mer_surgeon",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,217,weight(5)|abundance(70)|head_armor(0)|body_armor(10)|leg_armor(2)|difficulty(0),imodbits_armor,[],[fac_player_faction]],
["ar_pla_pri_decoratedrobe","Decorated Priest Robe",[("ar_pla_pri_decoratedrobe",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,350,weight(4)|abundance(70)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0),imodbits_armor,[],[fac_player_faction]],
["ar_pla_pri_monkrobe","Monk Robe",[("ar_pla_pri_monkrobe",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,30,weight(4)|abundance(90)|head_armor(0)|body_armor(10)|leg_armor(2)|difficulty(0),imodbits_armor,[],[fac_player_faction]],
["ar_pla_pri_pilgrimdisguise", "Pilgrim Disguise", [("ar_pla_pri_pilgrimdisguise",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(80)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth,[],[fac_player_faction]],
["ar_pla_pri_robe", "Robe", [("ar_pla_pri_robe",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,13,weight(1.5)|abundance(90)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth,[],[fac_player_faction]],
["ar_pla_tun_tribal", "Tribal Warrior Outfit", [("ar_pla_tun_tribal",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,35,weight(14)|abundance(90)|head_armor(0)|body_armor(15)|leg_armor(4)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],
["ar_pla_tun_tunic", "Scout Tunic", [("ar_pla_tun_tunic",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0,25,weight(7)|abundance(90)|head_armor(0)|body_armor(13)|leg_armor(3)|difficulty(0) ,imodbits_cloth,[],[fac_player_faction]],

###Dresses - 45
##General - 1
#Minimal - 1
["dress_general_bride", "Bride Dress", [("general_dress_bride",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,500,weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth],
##Swadia - 8
#Minimal - 5
["dress_swadia_common_a","Swadian Pink Dress",[("swadia_dress_common_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,6,weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["dress_swadia_common_b","Swadian Woolen Dress",[("swadia_dress_common_b",0)], itp_merchandise|itp_type_body_armor|itp_civilian|itp_covers_legs,0,10,weight(1.75)|abundance(90)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["dress_swadia_lady_a", "Swadian Red Court Dress", [("swadia_dress_lady_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["dress_swadia_lady_b", "Swadian Brown Court Dress", [("swadia_dress_lady_b",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(4)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["dress_swadia_lady_isolla", "Swadian Queen Dress", [("swadia_dress_lady_isolla",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,5000,weight(4)|abundance(5)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1,fac_player_faction]],
##Vaegir - 7
#Minimal - 4
["dress_vaegir_common_a","Vaegir Peasant Dress",[("vaegir_dress_common_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,6,weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["dress_vaegir_common_b","Vaegir Brown Dress",[("vaegir_dress_common_b",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,10,weight(3)|abundance(90)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["dress_vaegir_lady_a","Vaegir Red Court Dress",[("vaegir_dress_lady_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(3)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["dress_vaegir_lady_b","Vaegir Black Court Dress",[("vaegir_dress_lady_b",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(3)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
##Khergit - 7
#Minimal - 4
["dress_khergit_common_a","Khergit Red Leather Dress",[("khergit_dress_common_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,6,weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["dress_khergit_common_b","Khergit Blue Dress",[("khergit_dress_common_b",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,10,weight(3)|abundance(90)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["dress_khergit_lady_a","Khergit Blue Court Dress",[("khergit_dress_lady_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(3)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["dress_khergit_lady_b","Khergit Green Court Dress",[("khergit_dress_lady_b",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(3)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
##Nord - 7
#Minimal - 4
["dress_nord_common_a","Nord Peasant Dress",[("nord_dress_common_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,6,weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["dress_nord_common_b","Nord Blue Dress",[("nord_dress_common_b",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,10,weight(1)|abundance(90)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["dress_nord_lady_a","Nord Green Court Dress",[("nord_dress_lady_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(3)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["dress_nord_lady_b","Nord Purple Court Dress",[("nord_dress_lady_b",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(3)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
##Rhodok- 7
#Minimal - 4
["dress_rhodok_common_a","Rhodok Red Dress",[("rhodok_dress_common_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,6,weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["dress_rhodok_common_b","Rhodok Peasant Dress",[("rhodok_dress_common_b",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,10,weight(1)|abundance(90)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["dress_rhodok_lady_a","Rhodok Blue Court Dress",[("rhodok_dress_lady_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(3)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["dress_rhodok_lady_b","Rhodok Green Court Dress",[("rhodok_dress_lady_b",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(3)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
##Sarranid - 8
#Minimal - 5
["dress_sarranid_common_a","Sarranid Gray Dress",[("sarranid_dress_common_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,6,weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["dress_sarranid_common_b","Sarranid Brown Dress",[("sarranid_dress_common_b",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,10,weight(3)|abundance(90)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["dress_sarranid_lady_a","Sarranid Purple Court Dress",[("sarranid_dress_lady_a",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(3)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["dress_sarranid_lady_b","Sarranid Orange Court Dress",[("sarranid_dress_lady_b",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,1500,weight(3)|abundance(40)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["dress_sarranid_lady_arwa","Sarranid Queen Dress",[("sarranid_dress_lady_arwa",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,5000,weight(3)|abundance(5)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6,fac_player_faction]],
#Player Faction - 0

### Footgear - 59
##General - 1
#Minimal - 1
["bo_gen_t0_bride_shoes", "Bride Shoes", [("bo_gen_t0_bride_shoes",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0,30,weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0),imodbits_cloth],
##Swadia - 8
#Minimal - 8
["bo_swa_t0_sandal", "Swadian Slave Sandals", [("bo_swa_t0_sandal",0)],itp_type_foot_armor|itp_attach_armature|itp_civilian,0,2,weight(0.5)|abundance(120)|head_armor(0)|body_armor(0)|leg_armor(1)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["bo_swa_t1_sandal", "Swadian Sandals", [("bo_swa_t1_sandal",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,9,weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["bo_swa_t2_hose", "Woolen Hose", [("bo_swa_t2_hose",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,14,weight(1)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["bo_swa_t3_wrapping","Wrapping Boots",[("bo_swa_t3_wrapping",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,32,weight(1)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(7),imodbits_cloth,[],[fac_kingdom_1]],
["bo_swa_t4_sandal", "Swadian Plated Sandals", [("bo_swa_t4_sandal",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,162,weight(1.5)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(8),imodbits_cloth,[],[fac_kingdom_1]],
["bo_swa_t5_hose", "Mail Hose", [("bo_swa_t5_hose",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,390,weight(3)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(22)|difficulty(9),imodbits_armor,[],[fac_kingdom_1]],
["bo_swa_t6_mail", "Plated Mail Boots", [("bo_swa_t6_mail",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,1240,weight(3)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(10) ,imodbits_armor,[],[fac_kingdom_1]],
["bo_swa_t7_greaves", "Iron Greaves", [("bo_swa_t7_greaves",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,2661,weight(4)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(12),imodbits_armor,[],[fac_kingdom_1]],
##Vaegir - 8
#Minimal - 8
["bo_vae_t0_sandal", "Northern Slave Sandals", [("bo_vae_t0_sandal",0)],itp_type_foot_armor|itp_attach_armature|itp_civilian,0,1,weight(0.5)|abundance(120)|head_armor(0)|body_armor(0)|leg_armor(1)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["bo_vae_t1_sandal", "Vaegir Sandals", [("bo_vae_t1_sandal",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,9,weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["bo_vae_t2_shoes","Vaegir Shoes",[("bo_vae_t2_shoes",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,22,weight(1)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["bo_vae_t3_leather","Vaegir Leather Boots",[("bo_vae_t3_leather",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,76,weight(1.25)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(7),imodbits_cloth,[],[fac_kingdom_2]],
["bo_vae_t4_shoes", "Vaegir Leather Plated Shoes", [("bo_vae_t4_shoes",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,194,weight(1)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(8),imodbits_cloth,[],[fac_kingdom_2]],
["bo_vae_t5_chausses", "Mail Chausses", [("bo_vae_t5_chausses",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,582,weight(3)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(9),imodbits_armor,[],[fac_kingdom_2]],
["bo_vae_t6_leather", "Leather Mail Greaves", [("bo_vae_t6_leather",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,656,weight(3.25)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(10) ,imodbits_armor,[],[fac_kingdom_2]],
["bo_vae_t7_greaves", "Leather Greaves", [("bo_vae_t7_greaves",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,1755,weight(3)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(12),imodbits_armor,[],[fac_kingdom_2]],
##Khergit - 8
#Minimal - 8
["bo_khe_t0_sandal", "Eastern Slave Sandals", [("bo_khe_t0_sandal",0)],itp_type_foot_armor|itp_attach_armature|itp_civilian,0,3,weight(0.5)|abundance(120)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["bo_khe_t1_sandal", "Khergit Sandals", [("bo_khe_t1_sandal",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,5,weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["bo_khe_t2_boots","Khergit Leather Boots",[("bo_khe_t2_boots",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,26,weight(1)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["bo_khe_t3_boots","Kazakh Boots",[("bo_khe_t3_boots",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,65,weight(1.25)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(7),imodbits_cloth,[],[fac_kingdom_3]],
["bo_khe_t4_sandal", "Khergit Plated Sandals", [("bo_khe_t4_sandal",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,162,weight(1.25)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(8),imodbits_cloth,[],[fac_kingdom_3]],
["bo_khe_t5_mail", "Khergit Mail Boots", [("bo_khe_t5_mail",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,390,weight(3)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(22)|difficulty(9),imodbits_armor,[],[fac_kingdom_3]],
["bo_khe_t6_mail", "Lamellar Mail Boots", [("bo_khe_t6_mail",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,802,weight(3.25)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(10) ,imodbits_armor,[],[fac_kingdom_3]],
["bo_khe_t7_greaves", "Lamellar Greaves", [("bo_khe_t7_greaves",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,1678,weight(3.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(12),imodbits_armor,[],[fac_kingdom_3]],
##Nord - 8
#Minimal - 8
["bo_nor_t0_sandal", "Northern Slave Sandals", [("bo_vae_t0_sandal",0)],itp_type_foot_armor|itp_attach_armature|itp_civilian,0,1,weight(0.5)|abundance(120)|head_armor(0)|body_armor(0)|leg_armor(1)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["bo_nor_t1_sandal", "Nord Sandals", [("bo_nor_t1_sandal",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,5,weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["bo_nor_t2_shoes","Nord Shoes",[("bo_nor_t2_shoes",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,18,weight(1)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["bo_nor_t3_boots","Fur Boots",[("bo_nor_t3_boots",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,43,weight(1.25)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(7),imodbits_cloth,[],[fac_kingdom_4]],
["bo_nor_t4_sandal", "Nord Plated Sandals", [("bo_nor_t4_sandal",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,194,weight(1.25)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(8),imodbits_cloth,[],[fac_kingdom_4]],
["bo_nor_t5_mail", "Nord Mail Sandals", [("bo_nor_t5_mail",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,486,weight(3)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(9),imodbits_armor,[],[fac_kingdom_4]],
["bo_nor_t6_mail", "Nord Plated Mail Sandals", [("bo_nor_t6_mail",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,1240,weight(3.25)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(29)|difficulty(10) ,imodbits_armor,[],[fac_kingdom_4]],
["bo_nor_t7_greaves", "Dark Greaves", [("bo_nor_t7_greaves",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,2193,weight(3.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(12),imodbits_armor,[],[fac_kingdom_4]],
##Rhodok - 8
#Minimal - 8
["bo_rho_t0_sandal", "Rhodok Slave Sandals", [("bo_rho_t0_sandal",0)],itp_type_foot_armor|itp_attach_armature|itp_civilian,0,2,weight(0.5)|abundance(120)|head_armor(0)|body_armor(0)|leg_armor(1)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["bo_rho_t1_bear", "Bear Paw Boots", [("bo_rho_t1_bear",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,7,weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["bo_rho_t2_highlander","Brown Highlander Boots",[("bo_rho_t2_highlander",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,22,weight(1)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["bo_rho_t3_highlander","Brown Highlander Fur Boots",[("bo_rho_t3_highlander",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,32,weight(1.25)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(11)|difficulty(7),imodbits_cloth,[],[fac_kingdom_5]],
["bo_rho_t4_greaves", "Splinted Greaves", [("bo_rho_t4_greaves",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,194,weight(1.5)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(8),imodbits_cloth,[],[fac_kingdom_5]],
["bo_rho_t5_greaves", "Splinted Mail Greaves", [("bo_rho_t5_greaves",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,678,weight(3)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(9),imodbits_armor,[],[fac_kingdom_5]],
["bo_rho_t6_shynbaulds", "Shynbaulds", [("bo_rho_t6_shynbaulds",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,1094,weight(3.25)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(10) ,imodbits_armor,[],[fac_kingdom_5]],
["bo_rho_t7_greaves", "Steel Greaves", [("bo_rho_t7_greaves",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,2514,weight(3.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(34)|difficulty(12),imodbits_armor,[],[fac_kingdom_5]],
##Sarranid - 8
#Minimal - 8
["bo_sar_t0_sandal", "Eastern Slave Sandals", [("bo_khe_t0_sandal",0)],itp_type_foot_armor|itp_attach_armature|itp_civilian,0,3,weight(0.5)|abundance(120)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["bo_sar_t1_sandal", "Sarranid Sandal", [("bo_sar_t1_sandal",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,7,weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["bo_sar_t2_shoes", "Sarranid Shoes", [("bo_sar_t2_shoes",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,14,weight(1)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["bo_sar_t3_boots", "Sarranid Leather Boots", [("bo_sar_t3_boots",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,65,weight(1.25)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(7),imodbits_cloth,[],[fac_kingdom_6]],
["bo_sar_t4_camel", "Plated Camel Boots", [("bo_sar_t4_camel",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,194,weight(1.25)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(8),imodbits_cloth,[],[fac_kingdom_6]],
["bo_sar_t5_mail", "Brass Mail Boots", [("bo_sar_t5_mail",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,390,weight(3)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(22)|difficulty(9),imodbits_armor,[],[fac_kingdom_6]],
["bo_sar_t6_mail", "Brass Plated Mail Boots", [("bo_sar_t6_mail",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,1111,weight(3)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(27)|difficulty(10) ,imodbits_armor,[],[fac_kingdom_6]],
["bo_sar_t7_greaves", "Brass Greaves", [("bo_sar_t7_greaves",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,2181,weight(3)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(12),imodbits_armor,[],[fac_kingdom_6]],
##Player Faction - 10
#Minimal - 10
["bo_pla_str_samurai", "Strange Boots", [("bo_pla_str_samurai",0)], itp_type_foot_armor|itp_attach_armature,0,465,weight(1)|abundance(10)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_cloth,[],[fac_player_faction]],
["bo_pla_t0_sandal", "Monk Sandals", [("bo_pla_t0_sandal",0)],itp_type_foot_armor|itp_attach_armature|itp_civilian,0,2,weight(0.5)|abundance(120)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],
["bo_pla_t1_priest", "Priest Leggings", [("bo_pla_t1_priest",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,7,weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],
["bo_pla_t2_ankle", "Ankle Boots", [("bo_pla_t2_ankle",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,22,weight(1)|abundance(90)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],
["bo_pla_t3_hunter", "Hunter Boots", [("bo_pla_t3_hunter",0)],itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian,0,54,weight(1.25)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(7),imodbits_cloth,[],[fac_player_faction]],
["bo_pla_t4_greaves", "White Splinted Greaves", [("bo_pla_t4_greaves",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,162,weight(1.25)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(8),imodbits_cloth,[],[fac_player_faction]],
["bo_pla_t4_greaves_b", "Black Splinted Greaves", [("bo_pla_t4_greaves_b",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,162,weight(1.25)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(8),imodbits_cloth,[],[fac_player_faction]],
["bo_pla_t5_highlander", "Highlander Mail Boots", [("bo_pla_t5_highlander",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,486,weight(3)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(9),imodbits_armor,[],[fac_player_faction]],
["bo_pla_t6_shynbaulds", "Dragon Shynbaulds", [("bo_pla_t6_shynbaulds",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,1094,weight(3.25)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(10) ,imodbits_armor,[],[fac_player_faction]],
["bo_pla_t7_greaves", "Dragon Greaves", [("bo_pla_t7_greaves",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0,2209,weight(3.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(12),imodbits_armor,[],[fac_player_faction]],

###Handgear - 36
##Swadia - 5
#Minimal - 4
["ga_swa_a2_leather","White Leather Gloves", [("ga_swa_a2_leather_L",0)], itp_merchandise|itp_type_hand_armor,0,100,weight(0.25)|abundance(100)|body_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["ga_swa_a4_plate","Plate Mittens", [("ga_swa_a4_plate_L",0)], itp_merchandise|itp_type_hand_armor,0,350,weight(0.5)|abundance(80)|body_armor(4)|difficulty(0),imodbits_armor,[],[fac_kingdom_1]],
["ga_swa_a5_churburg","Mail Gauntlets", [("ga_swa_a5_churburg_L",0)], itp_merchandise|itp_type_hand_armor,0,750,weight(0.75)|abundance(60)|body_armor(5)|difficulty(7),imodbits_armor,[],[fac_kingdom_1]],
["ga_swa_a6_plate","Plate Gauntlets", [("ga_swa_a6_plate_L",0)], itp_merchandise|itp_type_hand_armor,0,1100,weight(1)|abundance(40)|body_armor(6)|difficulty(8),imodbits_armor,[],[fac_kingdom_1]],
##Vaegir - 5
#Minimal - 4
["ga_vae_a2_leather","Dark Leather Gloves", [("ga_vae_a2_leather_L",0)], itp_merchandise|itp_type_hand_armor,0,100,weight(0.25)|abundance(100)|body_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["ga_vae_a4_leather","Leather Mittens", [("ga_vae_a4_leather_L",0)], itp_merchandise|itp_type_hand_armor,0,350,weight(0.5)|abundance(80)|body_armor(4)|difficulty(0),imodbits_armor,[],[fac_kingdom_2]],
["ga_vae_a5_mail","Mail Gauntlets", [("ga_vae_a5_mail_L",0)], itp_merchandise|itp_type_hand_armor,0,750,weight(0.75)|abundance(60)|body_armor(5)|difficulty(7),imodbits_armor,[],[fac_kingdom_2]],
["ga_vae_a6_black","Black Wisby Gauntlets", [("ga_vae_a6_black_L",0)], itp_merchandise|itp_type_hand_armor,0,1100,weight(1)|abundance(40)|body_armor(6)|difficulty(8),imodbits_armor,[],[fac_kingdom_2]],
##Khergit - 5
#Minimal - 4
["ga_khe_a2_leather","Green Leather Gloves", [("ga_khe_a2_leather_L",0)], itp_merchandise|itp_type_hand_armor,0,100,weight(0.25)|abundance(100)|body_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["ga_khe_a4_lamellar","Lamellar Mittens", [("ga_khe_a4_lamellar_L",0)], itp_merchandise|itp_type_hand_armor,0,350,weight(0.5)|abundance(80)|body_armor(4)|difficulty(0),imodbits_armor,[],[fac_kingdom_3]],
["ga_khe_a5_armor","Khergit Armor Gauntlets", [("ga_khe_a5_armor_L",0)], itp_merchandise|itp_type_hand_armor,0,750,weight(0.75)|abundance(60)|body_armor(5)|difficulty(7),imodbits_armor,[],[fac_kingdom_3]],
["ga_khe_a6_lamellar","Lamellar Gauntlets", [("ga_khe_a6_lamellar_L",0)], itp_merchandise|itp_type_hand_armor,0,1100,weight(1)|abundance(40)|body_armor(6)|difficulty(8),imodbits_armor,[],[fac_kingdom_3]],
##Nord - 5
#Minimal - 4
["ga_nor_a2_leather","Red Cloth Gloves", [("ga_nor_a2_leather_L",0)], itp_merchandise|itp_type_hand_armor,0,100,weight(0.25)|abundance(100)|body_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["ga_nor_a4_scale","Scale Mittens", [("ga_nor_a4_scale_L",0)], itp_merchandise|itp_type_hand_armor,0,350,weight(0.5)|abundance(80)|body_armor(4)|difficulty(0),imodbits_armor,[],[fac_kingdom_4]],
["ga_nor_a5_scale","Nord Scale Gauntlets", [("ga_nor_a5_scale_L",0)], itp_merchandise|itp_type_hand_armor,0,750,weight(1)|abundance(60)|body_armor(5)|difficulty(7),imodbits_armor,[],[fac_kingdom_4]],
["ga_nor_a6_mail","Nord Mail Gauntlets", [("ga_nor_a6_mail_L",0)], itp_merchandise|itp_type_hand_armor,0,1100,weight(1)|abundance(40)|body_armor(6)|difficulty(8),imodbits_armor,[],[fac_kingdom_4]],
##Rhodok - 5
#Minimal - 4
["ga_rho_a2_leather","Red Leather Gloves", [("ga_rho_a2_leather_L",0)], itp_merchandise|itp_type_hand_armor,0,100,weight(0.25)|abundance(100)|body_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["ga_rho_a4_brigandine","Brigandine Mittens", [("ga_rho_a4_brigandine_L",0)], itp_merchandise|itp_type_hand_armor,0,350,weight(0.5)|abundance(80)|body_armor(4)|difficulty(0),imodbits_armor,[],[fac_kingdom_5]],
["ga_rho_a5_bnw","Black and White Gauntlets", [("ga_rho_a5_bnw_L",0)], itp_merchandise|itp_type_hand_armor,0,750,weight(0.75)|abundance(60)|body_armor(5)|difficulty(7),imodbits_armor,[],[fac_kingdom_5]],
["ga_rho_a6_hourglass","Hourglass Gauntlets", [("ga_rho_a6_hourglass_L",0)], itp_merchandise|itp_type_hand_armor,0,1100,weight(1)|abundance(40)|body_armor(6)|difficulty(8),imodbits_armor,[],[fac_kingdom_5]],
##Sarranid - 5
#Minimal - 4
["ga_sar_a2_leather","Blue Leather Gloves", [("ga_sar_a2_leather_L",0)], itp_merchandise|itp_type_hand_armor,0,100,weight(0.25)|abundance(100)|body_armor(2)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["ga_sar_a4_brass","Brass Mail Mittens", [("ga_sar_a4_brass_L",0)], itp_merchandise|itp_type_hand_armor,0,350,weight(0.5)|abundance(80)|body_armor(4)|difficulty(0),imodbits_armor,[],[fac_kingdom_6]],
["ga_sar_a5_scale","Brass Scale Gauntlets", [("ga_sar_a5_scale_L",0)], itp_merchandise|itp_type_hand_armor,0,750,weight(0.75)|abundance(60)|body_armor(5)|difficulty(7),imodbits_armor,[],[fac_kingdom_6]],
["ga_sar_a6_lamellar","Brass Lamellar Gauntlets", [("ga_sar_a6_lamellar_L",0)], itp_merchandise|itp_type_hand_armor,0,1100,weight(1)|abundance(40)|body_armor(6)|difficulty(8),imodbits_armor,[],[fac_kingdom_6]],
##Player Faction - 6
#Minimal - 5
["ga_pla_a2_leather","Leather Gloves", [("ga_pla_a2_leather_L",0)], itp_merchandise|itp_type_hand_armor,0,100,weight(0.25)|abundance(100)|body_armor(2)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],
["ga_pla_a4_iron","Mail Mittens", [("ga_pla_a4_iron_L",0)], itp_merchandise|itp_type_hand_armor,0,350,weight(0.5)|abundance(80)|body_armor(4)|difficulty(0),imodbits_armor,[],[fac_player_faction]],
["ga_pla_a5_iron","Iron Articulated Gauntlets", [("ga_pla_a5_iron_L",0)], itp_merchandise|itp_type_hand_armor,0,750,weight(0.75)|abundance(60)|body_armor(5)|difficulty(7),imodbits_armor,[],[fac_player_faction]],
["ga_pla_a6_iron","Iron Gauntlets", [("ga_pla_a6_iron_L",0),("ga_pla_a6_iron_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0,1100,weight(1)|abundance(40)|body_armor(6)|difficulty(8),imodbits_armor,[],[fac_player_faction]],
["ga_pla_pri_bishop","Bishop Gloves", [("ga_pla_pri_bishop_L",0)],itp_type_hand_armor,0,100,weight(0.25)|abundance(10)|body_armor(2)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],

###Headgear (civilian) - 72
##General - 1
#Minimal - 1
["he_gen_lad_bride_crown", "Crown of Flowers", [("he_gen_lad_bride_crown",0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_attach_armature|itp_civilian,0,1,weight(0.5)|abundance(100)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
##Swadia - 11
#Minimal - 5
["he_swa_lad_common_a", "White Headcloth",[("he_swa_lad_common_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,5,weight(0.5)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["he_swa_lad_lady_a", "Ruby Turret Hat", [("he_swa_lad_lady_a",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,180,weight(0.5)|abundance(40)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["he_swa_t1_common_a", "Yellow Hood",[("he_swa_t1_common_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,5,weight(0.5)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["he_swa_t1_crown", "Swadian Crown",[("he_swa_t1_crown",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,1000,weight(1)|abundance(10)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["he_swa_t1_noble_a", "White Arming Cap",[("he_swa_t1_noble_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,7,weight(0.5)|abundance(40)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
##Vaegir - 11
#Minimal - 5
["he_vae_lad_common_a", "White Head Wrapping",[("he_vae_lad_common_a",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,5,weight(0.5)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["he_vae_lad_lady_a", "Red Barbette", [("he_vae_lad_lady_a",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,180,weight(0.5)|abundance(40)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["he_vae_t1_common_a", "Red Felt Hat",[("he_vae_t1_common_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,7,weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["he_vae_t1_crown", "Vaegir Crown",[("he_vae_t1_crown",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,1000,weight(1)|abundance(10)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["he_vae_t1_noble_a", "Ruby Vaegir Top",[("he_vae_t1_noble_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,3,weight(0.5)|abundance(40)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
##Khergit - 11
#Minimal - 5
["he_khe_lad_common_a", "Leather Nomad Cap",[("he_khe_lad_common_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,9,weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["he_khe_lad_lady_a", "Khergit Blue Lady Hat", [("he_khe_lad_lady_a",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_doesnt_cover_hair|itp_civilian,0,180,weight(0.5)|abundance(40)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["he_khe_t1_common_a", "Red Douli",[("he_khe_t1_common_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,5,weight(0.5)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["he_khe_t1_crown", "Khergit Crown",[("he_khe_t1_crown",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,1000,weight(1)|abundance(10)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["he_khe_t1_noble_a", "Brown Kazakh Hat",[("he_khe_t1_noble_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,9,weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
##Nord - 11
#Minimal - 5
["he_nor_lad_common_a", "Green Wimple Top", [("he_nor_lad_common_a",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,3,weight(0.5)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["he_nor_lad_lady_a", "Green Wimple", [("he_nor_lad_lady_a",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,180,weight(0.5)|abundance(40)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["he_nor_t1_common_a", "Green Woolen Cap",[("he_nor_t1_common_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,3,weight(0.5)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["he_nor_t1_crown", "Nord Crown",[("he_nor_t1_crown",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,1000,weight(1)|abundance(10)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
["he_nor_t1_noble_a", "Red Nord Cap",[("he_nor_t1_noble_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,9,weight(0.5)|abundance(40)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_4]],
##Rhodok - 11
#Minimal - 5
["he_rho_lad_common_a", "Blue Lady's Hood", [("he_rho_lad_common_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,5,weight(0.5)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["he_rho_lad_lady_a", "Blue Turret Hat", [("he_rho_lad_lady_a",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,180,weight(0.5)|abundance(40)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["he_rho_t1_common_a", "Dark Felt Hat",[("he_rho_t1_common_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,3,weight(0.5)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["he_rho_t1_crown", "Rhodok Crown",[("he_rho_t1_crown",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,1000,weight(1)|abundance(10)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["he_rho_t1_noble_a", "Black Highlander Beret",[("he_rho_t1_noble_a",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_fit_to_head|itp_civilian,0,5,weight(0.5)|abundance(40)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
##Sarranid - 11
#Minimal - 5
["he_sar_lad_common_a", "Brown Common Head Cloth", [("he_sar_lad_common_a",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian,0,7,weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["he_sar_lad_lady_a", "Purple Lady Head Cloth", [("he_sar_lad_lady_a",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_doesnt_cover_hair|itp_civilian,0,180,weight(0.5)|abundance(40)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["he_sar_t1_common_a", "Yellow Turban", [("he_sar_t1_common_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,7,weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["he_sar_t1_crown", "Sarranid Crown",[("he_sar_t1_crown",0)], itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,1000,weight(1)|abundance(10)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
["he_sar_t1_noble_a", "Yellow Noble Turban", [("he_sar_t1_noble_a",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,3,weight(0.5)|abundance(40)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_6]],
##Player Faction - 5
#Minimal - 5
["he_pla_pri_bishopmitre", "Bishop Mitre", [("he_pla_pri_bishopmitre",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,25,weight(1)|abundance(10)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],
["he_pla_pri_hood", "Black Hood", [("he_pla_pri_hood",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,28,weight(1.25)|abundance(10)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],
["he_pla_pri_noel", "Noel Helmet", [("he_pla_pri_noel",0)],itp_type_head_armor|itp_fit_to_head|itp_civilian,0,10,weight(1)|abundance(10)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],
["he_pla_pri_pilgrim", "Pilgrim Hood", [("he_pla_pri_pilgrim",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,28,weight(1.25)|abundance(10)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],
["he_pla_pri_priestcoif", "Priest Coif", [("he_pla_pri_priestcoif",0)],itp_merchandise|itp_type_head_armor|itp_fit_to_head|itp_civilian,0,10,weight(1)|abundance(10)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],
["he_pla_pri_surgeoncoif", "Surgeon Coif", [("he_pla_pri_surgeoncoif",0)], itp_merchandise|itp_type_head_armor|itp_civilian,0,7,weight(1)|abundance(10)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_player_faction]],

###Headgear (war) - 256
##Swadia - 36
#Minimal - 7
["he_swa_t2_coif_a", "Red Padded Coif", [("he_swa_t2_coif_a",0)], itp_merchandise|itp_type_head_armor,0,16,weight(1)|abundance(90)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["he_swa_t3_helmet_a", "Segmented Helmet", [("he_swa_t3_helmet_a",0)], itp_merchandise|itp_type_head_armor,0,60,weight(1.5)|abundance(80)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_1]],
["he_swa_t4_bascinet_a", "Brown Bascinet with Aventail", [("he_swa_t4_bascinet_a",0)], itp_merchandise|itp_type_head_armor,0,135,weight(1.75)|abundance(70)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7),imodbits_plate,[],[fac_kingdom_1]],
["he_swa_t5_flat_a", "Red Flattop Helmet", [("he_swa_t5_flat_a",0)], itp_merchandise|itp_type_head_armor,0,278,weight(2)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8),imodbits_plate,[],[fac_kingdom_1]],
["he_swa_t6_full_a", "Blue Full Helmet", [("he_swa_t6_full_a",0)], itp_merchandise|itp_type_head_armor,0,563,weight(2.5)|abundance(50)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(9),imodbits_plate,[],[fac_kingdom_1]],
["he_swa_t7_great_a", "Great Red Helmet", [("he_swa_t7_great_a",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,1275,weight(2.75)|abundance(40)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_1]],
["he_swa_t7_great_b", "Winged Great Red Helmet", [("he_swa_t7_great_b",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0,1575,weight(3)|abundance(40)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_1]],
##Vaegir - 36
#Minimal - 7
["he_vae_t2_furcap_a", "Cap with Fur", [("he_vae_t2_furcap_a",0)], itp_merchandise|itp_type_head_armor,0,24,weight(1)|abundance(90)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["he_vae_t3_furcap_a", "Cap with Lamellar Fur", [("he_vae_t3_furcap_a",0)], itp_merchandise|itp_type_head_armor,0,72,weight(1.5)|abundance(80)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_2]],
["he_vae_t4_helmet_a", "Vaegir Helmet", [("he_vae_t4_helmet_a",0)], itp_merchandise|itp_type_head_armor,0,135,weight(1.75)|abundance(70)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7),imodbits_plate,[],[fac_kingdom_2]],
["he_vae_t5_helmet_a", "Vaegir Nobleman Helmet", [("he_vae_t5_helmet_a",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,278,weight(2)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8),imodbits_plate,[],[fac_kingdom_2]],
["he_vae_t6_warhelmet_a", "Vaegir War Helmet", [("he_vae_t6_warhelmet_a",0)], itp_merchandise|itp_type_head_armor,0,563,weight(2.5)|abundance(50)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(9),imodbits_plate,[],[fac_kingdom_2]],
["he_vae_t7_warmask_a", "Vaegir War Mask", [("he_vae_t7_warmask_a",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,1125,weight(2.75)|abundance(40)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_2]],
["he_vae_t7_warmask_b", "Lichina", [("he_vae_t7_warmask_b",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,1275,weight(2.75)|abundance(40)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_2]],
##Khergit - 36
#Minimal - 7
["he_khe_t2_steppe_a", "Leather Steppe Cap", [("he_khe_t2_steppe_a",0)], itp_merchandise|itp_type_head_armor,0,16,weight(1)|abundance(90)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["he_khe_t3_steppe_a", "Steppe Cap", [("he_khe_t3_steppe_a",0)], itp_merchandise|itp_type_head_armor,0,48,weight(1.3)|abundance(80)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_3]],
["he_khe_t4_war_a", "Khergit War Helmet", [("he_khe_t4_war_a",0)], itp_merchandise|itp_type_head_armor,0,126,weight(1.75)|abundance(70)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(7),imodbits_plate,[],[fac_kingdom_3]],
["he_khe_t5_neck_a", "Magyar Helmet", [("he_khe_t5_neck_a",0)], itp_merchandise|itp_type_head_armor,0,238,weight(2)|abundance(60)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(8),imodbits_plate,[],[fac_kingdom_3]],
["he_khe_t6_helmet_a", "Khergit Lamellar Helmet", [("he_khe_t6_helmet_a",0)], itp_merchandise|itp_type_head_armor,0,638,weight(2.5)|abundance(50)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(9),imodbits_plate,[],[fac_kingdom_3]],
["he_khe_t7_mask_a", "Iron Noken Mask", [("he_khe_t7_mask_a",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,975,weight(2.5)|abundance(40)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_3]],
["he_khe_t7_mask_b", "Khergit Great Mask", [("he_khe_t7_mask_b",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,1125,weight(2.9)|abundance(40)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_3]],
##Nord - 36
#Minimal - 7
["he_nor_t2_spangen_a", "Eyebrow Spangen Helmet", [("he_nor_t2_spangen_a",0)], itp_merchandise|itp_type_head_armor,0,28,weight(1)|abundance(90)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_plate,[],[fac_kingdom_4]],
["he_nor_t3_valsgarde_a", "Small Iron Valsgarde Helmet", [("he_nor_t3_valsgarde_a",0)], itp_merchandise|itp_type_head_armor,0,72,weight(1.5)|abundance(80)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_plate,[],[fac_kingdom_4]],
["he_nor_t4_valsgarde_a", "Black Valsgarde Cheek Helmet", [("he_nor_t4_valsgarde_a",0)], itp_merchandise|itp_type_head_armor,0,144,weight(1.75)|abundance(70)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(7),imodbits_plate,[],[fac_kingdom_4]],
["he_nor_t5_valsgarde_a", "Blue Valsgarde Chain Helmet", [("he_nor_t5_valsgarde_a",0)], itp_merchandise|itp_type_head_armor,0,278,weight(2)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8),imodbits_plate,[],[fac_kingdom_4]],
["he_nor_t6_valsgarde_a", "Golden Valsgarde Helmet", [("he_nor_t6_valsgarde_a",0)], itp_merchandise|itp_type_head_armor,0,488,weight(2.5)|abundance(50)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(9),imodbits_plate,[],[fac_kingdom_4]],
["he_nor_t7_valsgarde_a", "Large Marble Valsgarde Helmet", [("he_nor_t7_valsgarde_a",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,825,weight(2.75)|abundance(40)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_4]],
["he_nor_t7_valsgarde_b", "Large Vendel Helmet", [("he_nor_t7_valsgarde_b",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard|itp_fit_to_head,0,975,weight(2.75)|abundance(40)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_4]],
##Rhodok - 36
#Minimal - 7
["he_rho_t2_beret_a", "Leather Cap", [("he_rho_t2_beret_a",0)], itp_merchandise|itp_type_head_armor,0,18,weight(1)|abundance(90)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[],[fac_kingdom_5]],
["he_rho_t3_bascinet_a", "Gold Plated Bascinet", [("he_rho_t3_bascinet_a",0)], itp_merchandise|itp_type_head_armor,0,60,weight(1.5)|abundance(80)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_plate,[],[fac_kingdom_5]],
["he_rho_t4_kettle_a", "Byzantion Helmet", [("he_rho_t4_kettle_a",0)], itp_merchandise|itp_type_head_armor,0,117,weight(1.6)|abundance(70)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(7),imodbits_plate,[],[fac_kingdom_5]],
["he_rho_t5_kettle_a", "Round Kettle Helmet", [("he_rho_t5_kettle_a",0)], itp_merchandise|itp_type_head_armor,0,278,weight(2)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8),imodbits_plate,[],[fac_kingdom_5]],
["he_rho_t6_kettle_a", "Prato Chapel-de-fer", [("he_rho_t6_kettle_a",0)], itp_merchandise|itp_type_head_armor,0,563,weight(2.5)|abundance(50)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(9),imodbits_plate,[],[fac_kingdom_5]],
["he_rho_t7_clap_a", "Clap Visored Bascinet", [("he_rho_t7_clap_a",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,1125,weight(2.75)|abundance(40)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_5]],
["he_rho_t7_clap_b", "Hound Helmet", [("he_rho_t7_clap_b",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,1275,weight(2.9)|abundance(40)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_5]],
##Sarranid - 36
#Minimal - 7
["he_sar_t2_tuareg_a", "Yellow Tuareg", [("he_sar_t2_tuareg_a",0)], itp_merchandise|itp_type_head_armor,0,16,weight(1)|abundance(90)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_plate,[],[fac_kingdom_6]],
["he_sar_t3_rabati_a", "Blue Rabati", [("he_sar_t3_rabati_a",0)], itp_merchandise|itp_type_head_armor,0,72,weight(1.5)|abundance(80)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_plate,[],[fac_kingdom_6]],
["he_sar_t4_tuareg_a", "Sarranid Yellow Mail Coif", [("he_sar_t4_tuareg_a",0)], itp_merchandise|itp_type_head_armor,0,153,weight(1.75)|abundance(70)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7),imodbits_plate,[],[fac_kingdom_6]],
["he_sar_t5_horseman_a", "Yellow Horseman Helmet", [("he_sar_t5_horseman_a",0)], itp_merchandise|itp_type_head_armor,0,258,weight(2)|abundance(60)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(8),imodbits_plate,[],[fac_kingdom_6]],
["he_sar_t6_spire_a", "Iron Spire Helmet", [("he_sar_t6_spire_a",0)], itp_merchandise|itp_type_head_armor,0,488,weight(2.5)|abundance(50)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(9),imodbits_plate,[],[fac_kingdom_6]],
["he_sar_t7_veiled_a", "Iron Veiled Helmet", [("he_sar_t7_veiled_a",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,1125,weight(2.75)|abundance(40)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_6]],
["he_sar_t7_veiled_b", "Brass Veiled Helmet", [("he_sar_t7_veiled_b",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,1125,weight(2.75)|abundance(40)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_kingdom_6]],
##Player Faction
#Minimal - 11
["he_pla_pri_bishoptophelm", "Bishop Tophelm", [("he_pla_pri_bishoptophelm",0)],itp_merchandise|itp_fit_to_head|itp_covers_beard,0,1350,weight(2.75)|abundance(5)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_player_faction]],
["he_pla_pri_captain", "Frisian Helmet", [("he_pla_pri_captain",0)],itp_merchandise|itp_fit_to_head,0,250,weight(2)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8),imodbits_plate,[],[fac_player_faction]],
["he_pla_str_samurai", "Strange Helmet", [("he_pla_str_samurai",0)], itp_type_head_armor,0,824,weight(2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7),imodbits_plate,[],[fac_player_faction]],
["he_pla_t2_cap_a", "Nasal Cap", [("he_pla_t2_cap_a",0)], itp_merchandise|itp_type_head_armor,0,20,weight(1)|abundance(90)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_plate,[],[fac_player_faction]],
["he_pla_t3_nasal_a", "Mailed Nasal Helmet", [("he_pla_t3_nasal_a",0)], itp_merchandise|itp_type_head_armor,0,60,weight(1.5)|abundance(80)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_plate,[],[fac_player_faction]],
["he_pla_t4_kettle_a", "Mercenary Kettle Helmet", [("he_pla_t4_kettle_a",0)], itp_merchandise|itp_type_head_armor,0,135,weight(1.75)|abundance(70)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7),imodbits_plate,[],[fac_player_faction]],
["he_pla_t5_nasal_a", "Bas Helmet", [("he_pla_t5_nasal_a",0)], itp_merchandise|itp_type_head_armor,0,278,weight(2)|abundance(60)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8),imodbits_plate,[],[fac_player_faction]],
["he_pla_t6_faceplate_a", "White Faceplate Helmet", [("he_pla_t6_faceplate_a",0)], itp_merchandise|itp_type_head_armor,0,563,weight(2.5)|abundance(50)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(9),imodbits_plate,[],[fac_player_faction]],
["he_pla_t7_gerulfingen", "Gerulfingen Great Helmet", [("he_pla_t7_gerulfingen",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard,0,1125,weight(2.75)|abundance(40)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_player_faction]],
["he_pla_t7_crusader_a", "White Crusader Helmet", [("he_pla_t7_crusader_a",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0,1125,weight(2.75)|abundance(40)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_player_faction]],
["he_pla_t7_crusader_b", "Black Crusader Helmet", [("he_pla_t7_crusader_b",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0,1125,weight(2.75)|abundance(40)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10),imodbits_plate,[],[fac_player_faction]],

### Shields - 128
##Swadia - 18
#Minimal - 9
["sh_swa_rou_bandit_a","Spiked Black Highlander Shield",[("sh_swa_rou_bandit_a",0)],itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,95,weight(2.5)|abundance(10)|hit_points(300)|body_armor(12)|spd_rtng(100)|shield_width(30)|difficulty(2),imodbits_shield,[],[fac_kingdom_1]],
["sh_swa_hea_english_a", "Swadian Corner Heater Shield", [("sh_swa_hea_english_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,40,weight(2.5)|abundance(100)|hit_points(170)|body_armor(6)|spd_rtng(90)|shield_width(50)|difficulty(1),imodbits_shield,[],[fac_kingdom_1]],
["sh_swa_hea_english_b", "Swadian Top Heater Shield", [("sh_swa_hea_english_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,40,weight(2.5)|abundance(100)|hit_points(170)|body_armor(6)|spd_rtng(90)|shield_width(50)|difficulty(1),imodbits_shield,[],[fac_kingdom_1]],
["sh_swa_hea_english_c", "Swadian Striped Heater Shield", [("sh_swa_hea_english_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,40,weight(2.5)|abundance(100)|hit_points(170)|body_armor(6)|spd_rtng(90)|shield_width(50)|difficulty(1),imodbits_shield,[],[fac_kingdom_1]],
["sh_swa_hea_plain", "Plain Heater Shield", [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,80,weight(2.5)|abundance(85)|hit_points(220)|body_armor(13)|spd_rtng(93)|shield_width(36)|shield_height(70)|difficulty(2),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])],[fac_kingdom_1]],
["sh_swa_hea_swadian", "Swadian Heater Shield", [("sh_swa_hea_swadian",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,80,weight(3)|abundance(85)|hit_points(220)|body_armor(13)|spd_rtng(80)|shield_width(50)|difficulty(2),imodbits_shield,[],[fac_kingdom_1]],
["sh_swa_kit_horseman", "Horseman's Kite Shield", [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,85,weight(3)|abundance(85)|hit_points(225)|body_armor(13)|spd_rtng(103)|shield_width(30)|shield_height(50)|difficulty(2),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])],[fac_kingdom_1]],
["sh_swa_kit_swadian_a", "Black and White Kite Shield", [("sh_swa_kit_swadian_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,140,weight(3.5)|abundance(70)|hit_points(250)|body_armor(15)|spd_rtng(76)|shield_width(81)|difficulty(3),imodbits_shield,[],[fac_kingdom_1]],
["sh_swa_hea_horseman", "Horseman's Heater Shield", [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,300,weight(3)|abundance(55)|hit_points(290)|body_armor(18)|spd_rtng(103)|shield_width(30)|shield_height(50)|difficulty(4),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])],[fac_kingdom_1]],
##Vaegir - 18
#Minimal - 9
["sh_vae_rou_bandit_a", "Hide Covered Round Shield", [("sh_vae_rou_bandit_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,97,weight(2)|abundance(10)|hit_points(310)|body_armor(13)|spd_rtng(100)|shield_width(40)|difficulty(2),imodbits_shield,[],[fac_kingdom_2]],
["sh_vae_kit_fur", "Fur Covered Kite Shield", [("sh_vae_kit_fur",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,38,weight(3.5)|abundance(100)|hit_points(170)|body_armor(5)|spd_rtng(76)|shield_width(81)|difficulty(1),imodbits_shield,[],[fac_kingdom_2]],
["sh_vae_kit_old", "Old Kite Shield", [("tableau_shield_kite_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,38,weight(2)|abundance(100)|hit_points(170)|body_armor(5)|spd_rtng(96)|shield_width(36)|shield_height(70)|difficulty(1),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":agent_no", ":troop_no")])],[fac_kingdom_2]],
["sh_vae_kit_plain", "Plain Kite Shield", [("tableau_shield_kite_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,38,weight(2.5)|abundance(100)|hit_points(170)|body_armor(5)|spd_rtng(93)|shield_width(36)|shield_height(70)|difficulty(1),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":agent_no", ":troop_no")])],[fac_kingdom_2]],
["sh_vae_kit_leather", "Leather Kite Shield", [("sh_vae_kit_leather",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,65,weight(3.5)|abundance(85)|hit_points(205)|body_armor(13)|spd_rtng(76)|shield_width(81)|difficulty(2),imodbits_shield,[],[fac_kingdom_2]],
["sh_vae_hae_striped_a", "Red Shield", [("sh_vae_hae_striped_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,150,weight(3.5)|abundance(70)|hit_points(250)|body_armor(15)|spd_rtng(80)|shield_width(50)|difficulty(3),imodbits_shield,[],[fac_kingdom_2]],
["sh_vae_hae_striped_b", "Blue Shield", [("sh_vae_hae_striped_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,150,weight(3.5)|abundance(70)|hit_points(250)|body_armor(15)|spd_rtng(80)|shield_width(50)|difficulty(3),imodbits_shield,[],[fac_kingdom_2]],
["sh_vae_kit_heavy", "Heavy Kite Shield", [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,146,weight(3.5)|abundance(70)|hit_points(255)|body_armor(13)|spd_rtng(87)|shield_width(36)|shield_height(70)|difficulty(2),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])],[fac_kingdom_2]],
["sh_vae_kit_vaegir_a", "Blue-Red Vaegir Kite Shield", [("sh_vae_kit_vaegir_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,340,weight(3.5)|abundance(55)|hit_points(330)|body_armor(18)|spd_rtng(76)|shield_width(81)|difficulty(4),imodbits_shield,[],[fac_kingdom_2]],
##Khergit - 18
#Minimal - 9
["sh_khe_rou_bandit_a", "Face Shield", [("sh_khe_rou_bandit_a",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,115,weight(4)|abundance(10)|hit_points(320)|body_armor(13)|spd_rtng(61)|shield_width(40)|difficulty(2),imodbits_shield,[],[fac_kingdom_3]],
["sh_khe_rou_old", "Old Round Shield", [("tableau_shield_round_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,20,weight(2.5)|abundance(100)|hit_points(185)|body_armor(4)|spd_rtng(93)|shield_width(50)|difficulty(1),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])],[fac_kingdom_3]],
["sh_khe_rou_plain", "Plain Round Shield", [("tableau_shield_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,76,weight(3)|abundance(85)|hit_points(270)|body_armor(8)|spd_rtng(90)|shield_width(50)|difficulty(1),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])],[fac_kingdom_3]],
["sh_khe_rou_round", "Round Shield", [("tableau_shield_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,117,weight(3.5)|abundance(70)|hit_points(320)|body_armor(13)|spd_rtng(87)|shield_width(50)|difficulty(2),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])],[fac_kingdom_3]],
["sh_khe_rou_heavy", "Heavy Round Shield", [("tableau_shield_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,200,weight(4)|abundance(55)|hit_points(340)|body_armor(15)|spd_rtng(84)|shield_width(50)|difficulty(3),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])],[fac_kingdom_3]],
["sh_khe_rou_steel_a", "Khergit Brass Shield", [("sh_khe_rou_steel_a",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,200,weight(4.2)|abundance(55)|hit_points(340)|body_armor(15)|spd_rtng(61)|shield_width(40)|difficulty(3),imodbits_shield,[],[fac_kingdom_3]],
["sh_khe_rou_steel_b", "Decorated Brass Shield", [("sh_khe_rou_steel_b",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,200,weight(4.5)|abundance(55)|hit_points(340)|body_armor(15)|spd_rtng(63)|shield_width(40)|difficulty(3),imodbits_shield,[],[fac_kingdom_3]],
["sh_khe_rou_steel_c", "Mercenary Steel Shield", [("sh_khe_rou_steel_c",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,410,weight(4.2)|abundance(40)|hit_points(400)|body_armor(19)|spd_rtng(61)|shield_width(40)|difficulty(4),imodbits_shield,[],[fac_kingdom_3]],
["sh_khe_rou_steel_d", "Khergit Steel Shield", [("sh_khe_rou_steel_d",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,410,weight(4.2)|abundance(40)|hit_points(400)|body_armor(19)|spd_rtng(61)|shield_width(40)|difficulty(4),imodbits_shield,[],[fac_kingdom_3]],
##Nord - 18
#Minimal - 9
["sh_nor_rou_bandit_a", "Jomsviking Shield", [("sh_nor_rou_bandit_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,120,weight(4)|abundance(10)|hit_points(310)|body_armor(13)|spd_rtng(90)|shield_width(40)|difficulty(3),imodbits_shield,[],[fac_kingdom_4]],
["sh_nor_rou_small_a", "Small Red Woodenshield", [("sh_nor_rou_small_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,21,weight(3)|abundance(100)|hit_points(185)|body_armor(4)|spd_rtng(87)|shield_width(40)|difficulty(1),imodbits_shield,[],[fac_kingdom_4]],
["sh_nor_rou_small_b", "Small Black Leathershield", [("sh_nor_rou_small_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,21,weight(3)|abundance(100)|hit_points(185)|body_armor(4)|spd_rtng(87)|shield_width(40)|difficulty(1),imodbits_shield,[],[fac_kingdom_4]],
["sh_nor_rou_medium_a", "Medium Red Woodenshield", [("sh_nor_rou_medium_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,58,weight(3.5)|abundance(85)|hit_points(260)|body_armor(8)|spd_rtng(84)|shield_width(50)|difficulty(2),imodbits_shield,[],[fac_kingdom_4]],
["sh_nor_rou_medium_b", "Medium Black Leathershield", [("sh_nor_rou_medium_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,58,weight(3.5)|abundance(85)|hit_points(260)|body_armor(8)|spd_rtng(84)|shield_width(50)|difficulty(2),imodbits_shield,[],[fac_kingdom_4]],
["sh_nor_rou_roundshield_a", "Red Roundshield", [("sh_nor_rou_roundshield_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,120,weight(3.5)|abundance(70)|hit_points(310)|body_armor(13)|spd_rtng(84)|shield_width(50)|difficulty(3),imodbits_shield,[],[fac_kingdom_4]],
["sh_nor_rou_roundshield_b", "Yellow Roundshield", [("sh_nor_rou_roundshield_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,120,weight(3.5)|abundance(70)|hit_points(310)|body_armor(13)|spd_rtng(84)|shield_width(50)|difficulty(3),imodbits_shield,[],[fac_kingdom_4]],
["sh_nor_rou_large_a", "Large Red Woodenshield", [("sh_nor_rou_large_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,240,weight(4)|abundance(55)|hit_points(350)|body_armor(17)|spd_rtng(81)|shield_width(60)|difficulty(4),imodbits_shield,[],[fac_kingdom_4]],
["sh_nor_rou_large_b", "Large Black Leathershield", [("sh_nor_rou_large_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,240,weight(4)|abundance(55)|hit_points(350)|body_armor(17)|spd_rtng(81)|shield_width(60)|difficulty(4),imodbits_shield,[],[fac_kingdom_4]],
##Rhodok - 18
#Minimal - 9
["sh_rho_rou_bandit_a","Spiked Highlander Shield",[("sh_rho_rou_bandit_a",0)],itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,116,weight(2.5)|hit_points(320)|body_armor(13)|spd_rtng(100)|shield_width(30)|difficulty(3),imodbits_shield,[],[fac_kingdom_5]],
["sh_rho_buc_steel_a", "Round Steel Buckler", [("sh_rho_buc_steel_a",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,60,weight(3.5)|abundance(85)|hit_points(250)|body_armor(7)|spd_rtng(98)|shield_width(35)|shield_height(35)|difficulty(1),imodbits_shield,[],[fac_kingdom_5]],
["sh_rho_hea_golden", "Golden Heater Shield", [("sh_rho_hea_golden",0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,175,weight(5)|abundance(70)|hit_points(260)|body_armor(15)|spd_rtng(58)|shield_width(50)|difficulty(3),imodbits_shield,[],[fac_kingdom_5]],
["sh_rho_pav_deploy_a", "Deployable Sun Pavise", [("sh_rho_pav_deploy_a" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,400,weight(6.5)|abundance(55)|hit_points(600)|body_armor(14)|spd_rtng(60)|shield_width(57)|shield_height(132)|difficulty(2),imodbits_shield,[],[fac_kingdom_5]],
["sh_rho_pav_deploy_b", "Deployable Flower Pavise", [("sh_rho_pav_deploy_b" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,400,weight(6.5)|abundance(55)|hit_points(600)|body_armor(14)|spd_rtng(60)|shield_width(57)|shield_height(132)|difficulty(2),imodbits_shield,[],[fac_kingdom_5]],
["sh_rho_pav_deploy_c", "Deployable Jelkalan Pavise", [("sh_rho_pav_deploy_c" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,400,weight(6.5)|abundance(55)|hit_points(600)|body_armor(14)|spd_rtng(60)|shield_width(57)|shield_height(132)|difficulty(2),imodbits_shield,[],[fac_kingdom_5]],
["sh_rho_pav_deploy_d", "Deployable Squire Pavise", [("sh_rho_pav_deploy_d" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,400,weight(6.5)|abundance(55)|hit_points(600)|body_armor(14)|spd_rtng(60)|shield_width(57)|shield_height(132)|difficulty(2),imodbits_shield,[],[fac_kingdom_5]],
["sh_rho_pav_deploy_e", "Deployable Castle Pavise", [("sh_rho_pav_deploy_d" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,400,weight(6.5)|abundance(55)|hit_points(600)|body_armor(14)|spd_rtng(60)|shield_width(57)|shield_height(132)|difficulty(2),imodbits_shield,[],[fac_kingdom_5]],
["sh_rho_pav_deploy_f", "Deployable Noble Pavise", [("sh_rho_pav_deploy_d" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,400,weight(6.5)|abundance(55)|hit_points(600)|body_armor(14)|spd_rtng(60)|shield_width(57)|shield_height(132)|difficulty(2),imodbits_shield,[],[fac_kingdom_5]],
##Sarranid - 21
#Minimal - 12
["sh_sar_rou_bandit_a", "Leather Covered Round Shield", [("sh_sar_rou_bandit_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,100,weight(2.5)|abundance(10)|hit_points(305)|body_armor(13)|spd_rtng(96)|shield_width(40)|difficulty(3),imodbits_shield,[],[fac_kingdom_6]],
["sh_sar_pav_slaver_a", "Brown Balayan Pavise", [("sh_sar_pav_slaver_a" ,0)], itp_type_shield, itcf_carry_board_shield,230,weight(6.5)|abundance(10)|hit_points(450)|body_armor(10)|spd_rtng(60)|shield_width(57)|shield_height(132)|difficulty(1),imodbits_shield,[],[fac_kingdom_6]],
["sh_sar_pav_slaver_b", "Red Balayan Pavise", [("sh_sar_pav_slaver_b" ,0)], itp_type_shield, itcf_carry_board_shield,230,weight(6.5)|abundance(10)|hit_points(450)|body_armor(10)|spd_rtng(60)|shield_width(57)|shield_height(132)|difficulty(1),imodbits_shield,[],[fac_kingdom_6]],
["sh_sar_pav_slaver_c", "Flower Balayan Pavise", [("sh_sar_pav_slaver_c" ,0)], itp_type_shield, itcf_carry_board_shield,230,weight(6.5)|abundance(10)|hit_points(450)|body_armor(10)|spd_rtng(60)|shield_width(57)|shield_height(132)|difficulty(1),imodbits_shield,[],[fac_kingdom_6]],
["sh_sar_rou_plain", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,106,weight(2)|abundance(85)|hit_points(170)|body_armor(8)|spd_rtng(105)|shield_width(40)|difficulty(1),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])],[fac_kingdom_6]],
["sh_sar_rou_round", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,180,weight(2.5)|abundance(70)|hit_points(190)|body_armor(14)|spd_rtng(103)|shield_width(40)|difficulty(3),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])],[fac_kingdom_6]],
["sh_sar_rou_steel_a", "Sarranid Steel Shield", [("sh_sar_rou_steel_a",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,230,weight(4.2)|abundance(55)|hit_points(360)|body_armor(15)|spd_rtng(61)|shield_width(40)|difficulty(3),imodbits_shield,[],[fac_kingdom_6]],
["sh_sar_rou_steel_b", "Hindu Steel Shield", [("sh_sar_rou_steel_b",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,230,weight(4.2)|abundance(55)|hit_points(360)|body_armor(15)|spd_rtng(61)|shield_width(40)|difficulty(3),imodbits_shield,[],[fac_kingdom_6]],
["sh_sar_rou_steel_c", "Rajputi Steel Shield", [("sh_sar_rou_steel_c",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,230,weight(4.2)|abundance(55)|hit_points(360)|body_armor(15)|spd_rtng(61)|shield_width(40)|difficulty(3),imodbits_shield,[],[fac_kingdom_6]],
["sh_sar_rou_steel_d", "Turk Steel Shield", [("sh_sar_rou_steel_d",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,230,weight(4.2)|abundance(55)|hit_points(360)|body_armor(15)|spd_rtng(61)|shield_width(40)|difficulty(3),imodbits_shield,[],[fac_kingdom_6]],
["sh_sar_rou_elite", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,350,weight(3)|abundance(40)|hit_points(250)|body_armor(21)|spd_rtng(100)|shield_width(40)|difficulty(4),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])],[fac_kingdom_6]],
["sh_sar_rou_mamluk", "Mamluk's Round Shield", [("tableau_shield_round_4",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,450,weight(4.5)|abundance(40)|hit_points(420)|body_armor(19)|spd_rtng(81)|shield_width(50)|difficulty(4),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])],[fac_kingdom_6]],
##Player Faction - 17
#Minimal - 9
["sh_pla_mus_lyre", "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,118,weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90)|difficulty(0),0,[],[fac_player_faction]],
["sh_pla_mus_lute", "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,118,weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90)|difficulty(0),0,[],[fac_player_faction]],
["sh_pla_mus_violin", "Violin", [("violin",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,118,weight(2)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(60)|difficulty(0),0,[],[fac_player_faction]],
["sh_pla_hea_big_c", "Gerulfingen Heater Shield", [("sh_pla_hea_big_c",0)], itp_type_shield, itcf_carry_kite_shield,332,weight(5)|abundance(55)|hit_points(305)|body_armor(19)|spd_rtng(58)|shield_width(50)|difficulty(4),imodbits_shield,[],[fac_player_faction]],
["sh_pla_kit_cross_a", "Big Cross Kite Shield", [("sh_pla_kit_cross_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,70,weight(2.5)|abundance(85)|hit_points(215)|body_armor(10)|spd_rtng(82)|shield_width(36)|shield_height(70)|difficulty(2),imodbits_shield,[],[fac_player_faction]],
["sh_pla_kit_eagle", "Black Eagle Kite Shield", [("sh_pla_kit_eagle",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,70,weight(2.5)|abundance(85)|hit_points(215)|body_armor(10)|spd_rtng(76)|shield_width(81)|difficulty(2),imodbits_shield,[],[fac_player_faction]],
["sh_pla_pav_plain", "Plain Pavise", [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,114,weight(4)|abundance(85)|hit_points(360)|body_armor(8)|spd_rtng(85)|shield_width(43)|shield_height(100)|difficulty(2),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])],[fac_player_faction]],
["sh_pla_pav_heavy", "Heavy Pavise", [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,210,weight(5)|abundance(70)|hit_points(430)|body_armor(10)|spd_rtng(78)|shield_width(43)|shield_height(100)|difficulty(2),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])],[fac_player_faction]],
["sh_pla_hea_big_a", "Big Cross Heater Shield", [("sh_pla_hea_big_a",0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,332,weight(5)|abundance(55)|hit_points(305)|body_armor(19)|spd_rtng(58)|shield_width(50)|difficulty(4),imodbits_shield,[],[fac_player_faction]],
["sh_pla_hea_big_b", "Steel Heater Shield", [("sh_pla_hea_big_b",0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,332,weight(5)|abundance(55)|hit_points(305)|body_armor(19)|spd_rtng(58)|shield_width(50)|difficulty(4),imodbits_shield,[],[fac_player_faction]],
["sh_pla_rou_dragon", "Dragon Steel Shield", [("sh_pla_rou_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,430,weight(4)|abundance(40)|hit_points(410)|body_armor(19)|spd_rtng(61)|shield_width(40)|difficulty(4),imodbits_shield,[],[fac_player_faction]],
["sh_pla_pav_eagle", "Eagle Pavise", [("sh_pla_pav_eagle" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,370,weight(6.5)|abundance(55)|hit_points(550)|body_armor(14)|spd_rtng(78)|shield_width(43)|shield_height(100)|difficulty(3),imodbits_shield,[],[fac_player_faction]],
####
["items_end", "Items End", [("practice_shield",0)], 0, 0, 1, 0, 0],

]

# modmerger_start version=201 type=2
try:
    component_name = "items"
    var_set = { "items" : items }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
