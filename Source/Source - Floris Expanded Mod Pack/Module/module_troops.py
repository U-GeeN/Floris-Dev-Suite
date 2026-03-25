#####Floris Notes#####
# All units are now in a logical order. Their troop id's now reflect their name.
# I added some extra troops for future use. If you want to add extra units, you thus can do very easily because of this!
# Some faces I based on real people. Their names are behind the face code. I don't claim any accuracy.
# The multiple troop trees are marked in other files as '## Floris: Multiple troop trees'.
######################

import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = str_14 | agi_14 | int_4 | cha_4



knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_23|agi_23|int_23|cha_23|level(45)

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(30)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(33)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(36)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(39)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(42)
knight_attrib_6 = str_22|agi_22|int_17|cha_28|level(48)
knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5
knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6
knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7
knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

#Swadia, men
swadian_man_face_younger_1 = 0x000000000000a0047bd98debb1efbf3e00000000001ed77d0000000000000000 ##Floris: Alfred Hitchcock
swadian_man_face_younger_2 = 0x000000000000b0c1274bb1cb1561991400000000001e28d20000000000000000 ##Floris: William Shakespeare
swadian_man_face_younger_3 = 0x000000003f00800446eba876dfa5f30b00000000001dc8d80000000000000000 ##Floris: Napoleon Boneparte
swadian_man_face_younger_4 = 0x000000002100a004444bb6cb6e9d0cc600000000001da8a00000000000000000 ##Floris: Patrick Stewart

swadian_man_face_young_1   = 0x000000088000a0047bd98debb1efbf3e00000000001ed77d0000000000000000 ##Floris: Alfred Hitchcock
swadian_man_face_young_2   = 0x000000084000b0c1274bb1cb1561991400000000001e28d20000000000000000 ##Floris: William Shakespeare
swadian_man_face_young_3   = 0x000000083f00800446eba876dfa5f30b00000000001dc8d80000000000000000 ##Floris: Napoleon Boneparte
swadian_man_face_young_4   = 0x000000086100a005444bb6cb6e9d0cc600000000001da8a00000000000000000 ##Floris: Patrick Stewart

swadian_man_face_middle_1  = 0x0000000b8000a0057bd98debb1efbf3e00000000001ed77d0000000000000000 ##Floris: Alfred Hitchcock
swadian_man_face_middle_2  = 0x0000000b8000b0c1274bb1cb1561991400000000001e28d20000000000000000 ##Floris: William Shakespeare
swadian_man_face_middle_3  = 0x0000000bff00800446eba876dfa5f30b00000000001dc8d80000000000000000 ##Floris: Napoleon Boneparte
swadian_man_face_middle_4  = 0x0000000aa100a000444bb6cb6e9d0cc600000000001da8a00000000000000000 ##Floris: Patrick Stewart

swadian_man_face_old_1     = 0x0000000dc000a0057bd98debb1efbf3e00000000001ed77d0000000000000000 ##Floris: Alfred Hitchcock
swadian_man_face_old_2     = 0x0000000e0000b0c1274bb1cb1561991400000000001e28d20000000000000000 ##Floris: William Shakespeare
swadian_man_face_old_3     = 0x0000000e3f00800446eba876dfa5f30b00000000001dc8d80000000000000000 ##Floris: Napoleon Boneparte
swadian_man_face_old_4     = 0x0000000de100a000444bb6cb6e9d0cc600000000001da8a00000000000000000 ##Floris: Patrick Stewart

swadian_man_face_older_1   = 0x0000000fc000a0057bd98debb1efbf3e00000000001ed77d0000000000000000 ##Floris: Alfred Hitchcock
swadian_man_face_older_2   = 0x0000000fc000b0c1274bb1cb1561991400000000001e28d20000000000000000 ##Floris: William Shakespeare
swadian_man_face_older_3   = 0x0000000fff00800446eba876dfa5f30b00000000001dc8d80000000000000000 ##Floris: Napoleon Boneparte
swadian_man_face_older_4   = 0x0000000fe100a000444bb6cb6e9d0cc600000000001da8a00000000000000000 ##Floris: Patrick Stewart

#Swadia, women
swadian_woman_face_younger_1 = 0x000000001d083002151180776f4ec94400000000001cebae0000000000000000 ##Floris: Wendy Hiller
swadian_woman_face_younger_2 = 0x00000000000840010e8881730ed2e72f00000000001deb810000000000000000 ##Floris: Ronni Ancona
swadian_woman_face_younger_3 = 0x00000000190840010f086072d48564c700000000001c6bde0000000000000000 ##Floris: Elaine Cassidy
swadian_woman_face_younger_4 = 0x00000000000850031e08607087a9545700000000001cebce0000000000000000 ##Floris: Sophie Marceau

swadian_woman_face_young_1   = 0x000000089d083002151180776f4ec94400000000001cebae0000000000000000 ##Floris: Wendy Hiller
swadian_woman_face_young_2   = 0x00000008800840010e8881730ed2e72f00000000001deb810000000000000000 ##Floris: Ronni Ancona
swadian_woman_face_young_3   = 0x00000008990840010f086072d48564c700000000001c6bde0000000000000000 ##Floris: Elaine Cassidy
swadian_woman_face_young_4   = 0x00000008800850031e08607087a9545700000000001cebce0000000000000000 ##Floris: Sophie Marceau

swadian_woman_face_middle_1  = 0x0000000b5d083002151180776f4ec94400000000001cebae0000000000000000 ##Floris: Wendy Hiller
swadian_woman_face_middle_2  = 0x0000000bc00840010e8881730ed2e72f00000000001deb810000000000000000 ##Floris: Ronni Ancona
swadian_woman_face_middle_3  = 0x0000000b990840010f086072d48564c700000000001c6bde0000000000000000 ##Floris: Elaine Cassidy
swadian_woman_face_middle_4  = 0x0000000b400850031e08607087a9545700000000001cebce0000000000000000 ##Floris: Sophie Marceau

swadian_woman_face_old_1     = 0x0000000d9d083002151180776f4ec94400000000001cebae0000000000000000 ##Floris: Wendy Hiller
swadian_woman_face_old_2     = 0x0000000e400840010e8881730ed2e72f00000000001deb810000000000000000 ##Floris: Ronni Ancona
swadian_woman_face_old_3     = 0x0000000e190840010f086072d48564c700000000001c6bde0000000000000000 ##Floris: Elaine Cassidy
swadian_woman_face_old_4     = 0x0000000e000850031e08607087a9545700000000001cebce0000000000000000 ##Floris: Sophie Marceau

swadian_woman_face_older_1   = 0x0000000fdd083002151180776f4ec94400000000001cebae0000000000000000 ##Floris: Wendy Hiller
swadian_woman_face_older_2   = 0x0000000fc00840010e8881730ed2e72f00000000001deb810000000000000000 ##Floris: Ronni Ancona
swadian_woman_face_older_3   = 0x0000000fd90840010f086072d48564c700000000001c6bde0000000000000000 ##Floris: Elaine Cassidy
swadian_woman_face_older_4   = 0x0000000fc00850031e08607087a9545700000000001cebce0000000000000000 ##Floris: Sophie Marceau

#Vaegir, men
vaegir_man_face_younger_1 = 0x000000003f003288252acee9b2750ff800000000001d8a280000000000000000 ##Floris: Ivan Pavlov
vaegir_man_face_younger_2 = 0x00000000200035862883e828eb85050300000000001d26f80000000000000000 ##Floris: Vladimir Lenin
vaegir_man_face_younger_3 = 0x000000002b0020082ab3b296cd68b8d200000000001f38c70000000000000000 ##Floris: Yuri Gagarin
vaegir_man_face_younger_4 = 0x000000003a0025492a82b254e0594d3700000000001f07a90000000000000000 ##Floris: Vyacheslav Molotov

vaegir_man_face_young_1   = 0x000000087f003288252acee9b2750ff800000000001d8a280000000000000000 ##Floris: Ivan Pavlov
vaegir_man_face_young_2   = 0x00000007600035852883e828eb85050300000000001d26f80000000000000000 ##Floris: Vladimir Lenin
vaegir_man_face_young_3   = 0x00000008eb0020082ab3b296cd68b8d200000000001f38c70000000000000000 ##Floris: Yuri Gagarin
vaegir_man_face_young_4   = 0x00000008ba0025492a82b254e0594d3700000000001f07a90000000000000000 ##Floris: Vyacheslav Molotov

vaegir_man_face_middle_1  = 0x0000000bbf003288252acee9b2750ff800000000001d8a280000000000000000 ##Floris: Ivan Pavlov
vaegir_man_face_middle_2  = 0x0000000b600035852883e828eb85050300000000001d26f80000000000000000 ##Floris: Vladimir Lenin
vaegir_man_face_middle_3  = 0x0000000beb0020082ab3b296cd68b8d200000000001f38c70000000000000000 ##Floris: Yuri Gagarin
vaegir_man_face_middle_4  = 0x0000000bba0025492a82b254e0594d3700000000001f07a90000000000000000 ##Floris: Vyacheslav Molotov

vaegir_man_face_old_1     = 0x0000000e3f003288252acee9b2750ff800000000001d8a280000000000000000 ##Floris: Ivan Pavlov
vaegir_man_face_old_2     = 0x0000000e200035852883e828eb85050300000000001d26f80000000000000000 ##Floris: Vladimir Lenin
vaegir_man_face_old_3     = 0x0000000e2b0020082ab3b296cd68b8d200000000001f38c70000000000000000 ##Floris: Yuri Gagarin
vaegir_man_face_old_4     = 0x0000000e3a0025492a82b254e0594d3700000000001f07a90000000000000000 ##Floris: Vyacheslav Molotov

vaegir_man_face_older_1   = 0x0000000fff003288252acee9b2750ff800000000001d8a280000000000000000 ##Floris: Ivan Pavlov
vaegir_man_face_older_2   = 0x0000000fe00035852883e828eb85050300000000001d26f80000000000000000 ##Floris: Vladimir Lenin
vaegir_man_face_older_3   = 0x0000000feb0020072ab3b296cd68b8d200000000001f38c70000000000000000 ##Floris: Yuri Gagarin
vaegir_man_face_older_4   = 0x0000000ffa0025492a82b254e0594d3700000000001f07a90000000000000000 ##Floris: Vyacheslav Molotov

#Vaegir, women
vaegir_woman_face_younger_1 = 0x00000000010080052290a0bcc56dbb7d00000000001cab0d0000000000000000 ##Floris: Mathilde Kschessinska
vaegir_woman_face_younger_2 = 0x00000000130060052290a1f046cd6b4500000000001cab250000000000000000 ##Floris: Anna Pavlovna
vaegir_woman_face_younger_3 = 0x00000000130060042290acf506716b4500000000001cab2d0000000000000000 ##Floris: Milla Jovovich
vaegir_woman_face_younger_4 = 0x0000000023007006221082730a6debbb00000000001cab2d0000000000000000 ##Floris: Anna Netrebko

vaegir_woman_face_young_1   = 0x00000008410080052290a0bcc56dbb7d00000000001cab0d0000000000000000 ##Floris: Mathilde Kschessinska
vaegir_woman_face_young_2   = 0x00000008530060052290a1f046cd6b4500000000001cab250000000000000000 ##Floris: Anna Pavlovna
vaegir_woman_face_young_3   = 0x00000008530060042290acf506716b4500000000001cab2d0000000000000000 ##Floris: Milla Jovovich
vaegir_woman_face_young_4   = 0x00000008e3007006221082730a6debbb00000000001cab2d0000000000000000 ##Floris: Anna Netrebko

vaegir_woman_face_middle_1  = 0x0000000b410080052290a0bcc56dbb7d00000000001cab0d0000000000000000 ##Floris: Mathilde Kschessinska
vaegir_woman_face_middle_2  = 0x0000000b530060052290a1f046cd6b4500000000001cab250000000000000000 ##Floris: Anna Pavlovna
vaegir_woman_face_middle_3  = 0x0000000c530060042290acf506716b4500000000001cab2d0000000000000000 ##Floris: Milla Jovovich
vaegir_woman_face_middle_4  = 0x0000000c23007006221082730a6debbb00000000001cab2d0000000000000000 ##Floris: Anna Netrebko

vaegir_woman_face_old_1     = 0x0000000e010080052290a0bcc56dbb7d00000000001cab0d0000000000000000 ##Floris: Mathilde Kschessinska
vaegir_woman_face_old_2     = 0x0000000e530060052290a1f046cd6b4500000000001cab250000000000000000 ##Floris: Anna Pavlovna
vaegir_woman_face_old_3     = 0x0000000e130060042290acf506716b4500000000001cab2d0000000000000000 ##Floris: Milla Jovovich
vaegir_woman_face_old_4     = 0x0000000e23007006221082730a6debbb00000000001cab2d0000000000000000 ##Floris: Anna Netrebko

vaegir_woman_face_older_1   = 0x0000000fc10080052290a0bcc56dbb7d00000000001cab0d0000000000000000 ##Floris: Mathilde Kschessinska
vaegir_woman_face_older_2   = 0x0000000fd30060052290a1f046cd6b4500000000001cab250000000000000000 ##Floris: Anna Pavlovna
vaegir_woman_face_older_3   = 0x0000000fd30060042290acf506716b4500000000001cab2d0000000000000000 ##Floris: Milla Jovovich
vaegir_woman_face_older_4   = 0x0000000fe3007006221082730a6debbb00000000001cab2d0000000000000000 ##Floris: Anna Netrebko

#Khergit, men
khergit_man_face_younger_1 = 0x000000003f00d38d0a698ce9f564ab2b00000000001d55160000000000000000 ##Floris: Byambyn Rinchen
khergit_man_face_younger_2 = 0x000000000000c4c8687633576aaed6b400000000001f22e80000000000000000 ##Floris: Peljidiin Genden
khergit_man_face_younger_3 = 0x000000000000e0cc6c3e47772fa0eb3d00000000001e62890000000000000000 ##Floris: Kublai Khan
khergit_man_face_younger_4 = 0x000000000000e38b6c3f53f6ef8c40fd00000000001f6afd0000000000000000 ##Floris: Ogedei Khan

khergit_man_face_young_1   = 0x00000008bf00d38d0a698ce9f564ab2b00000000001d55160000000000000000 ##Floris: Byambyn Rinchen
khergit_man_face_young_2   = 0x000000084000c4c9687633576aaed6b400000000001f22e80000000000000000 ##Floris: Peljidiin Genden
khergit_man_face_young_3   = 0x000000078000e0cc6c3e47772fa0eb3d00000000001e62890000000000000000 ##Floris: Kublai Khan
khergit_man_face_young_4   = 0x000000088000e38b6c3f53f6ef8c40fd00000000001f6afd0000000000000000 ##Floris: Ogedei Khan

khergit_man_face_middle_1  = 0x0000000b7f00d38d0a698ce9f564ab2b00000000001d55160000000000000000 ##Floris: Byambyn Rinchen
khergit_man_face_middle_2  = 0x0000000b4000c4c9687633576aaed6b400000000001f22e80000000000000000 ##Floris: Peljidiin Genden
khergit_man_face_middle_3  = 0x0000000b4000e0cc6c3e47772fa0eb3d00000000001e62890000000000000000 ##Floris: Kublai Khan
khergit_man_face_middle_4  = 0x0000000b8000e38b6c3f53f6ef8c40fd00000000001f6afd0000000000000000 ##Floris: Ogedei Khan

khergit_man_face_old_1     = 0x0000000dff00d38d0a698ce9f564ab2b00000000001d55160000000000000000 ##Floris: Byambyn Rinchen
khergit_man_face_old_2     = 0x0000000dc000c4c9687633576aaed6b400000000001f22e80000000000000000 ##Floris: Peljidiin Genden
khergit_man_face_old_3     = 0x0000000e0000e0cc6c3e47772fa0eb3d00000000001e62890000000000000000 ##Floris: Kublai Khan
khergit_man_face_old_4     = 0x0000000d8000e38b6c3f53f6ef8c40fd00000000001f6afd0000000000000000 ##Floris: Ogedei Khan

khergit_man_face_older_1   = 0x0000000fff00d38d0a698ce9f564ab2b00000000001d55160000000000000000 ##Floris: Byambyn Rinchen
khergit_man_face_older_2   = 0x0000000fc000c4c9687633576aaed6b400000000001f22e80000000000000000 ##Floris: Peljidiin Genden
khergit_man_face_older_3   = 0x0000000fc000e0cc6c3e47772fa0eb3d00000000001e62890000000000000000 ##Floris: Kublai Khan
khergit_man_face_older_4   = 0x0000000fc000e38b6c3f53f6ef8c40fd00000000001f6afd0000000000000000 ##Floris: Ogedei Khan

#Khergit, women
khergit_woman_face_younger_1 = 0x000000003f00c0476dd063e0b46b7c3800000000001c21420000000000000000 ##Floris: Semjidmaa Damba
khergit_woman_face_younger_2 = 0x000000002300e0081dd48b966bb9286200000000001ea0920000000000000000 ##Floris: Anun Chinbat
khergit_woman_face_younger_3 = 0x000000003f00c0875dd34bf01f8ade2400000000001ea1490000000000000000 ##Floris: Undraa Agvaanluvsan
khergit_woman_face_younger_4 = 0x000000003f00d0896dd26bf2cfaade1400000000001ea1520000000000000000 ##Floris: Xia Shujian

khergit_woman_face_young_1   = 0x00000008bf00c0476dd063e0b46b7c3800000000001c21420000000000000000 ##Floris: Semjidmaa Damba
khergit_woman_face_young_2   = 0x00000008e300e0081dd48b966bb9286200000000001ea0920000000000000000 ##Floris: Anun Chinbat
khergit_woman_face_young_3   = 0x00000008bf00c0875dd34bf01f8ade2400000000001ea1490000000000000000 ##Floris: Undraa Agvaanluvsan
khergit_woman_face_young_4   = 0x000000087f00d0896dd26bf2cfaade1400000000001ea1520000000000000000 ##Floris: Xia Shujian

khergit_woman_face_middle_1  = 0x0000000bbf00c0476dd063e0b46b7c3800000000001c21420000000000000000 ##Floris: Semjidmaa Damba
khergit_woman_face_middle_2  = 0x0000000be300e0081dd48b966bb9286200000000001ea0920000000000000000 ##Floris: Anun Chinbat
khergit_woman_face_middle_3  = 0x0000000bff00c0875dd34bf01f8ade2400000000001ea1490000000000000000 ##Floris: Undraa Agvaanluvsan
khergit_woman_face_middle_4  = 0x0000000bbf00d0896dd26bf2cfaade1400000000001ea1520000000000000000 ##Floris: Xia Shujian

khergit_woman_face_old_1     = 0x0000000e3f00c0476dd063e0b46b7c3800000000001c21420000000000000000 ##Floris: Semjidmaa Damba
khergit_woman_face_old_2     = 0x0000000e2300e0081dd48b966bb9286200000000001ea0920000000000000000 ##Floris: Anun Chinbat
khergit_woman_face_old_3     = 0x0000000e3f00c0875dd34bf01f8ade2400000000001ea1490000000000000000 ##Floris: Undraa Agvaanluvsan
khergit_woman_face_old_4     = 0x0000000dff00d0896dd26bf2cfaade1400000000001ea1520000000000000000 ##Floris: Xia Shujian

khergit_woman_face_older_1   = 0x0000000fff00c0476dd063e0b46b7c3800000000001c21420000000000000000 ##Floris: Semjidmaa Damba
khergit_woman_face_older_2   = 0x0000000fe300e0081dd48b966bb9286200000000001ea0920000000000000000 ##Floris: Anun Chinbat
khergit_woman_face_older_3   = 0x0000000fff00c0875dd34bf01f8ade2400000000001ea1490000000000000000 ##Floris: Undraa Agvaanluvsan
khergit_woman_face_older_4   = 0x0000000fff00d0896dd26bf2cfaade1400000000001ea1520000000000000000 ##Floris: Xia Shujian

#Nord, men
nord_man_face_younger_1 = 0x000000000b001250294372bb2bb08dbe00000000001d18780000000000000000 ##Floris: Alfred Nobel
nord_man_face_younger_2 = 0x000000000000004f219570695182a8f100000000001e08880000000000000000 ##Floris: Edvard Grieg
nord_man_face_younger_3 = 0x000000003800201046fb6d355396304400000000001d0d000000000000000000 ##Floris: Hans Christian Andersen
nord_man_face_younger_4 = 0x000000000000100f59bcb4ca57b1529500000000001c36d50000000000000000 ##Floris: Anders Celcius

nord_man_face_young_1   = 0x000000084b001252294372bb2bb08dbe00000000001d18780000000000000000 ##Floris: Alfred Nobel
nord_man_face_young_2   = 0x000000084000004f219570695182a8f100000000001e08880000000000000000 ##Floris: Edvard Grieg
nord_man_face_young_3   = 0x000000083800200f46fb6d355396304400000000001d0d000000000000000000 ##Floris: Hans Christian Andersen
nord_man_face_young_4   = 0x00000007c000100f59bcb4ca97b1529500000000001c36d50000000000000000 ##Floris: Anders Celcius

nord_man_face_middle_1  = 0x0000000b4b001252294372bb2bb08dbe00000000001d18780000000000000000 ##Floris: Alfred Nobel
nord_man_face_middle_2  = 0x0000000bc000004f219570695182a8f100000000001e08880000000000000000 ##Floris: Edvard Grieg
nord_man_face_middle_3  = 0x0000000bf800201146fb6d355396304400000000001d0d000000000000000000 ##Floris: Hans Christian Andersen
nord_man_face_middle_4  = 0x0000000a8000100f59bcb4ca97b1529500000000001c36d50000000000000000 ##Floris: Anders Celcius

nord_man_face_old_1     = 0x0000000dcb001251294372bb2bb08dbe00000000001d18780000000000000000 ##Floris: Alfred Nobel
nord_man_face_old_2     = 0x0000000e8000004f219570695182a8f100000000001e08880000000000000000 ##Floris: Edvard Grieg
nord_man_face_old_3     = 0x0000000df800201146fb6d355396304400000000001d0d000000000000000000 ##Floris: Hans Christian Andersen
nord_man_face_old_4     = 0x0000000d0000100f59bcb4cb17b1529500000000001c36d50000000000000000 ##Floris: Anders Celcius

nord_man_face_older_1   = 0x0000000fcb001251294372bb2bb08dbe00000000001d18780000000000000000 ##Floris: Alfred Nobel
nord_man_face_older_2   = 0x0000000fc000004f219570695182a8f100000000001e08880000000000000000 ##Floris: Edvard Grieg
nord_man_face_older_3   = 0x0000000ff800201146fb6d355396304400000000001d0d000000000000000000 ##Floris: Hans Christian Andersen
nord_man_face_older_4   = 0x0000000fc000100f59bcb4cb57b1529500000000001c36d50000000000000000 ##Floris: Anders Celcius

#Nord, women
nord_woman_face_younger_1 = 0x000000001b08100a03182011156f5bc400000000001d4d010000000000000000 ##Floris: Hulda Garborg
nord_woman_face_younger_2 = 0x000000000508000b02186618928ad9dd00000000001d4d110000000000000000 ##Floris: Marit Larsen
nord_woman_face_younger_3 = 0x000000000008100c0218226103631bc700000000001e4d010000000000000000 ##Floris: Rosanna Munter
nord_woman_face_younger_4 = 0x000000000308200a021861d48daa455600000000001cdd010000000000000000 ##Floris: Iben Hjejle

nord_woman_face_young_1   = 0x000000089b08100a03182011156f5bc400000000001d4d010000000000000000 ##Floris: Hulda Garborg
nord_woman_face_young_2   = 0x000000084508000b02186618928ad9dd00000000001d4d110000000000000000 ##Floris: Marit Larsen
nord_woman_face_young_3   = 0x000000084008100c0218226103631bc700000000001e4d010000000000000000 ##Floris: Rosanna Munter
nord_woman_face_young_4   = 0x000000084308200a021861d48daa455600000000001cdd010000000000000000 ##Floris: Iben Hjejle

nord_woman_face_middle_1  = 0x0000000c1b08100a03182011156f5bc400000000001d4d010000000000000000 ##Floris: Hulda Garborg
nord_woman_face_middle_2  = 0x0000000b8508000b02186618928ad9dd00000000001d4d110000000000000000 ##Floris: Marit Larsen
nord_woman_face_middle_3  = 0x0000000c0008100c0218226103631bc700000000001e4d010000000000000000 ##Floris: Rosanna Munter
nord_woman_face_middle_4  = 0x0000000bc308200a021861d48daa455600000000001cdd010000000000000000 ##Floris: Iben Hjejle

nord_woman_face_old_1     = 0x0000000e5b08100a03182011156f5bc400000000001d4d010000000000000000 ##Floris: Hulda Garborg
nord_woman_face_old_2     = 0x0000000e0508000b02186618928ad9dd00000000001d4d110000000000000000 ##Floris: Marit Larsen
nord_woman_face_old_3     = 0x0000000e8008100c0218226103631bc700000000001e4d010000000000000000 ##Floris: Rosanna Munter
nord_woman_face_old_4     = 0x0000000e4308200a021861d48daa455600000000001cdd010000000000000000 ##Floris: Iben Hjejle

nord_woman_face_older_1   = 0x0000000fdb08100a03182011156f5bc400000000001d4d010000000000000000 ##Floris: Hulda Garborg
nord_woman_face_older_2   = 0x0000000fc508000b02186618928ad9dd00000000001d4d110000000000000000 ##Floris: Marit Larsen
nord_woman_face_older_3   = 0x0000000fc008100c0218226103631bc700000000001e4d010000000000000000 ##Floris: Rosanna Munter
nord_woman_face_older_4   = 0x0000000fc308200a021861d48daa455600000000001cdd010000000000000000 ##Floris: Iben Hjejle

#Rhodok, men
rhodok_man_face_younger_1 = 0x000000003c006012676dac396368560e00000000001cc8d60000000000000000 ##Floris: Joseph Louis Lagrange
rhodok_man_face_younger_2 = 0x000000003f005012728c517eef80385f00000000001d9b400000000000000000 ##Floris: Cosimo de' Medici
rhodok_man_face_younger_3 = 0x000000003f0071522b4336d9a8659cf400000000001e9ad00000000000000000 ##Floris: Andrea Bocelli
rhodok_man_face_younger_4 = 0x000000003f005022348ca8fae6d979bf00000000001ed9320000000000000000 ##Floris: Benito Mussolini

rhodok_man_face_young_1   = 0x00000007fc006013676dac396368560e00000000001cc8d60000000000000000 ##Floris: Joseph Louis Lagrange
rhodok_man_face_young_2   = 0x000000087f005012728c517eef80385f00000000001d9b400000000000000000 ##Floris: Cosimo de' Medici
rhodok_man_face_young_3   = 0x000000083f0071522b4336d9a8659cf400000000001e9ad00000000000000000 ##Floris: Andrea Bocelli
rhodok_man_face_young_4   = 0x000000077f005022348ca8fb26d979bf00000000001ed9320000000000000000 ##Floris: Benito Mussolini

rhodok_man_face_middle_1  = 0x0000000b7c006013676dac396368560e00000000001cc8d60000000000000000 ##Floris: Joseph Louis Lagrange
rhodok_man_face_middle_2  = 0x0000000bff005011728c517eef80385f00000000001d9b400000000000000000 ##Floris: Cosimo de' Medici
rhodok_man_face_middle_3  = 0x0000000c3f0071522b4336d9a8659cf400000000001e9ad00000000000000000 ##Floris: Andrea Bocelli
rhodok_man_face_middle_4  = 0x0000000a7f005023348ca8fb66d979bf00000000001ed9320000000000000000 ##Floris: Benito Mussolini

rhodok_man_face_old_1     = 0x0000000dfc006013676dac396368560e00000000001cc8d60000000000000000 ##Floris: Joseph Louis Lagrange
rhodok_man_face_old_2     = 0x0000000e7f005011728c517eef80385f00000000001d9b400000000000000000 ##Floris: Cosimo de' Medici
rhodok_man_face_old_3     = 0x0000000d7f0071522b4336d9a8659cf400000000001e9ad00000000000000000 ##Floris: Andrea Bocelli
rhodok_man_face_old_4     = 0x0000000d7f005023348ca8fb66d979bf00000000001ed9320000000000000000 ##Floris: Benito Mussolini

rhodok_man_face_older_1   = 0x0000000ffc006013676dac396368560e00000000001cc8d60000000000000000 ##Floris: Joseph Louis Lagrange
rhodok_man_face_older_2   = 0x0000000fff005011728c517eef80385f00000000001d9b400000000000000000 ##Floris: Cosimo de' Medici
rhodok_man_face_older_3   = 0x0000000fff0071522b4336d9a8659cf400000000001e9ad00000000000000000 ##Floris: Andrea Bocelli
rhodok_man_face_older_4   = 0x0000000fff005023348ca8fba6d979bf00000000001ed9320000000000000000 ##Floris: Benito Mussolini

#Rhodok, women
rhodok_woman_face_younger_1 = 0x000000001908900f0ea0aa516758ad5f00000000001cedaf0000000000000000 ##Floris: Asia Argento
rhodok_woman_face_younger_2 = 0x000000001f08900e0ea0a3d155b8336d00000000001c6dc70000000000000000 ##Floris: Caterina Murino
rhodok_woman_face_younger_3 = 0x000000001508b00f0e11827151af555500000000001c6dcf0000000000000000 ##Floris: Delia Scala
rhodok_woman_face_younger_4 = 0x000000002408b00f0ed12579548b574600000000001c6ddf0000000000000000 ##Floris: Stefania Sandrelli

rhodok_woman_face_young_1   = 0x000000089908900f0ea0aa516758ad5f00000000001cedaf0000000000000000 ##Floris: Asia Argento
rhodok_woman_face_young_2   = 0x000000089f08900e0ea0a3d155b8336d00000000001c6dc70000000000000000 ##Floris: Caterina Murino
rhodok_woman_face_young_3   = 0x000000089508b00f0e11827151af555500000000001c6dcf0000000000000000 ##Floris: Delia Scala
rhodok_woman_face_young_4   = 0x00000008a408b00f0ed12579548b574600000000001c6ddf0000000000000000 ##Floris: Stefania Sandrelli

rhodok_woman_face_middle_1  = 0x0000000bd908900f0ea0aa516758ad5f00000000001cedaf0000000000000000 ##Floris: Asia Argento
rhodok_woman_face_middle_2  = 0x0000000bdf08900e0ea0a3d155b8336d00000000001c6dc70000000000000000 ##Floris: Caterina Murino
rhodok_woman_face_middle_3  = 0x0000000b9508b00f0e11827151af555500000000001c6dcf0000000000000000 ##Floris: Delia Scala
rhodok_woman_face_middle_4  = 0x0000000ba408b00f0ed12579548b574600000000001c6ddf0000000000000000 ##Floris: Stefania Sandrelli

rhodok_woman_face_old_1     = 0x0000000dd908900f0ea0aa516758ad5f00000000001cedaf0000000000000000 ##Floris: Asia Argento
rhodok_woman_face_old_2     = 0x0000000e1f08900e0ea0a3d155b8336d00000000001c6dc70000000000000000 ##Floris: Caterina Murino
rhodok_woman_face_old_3     = 0x0000000e1508b00f0e11827151af555500000000001c6dcf0000000000000000 ##Floris: Delia Scala
rhodok_woman_face_old_4     = 0x0000000e6408b00f0ed12579548b574600000000001c6ddf0000000000000000 ##Floris: Stefania Sandrelli

rhodok_woman_face_older_1   = 0x0000000fd908900f0ea0aa516758ad5f00000000001cedaf0000000000000000 ##Floris: Asia Argento
rhodok_woman_face_older_2   = 0x0000000fdf08900e0ea0a3d155b8336d00000000001c6dc70000000000000000 ##Floris: Caterina Murino
rhodok_woman_face_older_3   = 0x0000000fd508b00f0e11827151af555500000000001c6dcf0000000000000000 ##Floris: Delia Scala
rhodok_woman_face_older_4   = 0x0000000fe408b00f0ed12579548b574600000000001c6ddf0000000000000000 ##Floris: Stefania Sandrelli

#Sarranid, men
sarranid_man_face_younger_1 = 0x00000000000115556acc51b92679fbbe00000000001ebb190000000000000000 ##Floris: Gamal Abdel Nasser
sarranid_man_face_younger_2 = 0x000000001500f356548a960f27888dcf00000000001d28790000000000000000 ##Floris: Saladin
sarranid_man_face_younger_3 = 0x0000000015010196088976df6ac59bb500000000001f29480000000000000000 ##Floris: Mohammed Bin Rashid Al Maktoum
sarranid_man_face_younger_4 = 0x0000000014010556058a8e2d2d771cd300000000001f53a90000000000000000 ##Floris: Mustafa Kemal Ataturk

sarranid_man_face_young_1   = 0x00000006c00115556acc51b92679fbbe00000000001ebb190000000000000000 ##Floris: Gamal Abdel Nasser
sarranid_man_face_young_2   = 0x000000075500f355548a960f27888dcf00000000001d28790000000000000000 ##Floris: Saladin
sarranid_man_face_young_3   = 0x0000000715010196088976df6ac59bb500000000001f29480000000000000000 ##Floris: Mohammed Bin Rashid Al Maktoum
sarranid_man_face_young_4   = 0x0000000714010556058a8e2d2d771cd300000000001f53a90000000000000000 ##Floris: Mustafa Kemal Ataturk

sarranid_man_face_middle_1  = 0x0000000b400115556acc51b92679fbbe00000000001ebb190000000000000000 ##Floris: Gamal Abdel Nasser
sarranid_man_face_middle_2  = 0x0000000b1500f355548a960f27888dcf00000000001d28790000000000000000 ##Floris: Saladin
sarranid_man_face_middle_3  = 0x0000000bd5010195088976df6ac59bb500000000001f29480000000000000000 ##Floris: Mohammed Bin Rashid Al Maktoum
sarranid_man_face_middle_4  = 0x0000000ad4010556058a8e2d2d771cd300000000001f53a90000000000000000 ##Floris: Mustafa Kemal Ataturk

sarranid_man_face_old_1     = 0x0000000dc00115556acc51b92679fbbe00000000001ebb190000000000000000 ##Floris: Gamal Abdel Nasser
sarranid_man_face_old_2     = 0x0000000dd500f355548a960f27888dcf00000000001d28790000000000000000 ##Floris: Saladin
sarranid_man_face_old_3     = 0x0000000dd5010195088976df6ac59bb500000000001f29480000000000000000 ##Floris: Mohammed Bin Rashid Al Maktoum
sarranid_man_face_old_4     = 0x0000000dd4010555058a8e2d2d771cd300000000001f53a90000000000000000 ##Floris: Mustafa Kemal Ataturk

sarranid_man_face_older_1   = 0x0000000fc00115556acc51b92679fbbe00000000001ebb190000000000000000 ##Floris: Gamal Abdel Nasser
sarranid_man_face_older_2   = 0x0000000fd500f355548a960f27888dcf00000000001d28790000000000000000 ##Floris: Saladin
sarranid_man_face_older_3   = 0x0000000fd5010195088976df6ac59bb500000000001f29480000000000000000 ##Floris: Mohammed Bin Rashid Al Maktoum
sarranid_man_face_older_4   = 0x0000000fd4010555058a8e2d2d771cd300000000001f53a90000000000000000 ##Floris: Mustafa Kemal Ataturk

#Sarranid, women
sarranid_woman_face_younger_1 = 0x000000002300f01043616dd4d564c8ae00000000001ce4cf0000000000000000 ##Floris: Asmahan
sarranid_woman_face_younger_2 = 0x000000002c0110110b6156d15eacc8ad00000000001ce51f0000000000000000 ##Floris: Umm Kulthum
sarranid_woman_face_younger_3 = 0x00000000230100120ba48a71478e588600000000001ce52f0000000000000000 ##Floris: Deniz Akkaya
sarranid_woman_face_younger_4 = 0x000000002b0100130fa06f718fccc6bd00000000001ce51f0000000000000000 ##Floris: Aravane Rezai

sarranid_woman_face_young_1   = 0x000000086300f01043616dd4d564c8ae00000000001ce4cf0000000000000000 ##Floris: Asmahan
sarranid_woman_face_young_2   = 0x000000092c0110110b6156d15eacc8ad00000000001ce51f0000000000000000 ##Floris: Umm Kulthum
sarranid_woman_face_young_3   = 0x00000008a30100120ba48a71478e588600000000001ce52f0000000000000000 ##Floris: Deniz Akkaya
sarranid_woman_face_young_4   = 0x00000008eb0100130fa06f718fccc6bd00000000001ce51f0000000000000000 ##Floris: Aravane Rezai

sarranid_woman_face_middle_1  = 0x0000000b6300f01043616dd4d564c8ae00000000001ce4cf0000000000000000 ##Floris: Asmahan
sarranid_woman_face_middle_2  = 0x0000000c6c0110110b6156d15eacc8ad00000000001ce51f0000000000000000 ##Floris: Umm Kulthum
sarranid_woman_face_middle_3  = 0x0000000be30100120ba48a71478e588600000000001ce52f0000000000000000 ##Floris: Deniz Akkaya
sarranid_woman_face_middle_4  = 0x0000000c2b0100130fa06f718fccc6bd00000000001ce51f0000000000000000 ##Floris: Aravane Rezai

sarranid_woman_face_old_1     = 0x0000000e2300f01043616dd4d564c8ae00000000001ce4cf0000000000000000 ##Floris: Asmahan
sarranid_woman_face_old_2     = 0x0000000e6c0110110b6156d15eacc8ad00000000001ce51f0000000000000000 ##Floris: Umm Kulthum
sarranid_woman_face_old_3     = 0x0000000de30100120ba48a71478e588600000000001ce52f0000000000000000 ##Floris: Deniz Akkaya
sarranid_woman_face_old_4     = 0x0000000e2b0100130fa06f718fccc6bd00000000001ce51f0000000000000000 ##Floris: Aravane Rezai

sarranid_woman_face_older_1   = 0x0000000fe300f01043616dd4d564c8ae00000000001ce4cf0000000000000000 ##Floris: Asmahan
sarranid_woman_face_older_2   = 0x0000000fec0110110b6156d15eacc8ad00000000001ce51f0000000000000000 ##Floris: Umm Kulthum
sarranid_woman_face_older_3   = 0x0000000fe30100120ba48a71478e588600000000001ce52f0000000000000000 ##Floris: Deniz Akkaya
sarranid_woman_face_older_4   = 0x0000000feb0100130fa06f718fccc6bd00000000001ce51f0000000000000000 ##Floris: Aravane Rezai

#General, HRE men
mercenary_man_face_younger_1 = 0x00000003000c74912de98c56ebc93b7400000000001f16c40000000000000000 ##Floris: Paul von Hindenburg
mercenary_man_face_younger_2 = 0x000000003f0c75432dcb705a2fd254ea00000000001d1b860000000000000000 ##Floris: Albert Einstein
mercenary_man_face_younger_3 = 0x00000000140c800f1d6c883a876088b300000000001d99970000000000000000 ##Floris: Carl von Clausewitz
mercenary_man_face_younger_4 = 0x00000000000ca00614fa6866ac6dd7b500000000001c9b510000000000000000 ##Floris: Erwin Rommel

mercenary_man_face_young_1   = 0x00000007400c74912de98c572bc93b7400000000001f16c40000000000000000 ##Floris: Paul von Hindenburg
mercenary_man_face_young_2   = 0x00000008ff0c75432dcb705aafd254ea00000000001d1b860000000000000000 ##Floris: Albert Einstein
mercenary_man_face_young_3   = 0x00000007140c800f1d6c883ac76088b300000000001d99970000000000000000 ##Floris: Carl von Clausewitz
mercenary_man_face_young_4   = 0x00000007000ca00614fa6866ec6dd7b500000000001c9b510000000000000000 ##Floris: Erwin Rommel

mercenary_man_face_middle_1  = 0x0000000a400c74912de98c596bc93b7400000000001f16c40000000000000000 ##Floris: Paul von Hindenburg
mercenary_man_face_middle_2  = 0x0000000cff0c75432dcb705aefd254ea00000000001d1b860000000000000000 ##Floris: Albert Einstein
mercenary_man_face_middle_3  = 0x00000008d40c800f1d6c883b076088b300000000001d99970000000000000000 ##Floris: Carl von Clausewitz
mercenary_man_face_middle_4  = 0x0000000b400ca00614fa68676c6dd7b500000000001c9b510000000000000000 ##Floris: Erwin Rommel

mercenary_man_face_old_1     = 0x0000000dc00c74912de98c57abc93b7400000000001f16c40000000000000000 ##Floris: Paul von Hindenburg
mercenary_man_face_old_2     = 0x0000000e7f0c75432dcb705d6fd254ea00000000001d1b860000000000000000 ##Floris: Albert Einstein
mercenary_man_face_old_3 	   = 0x0000000c140c800f1d6c883d476088b300000000001d99970000000000000000 ##Floris: Carl von Clausewitz
mercenary_man_face_old_4	   = 0x0000000e400ca00614fa6867ac6dd7b500000000001c9b510000000000000000 ##Floris: Erwin Rommel

mercenary_man_face_older_1   = 0x0000000fc00c74912de98c59ebc93b7400000000001f16c40000000000000000 ##Floris: Paul von Hindenburg
mercenary_man_face_older_2   = 0x0000000fff0c75432dcb705dafd254ea00000000001d1b860000000000000000 ##Floris: Albert Einstein
mercenary_man_face_older_3   = 0x0000000fd40c800f1d6c883d876088b300000000001d99970000000000000000 ##Floris: Carl von Clausewitz
mercenary_man_face_older_4   = 0x0000000fc00ca00614fa6869ac6dd7b500000000001c9b510000000000000000 ##Floris: Erwin Rommel

#General, HRE women
mercenary_woman_face_younger_1 = 0x00000000000800015e10b6966b55996700000000001cea820000000000000000 ##Floris: Claudia Schiffer
mercenary_woman_face_younger_2 = 0x00000000050800025e108a90ad499d6d00000000001ceaaa0000000000000000 ##Floris: Marlene Dietrich
mercenary_woman_face_younger_3 = 0x00000000240810035e10ca71158dbd6d00000000001ceab20000000000000000 ##Floris: Famke Janssen
mercenary_woman_face_younger_4 = 0x00000000020800055e10c9710b86234600000000001cea920000000000000000 ##Floris: Eva Habermann

mercenary_woman_face_young_1   = 0x00000003800800015e10b6966b55996700000000001cea820000000000000000 ##Floris: Claudia Schiffer
mercenary_woman_face_young_2   = 0x00000003850800025e108a90ad499d6d00000000001ceaaa0000000000000000 ##Floris: Marlene Dietrich
mercenary_woman_face_young_3   = 0x00000003a40810035e10ca71158dbd6d00000000001ceab20000000000000000 ##Floris: Famke Janssen
mercenary_woman_face_young_4   = 0x00000003c20800055e10c9710b86234600000000001cea920000000000000000 ##Floris: Eva Habermann

mercenary_woman_face_middle_1  = 0x00000008000800015e10b6966b55996700000000001cea820000000000000000 ##Floris: Claudia Schiffer
mercenary_woman_face_middle_2  = 0x00000008050800025e108a90ad499d6d00000000001ceaaa0000000000000000 ##Floris: Marlene Dietrich
mercenary_woman_face_middle_3  = 0x00000007e40810035e10ca71158dbd6d00000000001ceab20000000000000000 ##Floris: Famke Janssen
mercenary_woman_face_middle_4  = 0x00000007820800055e10c9710b86234600000000001cea920000000000000000 ##Floris: Eva Habermann

mercenary_woman_face_old_1     = 0x0000000bc00800015e10b6966b55996700000000001cea820000000000000000 ##Floris: Claudia Schiffer
mercenary_woman_face_old_2     = 0x0000000bc50800025e108a90ad499d6d00000000001ceaaa0000000000000000 ##Floris: Marlene Dietrich
mercenary_woman_face_old_3     = 0x0000000c240810035e10ca71158dbd6d00000000001ceab20000000000000000 ##Floris: Famke Janssen
mercenary_woman_face_old_4     = 0x0000000bc20800055e10c9710b86234600000000001cea920000000000000000 ##Floris: Eva Habermann

mercenary_woman_face_older_1   = 0x0000000fc00800015e10b6966b55996700000000001cea820000000000000000 ##Floris: Claudia Schiffer
mercenary_woman_face_older_2   = 0x0000000fc50800025e108a90ad499d6d00000000001ceaaa0000000000000000 ##Floris: Marlene Dietrich
mercenary_woman_face_older_3   = 0x0000000fe40810035e10ca71158dbd6d00000000001ceab20000000000000000 ##Floris: Famke Janssen
mercenary_woman_face_older_4   = 0x0000000fc20800055e10c9710b86234600000000001cea920000000000000000 ##Floris: Eva Habermann

#Africa, men
african_man_face_younger_1 = 0x0000000000016005454a2255c6e2531100000000001dcb450000000000000000 ##Floris: Nelson Mandela
african_man_face_younger_2 = 0x000000002e0140041b4872528ef7e31100000000001dcaed0000000000000000 ##Floris: Chinua Achebe
african_man_face_younger_3 = 0x000000042e0125d047627253b99f731100000000001d4af50000000000000000 ##Floris: Ngugi wa Thiong'o
african_man_face_younger_4 = 0x000000002e0160115ada5a59ffdae8c100000000001dda960000000000000000 ##Floris: Morgan Freeman

african_man_face_young_1   = 0x0000000700016005454a2255c6e2531100000000001dcb450000000000000000 ##Floris: Nelson Mandela
african_man_face_young_2   = 0x000000082e0140041b4872528ef7e31100000000001dcaed0000000000000000 ##Floris: Chinua Achebe
african_man_face_young_3   = 0x000000092e0125d047627253b99f731100000000001d4af50000000000000000 ##Floris: Ngugi wa Thiong'o
african_man_face_young_4   = 0x000000086e0160115ada5a59ffdae8c100000000001dda960000000000000000 ##Floris: Morgan Freeman

african_man_face_middle_1  = 0x0000000b40016005454a2255c6e2531100000000001dcb450000000000000000 ##Floris: Nelson Mandela
african_man_face_middle_2  = 0x0000000bee0140041b4872528ef7e31100000000001dcaed0000000000000000 ##Floris: Chinua Achebe
african_man_face_middle_3  = 0x0000000cae01259047627253b99f731100000000001d4af50000000000000000 ##Floris: Ngugi wa Thiong'o
african_man_face_middle_4  = 0x0000000bee0160115ada5a59ffdae8c100000000001dda960000000000000000 ##Floris: Morgan Freeman

african_man_face_old_1     = 0x0000000d80016005454a2255c6e2531100000000001dcb450000000000000000 ##Floris: Nelson Mandela
african_man_face_old_2     = 0x0000000dee0140041b4872528ef7e31100000000001dcaed0000000000000000 ##Floris: Chinua Achebe
african_man_face_old_3     = 0x0000000e2e01259247627253b99f731100000000001d4af50000000000000000 ##Floris: Ngugi wa Thiong'o
african_man_face_old_4     = 0x0000000e6e0165d15ada5a59ffdae8c100000000001dda960000000000000000 ##Floris: Morgan Freeman

african_man_face_older_1   = 0x0000000fc0016005454a2255c6e2531100000000001dcb450000000000000000 ##Floris: Nelson Mandela
african_man_face_older_2   = 0x0000000fee0140041b4872528ef7e31100000000001dcaed0000000000000000 ##Floris: Chinua Achebe
african_man_face_older_3   = 0x0000000fee01259247627253b99f731100000000001d4af50000000000000000 ##Floris: Ngugi wa Thiong'o
african_man_face_older_4   = 0x0000000fee0165915ada5a57ffdae8c100000000001dda960000000000000000 ##Floris: Morgan Freeman



undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

#######
# When you scroll to the right, you'll get an explanation of the item order. ----->																																																[Horses								,Dresses & Cloths				,Armors							,Boots (civilian)				,Boots (War)					,Helmets (civilian)				,Helmets (War)						,Gauntlets						,Shields						,Primary Weapon							,Secondary Weapon						,Ammunition								,Extra items]
#######
##### Here are several troops using the Minimal items #####
from module_troops_part1 import *
from module_troops_part2 import *

troops = troops_part1 + troops_part2


####Troop upgrade declarations
## Floris: Multiple troop trees
###Mercenaries
##Native troop tree
#Tier 1-2
upgrade(troops,"mercenary_n_townsman","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_farmer","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_extra1","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_extra2","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_extra3","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_extra4","mercenary_n_spiessknecht")
upgrade(troops,"mercenary_n_extra5","mercenary_n_spiessknecht")
#Tier 2-3
upgrade2(troops,"mercenary_n_spiessknecht","mercenary_n_page","mercenary_n_armbrust_soldner")
#Tier 3-4
upgrade2(troops,"mercenary_n_page","mercenary_n_soldner","mercenary_n_ritter")
#Tier 4-5
upgrade(troops,"mercenary_n_soldner","mercenary_n_komtur")
upgrade(troops,"mercenary_n_ritter","mercenary_n_komtur_ritter")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"mercenary_r_townsman","mercenary_r_edelknecht","mercenary_r_spiessknecht")
upgrade2(troops,"mercenary_r_farmer","mercenary_r_spiessknecht","mercenary_r_armbruster")
upgrade2(troops,"mercenary_r_extra1","mercenary_r_edelknecht","mercenary_r_spiessknecht")
upgrade2(troops,"mercenary_r_extra2","mercenary_r_edelknecht","mercenary_r_spiessknecht")
upgrade2(troops,"mercenary_r_extra3","mercenary_r_edelknecht","mercenary_r_spiessknecht")
upgrade2(troops,"mercenary_r_extra4","mercenary_r_edelknecht","mercenary_r_spiessknecht")
upgrade2(troops,"mercenary_r_extra5","mercenary_r_edelknecht","mercenary_r_spiessknecht")
#Tier 2-3
upgrade(troops,"mercenary_r_edelknecht","mercenary_r_burger")
upgrade2(troops,"mercenary_r_spiessknecht","mercenary_r_halberdier","mercenary_r_page")
upgrade(troops,"mercenary_r_armbruster","mercenary_r_armbrust_miliz")
#Tier 3-4
upgrade(troops,"mercenary_r_burger","mercenary_r_brabanzon")
upgrade(troops,"mercenary_r_halberdier","mercenary_r_reichslandser")
upgrade(troops,"mercenary_r_page","mercenary_r_ritter")
upgrade(troops,"mercenary_r_armbrust_miliz","mercenary_r_armbrust_soldner")
#Tier 4-5
upgrade(troops,"mercenary_r_brabanzon","mercenary_r_doppelsoldner")
upgrade(troops,"mercenary_r_reichslandser","mercenary_r_burgmann")
upgrade(troops,"mercenary_r_ritter","mercenary_r_komtur_ritter")
upgrade(troops,"mercenary_r_armbrust_soldner","mercenary_r_armbrust_komtur")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"mercenary_e_townsman","mercenary_e_miliz","mercenary_e_edelknecht")
upgrade2(troops,"mercenary_e_farmer","mercenary_e_spiessknecht","mercenary_e_armbruster")
upgrade2(troops,"mercenary_e_extra1","mercenary_e_miliz","mercenary_e_edelknecht")
upgrade2(troops,"mercenary_e_extra2","mercenary_e_miliz","mercenary_e_edelknecht")
upgrade2(troops,"mercenary_e_extra3","mercenary_e_miliz","mercenary_e_edelknecht")
upgrade2(troops,"mercenary_e_extra4","mercenary_e_miliz","mercenary_e_edelknecht")
upgrade2(troops,"mercenary_e_extra5","mercenary_e_miliz","mercenary_e_edelknecht")
#Tier 2-3
upgrade2(troops,"mercenary_e_miliz","mercenary_e_brabanzon","mercenary_e_burger")
upgrade2(troops,"mercenary_e_edelknecht","mercenary_e_volksheer","mercenary_e_halberdier")
upgrade2(troops,"mercenary_e_spiessknecht","mercenary_e_halberdier","mercenary_e_page")
upgrade2(troops,"mercenary_e_armbruster","mercenary_e_armbrust_soldner","mercenary_e_armbrust_miliz")
#Tier 3-4
upgrade(troops,"mercenary_e_brabanzon","mercenary_e_ritterbroeder")
upgrade(troops,"mercenary_e_volksheer","mercenary_e_soldner")
upgrade(troops,"mercenary_e_halberdier","mercenary_e_reichslandser")
upgrade(troops,"mercenary_e_page","mercenary_e_ritter")
upgrade(troops,"mercenary_e_armbrust_soldner","mercenary_e_armbrust_komtur")
#Tier 4-5
upgrade(troops,"mercenary_e_ritterbroeder","mercenary_e_doppelsoldner")
upgrade(troops,"mercenary_e_soldner","mercenary_e_komtur")
upgrade(troops,"mercenary_e_reichslandser","mercenary_e_burgmann")
upgrade2(troops,"mercenary_e_ritter","mercenary_e_komtur_ritter","mercenary_e_kreuzritter")
#Tier 5-6
upgrade(troops,"mercenary_e_komtur","mercenary_e_grosskomtur")
upgrade(troops,"mercenary_e_burgmann","mercenary_e_landsknecht")
upgrade(troops,"mercenary_e_komtur_ritter","mercenary_e_hochmeister")
##

###Swadia
##Native troop tree
#Tier 1-2
upgrade(troops,"swadian_n_peasant","swadian_n_militia")
upgrade(troops,"swadian_n_extra1","swadian_n_militia")
upgrade(troops,"swadian_n_extra2","swadian_n_militia")
upgrade(troops,"swadian_n_extra3","swadian_n_militia")
upgrade(troops,"swadian_n_extra4","swadian_n_militia")
upgrade(troops,"swadian_n_extra5","swadian_n_militia")
#Tier 2-3
upgrade2(troops,"swadian_n_militia","swadian_n_page","swadian_n_archer_militia")
#Tier 3-4
upgrade2(troops,"swadian_n_page","swadian_n_ecuyer","swadian_n_jacobite")
upgrade(troops,"swadian_n_archer_militia","swadian_n_longbowman")
#Tier 4-5
upgrade(troops,"swadian_n_ecuyer","swadian_n_chevalier")
upgrade(troops,"swadian_n_jacobite","swadian_n_jock")
upgrade(troops,"swadian_n_longbowman","swadian_n_selfbow_archer")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"swadian_r_peasant","swadian_r_militia","swadian_r_peasant_archer")
upgrade2(troops,"swadian_r_extra1","swadian_r_militia","swadian_r_peasant_archer")
upgrade2(troops,"swadian_r_extra2","swadian_r_militia","swadian_r_peasant_archer")
upgrade2(troops,"swadian_r_extra3","swadian_r_militia","swadian_r_peasant_archer")
upgrade2(troops,"swadian_r_extra4","swadian_r_militia","swadian_r_peasant_archer")
upgrade2(troops,"swadian_r_extra5","swadian_r_militia","swadian_r_peasant_archer")
#Tier 2-3
upgrade(troops,"swadian_r_militia","swadian_r_page")
upgrade2(troops,"swadian_r_peasant_archer","swadian_r_sergeant_at_arms","swadian_r_archer_militia")
#Tier 3-4
upgrade2(troops,"swadian_r_page","swadian_r_hobilar","swadian_r_ecuyer")
upgrade2(troops,"swadian_r_sergeant_at_arms","swadian_r_piquier","swadian_r_jacobite")
upgrade(troops,"swadian_r_archer_militia","swadian_r_longbowman")
#Tier 4-5
upgrade(troops,"swadian_r_ecuyer","swadian_r_chevalier")
upgrade(troops,"swadian_r_jacobite","swadian_r_jock")
upgrade(troops,"swadian_r_longbowman","swadian_r_selfbow_archer")
#Tier 5-6
upgrade(troops,"swadian_r_chevalier","swadian_r_chevalier_banneret")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"swadian_e_peasant","swadian_e_militia","swadian_e_peasant_archer")
upgrade2(troops,"swadian_e_extra1","swadian_e_militia","swadian_e_peasant_archer")
upgrade2(troops,"swadian_e_extra2","swadian_e_militia","swadian_e_peasant_archer")
upgrade2(troops,"swadian_e_extra3","swadian_e_militia","swadian_e_peasant_archer")
upgrade2(troops,"swadian_e_extra4","swadian_e_militia","swadian_e_peasant_archer")
upgrade2(troops,"swadian_e_extra5","swadian_e_militia","swadian_e_peasant_archer")
#Tier 2-3
upgrade2(troops,"swadian_e_militia","swadian_e_vougier","swadian_e_page")
upgrade2(troops,"swadian_e_peasant_archer","swadian_e_sergeant_at_arms","swadian_e_archer_militia")
#Tier 3-4
upgrade2(troops,"swadian_e_vougier","swadian_e_piquier","swadian_e_ecuyer")
upgrade2(troops,"swadian_e_page","swadian_e_ecuyer","swadian_e_jacobite")
upgrade2(troops,"swadian_e_sergeant_at_arms","swadian_e_jacobite","swadian_e_guard")
upgrade2(troops,"swadian_e_archer_militia","swadian_e_longbowman","swadian_e_tracker")
#Tier 4-5
upgrade(troops,"swadian_e_ecuyer","swadian_e_chevalier")
upgrade2(troops,"swadian_e_jacobite","swadian_e_hobilar","swadian_e_jock")
upgrade2(troops,"swadian_e_guard","swadian_e_man_at_arms","swadian_e_sheriff")
upgrade(troops,"swadian_e_longbowman","swadian_e_selfbow_archer")
upgrade(troops,"swadian_e_tracker","swadian_e_skirmisher")
#Tier 5-6
upgrade(troops,"swadian_e_chevalier","swadian_e_chevalier_banneret")
upgrade(troops,"swadian_e_jock","swadian_e_highlander")
upgrade(troops,"swadian_e_man_at_arms","swadian_e_lancer")
upgrade(troops,"swadian_e_selfbow_archer","swadian_e_yeoman_archer")
#Tier 6-7
upgrade(troops,"swadian_e_chevalier_banneret","swadian_e_baron_mineures")
upgrade(troops,"swadian_e_yeoman_archer","swadian_e_retinue_longbowman")
##

###Vaegir
##Native troop tree
#Tier 1-2
upgrade(troops,"vaegir_n_kholop","vaegir_n_otrok")
upgrade(troops,"vaegir_n_extra1","vaegir_n_otrok")
upgrade(troops,"vaegir_n_extra2","vaegir_n_otrok")
upgrade(troops,"vaegir_n_extra3","vaegir_n_otrok")
upgrade(troops,"vaegir_n_extra4","vaegir_n_otrok")
upgrade(troops,"vaegir_n_extra5","vaegir_n_otrok")
#Tier 2-3
upgrade2(troops,"vaegir_n_otrok","vaegir_n_kazak","vaegir_n_kmet")
#Tier 3-4
upgrade2(troops,"vaegir_n_kazak","vaegir_n_yesaul","vaegir_n_plastun")
upgrade(troops,"vaegir_n_kmet","vaegir_n_zalstrelshik")
#Tier 4-5
upgrade(troops,"vaegir_n_yesaul","vaegir_n_pansirniy_kazan")
upgrade(troops,"vaegir_n_plastun","vaegir_n_druzhinnik_veteran")
upgrade(troops,"vaegir_n_zalstrelshik","vaegir_n_luchnik")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"vaegir_r_kholop","vaegir_r_otrok","vaegir_r_pasynok")
upgrade2(troops,"vaegir_r_extra1","vaegir_r_otrok","vaegir_r_pasynok")
upgrade2(troops,"vaegir_r_extra2","vaegir_r_otrok","vaegir_r_pasynok")
upgrade2(troops,"vaegir_r_extra3","vaegir_r_otrok","vaegir_r_pasynok")
upgrade2(troops,"vaegir_r_extra4","vaegir_r_otrok","vaegir_r_pasynok")
upgrade2(troops,"vaegir_r_extra5","vaegir_r_otrok","vaegir_r_pasynok")
#Tier 2-3
upgrade2(troops,"vaegir_r_otrok","vaegir_r_kazak","vaegir_r_kmet")
upgrade2(troops,"vaegir_r_pasynok","vaegir_r_kmet","vaegir_r_grid")
#Tier 3-4
upgrade(troops,"vaegir_r_kazak","vaegir_r_yesaul")
upgrade2(troops,"vaegir_r_kmet","vaegir_r_ratnik","vaegir_r_zalstrelshik")
upgrade2(troops,"vaegir_r_grid","vaegir_r_plastun","vaegir_r_mladshiy_druzhinnik")
#Tier 4-5
upgrade(troops,"vaegir_r_yesaul","vaegir_r_ataman")
upgrade(troops,"vaegir_r_zalstrelshik","vaegir_r_luchnik")
upgrade(troops,"vaegir_r_mladshiy_druzhinnik","vaegir_r_druzhinnik_veteran")
#Tier 5-6
upgrade(troops,"vaegir_r_luchnik","vaegir_r_metkiy_luchnik")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"vaegir_e_kholop","vaegir_e_otrok","vaegir_e_pasynok")
upgrade2(troops,"vaegir_e_extra1","vaegir_e_otrok","vaegir_e_pasynok")
upgrade2(troops,"vaegir_e_extra2","vaegir_e_otrok","vaegir_e_pasynok")
upgrade2(troops,"vaegir_e_extra3","vaegir_e_otrok","vaegir_e_pasynok")
upgrade2(troops,"vaegir_e_extra4","vaegir_e_otrok","vaegir_e_pasynok")
upgrade2(troops,"vaegir_e_extra5","vaegir_e_otrok","vaegir_e_pasynok")
#Tier 2-3
upgrade2(troops,"vaegir_e_otrok","vaegir_e_kazak","vaegir_e_kmet")
upgrade2(troops,"vaegir_e_pasynok","vaegir_e_kmet","vaegir_e_grid")
#Tier 3-4
upgrade2(troops,"vaegir_e_kazak","vaegir_e_yesaul","vaegir_e_plastun")
upgrade2(troops,"vaegir_e_kmet","vaegir_e_ratnik","vaegir_e_zalstrelshik")
upgrade2(troops,"vaegir_e_grid","vaegir_e_mladshiy_druzhinnik","vaegir_e_poztoma_druzhinaik")
#Tier 4-5
upgrade2(troops,"vaegir_e_yesaul","vaegir_e_ataman","vaegir_e_pansirniy_kazan")
upgrade2(troops,"vaegir_e_ratnik","vaegir_e_posadnik","vaegir_e_golova")
upgrade(troops,"vaegir_e_zalstrelshik","vaegir_e_luchnik")
upgrade(troops,"vaegir_e_mladshiy_druzhinnik","vaegir_e_druzhinnik")
upgrade(troops,"vaegir_e_poztoma_druzhinaik","vaegir_e_druzhinnik_veteran")
#Tier 5-6
upgrade(troops,"vaegir_e_ataman","vaegir_e_legkoy_vityas")
upgrade(troops,"vaegir_e_pansirniy_kazan","vaegir_e_vityas")
upgrade(troops,"vaegir_e_posadnik","vaegir_e_voevoda")
upgrade(troops,"vaegir_e_luchnik","vaegir_e_metkiy_luchnik")
upgrade(troops,"vaegir_e_druzhinnik","vaegir_e_elitniy_druzhinnik")
#Tier 6-7
upgrade(troops,"vaegir_e_vityas","vaegir_e_bogatyr")
upgrade(troops,"vaegir_e_metkiy_luchnik","vaegir_e_sokoliniy_glaz")
##

###Khergit
##Native troop tree
#Tier 1-2
upgrade(troops,"khergit_n_tariachin","khergit_n_qarbughaci")
upgrade(troops,"khergit_n_extra1","khergit_n_qarbughaci")
upgrade(troops,"khergit_n_extra2","khergit_n_qarbughaci")
upgrade(troops,"khergit_n_extra3","khergit_n_qarbughaci")
upgrade(troops,"khergit_n_extra4","khergit_n_qarbughaci")
upgrade(troops,"khergit_n_extra5","khergit_n_qarbughaci")
#Tier 2-3
upgrade(troops,"khergit_n_qarbughaci","khergit_n_morici")
#Tier 3-4
upgrade2(troops,"khergit_n_morici","khergit_n_kipchak","khergit_n_qubuci")
#Tier 4-5
upgrade(troops,"khergit_n_qubuci","khergit_n_borjigin")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"khergit_r_tariachin","khergit_r_tsereg","khergit_r_qarbughaci")
upgrade2(troops,"khergit_r_extra1","khergit_r_qarbughaci","khergit_r_tsereg")
upgrade2(troops,"khergit_r_extra2","khergit_r_qarbughaci","khergit_r_tsereg")
upgrade2(troops,"khergit_r_extra3","khergit_r_qarbughaci","khergit_r_tsereg")
upgrade2(troops,"khergit_r_extra4","khergit_r_qarbughaci","khergit_r_tsereg")
upgrade2(troops,"khergit_r_extra5","khergit_r_qarbughaci","khergit_r_tsereg")
#Tier 2-3
upgrade(troops,"khergit_r_tsereg","khergit_r_asud")
upgrade2(troops,"khergit_r_qarbughaci","khergit_r_morici","khergit_r_abaci")
#Tier 3-4
upgrade2(troops,"khergit_r_morici","khergit_r_quaqli","khergit_r_kipchak")
upgrade2(troops,"khergit_r_abaci","khergit_r_teriguci","khergit_r_qubuci")
upgrade(troops,"khergit_r_asud","khergit_r_aqala_asud")
#Tier 4-5
upgrade(troops,"khergit_r_quaqli","khergit_r_khevtuul")
upgrade(troops,"khergit_r_teriguci","khergit_r_aqala_teriguci")
upgrade(troops,"khergit_r_qubuci","khergit_r_borjigin")
#Tier 5-6
upgrade(troops,"khergit_r_aqala_teriguci","khergit_r_keshig")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"khergit_e_tariachin","khergit_e_tsereg","khergit_e_qarbughaci")
upgrade2(troops,"khergit_e_extra1","khergit_e_tsereg","khergit_e_qarbughaci")
upgrade2(troops,"khergit_e_extra2","khergit_e_tsereg","khergit_e_qarbughaci")
upgrade2(troops,"khergit_e_extra3","khergit_e_tsereg","khergit_e_qarbughaci")
upgrade2(troops,"khergit_e_extra4","khergit_e_tsereg","khergit_e_qarbughaci")
upgrade2(troops,"khergit_e_extra5","khergit_e_tsereg","khergit_e_qarbughaci")
#Tier 2-3
upgrade2(troops,"khergit_e_tsereg","khergit_e_morici","khergit_e_asud")
upgrade2(troops,"khergit_e_qarbughaci","khergit_e_surcin","khergit_e_abaci")
#Tier 3-4
upgrade2(troops,"khergit_e_morici","khergit_e_kipchak","khergit_e_quaqli")
upgrade(troops,"khergit_e_asud","khergit_e_aqala_asud")
upgrade(troops,"khergit_e_surcin","khergit_e_aqala_surcin")
upgrade2(troops,"khergit_e_abaci","khergit_e_teriguci","khergit_e_qubuci")
#Tier 4-5
upgrade(troops,"khergit_e_kipchak","khergit_e_torguu")
upgrade(troops,"khergit_e_quaqli","khergit_e_khevtuul")
upgrade(troops,"khergit_e_aqala_asud","khergit_e_yabagharu_morici")
upgrade2(troops,"khergit_e_aqala_surcin","khergit_e_numyn_ad","khergit_e_numici")
upgrade(troops,"khergit_e_teriguci","khergit_e_aqala_teriguci")
upgrade(troops,"khergit_e_qubuci","khergit_e_borjigin")
#Tier 5-6
upgrade(troops,"khergit_e_torguu","khergit_e_khorchen")
upgrade(troops,"khergit_e_khevtuul","khergit_e_keshig")
upgrade(troops,"khergit_e_numici","khergit_e_kharvaach")
upgrade(troops,"khergit_e_aqala_teriguci","khergit_e_jurtchi")
upgrade(troops,"khergit_e_borjigin","khergit_e_aqata_borjigin")
#Tier 6-7
upgrade(troops,"khergit_e_khorchen","khergit_e_cherbi")
upgrade(troops,"khergit_e_aqata_borjigin","khergit_e_mandugai")
##

###Nord
##Native troop tree
#Tier 1-2
upgrade2(troops,"nord_n_bondi","nord_n_huskarl","nord_n_gesith")
upgrade2(troops,"nord_n_extra1","nord_n_huskarl","nord_n_gesith")
upgrade2(troops,"nord_n_extra2","nord_n_huskarl","nord_n_gesith")
upgrade2(troops,"nord_n_extra3","nord_n_huskarl","nord_n_gesith")
upgrade2(troops,"nord_n_extra4","nord_n_huskarl","nord_n_gesith")
upgrade2(troops,"nord_n_extra5","nord_n_huskarl","nord_n_gesith")
#Tier 2-3
upgrade(troops,"nord_n_huskarl","nord_n_gridman")
upgrade(troops,"nord_n_gesith","nord_n_bogmadur")
#Tier 3-4
upgrade(troops,"nord_n_gridman","nord_n_vigamadr")
upgrade(troops,"nord_n_bogmadur","nord_n_bogsveigir")
#Tier 4-5
upgrade(troops,"nord_n_vigamadr","nord_n_skjadsveinn")
#Tier 5-6
upgrade(troops,"nord_n_skjadsveinn","nord_n_husbondi")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"nord_r_bondi","nord_r_berserkr","nord_r_huskarl")
upgrade2(troops,"nord_r_extra1","nord_r_berserkr","nord_r_huskarl")
upgrade2(troops,"nord_r_extra2","nord_r_berserkr","nord_r_huskarl")
upgrade2(troops,"nord_r_extra3","nord_r_berserkr","nord_r_huskarl")
upgrade2(troops,"nord_r_extra4","nord_r_berserkr","nord_r_huskarl")
upgrade2(troops,"nord_r_extra5","nord_r_berserkr","nord_r_huskarl")
#Tier 2-3
upgrade(troops,"nord_r_berserkr","nord_r_kertilsveinr")
upgrade2(troops,"nord_r_huskarl","nord_r_gesith","nord_r_gridman")
#Tier 3-4
upgrade(troops,"nord_r_kertilsveinr","nord_r_vikingr")
upgrade2(troops,"nord_r_gesith","nord_r_bogsveigir","nord_r_hermadur")
upgrade2(troops,"nord_r_gridman","nord_r_innaesmaen","nord_r_vigamadr")
#Tier 4-5
upgrade(troops,"nord_r_hermadur","nord_r_heahgerefa")
upgrade(troops,"nord_r_vigamadr","nord_r_skjadsveinn")
#Tier 5-6
upgrade(troops,"nord_r_skjadsveinn","nord_r_husbondi")
##Expanded troop tree
#Tier 1-2
upgrade(troops,"nord_e_bondi","nord_e_berserkr")
upgrade(troops,"nord_e_extra1","nord_e_berserkr")
upgrade(troops,"nord_e_extra2","nord_e_berserkr")
upgrade(troops,"nord_e_extra3","nord_e_berserkr")
upgrade(troops,"nord_e_extra4","nord_e_berserkr")
upgrade(troops,"nord_e_extra5","nord_e_berserkr")
#Tier 2-3
upgrade2(troops,"nord_e_berserkr","nord_e_bogmadur","nord_e_gridman")
#upgrade2(troops,"nord_e_huskarl","nord_e_gesith","nord_e_gridman")
#Tier 3-4
#upgrade2(troops,"nord_e_kertilsveinr","nord_e_ascoman","nord_e_vikingr")
upgrade2(troops,"nord_e_bogmadur","nord_e_ascoman","nord_e_bogsveigir")
#upgrade2(troops,"nord_e_gesith","nord_e_bogsveigir","nord_e_hermadur")
upgrade2(troops,"nord_e_gridman","nord_e_innaesmaen","nord_e_vigamadr")
#Tier 4-5
upgrade(troops,"nord_e_ascoman","nord_e_heimthegi")
#upgrade(troops,"nord_e_vikingr","nord_e_hirdman")
#upgrade(troops,"nord_e_einhleyping","nord_e_lausaman")
#upgrade(troops,"nord_e_hermadur","nord_e_heahgerefa")
#upgrade2(troops,"nord_e_innaesmaen","nord_e_himthige","nord_e_kappi")
upgrade2(troops,"nord_e_vigamadr","nord_e_hirdman","nord_e_skjadsveinn")
#Tier 5-6
upgrade(troops,"nord_e_hirdman","nord_e_skutilsveinr")
#upgrade(troops,"nord_e_heahgerefa","nord_e_ealdorman")
#upgrade(troops,"nord_e_himthige","nord_e_erfane_himthige")
#upgrade(troops,"nord_e_kappi","nord_e_hetja")
upgrade(troops,"nord_e_skjadsveinn","nord_e_husbondi")
#Tier 6-7
upgrade(troops,"nord_e_skutilsveinr","nord_e_aetheling")
upgrade(troops,"nord_e_husbondi","nord_e_vaeringi")
##

###Rhodok
##Native troop tree
#Tier 1-2
upgrade2(troops,"rhodok_n_cittadino","rhodok_n_novizio","rhodok_n_recluta_balestriere")
upgrade2(troops,"rhodok_n_extra1","rhodok_n_novizio","rhodok_n_recluta_balestriere")
upgrade2(troops,"rhodok_n_extra2","rhodok_n_novizio","rhodok_n_recluta_balestriere")
upgrade2(troops,"rhodok_n_extra3","rhodok_n_novizio","rhodok_n_recluta_balestriere")
upgrade2(troops,"rhodok_n_extra4","rhodok_n_novizio","rhodok_n_recluta_balestriere")
upgrade2(troops,"rhodok_n_extra5","rhodok_n_novizio","rhodok_n_recluta_balestriere")
#Tier 2-3
upgrade(troops,"rhodok_n_novizio","rhodok_n_milizia")
upgrade(troops,"rhodok_n_recluta_balestriere","rhodok_n_milizia_balestriere")
#Tier 3-4
upgrade(troops,"rhodok_n_milizia","rhodok_n_fante")
upgrade(troops,"rhodok_n_milizia_balestriere","rhodok_n_balestriere")
#Tier 4-5
upgrade(troops,"rhodok_n_fante","rhodok_n_veterano")
upgrade(troops,"rhodok_n_balestriere","rhodok_n_balestriere_veterano")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"rhodok_r_cittadino","rhodok_r_novizio","rhodok_r_recluta")
upgrade2(troops,"rhodok_r_extra1","rhodok_r_novizio","rhodok_r_recluta")
upgrade2(troops,"rhodok_r_extra2","rhodok_r_novizio","rhodok_r_recluta")
upgrade2(troops,"rhodok_r_extra3","rhodok_r_novizio","rhodok_r_recluta")
upgrade2(troops,"rhodok_r_extra4","rhodok_r_novizio","rhodok_r_recluta")
upgrade2(troops,"rhodok_r_extra5","rhodok_r_novizio","rhodok_r_recluta")
#Tier 2-3
upgrade(troops,"rhodok_r_novizio","rhodok_r_lanciere_a_cavallo")
upgrade2(troops,"rhodok_r_recluta","rhodok_r_recluta_balestriere","rhodok_r_lanciere")
#Tier 3-4
upgrade(troops,"rhodok_r_lanciere_a_cavallo","rhodok_r_lanza_spezzata")
upgrade2(troops,"rhodok_r_recluta_balestriere","rhodok_r_balestriere","rhodok_r_balestriere_leggero")
upgrade2(troops,"rhodok_r_lanciere","rhodok_r_lanciere_veterano","rhodok_r_fante")
#Tier 4-5
upgrade(troops,"rhodok_r_balestriere_leggero","rhodok_r_balestriere_d_assedio")
upgrade(troops,"rhodok_r_lanciere_veterano","rhodok_r_picchiere_veterano")
#Tier 5-6
upgrade(troops,"rhodok_r_balestriere_d_assedio","rhodok_r_capitano_d_assedio")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"rhodok_e_cittadino","rhodok_e_novizio","rhodok_e_recluta")
upgrade2(troops,"rhodok_e_extra1","rhodok_e_novizio","rhodok_e_recluta")
upgrade2(troops,"rhodok_e_extra2","rhodok_e_novizio","rhodok_e_recluta")
upgrade2(troops,"rhodok_e_extra3","rhodok_e_novizio","rhodok_e_recluta")
upgrade2(troops,"rhodok_e_extra4","rhodok_e_novizio","rhodok_e_recluta")
upgrade2(troops,"rhodok_e_extra5","rhodok_e_novizio","rhodok_e_recluta")
#Tier 2-3
upgrade2(troops,"rhodok_e_novizio","rhodok_e_milizia","rhodok_e_milizia_balestriere")
upgrade2(troops,"rhodok_e_recluta","rhodok_e_recluta_balestriere","rhodok_e_lanciere")
#Tier 3-4
upgrade(troops,"rhodok_e_milizia","rhodok_e_fante")
upgrade2(troops,"rhodok_e_milizia_balestriere","rhodok_e_fante","rhodok_e_balestriere")
upgrade2(troops,"rhodok_e_recluta_balestriere","rhodok_e_balestriere","rhodok_e_balestriere_leggero")
upgrade2(troops,"rhodok_e_lanciere","rhodok_e_lanciere_veterano","rhodok_e_lanciere_a_cavallo")
#Tier 4-5
#upgrade(troops,"rhodok_e_provisionato","rhodok_e_guardia")
upgrade(troops,"rhodok_e_fante","rhodok_e_veterano")
upgrade(troops,"rhodok_e_balestriere","rhodok_e_balestriere_d_assedio")
upgrade(troops,"rhodok_e_balestriere_leggero","rhodok_e_balestriere_a_cavallo")
upgrade(troops,"rhodok_e_lanciere_veterano","rhodok_e_picchiere_veterano")
upgrade(troops,"rhodok_e_lanciere_a_cavallo","rhodok_e_lanza_spezzata")
#Tier 5-6
#upgrade(troops,"rhodok_e_guardia","rhodok_e_guardia_ducale")
upgrade(troops,"rhodok_e_veterano","rhodok_e_capitano_di_ventura")
upgrade(troops,"rhodok_e_balestriere_d_assedio","rhodok_e_capitano_d_assedio")
upgrade(troops,"rhodok_e_picchiere_veterano","rhodok_e_picchiere_fiammingo")
#Tier 6-7
upgrade(troops,"rhodok_e_capitano_d_assedio","rhodok_e_condottiero_d_assedio")
upgrade(troops,"rhodok_e_picchiere_fiammingo","rhodok_e_condottiero")
##

###Sarranid
##Native troop tree
#Tier 1-2
upgrade(troops,"sarranid_n_millet","sarranid_n_ajam")
upgrade(troops,"sarranid_n_extra1","sarranid_n_ajam")
upgrade(troops,"sarranid_n_extra2","sarranid_n_ajam")
upgrade(troops,"sarranid_n_extra3","sarranid_n_ajam")
upgrade(troops,"sarranid_n_extra4","sarranid_n_ajam")
upgrade(troops,"sarranid_n_extra5","sarranid_n_ajam")
#Tier 2-3
upgrade2(troops,"sarranid_n_ajam","sarranid_n_cemaat","sarranid_n_jebelus")
#Tier 3-4
upgrade2(troops,"sarranid_n_cemaat","sarranid_n_yerliyya","sarranid_n_timariot")
upgrade(troops,"sarranid_n_jebelus","sarranid_n_garip")
#Tier 4-5
upgrade(troops,"sarranid_n_yerliyya","sarranid_n_yeniceri")
upgrade(troops,"sarranid_n_timariot","sarranid_n_kapikula")
upgrade(troops,"sarranid_n_garip","sarranid_n_uluteci")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"sarranid_r_millet","sarranid_r_ajam","sarranid_r_oglan")
upgrade2(troops,"sarranid_r_extra1","sarranid_r_ajam","sarranid_r_oglan")
upgrade2(troops,"sarranid_r_extra2","sarranid_r_ajam","sarranid_r_oglan")
upgrade2(troops,"sarranid_r_extra3","sarranid_r_ajam","sarranid_r_oglan")
upgrade2(troops,"sarranid_r_extra4","sarranid_r_ajam","sarranid_r_oglan")
upgrade2(troops,"sarranid_r_extra5","sarranid_r_ajam","sarranid_r_oglan")
#Tier 2-3
upgrade2(troops,"sarranid_r_ajam","sarranid_r_azab","sarranid_r_cemaat")
upgrade(troops,"sarranid_r_oglan","sarranid_r_jebelus")
#Tier 3-4
upgrade2(troops,"sarranid_r_azab","sarranid_r_kapikulu_savari","sarranid_r_timariot")
upgrade(troops,"sarranid_r_cemaat","sarranid_r_al_haqa")
upgrade2(troops,"sarranid_r_jebelus","sarranid_r_garip","sarranid_r_badw")
#Tier 4-5
upgrade(troops,"sarranid_r_timariot","sarranid_r_kapikula")
upgrade(troops,"sarranid_r_al_haqa","sarranid_r_yerliyya")
upgrade(troops,"sarranid_r_garip","sarranid_r_uluteci")
#Tier 5-6
upgrade(troops,"sarranid_r_yerliyya","sarranid_r_yeniceri")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"sarranid_e_millet","sarranid_e_ajam","sarranid_e_oglan")
upgrade2(troops,"sarranid_e_extra1","sarranid_e_ajam","sarranid_e_oglan")
upgrade2(troops,"sarranid_e_extra2","sarranid_e_ajam","sarranid_e_oglan")
upgrade2(troops,"sarranid_e_extra3","sarranid_e_ajam","sarranid_e_oglan")
upgrade2(troops,"sarranid_e_extra4","sarranid_e_ajam","sarranid_e_oglan")
upgrade2(troops,"sarranid_e_extra5","sarranid_e_ajam","sarranid_e_oglan")
#Tier 2-3
upgrade2(troops,"sarranid_e_ajam","sarranid_e_azab","sarranid_e_cemaat")
upgrade2(troops,"sarranid_e_oglan","sarranid_e_jebelus","sarranid_e_ghulam")
#Tier 3-4
upgrade2(troops,"sarranid_e_azab","sarranid_e_al_haqa","sarranid_e_timariot")
upgrade2(troops,"sarranid_e_cemaat","sarranid_e_yerliyya","sarranid_e_kapikulu_savari")
upgrade2(troops,"sarranid_e_jebelus","sarranid_e_garip","sarranid_e_badw")
upgrade2(troops,"sarranid_e_ghulam","sarranid_e_serdengecti","sarranid_e_tabardariyya")
#Tier 4-5
upgrade(troops,"sarranid_e_timariot","sarranid_e_kapikula")
upgrade(troops,"sarranid_e_yerliyya","sarranid_e_yeniceri")
upgrade(troops,"sarranid_e_kapikulu_savari","sarranid_e_beylik")
upgrade(troops,"sarranid_e_garip","sarranid_e_uluteci")
upgrade(troops,"sarranid_e_badw","sarranid_e_akinci")
upgrade(troops,"sarranid_e_serdengecti","sarranid_e_terkes_serdengecti")
#Tier 5-6
upgrade2(troops,"sarranid_e_kapikula","sarranid_e_qilich_arslan","sarranid_e_memluk")
upgrade(troops,"sarranid_e_beylik","sarranid_e_sekban")
upgrade(troops,"sarranid_e_uluteci","sarranid_e_silahtar")
upgrade(troops,"sarranid_e_akinci","sarranid_e_sipahi")
#Tier 6-7
upgrade(troops,"sarranid_e_memluk","sarranid_e_hasham")
upgrade(troops,"sarranid_e_sipahi","sarranid_e_iqta_dar")
##
##STAT Upgrades
upgrade2(troops, "skill_monk", "skill_priest", "skill_surgeon")
upgrade(troops, "skill_priest", "skill_bishop")
###Bandits
##Native troop tree
#Looters
upgrade2(troops,"bandit_n_looter","bandit_n_mountain", "bandit_n_forest")
upgrade2(troops,"bandit_n_bandit","bandit_n_brigand","mercenary_n_soldner")
#Normal Bandits
upgrade(troops,"bandit_n_mountain","rhodok_n_cittadino")
upgrade(troops,"bandit_n_forest","swadian_n_peasant")
upgrade(troops,"bandit_n_sea_raider","nord_n_bondi")
upgrade(troops,"bandit_n_steppe","khergit_n_tariachin")
upgrade(troops,"bandit_n_taiga","vaegir_n_kholop")
upgrade(troops,"bandit_n_desert","sarranid_n_millet")
##Manhunters
upgrade(troops,"bandit_n_manhunter","bandit_n_slave_driver")
upgrade(troops,"bandit_n_slave_driver","bandit_n_slave_hunter")
upgrade(troops,"bandit_n_slave_hunter","bandit_n_slave_crusher")
upgrade(troops,"bandit_n_slave_crusher","bandit_n_slaver_chief")
##Reworked troop tree
#Looters
upgrade2(troops,"bandit_r_looter","bandit_r_bandit", "mercenary_r_edelknecht")
upgrade2(troops,"bandit_r_bandit","bandit_r_brigand","mercenary_r_halberdier")
upgrade2(troops,"bandit_r_brigand","mercenary_r_ritter","mercenary_r_reichslandser")
#Normal Bandits
upgrade2(troops,"bandit_r_mountain","rhodok_r_lanciere","rhodok_r_recluta_balestriere")
upgrade2(troops,"bandit_r_forest","swadian_r_longbowman","swadian_r_jacobite")
upgrade2(troops,"bandit_r_sea_raider","nord_r_vigamadr","nord_r_vikingr")
upgrade2(troops,"bandit_r_steppe","khergit_r_kipchak","khergit_r_qubuci")
upgrade2(troops,"bandit_r_taiga","vaegir_r_yesaul","vaegir_r_zalstrelshik")
upgrade2(troops,"bandit_r_desert","sarranid_r_timariot","sarranid_r_badw")
##Manhunters
upgrade(troops,"bandit_r_manhunter","bandit_r_slave_driver")
upgrade(troops,"bandit_r_slave_driver","bandit_r_slave_hunter")
upgrade(troops,"bandit_r_slave_hunter","bandit_r_slave_crusher")
upgrade(troops,"bandit_r_slave_crusher","bandit_r_slaver_chief")
##Expanded troop tree
#Looters
upgrade2(troops,"bandit_e_looter","bandit_e_bandit", "mercenary_e_edelknecht")
upgrade2(troops,"bandit_e_bandit","bandit_e_brigand","mercenary_e_halberdier")
upgrade2(troops,"bandit_e_brigand","mercenary_e_ritter","mercenary_e_reichslandser")
#Normal Bandits
upgrade2(troops,"bandit_e_mountain","rhodok_e_milizia","rhodok_e_recluta_balestriere")
upgrade2(troops,"bandit_e_forest","swadian_e_longbowman","swadian_e_jacobite")
upgrade2(troops,"bandit_e_sea_raider","nord_e_vigamadr","nord_e_vikingr")
upgrade2(troops,"bandit_e_steppe","khergit_e_kipchak","khergit_e_qubuci")
upgrade2(troops,"bandit_e_taiga","vaegir_e_yesaul","vaegir_e_zalstrelshik")
upgrade2(troops,"bandit_e_desert","sarranid_e_timariot","sarranid_e_badw")
##Manhunters
upgrade(troops,"bandit_e_manhunter","bandit_e_slave_driver")
upgrade(troops,"bandit_e_slave_driver","bandit_e_slave_hunter")
upgrade(troops,"bandit_e_slave_hunter","bandit_e_slave_crusher")
upgrade(troops,"bandit_e_slave_crusher","bandit_e_slaver_chief")
##



###Women
##Native troop tree
#Tier 1-2
upgrade(troops,"woman_n_refugee","woman_n_camp_follower")
upgrade(troops,"woman_n_peasant","woman_n_camp_follower")
upgrade(troops,"woman_n_extra1","woman_n_camp_follower")
upgrade(troops,"woman_n_extra2","woman_n_camp_follower")
upgrade(troops,"woman_n_extra3","woman_n_camp_follower")
upgrade(troops,"woman_n_extra4","woman_n_camp_follower")
upgrade(troops,"woman_n_extra5","woman_n_camp_follower")
#Tier 2-3
upgrade(troops,"woman_n_camp_follower","woman_n_huntress")
#Tier 3-4
upgrade(troops,"woman_n_huntress","woman_n_maiden")
#Tier 4-5
upgrade(troops,"woman_n_maiden","woman_n_swob_ridder")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"woman_r_refugee","woman_r_militia","woman_r_camp_follower")
upgrade2(troops,"woman_r_peasant","woman_r_camp_follower","woman_r_dressed_up")
upgrade2(troops,"woman_r_extra1","woman_r_militia","woman_r_camp_follower")
upgrade2(troops,"woman_r_extra2","woman_r_militia","woman_r_camp_follower")
upgrade2(troops,"woman_r_extra3","woman_r_militia","woman_r_camp_follower")
upgrade2(troops,"woman_r_extra4","woman_r_militia","woman_r_camp_follower")
upgrade2(troops,"woman_r_extra5","woman_r_militia","woman_r_camp_follower")
#Tier 2-3
upgrade(troops,"woman_r_militia","woman_r_warrior")
upgrade(troops,"woman_r_camp_follower","woman_r_huntress")
upgrade(troops,"woman_r_dressed_up","woman_r_stedinger")
#Tier 3-4
upgrade(troops,"woman_r_warrior","woman_r_truus_te_paard")
upgrade2(troops,"woman_r_huntress","woman_r_markswoman","woman_r_mounted_markswoman")
upgrade(troops,"woman_r_stedinger","woman_r_kriegerin")
#Tier 4-5
upgrade(troops,"woman_r_truus_te_paard","woman_r_swob_ridder")
upgrade(troops,"woman_r_markswoman","woman_r_virago")
upgrade(troops,"woman_r_mounted_markswoman","woman_r_amazon")
upgrade(troops,"woman_r_kriegerin","woman_r_schildmaid")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"woman_e_refugee","woman_e_militia","woman_e_camp_follower")
upgrade2(troops,"woman_e_peasant","woman_e_camp_follower","woman_e_dressed_up")
upgrade2(troops,"woman_e_extra1","woman_e_militia","woman_e_camp_follower")
upgrade2(troops,"woman_e_extra2","woman_e_militia","woman_e_camp_follower")
upgrade2(troops,"woman_e_extra3","woman_e_militia","woman_e_camp_follower")
upgrade2(troops,"woman_e_extra4","woman_e_militia","woman_e_camp_follower")
upgrade2(troops,"woman_e_extra5","woman_e_militia","woman_e_camp_follower")
#Tier 2-3
upgrade2(troops,"woman_e_militia","woman_e_warrior","woman_e_nurse")
upgrade(troops,"woman_e_camp_follower","woman_e_huntress")
upgrade2(troops,"woman_e_dressed_up","woman_e_stedinger","woman_e_hospitaller")
#Tier 3-4
upgrade2(troops,"woman_e_warrior","woman_e_sword_sister","woman_e_truus_te_paard")
upgrade(troops,"woman_e_nurse","woman_e_maiden")
upgrade2(troops,"woman_e_huntress","woman_e_markswoman","woman_e_mounted_markswoman")
upgrade(troops,"woman_e_stedinger","woman_e_kriegerin")
upgrade2(troops,"woman_e_hospitaller","woman_e_beritten_jungfrau","woman_e_jungfrau")
#Tier 4-5
upgrade(troops,"woman_e_truus_te_paard","woman_e_swob_ridder")
upgrade(troops,"woman_e_maiden","woman_e_femme_fatale")
upgrade(troops,"woman_e_markswoman","woman_e_virago")
upgrade(troops,"woman_e_mounted_markswoman","woman_e_amazon")
upgrade(troops,"woman_e_kriegerin","woman_e_schildmaid")
upgrade(troops,"woman_e_beritten_jungfrau","woman_e_schildjungfer")
#Tier 5-6
upgrade(troops,"woman_e_swob_ridder","woman_e_kenau")
upgrade(troops,"woman_e_amazon","woman_e_black_widow")
upgrade(troops,"woman_e_schildjungfer","woman_e_walkure")
##
###

### Custom Troops
##Native troop tree
#Tier 1-2
upgrade(troops,"custom_n_recruit","custom_n_militia")
#Tier 2-3
upgrade2(troops,"custom_n_militia","custom_n_guard","custom_n_page")
#Tier 3-4
upgrade2(troops,"custom_n_guard","custom_n_swordman","custom_n_archer")
upgrade(troops,"custom_n_page","custom_n_squire")
#Tier 4-5
upgrade(troops,"custom_n_swordman","custom_n_swordmaster")
upgrade(troops,"custom_n_squire","custom_n_knight")
upgrade(troops,"custom_n_archer","custom_n_expert_archer")
##Reworked troop tree
#Tier 1-2
upgrade2(troops,"custom_r_recruit","custom_r_militia","custom_r_hunter")
#Tier 2-3
upgrade2(troops,"custom_r_militia","custom_r_guard","custom_r_page")
upgrade(troops,"custom_r_hunter","custom_r_woodsman")
#Tier 3-4
upgrade2(troops,"custom_r_guard","custom_r_swordman","custom_r_spearman")
upgrade(troops,"custom_r_page","custom_r_squire")
upgrade2(troops,"custom_r_woodsman","custom_r_archer","custom_r_skirmisher")
#Tier 4-5
upgrade(troops,"custom_r_swordman","custom_r_swordmaster")
upgrade(troops,"custom_r_squire","custom_r_knight")
upgrade(troops,"custom_r_archer","custom_r_expert_archer")
upgrade(troops,"custom_r_skirmisher","custom_r_frontline_skirmisher")
##Expanded troop tree
#Tier 1-2
upgrade2(troops,"custom_e_recruit","custom_e_militia","custom_e_hunter")
#Tier 2-3
upgrade2(troops,"custom_e_militia","custom_e_guard","custom_e_page")
upgrade2(troops,"custom_e_hunter","custom_e_page","custom_e_woodsman")
#Tier 3-4
upgrade2(troops,"custom_e_guard","custom_e_swordman","custom_e_spearman")
upgrade(troops,"custom_e_page","custom_e_squire")
upgrade2(troops,"custom_e_woodsman","custom_e_archer","custom_e_skirmisher")
#Tier 4-5
upgrade(troops,"custom_e_swordman","custom_e_swordmaster")
upgrade(troops,"custom_e_spearman","custom_e_spearmaster")
upgrade2(troops,"custom_e_squire","custom_e_knight","custom_e_horse_archer")
upgrade(troops,"custom_e_archer","custom_e_expert_archer")
upgrade(troops,"custom_e_skirmisher","custom_e_frontline_skirmisher")
#Tier 5-6
upgrade(troops,"custom_e_knight","custom_e_heavy_knight")
upgrade(troops,"custom_e_horse_archer","custom_e_heavy_horse_archer")
##

# modmerger_start version=201 type=2
try:
    component_name = "troops"
    var_set = { "troops" : troops }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end