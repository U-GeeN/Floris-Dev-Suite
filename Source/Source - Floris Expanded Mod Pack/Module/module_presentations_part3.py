from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

## CC
from header_skills import *
from header_items import *
##diplomacy start+ Import for use with terrain advantage
from header_terrain_types import *
##diplomacy end+
from module_items import *
from module_my_mod_set import *
## CC

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

presentations_part3 = [


## Floris: Multiple troop trees
## Rhodok: Reworked
  ("upgrade_tree_15", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (create_mesh_overlay, reg0, "mesh_pic_arms_rhodok"),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_size, reg0, pos1),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_rhodok_r_cittadino", 60, 410), #Tier 1
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_rhodok_r_novizio", 210, 510), #Tier 2
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_rhodok_r_recluta", 210, 310),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_rhodok_r_lanciere_a_cavallo", 360, 510), #Tier 3
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_rhodok_r_recluta_balestriere", 360, 390),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_rhodok_r_lanciere", 360, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_rhodok_r_lanza_spezzata", 500, 510), #Tier 4
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_rhodok_r_balestriere", 500, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_rhodok_r_balestriere_leggero", 500, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_rhodok_r_lanciere_veterano", 500, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_rhodok_r_fante", 500, 190),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_rhodok_r_balestriere_veterano", 640, 430), #Tier 5
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_rhodok_r_balestriere_d_assedio", 640, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_rhodok_r_picchiere_veterano", 640, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_rhodok_r_capitano_d_assedio", 790, 350), #Tier 6
		
        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_r_cittadino", 115, 465), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_r_novizio", 265, 565), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_r_recluta", 265, 365),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_r_lanciere_a_cavallo", 415, 565), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_r_recluta_balestriere", 415, 445),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_r_lanciere", 415, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_r_balestriere", 545, 485), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_r_balestriere_leggero", 545, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_r_lanciere_veterano", 545,325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_r_balestriere_d_assedio", 695, 405), #Tier 5-6
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 450), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 550),
        (call_script, "script_prsnt_lines", 55, 4, 140, 350),
        (call_script, "script_prsnt_lines", 110, 4, 235, 550), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 235, 350),
        (call_script, "script_prsnt_lines", 55, 4, 290, 430),
        (call_script, "script_prsnt_lines", 55, 4, 290, 270),
        (call_script, "script_prsnt_lines", 100, 4, 390, 550), #Tier 3-4
        (call_script, "script_prsnt_lines", 50, 4, 390, 430),
        (call_script, "script_prsnt_lines", 50, 4, 440, 470),
        (call_script, "script_prsnt_lines", 50, 4, 440, 390),
        (call_script, "script_prsnt_lines", 50, 4, 390, 270),
        (call_script, "script_prsnt_lines", 50, 4, 440, 310),
        (call_script, "script_prsnt_lines", 50, 4, 440, 230),
        (call_script, "script_prsnt_lines", 110, 4, 520, 470), #Tier 4-5
        (call_script, "script_prsnt_lines", 110, 4, 520, 390),
        (call_script, "script_prsnt_lines", 110, 4, 520, 310),
        (call_script, "script_prsnt_lines", 110, 4, 665, 390), #Tier 5-6
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 200, 140, 350), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 160, 290, 270), #Tier 2-3
        (call_script, "script_prsnt_lines", 4, 80, 440, 390), #Tier 3-4
        (call_script, "script_prsnt_lines", 4, 80, 440, 230),
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 15),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_15"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),

## Floris: Multiple troop trees
## Sarranid: Reworked
  ("upgrade_tree_16", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (create_mesh_overlay, reg0, "mesh_pic_sarranid_arms"),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_size, reg0, pos1),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_sarranid_r_millet", 60, 320), #Tier 1
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_sarranid_r_ajam", 210, 410), #Tier 2
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_sarranid_r_oglan", 210, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_sarranid_r_azab", 360, 470), #Tier 3
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_sarranid_r_cemaat", 360, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_sarranid_r_jebelus", 360, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_sarranid_r_kapikulu_savari", 500, 510), #Tier 4
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_sarranid_r_timariot", 500, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_sarranid_r_al_haqa", 500, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_sarranid_r_garip", 500, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_sarranid_r_badw", 500, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_sarranid_r_kapikula", 640, 430), #Tier 5
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_sarranid_r_yerliyya", 640, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_sarranid_r_uluteci", 640, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_sarranid_r_yeniceri", 790, 350), #Tier 6
		
        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_r_millet", 115, 375), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_r_ajam", 265, 465), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_r_oglan", 265, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_r_azab", 415, 525), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_r_cemaat", 415, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_r_jebelus", 415, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_r_timariot", 545, 485), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_r_al_haqa", 545, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_r_garip", 545, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_r_yerliyya", 695, 405), #Tier 5-6
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 360), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 450),
        (call_script, "script_prsnt_lines", 55, 4, 140, 270),
        (call_script, "script_prsnt_lines", 55, 4, 235, 450), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 290, 510),
        (call_script, "script_prsnt_lines", 55, 4, 290, 390),
        (call_script, "script_prsnt_lines", 110, 4, 235, 270),
        (call_script, "script_prsnt_lines", 50, 4, 390, 510), #Tier 3-4
        (call_script, "script_prsnt_lines", 50, 4, 440, 550),
        (call_script, "script_prsnt_lines", 50, 4, 440, 470),
        (call_script, "script_prsnt_lines", 100, 4, 390, 390),
        (call_script, "script_prsnt_lines", 50, 4, 390, 270),
        (call_script, "script_prsnt_lines", 50, 4, 440, 310),
        (call_script, "script_prsnt_lines", 50, 4, 440, 230),
        (call_script, "script_prsnt_lines", 110, 4, 520, 470), #Tier 4-5
        (call_script, "script_prsnt_lines", 110, 4, 520, 390),
        (call_script, "script_prsnt_lines", 110, 4, 520, 310),
        (call_script, "script_prsnt_lines", 110, 4, 665, 390), #Tier 5-6
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 180, 140, 270), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 120, 290, 390), #Tier 2-3
        (call_script, "script_prsnt_lines", 4, 80, 440, 470), #Tier 3-4
        (call_script, "script_prsnt_lines", 4, 80, 440, 230),
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 15),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_16"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
      ]),
    ]),

## Floris: Multiple troop trees
## Mercenaries: Reworked
  ("upgrade_tree_17", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_mercenary_r_townsman", 60, 370), #Tier 1
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_mercenary_r_farmer", 60, 250),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_mercenary_r_edelknecht", 210, 430), #Tier 2
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_mercenary_r_spiessknecht", 210, 310),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_mercenary_r_armbruster", 210, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_mercenary_r_burger", 360, 430), #Tier 3
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_mercenary_r_halberdier", 360, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_mercenary_r_page", 360, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_mercenary_r_armbrust_miliz", 360, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_mercenary_r_brabanzon", 500, 430), #Tier 4
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_mercenary_r_reichslandser", 500, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_mercenary_r_ritter", 500, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_mercenary_r_armbrust_soldner", 500, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_mercenary_r_doppelsoldner", 640, 430), #Tier 5
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_mercenary_r_burgmann", 640, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_mercenary_r_komtur_ritter", 640, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_mercenary_r_armbrust_komtur", 640, 190),

        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_townsman", 115, 425), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_farmer", 115, 305),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_edelknecht", 265, 485), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_spiessknecht", 265, 365),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_armbruster", 265, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_burger", 420, 485), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_halberdier", 420, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_page", 420, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_armbrust_miliz", 420, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_brabanzon", 550, 485), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_reichslandser", 550, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_ritter", 550, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_r_armbrust_soldner", 550, 245),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 410), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 470),
        (call_script, "script_prsnt_lines", 55, 4, 140, 355),
        (call_script, "script_prsnt_lines", 55, 4, 85, 290),
        (call_script, "script_prsnt_lines", 55, 4, 140, 345),
        (call_script, "script_prsnt_lines", 55, 4, 140, 230),
        (call_script, "script_prsnt_lines", 110, 4, 235, 470), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 235, 350),
        (call_script, "script_prsnt_lines", 55, 4, 290, 390),
        (call_script, "script_prsnt_lines", 55, 4, 290, 310),
        (call_script, "script_prsnt_lines", 110, 4, 235, 230),
        (call_script, "script_prsnt_lines", 100, 4, 390, 470), #Tier 3-4
        (call_script, "script_prsnt_lines", 100, 4, 390, 390),
        (call_script, "script_prsnt_lines", 100, 4, 390, 310),
        (call_script, "script_prsnt_lines", 100, 4, 390, 230),
        (call_script, "script_prsnt_lines", 110, 4, 520, 470), #Tier 4-5
        (call_script, "script_prsnt_lines", 110, 4, 520, 390),
        (call_script, "script_prsnt_lines", 110, 4, 520, 310),
        (call_script, "script_prsnt_lines", 110, 4, 520, 230),
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 115, 140, 355), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 115, 140, 230),
        (call_script, "script_prsnt_lines", 4, 80, 290, 310), #Tier 2-3
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 17),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_17"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),

## Floris: Multiple troop trees
## Outlaws: Reworked
  ("upgrade_tree_18", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_bandit_r_looter", 60, 590), #Looters
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_bandit_r_bandit", 210, 590),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_bandit_r_brigand", 360, 590),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_bandit_r_mountain", 60, 390), #Bandits
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_bandit_r_forest", 60, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_bandit_r_sea_raider", 360, 390),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_bandit_r_steppe", 360, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_bandit_r_taiga", 640, 390),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_bandit_r_desert", 640, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_mercenary_r_edelknecht", 210, 510), #Other units: Mercenaries
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_mercenary_r_armbrust_soldner", 360, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_mercenary_r_brabanzon", 500, 590),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_mercenary_r_reichslandser", 500, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_rhodok_r_lanciere", 210, 430), #Bandit evolutions
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_rhodok_r_recluta_balestriere", 210, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_swadian_r_longbowman", 210, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_swadian_r_jacobite", 210, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 17, "trp_nord_r_vigamadr", 500, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 18, "trp_nord_r_vikingr", 500, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 19, "trp_khergit_r_kipchak", 500, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 20, "trp_khergit_r_qubuci", 500, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 21, "trp_vaegir_r_yesaul", 790, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 22, "trp_vaegir_r_zalstrelshik", 790, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 23, "trp_sarranid_r_timariot", 790, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 24, "trp_sarranid_r_badw", 790, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 25, "trp_bandit_r_manhunter", 60, 110), #Slavers
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 26, "trp_bandit_r_slave_driver", 210, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 27, "trp_bandit_r_slave_hunter", 360, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 28, "trp_bandit_r_slave_crusher", 500, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 29, "trp_bandit_r_slaver_chief", 640, 110),

        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_looter", 115, 645), #Looters
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_bandit", 265, 645),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_brigand", 420, 645),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_mountain", 115, 445), #Bandits
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_forest", 115, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_sea_raider", 420, 445),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_steppe", 420, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_taiga", 695, 445),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_desert", 695, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_manhunter", 115, 165), #Slavers
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_slave_driver", 265, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_slave_hunter", 420, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_r_slave_crusher", 550, 165),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 110, 4, 85, 630), #Looters
        (call_script, "script_prsnt_lines", 55, 4, 140, 550),
        (call_script, "script_prsnt_lines", 110, 4, 235, 630),
        (call_script, "script_prsnt_lines", 55, 4, 290, 550),
        (call_script, "script_prsnt_lines", 100, 4, 390, 630),
        (call_script, "script_prsnt_lines", 50, 4, 440, 550),
        (call_script, "script_prsnt_lines", 55, 4, 85, 430), #Bandits
        (call_script, "script_prsnt_lines", 55, 4, 140, 470),
        (call_script, "script_prsnt_lines", 55, 4, 140, 390),
        (call_script, "script_prsnt_lines", 55, 4, 85, 270),
        (call_script, "script_prsnt_lines", 55, 4, 140, 310),
        (call_script, "script_prsnt_lines", 55, 4, 140, 230),
        (call_script, "script_prsnt_lines", 50, 4, 390, 430),
        (call_script, "script_prsnt_lines", 50, 4, 440, 470),
        (call_script, "script_prsnt_lines", 50, 4, 440, 390),
        (call_script, "script_prsnt_lines", 50, 4, 390, 270),
        (call_script, "script_prsnt_lines", 50, 4, 440, 310),
        (call_script, "script_prsnt_lines", 50, 4, 440, 230),
        (call_script, "script_prsnt_lines", 55, 4, 665, 430),
        (call_script, "script_prsnt_lines", 55, 4, 720, 470),
        (call_script, "script_prsnt_lines", 55, 4, 720, 390),
        (call_script, "script_prsnt_lines", 55, 4, 665, 270),
        (call_script, "script_prsnt_lines", 55, 4, 720, 310),
        (call_script, "script_prsnt_lines", 55, 4, 720, 230),
        (call_script, "script_prsnt_lines", 110, 4, 85, 150),
        (call_script, "script_prsnt_lines", 110, 4, 235, 150),
        (call_script, "script_prsnt_lines", 100, 4, 390, 150),
        (call_script, "script_prsnt_lines", 110, 4, 520, 150),
        ##### - lines
		
        ##### | lines
        (call_script, "script_prsnt_lines", 4, 80, 140, 550), #Looters
        (call_script, "script_prsnt_lines", 4, 80, 290, 550),
        (call_script, "script_prsnt_lines", 4, 80, 440, 550),
        (call_script, "script_prsnt_lines", 4, 80, 140, 390), #Bandits
        (call_script, "script_prsnt_lines", 4, 80, 140, 230),
        (call_script, "script_prsnt_lines", 4, 80, 440, 390),
        (call_script, "script_prsnt_lines", 4, 80, 440, 230),
        (call_script, "script_prsnt_lines", 4, 80, 720, 390),
        (call_script, "script_prsnt_lines", 4, 80, 720, 230),
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 30),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_18"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),

## Floris: Multiple troop trees
## Women: Reworked
  ("upgrade_tree_19", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_woman_r_refugee", 60, 370), #Tier 1
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_woman_r_peasant", 60, 250),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_woman_r_militia", 210, 430), #Tier 2
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_woman_r_camp_follower", 210, 310),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_woman_r_dressed_up", 210, 190),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_woman_r_warrior", 360, 430), #Tier 3
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_woman_r_huntress", 360, 310),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_woman_r_stedinger", 360, 190),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_woman_r_truus_te_paard", 500, 430), #Tier 4
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_woman_r_markswoman", 500, 350),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_woman_r_mounted_markswoman", 500, 270),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_woman_r_kriegerin", 500, 190),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_woman_r_swob_ridder", 640, 430), #Tier 5
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_woman_r_virago", 640, 350),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_woman_r_amazon", 640, 270),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_woman_r_schildmaid", 640, 190),
 
        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_refugee", 115, 425), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_peasant", 115, 305),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_militia", 265, 485), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_camp_follower", 265, 365),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_dressed_up", 265, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_warrior", 420, 485), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_huntress", 420, 365),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_stedinger", 420, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_truus_te_paard", 550, 485), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_markswoman", 550, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_mounted_markswoman", 550, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_r_kriegerin", 550, 245),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 410), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 470),
        (call_script, "script_prsnt_lines", 55, 4, 140, 355),
        (call_script, "script_prsnt_lines", 55, 4, 85, 260),
        (call_script, "script_prsnt_lines", 55, 4, 140, 345),
        (call_script, "script_prsnt_lines", 55, 4, 140, 230),
        (call_script, "script_prsnt_lines", 110, 4, 235, 470), #Tier 2-3
        (call_script, "script_prsnt_lines", 110, 4, 235, 350),
        (call_script, "script_prsnt_lines", 110, 4, 235, 230),
        (call_script, "script_prsnt_lines", 100, 4, 390, 470), #Tier 3-4
        (call_script, "script_prsnt_lines", 50, 4, 390, 350),
        (call_script, "script_prsnt_lines", 50, 4, 440, 390),
        (call_script, "script_prsnt_lines", 50, 4, 440, 310),
        (call_script, "script_prsnt_lines", 100, 4, 390, 230),
        (call_script, "script_prsnt_lines", 110, 4, 520, 470), #Tier 4-5
        (call_script, "script_prsnt_lines", 110, 4, 520, 390),
        (call_script, "script_prsnt_lines", 110, 4, 520, 310),
        (call_script, "script_prsnt_lines", 110, 4, 520, 230),
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 115, 140, 355), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 115, 140, 230),
        (call_script, "script_prsnt_lines", 4, 80, 440, 310), #Tier 3-4
        ##### | lines

        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_ready"),
        ####### mouse fix pos system #######
      ]),

    #(ti_on_presentation_run,
      #[
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_run"),
        ####### mouse fix pos system #######
    #]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 16),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_19"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),

## Floris: Multiple troop trees
## Custom Troops: Reworked
  ("upgrade_tree_20", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_custom_r_recruit", 60, 320), #Tier 1
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_custom_r_militia", 210, 410), #Tier 2
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_custom_r_hunter", 210, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_custom_r_guard", 360, 470), #Tier 3
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_custom_r_page", 360, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_custom_r_woodsman", 360, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_custom_r_spearman", 500, 510), #Tier 4
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_custom_r_swordman", 500, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_custom_r_squire", 500, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_custom_r_archer", 500, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_custom_r_skirmisher", 500, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_custom_r_swordmaster", 640, 430), #Tier 5
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_custom_r_knight", 640, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_custom_r_expert_archer", 640, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_custom_r_frontline_skirmisher", 640, 190),
		
        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_r_recruit", 115, 375), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_r_militia", 265, 465), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_r_hunter", 265, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_r_guard", 415, 525), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_r_page", 415, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_r_woodsman", 415, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_r_swordman", 545, 485), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_r_squire", 545, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_r_archer", 545, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_r_skirmisher", 545, 245),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 360), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 450),
        (call_script, "script_prsnt_lines", 55, 4, 140, 270),
        (call_script, "script_prsnt_lines", 55, 4, 235, 450), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 290, 510),
        (call_script, "script_prsnt_lines", 55, 4, 290, 390),
        (call_script, "script_prsnt_lines", 110, 4, 235, 270),
        (call_script, "script_prsnt_lines", 50, 4, 390, 510), #Tier 3-4
        (call_script, "script_prsnt_lines", 50, 4, 440, 550),
        (call_script, "script_prsnt_lines", 50, 4, 440, 470),
        (call_script, "script_prsnt_lines", 100, 4, 390, 390),
        (call_script, "script_prsnt_lines", 50, 4, 390, 270),
        (call_script, "script_prsnt_lines", 50, 4, 440, 310),
        (call_script, "script_prsnt_lines", 50, 4, 440, 230),
        (call_script, "script_prsnt_lines", 110, 4, 520, 470), #Tier 4-5
        (call_script, "script_prsnt_lines", 110, 4, 520, 390),
        (call_script, "script_prsnt_lines", 110, 4, 520, 310),
        (call_script, "script_prsnt_lines", 110, 4, 520, 230),
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 180, 140, 270), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 120, 290, 390), #Tier 2-3
        (call_script, "script_prsnt_lines", 4, 80, 440, 470), #Tier 3-4
        (call_script, "script_prsnt_lines", 4, 80, 440, 230),
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 15),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_20"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),

## Floris: Multiple troop trees
## Swadian: Expanded
  ("upgrade_tree_21", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (create_mesh_overlay, reg0, "mesh_pic_arms_swadian"),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_size, reg0, pos1),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_swadian_e_peasant", 60, 340), #Tier 1
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_swadian_e_militia", 210, 490), #Tier 2
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_swadian_e_peasant_archer", 210, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_swadian_e_vougier", 360, 550), #Tier 3
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_swadian_e_page", 360, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_swadian_e_sergeant_at_arms", 360, 310),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_swadian_e_archer_militia", 360, 70),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_swadian_e_piquier", 500, 590), #Tier 4
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_swadian_e_ecuyer", 500, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_swadian_e_jacobite", 500, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_swadian_e_guard", 500, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_swadian_e_longbowman", 500, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_swadian_e_tracker", 500, 30),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_swadian_e_chevalier", 640, 510), #Tier 5
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_swadian_e_hobilar", 640, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_swadian_e_jock", 640, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_swadian_e_man_at_arms", 640, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 17, "trp_swadian_e_sheriff", 640, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 18, "trp_swadian_e_selfbow_archer", 640, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 19, "trp_swadian_e_skirmisher", 640, 30),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 20, "trp_swadian_e_chevalier_banneret", 790, 510), #Tier 6
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 21, "trp_swadian_e_highlander", 790, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 22, "trp_swadian_e_lancer", 790, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 23, "trp_swadian_e_yeoman_archer", 790, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 24, "trp_swadian_e_baron_mineures", 940, 510), #Tier 7
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 25, "trp_swadian_e_retinue_longbowman", 940, 110),
		
        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_peasant", 115, 395), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_militia", 265, 545), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_peasant_archer", 265, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_vougier", 415, 605), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_page", 415, 485),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_sergeant_at_arms", 415, 365),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_archer_militia", 415, 125),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_ecuyer", 545, 565), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_jacobite", 545, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_guard", 545, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_longbowman", 545, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_tracker", 545, 85),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_chevalier", 695, 565), #Tier 5-6
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_jock", 695, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_man_at_arms", 695, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_selfbow_archer", 695, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_chevalier_banneret", 845, 565), #Tier 6-7
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_swadian_e_yeoman_archer", 845, 165), 
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 380), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 530),
        (call_script, "script_prsnt_lines", 55, 4, 140, 230),
        (call_script, "script_prsnt_lines", 55, 4, 235, 530), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 290, 590),
        (call_script, "script_prsnt_lines", 55, 4, 290, 470),
        (call_script, "script_prsnt_lines", 55, 4, 235, 230),
        (call_script, "script_prsnt_lines", 55, 4, 290, 350),
        (call_script, "script_prsnt_lines", 55, 4, 290, 110),
        (call_script, "script_prsnt_lines", 55, 4, 385, 590), #Tier 3-4
        (call_script, "script_prsnt_lines", 50, 4, 440, 630),
        (call_script, "script_prsnt_lines", 50, 4, 440, 555),
        (call_script, "script_prsnt_lines", 55, 4, 385, 470),
        (call_script, "script_prsnt_lines", 50, 4, 440, 545),
        (call_script, "script_prsnt_lines", 50, 4, 440, 395),
        (call_script, "script_prsnt_lines", 55, 4, 385, 350),
        (call_script, "script_prsnt_lines", 50, 4, 440, 385),
        (call_script, "script_prsnt_lines", 50, 4, 440, 270),
        (call_script, "script_prsnt_lines", 55, 4, 385, 110),
        (call_script, "script_prsnt_lines", 50, 4, 440, 150),
        (call_script, "script_prsnt_lines", 50, 4, 440, 70),
        (call_script, "script_prsnt_lines", 110, 4, 520, 550), #Tier 4-5
        (call_script, "script_prsnt_lines", 55, 4, 575, 470),
        (call_script, "script_prsnt_lines", 110, 4, 520, 390),
        (call_script, "script_prsnt_lines", 55, 4, 520, 270),
        (call_script, "script_prsnt_lines", 55, 4, 575, 310),
        (call_script, "script_prsnt_lines", 55, 4, 575, 230),
        (call_script, "script_prsnt_lines", 110, 4, 520, 150),
        (call_script, "script_prsnt_lines", 110, 4, 520, 70),
        (call_script, "script_prsnt_lines", 110, 4, 665, 550), #Tier 5-6
        (call_script, "script_prsnt_lines", 110, 4, 665, 390),
        (call_script, "script_prsnt_lines", 110, 4, 665, 310),
        (call_script, "script_prsnt_lines", 110, 4, 665, 150),
        (call_script, "script_prsnt_lines", 110, 4, 815, 550), #Tier 6-7
        (call_script, "script_prsnt_lines", 110, 4, 815, 150),
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 300, 140, 230), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 120, 290, 470), #Tier 2-3
        (call_script, "script_prsnt_lines", 4, 240, 290, 110), 
        (call_script, "script_prsnt_lines", 4, 75, 440, 555), #Tier 3-4
        (call_script, "script_prsnt_lines", 4, 150, 440, 395),
        (call_script, "script_prsnt_lines", 4, 115, 440, 270),
        (call_script, "script_prsnt_lines", 4, 80, 440, 70),
        (call_script, "script_prsnt_lines", 4, 80, 575, 390), #Tier 4-5
        (call_script, "script_prsnt_lines", 4, 80, 575, 230),
        ##### | lines

        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_ready"),
        ####### mouse fix pos system #######
      ]),

    #(ti_on_presentation_run,
     #[
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_run"),
        ####### mouse fix pos system #######
    #]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 26),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_21"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
      ]),
  ]),

## Floris: Multiple troop trees
## Vaegir: Expanded
  ("upgrade_tree_22", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (create_mesh_overlay, reg0, "mesh_pic_arms_vaegir"),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_size, reg0, pos1),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_vaegir_e_kholop", 60, 270), #Tier 1
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_vaegir_e_otrok", 210, 360), #Tier 2
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_vaegir_e_pasynok", 210, 180),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_vaegir_e_kazak", 360, 470), #Tier 3
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_vaegir_e_kmet", 360, 250),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_vaegir_e_grid", 360, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_vaegir_e_yesaul", 500, 510), #Tier 4
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_vaegir_e_plastun", 500, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_vaegir_e_ratnik", 500, 310),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_vaegir_e_zalstrelshik", 500, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_vaegir_e_mladshiy_druzhinnik", 500, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_vaegir_e_poztoma_druzhinaik", 500, 30),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_vaegir_e_ataman", 640, 590), #Tier 5
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_vaegir_e_pansirniy_kazan", 640, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_vaegir_e_posadnik", 640, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_vaegir_e_golova", 640, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_vaegir_e_luchnik", 640, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 17, "trp_vaegir_e_druzhinnik", 640, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 18, "trp_vaegir_e_druzhinnik_veteran", 640, 30),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 20, "trp_vaegir_e_legkoy_vityas", 790, 590), #Tier 6
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 19, "trp_vaegir_e_vityas", 790, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 21, "trp_vaegir_e_voevoda", 790, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 22, "trp_vaegir_e_metkiy_luchnik", 790, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 23, "trp_vaegir_e_elitniy_druzhinnik", 790, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 24, "trp_vaegir_e_bogatyr", 940, 510), #Tier 7
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 25, "trp_vaegir_e_sokoliniy_glaz", 940, 190),

        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_kholop", 115, 325), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_otrok", 265, 415), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_pasynok", 265, 235),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_kazak", 420, 525), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_kmet", 420, 305),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_grid", 420, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_yesaul", 550, 565), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_ratnik", 550, 365),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_zalstrelshik", 550, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_mladshiy_druzhinnik", 550, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_poztoma_druzhinaik", 550, 85),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_ataman", 695, 645), #Tier 5-6
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_pansirniy_kazan", 695, 565),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_posadnik", 695, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_luchnik", 695, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_druzhinnik", 695, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_vityas", 845, 565), #Tier 6-7
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_vaegir_e_metkiy_luchnik", 845, 245),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 310), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 400),
        (call_script, "script_prsnt_lines", 55, 4, 140, 220),
        (call_script, "script_prsnt_lines", 55, 4, 235, 400), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 290, 510),
        (call_script, "script_prsnt_lines", 55, 4, 290, 295),
        (call_script, "script_prsnt_lines", 55, 4, 235, 220),
        (call_script, "script_prsnt_lines", 55, 4, 290, 285),
        (call_script, "script_prsnt_lines", 55, 4, 290, 150),
        (call_script, "script_prsnt_lines", 50, 4, 390, 510), #Tier 3-4
        (call_script, "script_prsnt_lines", 50, 4, 440, 550),
        (call_script, "script_prsnt_lines", 50, 4, 440, 470),
        (call_script, "script_prsnt_lines", 50, 4, 390, 290),
        (call_script, "script_prsnt_lines", 50, 4, 440, 350),
        (call_script, "script_prsnt_lines", 50, 4, 440, 230),
        (call_script, "script_prsnt_lines", 100, 4, 390, 150),
        (call_script, "script_prsnt_lines", 50, 4, 440, 70), 
        (call_script, "script_prsnt_lines", 110, 4, 520, 550), #Tier 4-5
        (call_script, "script_prsnt_lines", 55, 4, 575, 630),
        (call_script, "script_prsnt_lines", 55, 4, 520, 350),
        (call_script, "script_prsnt_lines", 55, 4, 575, 390),
        (call_script, "script_prsnt_lines", 55, 4, 575, 310),
        (call_script, "script_prsnt_lines", 110, 4, 520, 230),
        (call_script, "script_prsnt_lines", 110, 4, 520, 150),
        (call_script, "script_prsnt_lines", 110, 4, 520, 70), 
        (call_script, "script_prsnt_lines", 110, 4, 665, 630), #Tier 5-6
        (call_script, "script_prsnt_lines", 110, 4, 665, 550),
        (call_script, "script_prsnt_lines", 110, 4, 665, 390),
        (call_script, "script_prsnt_lines", 110, 4, 665, 230),
        (call_script, "script_prsnt_lines", 110, 4, 665, 150),
        (call_script, "script_prsnt_lines", 110, 4, 815, 550), #Tier 6-7
        (call_script, "script_prsnt_lines", 110, 4, 815, 230),
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 180, 140, 220), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 215, 290, 295), #Tier 2-3
        (call_script, "script_prsnt_lines", 4, 135, 290, 150),
        (call_script, "script_prsnt_lines", 4, 80, 440, 470), #Tier 3-4
        (call_script, "script_prsnt_lines", 4, 120, 440, 230),
        (call_script, "script_prsnt_lines", 4, 80, 440, 70),
        (call_script, "script_prsnt_lines", 4, 80, 575, 550), #Tier 4-5
        (call_script, "script_prsnt_lines", 4, 80, 575, 310),
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 26),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_22"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
      ]),
    ]),

## Floris: Multiple troop trees
## Khergit: Expanded
  ("upgrade_tree_23", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (create_mesh_overlay, reg0, "mesh_pic_arms_khergit"),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_size, reg0, pos1),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_khergit_e_tariachin", 60, 350), #Tier 1
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_khergit_e_tsereg", 210, 490), #Tier 2
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_khergit_e_qarbughaci", 210, 210),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_khergit_e_morici", 360, 530), #Tier 3
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_khergit_e_asud", 360, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_khergit_e_surcin", 360, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_khergit_e_abaci", 360, 150),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_khergit_e_kipchak", 500, 590), #Tier 4
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_khergit_e_quaqli", 500, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_khergit_e_aqala_asud", 500, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_khergit_e_aqala_surcin", 500, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_khergit_e_teriguci", 500, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_khergit_e_qubuci", 500, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_khergit_e_torguu", 640, 590), #Tier 5
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_khergit_e_khevtuul", 640, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_khergit_e_yabagharu_morici", 640, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_khergit_e_numyn_ad", 640, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 17, "trp_khergit_e_numici", 640, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 18, "trp_khergit_e_aqala_teriguci", 640, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 19, "trp_khergit_e_borjigin", 640, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 20, "trp_khergit_e_khorchen", 790, 590), #Tier 6
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 21, "trp_khergit_e_keshig", 790, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 22, "trp_khergit_e_kharvaach", 790, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 23, "trp_khergit_e_jurtchi", 790, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 24, "trp_khergit_e_aqata_borjigin", 790, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 25, "trp_khergit_e_cherbi", 940, 590), #Tier 7
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 26, "trp_khergit_e_mandugai", 940, 110),

        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_tariachin", 115, 405), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_tsereg", 265, 545), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_qarbughaci", 265, 265),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_morici", 420, 605), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_asud", 420, 485),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_surcin", 420, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_abaci", 420, 205),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_kipchak", 550, 645), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_quaqli", 550, 565),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_aqala_asud", 550, 485),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_aqala_surcin", 550, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_teriguci", 550, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_qubuci", 550, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_torguu", 695, 645), #Tier 5-6
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_khevtuul", 695, 565),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_numici", 695, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_aqala_teriguci", 695, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_borjigin", 695, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_khorchen", 845, 645), #Tier 6-7
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_khergit_e_aqata_borjigin", 845, 165),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 390), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 530),
        (call_script, "script_prsnt_lines", 55, 4, 140, 250),
        (call_script, "script_prsnt_lines", 55, 4, 235, 530), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 290, 590),
        (call_script, "script_prsnt_lines", 55, 4, 290, 470),
        (call_script, "script_prsnt_lines", 55, 4, 235, 250),
        (call_script, "script_prsnt_lines", 55, 4, 290, 310),
        (call_script, "script_prsnt_lines", 55, 4, 290, 190),
        (call_script, "script_prsnt_lines", 50, 4, 390, 590), #Tier 3-4
        (call_script, "script_prsnt_lines", 50, 4, 440, 630),
        (call_script, "script_prsnt_lines", 50, 4, 440, 550),
        (call_script, "script_prsnt_lines", 100, 4, 390, 470),
        (call_script, "script_prsnt_lines", 100, 4, 390, 310),
        (call_script, "script_prsnt_lines", 50, 4, 390, 190),
        (call_script, "script_prsnt_lines", 50, 4, 440, 230),
        (call_script, "script_prsnt_lines", 50, 4, 440, 150),
        (call_script, "script_prsnt_lines", 110, 4, 520, 630), #Tier 4-5
        (call_script, "script_prsnt_lines", 110, 4, 520, 550),
        (call_script, "script_prsnt_lines", 110, 4, 520, 470),
        (call_script, "script_prsnt_lines", 110, 4, 520, 310),
        (call_script, "script_prsnt_lines", 55, 4, 575, 390),
        (call_script, "script_prsnt_lines", 110, 4, 520, 230),
        (call_script, "script_prsnt_lines", 110, 4, 520, 150),
        (call_script, "script_prsnt_lines", 110, 4, 665, 630), #Tier 5-6
        (call_script, "script_prsnt_lines", 110, 4, 665, 550),
        (call_script, "script_prsnt_lines", 110, 4, 665, 310),
        (call_script, "script_prsnt_lines", 110, 4, 665, 230),
        (call_script, "script_prsnt_lines", 110, 4, 665, 150),
        (call_script, "script_prsnt_lines", 110, 4, 815, 630), #Tier 6-7
        (call_script, "script_prsnt_lines", 110, 4, 815, 150),
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 280, 140, 250), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 120, 290, 470), #Tier 2-3
        (call_script, "script_prsnt_lines", 4, 120, 290, 190),
        (call_script, "script_prsnt_lines", 4, 80, 440, 550), #Tier 3-4
        (call_script, "script_prsnt_lines", 4, 80, 440, 150),
        (call_script, "script_prsnt_lines", 4, 80, 575, 310), #Tier 4-5
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 27),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_23"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),

## Floris: Multiple troop trees
## Nord: Expanded
  ("upgrade_tree_24", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (create_mesh_overlay, reg0, "mesh_pic_arms_nord"),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_size, reg0, pos1),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_nord_e_bondi", 80, 340), #Tier 1
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_nord_e_berserkr", 215, 340), #Tier 2
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_nord_e_huskarl", 350, 270),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_nord_e_kertilsveinr", 350, 590), #Tier 3
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_nord_e_bogmadur", 350, 390),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_nord_e_gesith", 350, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_nord_e_gridman", 350, 240),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_nord_e_ascoman", 485, 440), #Tier 4
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_nord_e_vikingr", 485, 550),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_nord_e_einhleyping", 485, 470),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_nord_e_bogsveigir", 485, 340),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_nord_e_hermadur", 485, 310),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_nord_e_innaesmaen", 485, 140),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_nord_e_vigamadr", 485, 240),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_nord_e_heimthegi", 620, 440), #Tier 5
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_nord_e_hirdman", 620, 140),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_nord_e_lausaman", 620, 470),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 17, "trp_nord_e_heahgerefa", 620, 390),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 18, "trp_nord_e_himthige", 620, 310),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 19, "trp_nord_e_kappi", 620, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_nord_e_skjadsveinn", 620, 240),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_nord_e_skutilsveinr", 755, 140), #Tier 6
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 22, "trp_nord_e_ealdorman", 755, 390),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 23, "trp_nord_e_erfane_himthige", 755, 310),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 24, "trp_nord_e_hetja", 755, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_nord_e_husbondi", 755, 240),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_nord_e_aetheling", 890, 140), #Tier 7
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_nord_e_vaeringi", 890, 240),

        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_nord_e_bondi", 125, 395), #Tier 1-2: 80+45=125
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_nord_e_berserkr", 260, 395), #Tier 2-3: 215+45=260
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_nord_e_bogmadur", 395, 445), #Tier 3-4: 350+45=395
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_nord_e_gridman", 395, 295),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_nord_e_ascoman", 530, 495), #Tier 4-5: 485+45=530
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_nord_e_vigamadr", 530, 295),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_nord_e_hirdman", 665, 195), #Tier 5-6: 620+45=665
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_nord_e_skjadsveinn", 665, 295),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_nord_e_skutilsveinr", 800, 195), #Tier 6-7: 755+45=800
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_nord_e_husbondi", 800, 295),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 105, 4, 103, 380), #Tier 1-2: X: 95+8=103
        (call_script, "script_prsnt_lines", 52, 4, 238, 380), #Tier 2-3 Out: X: 230+8=238
        (call_script, "script_prsnt_lines", 53, 4, 290, 430), #Tier 2-3 In (Upper): X: 282+8=290
        (call_script, "script_prsnt_lines", 53, 4, 290, 280), #Tier 2-3 In (Lower)
        (call_script, "script_prsnt_lines", 52, 4, 373, 430), #Tier 3-4 Out (Upper): X: 365+8=373
        (call_script, "script_prsnt_lines", 53, 4, 425, 480), #Tier 3-4 In (UU): X: 417+8=425
        (call_script, "script_prsnt_lines", 53, 4, 425, 380), #Tier 3-4 In (UL)
        (call_script, "script_prsnt_lines", 52, 4, 373, 280), #Tier 3-4 Out (Lower)
        (call_script, "script_prsnt_lines", 53, 4, 425, 280), #Tier 3-4 In (Vigamadr)
        (call_script, "script_prsnt_lines", 53, 4, 425, 180), #Tier 3-4 In (Innaesmaen)
        (call_script, "script_prsnt_lines", 105, 4, 508, 480), #Tier 4-5 (Ascoman -> Heimthegi): X: 485+15=500, W: 135-30=105
        (call_script, "script_prsnt_lines", 52, 4, 508, 280), #Tier 4-5 Out (Vigamadr)
        (call_script, "script_prsnt_lines", 53, 4, 560, 280), #Tier 4-5 In (Skjadsveinn): X: 552+8=560
        (call_script, "script_prsnt_lines", 53, 4, 560, 180), #Tier 4-5 In (Hirdman)
        (call_script, "script_prsnt_lines", 105, 4, 643, 180), #Tier 5-6 (Hirdman -> Skutilsveinr): X: 635+8=643
        (call_script, "script_prsnt_lines", 105, 4, 643, 280), #Tier 5-6 (Skjadsveinn -> Husbondi)
        (call_script, "script_prsnt_lines", 105, 4, 778, 180), #Tier 6-7 (Skutilsveinr -> Aetheling): X: 770+8=778
        (call_script, "script_prsnt_lines", 105, 4, 778, 280), #Tier 6-7 (Husbondi -> Vaeringi)

        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 150, 290, 280), #Tier 2-3 Split: X: 282+8=290
        (call_script, "script_prsnt_lines", 4, 100, 425, 380), #Tier 3-4 Upper Split: X: 417+8=425
        (call_script, "script_prsnt_lines", 4, 100, 425, 180),  #Tier 3-4 Lower Split
        (call_script, "script_prsnt_lines", 4, 100, 560, 180),  #Tier 4-5 Vigamadr Split: X: 552+8=560
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 15),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_24"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),

## Floris: Multiple troop trees
## Rhodok: Expanded
  ("upgrade_tree_25", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (create_mesh_overlay, reg0, "mesh_pic_arms_rhodok"),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_size, reg0, pos1),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_rhodok_e_cittadino", 60, 355), #Tier 1
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_rhodok_e_novizio", 210, 500), #Tier 2
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_rhodok_e_recluta", 210, 210),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_rhodok_e_milizia", 360, 550), #Tier 3
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_rhodok_e_milizia_balestriere", 360, 450),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_rhodok_e_recluta_balestriere", 360, 330),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_rhodok_e_lanciere", 360, 90),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_rhodok_e_provisionato", 500, 590), #Tier 4
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_rhodok_e_fante", 500, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_rhodok_e_balestriere", 500, 390),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_rhodok_e_balestriere_leggero", 500, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_rhodok_e_lanciere_veterano", 500, 150),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_rhodok_e_lanciere_a_cavallo", 500, 30),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_rhodok_e_guardia", 640, 590), #Tier 5
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_rhodok_e_veterano", 640, 510),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_rhodok_e_balestriere_veterano", 640, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_rhodok_e_balestriere_d_assedio", 640, 390),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 17, "trp_rhodok_e_balestriere_a_cavallo", 640, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 18, "trp_rhodok_e_picchiere_veterano", 640, 150),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 19, "trp_rhodok_e_lanza_spezzata", 640, 30),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 20, "trp_rhodok_e_guardia_ducale", 790, 590), #Tier 6
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 21, "trp_rhodok_e_capitano_di_ventura", 790, 510),
#        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 22, "trp_rhodok_e_balestriere_pesante", 790, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 23, "trp_rhodok_e_capitano_d_assedio", 790, 390),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 24, "trp_rhodok_e_picchiere_fiammingo", 790, 150),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 25, "trp_rhodok_e_condottiero_d_assedio", 940, 390), #Tier 7
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 26, "trp_rhodok_e_condottiero", 940, 150),

        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_cittadino", 115, 410), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_novizio", 265, 555), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_recluta", 265, 265),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_milizia", 420, 605), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_milizia_balestriere", 420, 505),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_recluta_balestriere", 420, 385),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_lanciere", 420, 145),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_provisionato", 550, 645), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_fante", 550, 565),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_balestriere", 550, 445),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_balestriere_leggero", 550, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_lanciere_veterano", 550, 205),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_lanciere_a_cavallo", 550, 85),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_guardia", 695, 645), #Tier 5-6
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_veterano", 695, 565),
#        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_balestriere_veterano", 695, 485),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_balestriere_d_assedio", 695, 445),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_picchiere_veterano", 695, 205),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_capitano_d_assedio", 845, 445), #Tier 6-7
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_rhodok_e_picchiere_fiammingo", 845, 205),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 395), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 540),
        (call_script, "script_prsnt_lines", 55, 4, 140, 250),
        (call_script, "script_prsnt_lines", 55, 4, 235, 540), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 290, 590),
        (call_script, "script_prsnt_lines", 55, 4, 290, 490),
        (call_script, "script_prsnt_lines", 55, 4, 235, 250),
        (call_script, "script_prsnt_lines", 55, 4, 290, 370),
        (call_script, "script_prsnt_lines", 55, 4, 290, 130),
        (call_script, "script_prsnt_lines", 50, 4, 390, 590), #Tier 3-4
        (call_script, "script_prsnt_lines", 50, 4, 440, 630),
        (call_script, "script_prsnt_lines", 50, 4, 440, 555),
        (call_script, "script_prsnt_lines", 50, 4, 390, 490),
        (call_script, "script_prsnt_lines", 50, 4, 440, 545),
        (call_script, "script_prsnt_lines", 50, 4, 440, 435),
        (call_script, "script_prsnt_lines", 50, 4, 390, 370),
        (call_script, "script_prsnt_lines", 50, 4, 440, 425),
        (call_script, "script_prsnt_lines", 50, 4, 440, 310),
        (call_script, "script_prsnt_lines", 50, 4, 390, 130),
        (call_script, "script_prsnt_lines", 50, 4, 440, 190),
        (call_script, "script_prsnt_lines", 50, 4, 440, 70),
        (call_script, "script_prsnt_lines", 110, 4, 520, 630), #Tier 4-5
        (call_script, "script_prsnt_lines", 110, 4, 520, 550),
        (call_script, "script_prsnt_lines", 110, 4, 520, 430), #balestr. - balestr. d'ass.
#        (call_script, "script_prsnt_lines", 55, 4, 575, 470),
#        (call_script, "script_prsnt_lines", 55, 4, 575, 390),
        (call_script, "script_prsnt_lines", 110, 4, 520, 310),
        (call_script, "script_prsnt_lines", 110, 4, 520, 190),
        (call_script, "script_prsnt_lines", 110, 4, 520, 70),
        (call_script, "script_prsnt_lines", 110, 4, 665, 630), #Tier 5-6
        (call_script, "script_prsnt_lines", 110, 4, 665, 550),
#        (call_script, "script_prsnt_lines", 110, 4, 665, 470),
        (call_script, "script_prsnt_lines", 110, 4, 665, 430),
        (call_script, "script_prsnt_lines", 110, 4, 665, 190),
        (call_script, "script_prsnt_lines", 110, 4, 815, 430), #Tier 6-7
        (call_script, "script_prsnt_lines", 110, 4, 815, 190),
        ##### - lineS

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 290, 140, 250), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 100, 290, 490), #Tier 2-3
        (call_script, "script_prsnt_lines", 4, 240, 290, 130),
        (call_script, "script_prsnt_lines", 4, 75, 440, 555), #Tier 3-4
        (call_script, "script_prsnt_lines", 4, 110, 440, 435),
        (call_script, "script_prsnt_lines", 4, 115, 440, 310),
        (call_script, "script_prsnt_lines", 4, 120, 440, 70),
#        (call_script, "script_prsnt_lines", 4, 40, 575, 390), #Tier 4-5
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 27),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_25"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),

## Floris: Multiple troop trees
## Sarranid: Expanded
  ("upgrade_tree_26", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (create_mesh_overlay, reg0, "mesh_pic_sarranid_arms"),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_size, reg0, pos1),


        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_sarranid_e_millet", 60, 310), #Tier 1
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_sarranid_e_ajam", 210, 470), #Tier 2
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_sarranid_e_oglan", 210, 150),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_sarranid_e_azab", 360, 550), #Tier 3
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_sarranid_e_cemaat", 360, 390),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_sarranid_e_jebelus", 360, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_sarranid_e_ghulam", 360, 70),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_sarranid_e_al_haqa", 500, 590), #Tier 4
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_sarranid_e_timariot", 500, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_sarranid_e_yerliyya", 500, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_sarranid_e_kapikulu_savari", 500, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_sarranid_e_garip", 500, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_sarranid_e_badw", 500, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_sarranid_e_serdengecti", 500, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_sarranid_e_tabardariyya", 500, 30),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_sarranid_e_kapikula", 640, 510), #Tier 5
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_sarranid_e_yeniceri", 640, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 17, "trp_sarranid_e_beylik", 640, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 18, "trp_sarranid_e_uluteci", 640, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 19, "trp_sarranid_e_akinci", 640, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 20, "trp_sarranid_e_terkes_serdengecti", 640, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 21, "trp_sarranid_e_qilich_arslan", 790, 590), #Tier 6
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 22, "trp_sarranid_e_memluk", 790, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 23, "trp_sarranid_e_sekban", 790, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 24, "trp_sarranid_e_silahtar", 790, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 25, "trp_sarranid_e_sipahi", 790, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 26, "trp_sarranid_e_hasham", 940, 510), #Tier 7
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 27, "trp_sarranid_e_iqta_dar", 940, 190),

        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_millet", 115, 365), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_ajam", 265, 525), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_oglan", 265, 205),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_azab", 420, 605), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_cemaat", 420, 445),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_jebelus", 420, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_ghulam", 420, 125),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_timariot", 550, 565), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_yerliyya", 550, 485),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_kapikulu_savari", 550, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_garip", 550, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_badw", 550, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_serdengecti", 550, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_kapikula", 695, 565), #Tier 5-6
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_beylik", 695, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_uluteci", 695, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_akinci", 695, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_memluk", 845, 565), #Tier 6-7
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_sarranid_e_sipahi", 845, 245),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 350), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 510),
        (call_script, "script_prsnt_lines", 55, 4, 140, 190),
        (call_script, "script_prsnt_lines", 55, 4, 235, 510), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 290, 590),
        (call_script, "script_prsnt_lines", 55, 4, 290, 430),
        (call_script, "script_prsnt_lines", 55, 4, 235, 190),
        (call_script, "script_prsnt_lines", 55, 4, 290, 270),
        (call_script, "script_prsnt_lines", 55, 4, 290, 110),
        (call_script, "script_prsnt_lines", 50, 4, 390, 590), #Tier 3-4
        (call_script, "script_prsnt_lines", 50, 4, 440, 630),
        (call_script, "script_prsnt_lines", 50, 4, 440, 550),
        (call_script, "script_prsnt_lines", 50, 4, 390, 430),
        (call_script, "script_prsnt_lines", 50, 4, 440, 470),
        (call_script, "script_prsnt_lines", 50, 4, 440, 390),
        (call_script, "script_prsnt_lines", 50, 4, 390, 270),
        (call_script, "script_prsnt_lines", 50, 4, 440, 310),
        (call_script, "script_prsnt_lines", 50, 4, 440, 230),
        (call_script, "script_prsnt_lines", 50, 4, 390, 110),
        (call_script, "script_prsnt_lines", 50, 4, 440, 150),
        (call_script, "script_prsnt_lines", 50, 4, 440, 70),
        (call_script, "script_prsnt_lines", 110, 4, 520, 550), #Tier 4-5
        (call_script, "script_prsnt_lines", 110, 4, 520, 470),
        (call_script, "script_prsnt_lines", 110, 4, 520, 390),
        (call_script, "script_prsnt_lines", 110, 4, 520, 310),
        (call_script, "script_prsnt_lines", 110, 4, 520, 230),
        (call_script, "script_prsnt_lines", 110, 4, 520, 150),
        (call_script, "script_prsnt_lines", 110, 4, 665, 550), #Tier 5-6
        (call_script, "script_prsnt_lines", 55, 4, 720, 630),
        (call_script, "script_prsnt_lines", 110, 4, 665, 390),
        (call_script, "script_prsnt_lines", 110, 4, 665, 310),
        (call_script, "script_prsnt_lines", 110, 4, 665, 230),
        (call_script, "script_prsnt_lines", 110, 4, 815, 550), #Tier 6-7
        (call_script, "script_prsnt_lines", 110, 4, 815, 230),
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 320, 140, 190), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 160, 290, 430), #Tier 2-3
        (call_script, "script_prsnt_lines", 4, 160, 290, 110),
        (call_script, "script_prsnt_lines", 4, 80, 440, 550), #Tier 3-4
        (call_script, "script_prsnt_lines", 4, 80, 440, 390),
        (call_script, "script_prsnt_lines", 4, 80, 440, 230),
        (call_script, "script_prsnt_lines", 4, 80, 440, 70),
        (call_script, "script_prsnt_lines", 4, 80, 720, 550), #Tier 5-6
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 28),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_26"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
      ]),
    ]),

## Floris: Multiple troop trees
## Mercenaries: Expanded
  ("upgrade_tree_27", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_mercenary_e_townsman", 60, 430), #Tier 1
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_mercenary_e_farmer", 60, 150),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_mercenary_e_miliz", 210, 550), #Tier 2
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_mercenary_e_edelknecht", 210, 390),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_mercenary_e_spiessknecht", 210, 310),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_mercenary_e_armbruster", 210, 70),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_mercenary_e_brabanzon", 360, 590), #Tier 3
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_mercenary_e_burger", 360, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_mercenary_e_volksheer", 360, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_mercenary_e_halberdier", 360, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_mercenary_e_page", 360, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_mercenary_e_armbrust_soldner", 360, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_mercenary_e_armbrust_miliz", 360, 30),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_mercenary_e_ritterbroeder", 500, 590), #Tier 4
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_mercenary_e_soldner", 500, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_mercenary_e_reichslandser", 500, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_mercenary_e_ritter", 500, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 17, "trp_mercenary_e_armbrust_komtur", 500, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 18, "trp_mercenary_e_doppelsoldner", 640, 590), #Tier 5
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 19, "trp_mercenary_e_komtur", 640, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 20, "trp_mercenary_e_burgmann", 640, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 21, "trp_mercenary_e_komtur_ritter", 640, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 22, "trp_mercenary_e_kreuzritter", 640, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 23, "trp_mercenary_e_grosskomtur", 790, 430), #Tier 6
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 24, "trp_mercenary_e_landsknecht", 790, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 25, "trp_mercenary_e_hochmeister", 790, 270),

        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_townsman", 115, 485), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_farmer", 115, 205),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_miliz", 265, 605), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_edelknecht", 265, 445),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_spiessknecht", 265, 365),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_armbruster", 265, 125),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_brabanzon", 420, 645), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_volksheer", 420, 485),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_halberdier", 420, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_page", 420, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_armbrust_soldner", 420, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_ritterbroeder", 550, 645), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_soldner", 550, 485),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_reichslandser", 550, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_ritter", 550, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_komtur", 695, 485), #Tier 5-6
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_burgmann", 695, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_mercenary_e_komtur_ritter", 695, 325),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 470), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 590),
        (call_script, "script_prsnt_lines", 55, 4, 140, 430),
        (call_script, "script_prsnt_lines", 55, 4, 85, 190),
        (call_script, "script_prsnt_lines", 55, 4, 140, 350),
        (call_script, "script_prsnt_lines", 55, 4, 140, 110),
        (call_script, "script_prsnt_lines", 55, 4, 235, 590), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 290, 630),
        (call_script, "script_prsnt_lines", 55, 4, 290, 550),
        (call_script, "script_prsnt_lines", 55, 4, 235, 430),
        (call_script, "script_prsnt_lines", 55, 4, 290, 470),
        (call_script, "script_prsnt_lines", 55, 4, 290, 395),
        (call_script, "script_prsnt_lines", 55, 4, 235, 350),
        (call_script, "script_prsnt_lines", 55, 4, 290, 385),
        (call_script, "script_prsnt_lines", 55, 4, 290, 310),
        (call_script, "script_prsnt_lines", 55, 4, 235, 110),
        (call_script, "script_prsnt_lines", 55, 4, 290, 150),
        (call_script, "script_prsnt_lines", 55, 4, 290, 70),
        (call_script, "script_prsnt_lines", 100, 4, 390, 630), #Tier 3-4
        (call_script, "script_prsnt_lines", 100, 4, 390, 470),
        (call_script, "script_prsnt_lines", 100, 4, 390, 390),
        (call_script, "script_prsnt_lines", 100, 4, 390, 310),
        (call_script, "script_prsnt_lines", 100, 4, 390, 150),
        (call_script, "script_prsnt_lines", 110, 4, 520, 630), #Tier 4-5
        (call_script, "script_prsnt_lines", 110, 4, 520, 470),
        (call_script, "script_prsnt_lines", 110, 4, 520, 390),
        (call_script, "script_prsnt_lines", 110, 4, 520, 310),
        (call_script, "script_prsnt_lines", 55, 4, 575, 230),
        (call_script, "script_prsnt_lines", 110, 4, 665, 470), #Tier 5-6
        (call_script, "script_prsnt_lines", 110, 4, 665, 390),
        (call_script, "script_prsnt_lines", 110, 4, 665, 310),
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 160, 140, 430), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 240, 140, 110),
        (call_script, "script_prsnt_lines", 4, 80, 290, 550), #Tier 2-3
        (call_script, "script_prsnt_lines", 4, 75, 290, 395),
        (call_script, "script_prsnt_lines", 4, 75, 290, 310),
        (call_script, "script_prsnt_lines", 4, 80, 290, 70),
        (call_script, "script_prsnt_lines", 4, 80, 575, 230), #Tier 4-5
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 26),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_27"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),

## Floris: Multiple troop trees
## Outlaws: Expanded
  ("upgrade_tree_28", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_bandit_e_looter", 60, 590), #Looters
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_bandit_e_bandit", 210, 590),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_bandit_e_brigand", 360, 590),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_bandit_e_mountain", 60, 390), #Bandits
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_bandit_e_forest", 60, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_bandit_e_sea_raider", 360, 390),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_bandit_e_steppe", 360, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_bandit_e_taiga", 640, 390),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_bandit_e_desert", 640, 230),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_mercenary_e_edelknecht", 210, 510), #Other units: Mercenaries
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_mercenary_e_armbrust_soldner", 360, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_mercenary_e_soldner", 500, 590),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_mercenary_e_reichslandser", 500, 510),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_rhodok_e_milizia", 210, 430), #Bandit evolutions
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_rhodok_e_recluta_balestriere", 210, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_swadian_e_longbowman", 210, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_swadian_e_jacobite", 210, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 17, "trp_nord_e_vigamadr", 500, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 18, "trp_nord_e_vikingr", 500, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 19, "trp_khergit_e_kipchak", 500, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 20, "trp_khergit_e_qubuci", 500, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 21, "trp_vaegir_e_yesaul", 790, 430),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 22, "trp_vaegir_e_zalstrelshik", 790, 350),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 23, "trp_sarranid_e_timariot", 790, 270),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 24, "trp_sarranid_e_badw", 790, 190),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 25, "trp_bandit_e_manhunter", 60, 110), #Slavers
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 26, "trp_bandit_e_slave_driver", 210, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 27, "trp_bandit_e_slave_hunter", 360, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 28, "trp_bandit_e_slave_crusher", 500, 110),
        (call_script, "script_prsnt_upgrade_tree_troop_and_name", 29, "trp_bandit_e_slaver_chief", 640, 110),

        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_looter", 115, 645), #Looters
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_bandit", 265, 645),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_brigand", 420, 645),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_mountain", 115, 445), #Bandits
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_forest", 115, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_sea_raider", 420, 445),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_steppe", 420, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_taiga", 695, 445),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_desert", 695, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_manhunter", 115, 165), #Slavers
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_slave_driver", 265, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_slave_hunter", 420, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_bandit_e_slave_crusher", 550, 165),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 110, 4, 85, 630), #Looters
        (call_script, "script_prsnt_lines", 55, 4, 140, 550),
        (call_script, "script_prsnt_lines", 110, 4, 235, 630),
        (call_script, "script_prsnt_lines", 55, 4, 290, 550),
        (call_script, "script_prsnt_lines", 100, 4, 390, 630),
        (call_script, "script_prsnt_lines", 50, 4, 440, 550),
        (call_script, "script_prsnt_lines", 55, 4, 85, 430), #Bandits
        (call_script, "script_prsnt_lines", 55, 4, 140, 470),
        (call_script, "script_prsnt_lines", 55, 4, 140, 390),
        (call_script, "script_prsnt_lines", 55, 4, 85, 270),
        (call_script, "script_prsnt_lines", 55, 4, 140, 310),
        (call_script, "script_prsnt_lines", 55, 4, 140, 230),
        (call_script, "script_prsnt_lines", 55, 4, 390, 430),
        (call_script, "script_prsnt_lines", 55, 4, 440, 470),
        (call_script, "script_prsnt_lines", 55, 4, 440, 390),
        (call_script, "script_prsnt_lines", 55, 4, 390, 270),
        (call_script, "script_prsnt_lines", 55, 4, 440, 310),
        (call_script, "script_prsnt_lines", 55, 4, 440, 230),
        (call_script, "script_prsnt_lines", 55, 4, 665, 430),
        (call_script, "script_prsnt_lines", 55, 4, 720, 470),
        (call_script, "script_prsnt_lines", 55, 4, 720, 390),
        (call_script, "script_prsnt_lines", 55, 4, 665, 270),
        (call_script, "script_prsnt_lines", 55, 4, 720, 310),
        (call_script, "script_prsnt_lines", 55, 4, 720, 230),
        (call_script, "script_prsnt_lines", 110, 4, 85, 150),
        (call_script, "script_prsnt_lines", 110, 4, 235, 150),
        (call_script, "script_prsnt_lines", 100, 4, 390, 150),
        (call_script, "script_prsnt_lines", 110, 4, 520, 150),
        ##### - lines
		
        ##### | lines
        (call_script, "script_prsnt_lines", 4, 80, 140, 550), #Looters
        (call_script, "script_prsnt_lines", 4, 80, 290, 550),
        (call_script, "script_prsnt_lines", 4, 80, 440, 550),
        (call_script, "script_prsnt_lines", 4, 80, 140, 390), #Bandits
        (call_script, "script_prsnt_lines", 4, 80, 140, 230),
        (call_script, "script_prsnt_lines", 4, 80, 440, 390),
        (call_script, "script_prsnt_lines", 4, 80, 440, 230),
        (call_script, "script_prsnt_lines", 4, 80, 720, 390),
        (call_script, "script_prsnt_lines", 4, 80, 720, 230),
        ##### | lines
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 30),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_28"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),

## Floris: Multiple troop trees
## Women: Expanded
  ("upgrade_tree_29", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_woman_e_refugee", 60, 400), #Tier 1
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_woman_e_peasant", 60, 220),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_woman_e_militia", 210, 490), #Tier 2
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_woman_e_camp_follower", 210, 310),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_woman_e_dressed_up", 210, 130),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_woman_e_warrior", 360, 550), #Tier 3
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_woman_e_nurse", 360, 430),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_woman_e_huntress", 360, 310),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_woman_e_stedinger", 360, 190),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_woman_e_hospitaller", 360, 70),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_woman_e_sword_sister", 500, 590), #Tier 4
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_woman_e_truus_te_paard", 500, 510),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_woman_e_maiden", 500, 430),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_woman_e_markswoman", 500, 350),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_woman_e_mounted_markswoman", 500, 270),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_woman_e_kriegerin", 500, 190),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_woman_e_beritten_jungfrau", 500, 110),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 17, "trp_woman_e_jungfrau", 500, 30),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 18, "trp_woman_e_swob_ridder", 640, 510), #Tier 5
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 19, "trp_woman_e_femme_fatale", 640, 430),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 20, "trp_woman_e_virago", 640, 350),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 21, "trp_woman_e_amazon", 640, 270),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 22, "trp_woman_e_schildmaid", 640, 190),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 23, "trp_woman_e_schildjungfer", 640, 110),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 24, "trp_woman_e_kenau", 790, 510), #Tier 6
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 25, "trp_woman_e_black_widow", 790, 270),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 26, "trp_woman_e_walkure", 790, 110),
 
        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_refugee", 115, 455), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_peasant", 115, 275),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_militia", 265, 545), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_camp_follower", 265, 365),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_dressed_up", 265, 185),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_warrior", 420, 605), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_nurse", 420, 485),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_huntress", 420, 365),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_stedinger", 420, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_hospitaller", 420, 125),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_truus_te_paard", 550, 565), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_maiden", 550, 485),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_markswoman", 550, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_mounted_markswoman", 550, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_kriegerin", 550, 245),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_beritten_jungfrau", 550, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_swob_ridder", 695, 565), #Tier 5-6
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_amazon", 695, 325),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_woman_e_schildmaid", 695, 165),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 440), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 530),
        (call_script, "script_prsnt_lines", 55, 4, 140, 355),
        (call_script, "script_prsnt_lines", 55, 4, 85, 260),
        (call_script, "script_prsnt_lines", 55, 4, 140, 345),
        (call_script, "script_prsnt_lines", 55, 4, 140, 170),
        (call_script, "script_prsnt_lines", 55, 4, 235, 530), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 290, 590),
        (call_script, "script_prsnt_lines", 55, 4, 290, 470),
        (call_script, "script_prsnt_lines", 110, 4, 235, 350),
        (call_script, "script_prsnt_lines", 55, 4, 235, 170),
        (call_script, "script_prsnt_lines", 55, 4, 290, 230),
        (call_script, "script_prsnt_lines", 55, 4, 290, 110),
        (call_script, "script_prsnt_lines", 50, 4, 390, 590), #Tier 3-4
        (call_script, "script_prsnt_lines", 50, 4, 440, 630),
        (call_script, "script_prsnt_lines", 50, 4, 440, 550),
        (call_script, "script_prsnt_lines", 100, 4, 390, 470),
        (call_script, "script_prsnt_lines", 50, 4, 390, 350),
        (call_script, "script_prsnt_lines", 50, 4, 440, 390),
        (call_script, "script_prsnt_lines", 50, 4, 440, 310),
        (call_script, "script_prsnt_lines", 100, 4, 390, 230),
        (call_script, "script_prsnt_lines", 50, 4, 390, 110),
        (call_script, "script_prsnt_lines", 50, 4, 440, 150),
        (call_script, "script_prsnt_lines", 50, 4, 440, 70),
        (call_script, "script_prsnt_lines", 110, 4, 520, 550), #Tier 4-5
        (call_script, "script_prsnt_lines", 110, 4, 520, 470),
        (call_script, "script_prsnt_lines", 110, 4, 520, 390),
        (call_script, "script_prsnt_lines", 110, 4, 520, 310),
        (call_script, "script_prsnt_lines", 110, 4, 520, 230),
        (call_script, "script_prsnt_lines", 110, 4, 520, 150),
        (call_script, "script_prsnt_lines", 110, 4, 665, 550), #Tier 5-6
        (call_script, "script_prsnt_lines", 110, 4, 665, 310),
        (call_script, "script_prsnt_lines", 110, 4, 665, 150),
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 175, 140, 355), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 175, 140, 170),
        (call_script, "script_prsnt_lines", 4, 120, 290, 470), #Tier 2-3
        (call_script, "script_prsnt_lines", 4, 120, 290, 110),
        (call_script, "script_prsnt_lines", 4, 80, 440, 550), #Tier 3-4
        (call_script, "script_prsnt_lines", 4, 80, 440, 550),
        (call_script, "script_prsnt_lines", 4, 80, 440, 310),
        (call_script, "script_prsnt_lines", 4, 80, 440, 70),
        ##### | lines

        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_ready"),
        ####### mouse fix pos system #######
      ]),

    #(ti_on_presentation_run,
      #[
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_run"),
        ####### mouse fix pos system #######
    #]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 27),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_29"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),

## Floris: Multiple troop trees
## Custom Troops: Expanded
  ("upgrade_tree_30", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (call_script, "script_prsnt_upgrade_tree_ready"),

		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 0, "trp_custom_e_recruit", 60, 230), #Tier 1
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 1, "trp_custom_e_militia", 210, 310), #Tier 2
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 2, "trp_custom_e_hunter", 210, 150),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 3, "trp_custom_e_guard", 360, 390), #Tier 3
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 4, "trp_custom_e_page", 360, 230),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 5, "trp_custom_e_woodsman", 360, 70),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 6, "trp_custom_e_swordman", 500, 430), #Tier 4
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 7, "trp_custom_e_spearman", 500, 350),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 8, "trp_custom_e_squire", 500, 230),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 9, "trp_custom_e_archer", 500, 110),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 10, "trp_custom_e_skirmisher", 500, 30),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 11, "trp_custom_e_swordmaster", 640, 430), #Tier 5
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 12, "trp_custom_e_spearmaster", 640, 350),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 13, "trp_custom_e_knight", 640, 270),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 14, "trp_custom_e_horse_archer", 640, 190),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 15, "trp_custom_e_expert_archer", 640, 110),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 16, "trp_custom_e_frontline_skirmisher", 640, 30),
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 17, "trp_custom_e_heavy_knight", 790, 270), #Tier 6
		(call_script, "script_prsnt_upgrade_tree_troop_and_name", 18, "trp_custom_e_heavy_horse_archer", 790, 190),

        ## cost
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_recruit", 115, 285), #Tier 1-2
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_militia", 265, 365), #Tier 2-3
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_hunter", 265, 205),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_guard", 420, 445), #Tier 3-4
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_page", 420, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_woodsman", 420, 125),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_swordman", 550, 485), #Tier 4-5
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_spearman", 550, 405),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_squire", 550, 285),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_archer", 550, 165),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_skirmisher", 550, 85),
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_knight", 695, 325), #Tier 5-6
        (call_script, "script_prsnt_upgrade_tree_troop_cost", "trp_custom_e_horse_archer", 695, 245),
        ## cost

        ##### - lines
        (call_script, "script_prsnt_lines", 55, 4, 85, 270), #Tier 1-2
        (call_script, "script_prsnt_lines", 55, 4, 140, 350),
        (call_script, "script_prsnt_lines", 55, 4, 140, 190),
        (call_script, "script_prsnt_lines", 55, 4, 235, 350), #Tier 2-3
        (call_script, "script_prsnt_lines", 55, 4, 290, 430),
        (call_script, "script_prsnt_lines", 55, 4, 290, 275),
        (call_script, "script_prsnt_lines", 55, 4, 235, 190),
        (call_script, "script_prsnt_lines", 55, 4, 290, 265),
        (call_script, "script_prsnt_lines", 55, 4, 290, 110),
        (call_script, "script_prsnt_lines", 50, 4, 390, 430), #Tier 3-4
        (call_script, "script_prsnt_lines", 50, 4, 440, 470),
        (call_script, "script_prsnt_lines", 50, 4, 440, 390),
        (call_script, "script_prsnt_lines", 100, 4, 390, 270),
        (call_script, "script_prsnt_lines", 50, 4, 390, 110),
        (call_script, "script_prsnt_lines", 50, 4, 440, 150),
        (call_script, "script_prsnt_lines", 50, 4, 440, 70),
        (call_script, "script_prsnt_lines", 110, 4, 520, 470), #Tier 4-5
        (call_script, "script_prsnt_lines", 110, 4, 520, 390),
        (call_script, "script_prsnt_lines", 55, 4, 520, 270),
        (call_script, "script_prsnt_lines", 55, 4, 575, 310),
        (call_script, "script_prsnt_lines", 55, 4, 575, 230),
        (call_script, "script_prsnt_lines", 110, 4, 520, 150),
        (call_script, "script_prsnt_lines", 110, 4, 520, 70),
        (call_script, "script_prsnt_lines", 110, 4, 665, 310), #Tier 5-6
        (call_script, "script_prsnt_lines", 110, 4, 665, 230),
        ##### - lines

        ##### | lines
        (call_script, "script_prsnt_lines", 4, 160, 140, 190), #Tier 1-2
        (call_script, "script_prsnt_lines", 4, 155, 290, 275), #Tier 2-3
        (call_script, "script_prsnt_lines", 4, 155, 290, 110),
        (call_script, "script_prsnt_lines", 4, 80, 440, 390), #Tier 3-4
        (call_script, "script_prsnt_lines", 4, 80, 440, 70),
        (call_script, "script_prsnt_lines", 4, 80, 575, 230), #Tier 4-5
        ##### | lines

      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        (call_script, "script_prsnt_upgrade_tree_switch", ":object", ":value"),

        (try_for_range, ":slot_no", 0, 19),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, "$temp", "trp_temp_array_b", ":slot_no"),
          (assign, "$g_presentation_next_presentation", "prsnt_upgrade_tree_30"),
          (start_presentation, "prsnt_troop_note"),
        (try_end),
    ]),
  ]),
##

  ("troop_note", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        ## init troop items
        (call_script, "script_copy_inventory", "$temp", "trp_temp_array_a"),
        (try_for_range, ":i_slot", 0, 10),
          (troop_get_inventory_slot, ":item", "trp_temp_array_a", ":i_slot"),
          (gt, ":item", -1),
          (troop_add_item,"trp_temp_array_a",":item"),
          (troop_set_inventory_slot, "trp_temp_array_a", ":i_slot", -1),
        (try_end),

        ## back
        (create_game_button_overlay, "$g_presentation_obj_1", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_1", pos1),

        ################
        (store_mul, ":cur_troop", "$temp", 2), #with weapons
        (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_game_party_window", ":cur_troop"),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, reg0, pos1),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 350),
        (overlay_set_position, reg0, pos1),

        (str_store_troop_name, s1, "$temp"),
        (store_character_level, ":troop_level", "$temp"),
        (assign, reg1, ":troop_level"),
        (str_store_string, s1, "@Name: {s1}^Level: {reg1}"),
        (call_script, "script_get_troop_max_hp", "$temp"),
        (str_store_string, s1, "@{s1}^HP: {reg0}"),

        (create_text_overlay, reg0, "@{s1}", tf_double_space),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_position, reg0, pos1),

        (str_store_string, s3, "@Attributes:"),
        (store_attribute_level, reg1, "$temp", ca_strength),
        (store_attribute_level, reg2, "$temp", ca_intelligence),
        (str_store_string, s3, "@{s3}^STR: {reg1}^INT: {reg2}^^Skills:"),
        (store_skill_level, reg1, skl_power_strike, "$temp"),
        (store_skill_level, reg2, skl_power_draw, "$temp"),
        (store_skill_level, reg3, skl_power_throw, "$temp"),
        (store_skill_level, reg4, skl_horse_archery, "$temp"),
        (str_store_string, s3, "@{s3}^Power Strike: {reg1}^Power Draw: {reg2}^Power Throw: {reg3}^Horse Archery: {reg4}^^Weapon Proficiencies:"),
        (store_proficiency_level, reg1, "$temp", wpt_one_handed_weapon),
        (store_proficiency_level, reg2, "$temp", wpt_two_handed_weapon),
        (store_proficiency_level, reg3, "$temp", wpt_polearm),
        (str_store_string, s3, "@{s3}^1 Hand Wpns: {reg1}^2 Hand Wpns: {reg2}^Polearms: {reg3}"),
        (create_text_overlay, reg0, "@{s3}", tf_double_space),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg0, pos1),

        (str_store_string, s4, "str_empty_string"),
        (store_attribute_level, reg1, "$temp", ca_agility),
        (store_attribute_level, reg2, "$temp", ca_charisma),
        (str_store_string, s4, "@{s4}^AGI: {reg1}^CHA: {reg2}^^"),
        (store_skill_level, reg1, skl_ironflesh, "$temp"),
        (store_skill_level, reg2, skl_athletics, "$temp"),
        (store_skill_level, reg3, skl_shield, "$temp"),
        (store_skill_level, reg4, skl_riding, "$temp"),
        (str_store_string, s4, "@{s4}^Ironflesh: {reg1}^Athletics: {reg2}^Shield: {reg3}^Riding: {reg4}^^"),
        (store_proficiency_level, reg1, "$temp", wpt_archery),
        (store_proficiency_level, reg2, "$temp", wpt_crossbow),
        (store_proficiency_level, reg3, "$temp", wpt_throwing),
        (str_store_string, s4, "@{s4}^Archery: {reg1}^Crossbows: {reg2}^Throwing: {reg3}"),
        (create_text_overlay, reg0, "@{s4}", tf_double_space),
        (position_set_x, pos1, 710),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg0, pos1),
        ################

        (str_clear, s0),
        (create_text_overlay, "$g_presentation_obj_2", s0, tf_scrollable),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 50),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 560),
        (overlay_set_area_size, "$g_presentation_obj_2", pos1),
        (set_container_overlay, "$g_presentation_obj_2"),

        (assign, ":pos_x", 0),
        (assign, ":pos_y", 1840),
        (assign, ":slot_no", 10),
        (try_for_range, ":unused_height", 0, 24),
          (try_for_range, ":unused_width", 0, 4),
            (create_mesh_overlay, reg1, "mesh_inv_slot"),
            (position_set_x, pos1, 800),
            (position_set_y, pos1, 800),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, ":pos_x"),
            (position_set_y, pos1, ":pos_y"),
            (overlay_set_position, reg1, pos1),
            (create_mesh_overlay, reg1, "mesh_mp_inventory_choose"),
            (position_set_x, pos1, 640),
            (position_set_y, pos1, 640),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, ":pos_x"),
            (position_set_y, pos1, ":pos_y"),
            (overlay_set_position, reg1, pos1),
            (troop_set_slot, "trp_temp_array_a", ":slot_no", reg1),
            (troop_get_inventory_slot, ":item_no", "trp_temp_array_a", ":slot_no"),
            (try_begin),
              (gt, ":item_no", -1),
              (create_mesh_overlay_with_item_id, reg1, ":item_no"),
              (position_set_x, pos1, 800),
              (position_set_y, pos1, 800),
              (overlay_set_size, reg1, pos1),
              (store_add, ":item_x", ":pos_x", 40),
              (store_add, ":item_y", ":pos_y", 40),
              (position_set_x, pos1, ":item_x"),
              (position_set_y, pos1, ":item_y"),
              (overlay_set_position, reg1, pos1),
              (troop_set_slot, "trp_temp_array_b", ":slot_no", reg1),
            (try_end),
            (val_add, ":pos_x", 80),
            (val_add, ":slot_no", 1),
          (try_end),
          (assign, ":pos_x", 0),
          (val_sub, ":pos_y", 80),
        (try_end),

        (set_container_overlay, -1),

        (create_text_overlay, reg1, "@Equipments: ", tf_vertical_align_center),
        (position_set_x, pos1, 60),
        (position_set_y, pos1, 635),
        (overlay_set_position, reg1, pos1),
        ## items

#        ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_ready"),
#        ####### mouse fix pos system #######
      ]),

#    (ti_on_presentation_run,
#      [
#        ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_run"),
#        ####### mouse fix pos system #######
#    ]),

    (ti_on_presentation_mouse_enter_leave,
      [
      (store_trigger_param_1, ":object"),
      (store_trigger_param_2, ":enter_leave"),

      (try_begin),
        (eq, ":enter_leave", 0),
        (try_for_range, ":slot_no", 10, 106),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_inventory_slot, ":item_no", "trp_temp_array_a", ":slot_no"),
          (try_begin),
            (gt, ":item_no", -1),
            (troop_get_slot, ":target_obj", "trp_temp_array_b", ":slot_no"),
            (overlay_get_position, pos0, ":target_obj"),
            (show_item_details, ":item_no", pos0, 100),
            (assign, "$g_current_opened_item_details", ":slot_no"),
          (try_end),
        (try_end),
      (else_try),
        (try_for_range, ":slot_no", 10, 106),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (try_begin),
            (eq, "$g_current_opened_item_details", ":slot_no"),
            (close_item_details),
          (try_end),
        (try_end),
      (try_end),
    ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (try_begin),
            (gt, "$g_presentation_next_presentation", -1),
            ##Floris - MTT Begin
			#(store_sub, "$temp_2", "$g_presentation_next_presentation", "prsnt_upgrade_tree_1"),
			(try_begin),
				(eq, "$troop_trees", troop_trees_0),
				(store_sub, "$temp_2", "$g_presentation_next_presentation", "prsnt_upgrade_tree_1"),
			(else_try),
				(eq, "$troop_trees", troop_trees_1),
				(store_sub, "$temp_2", "$g_presentation_next_presentation", "prsnt_upgrade_tree_11"),
			(else_try),
				(eq, "$troop_trees", troop_trees_2),
				(store_sub, "$temp_2", "$g_presentation_next_presentation", "prsnt_upgrade_tree_21"),
			(try_end),
			##Floris - MTT End
            (start_presentation, "$g_presentation_next_presentation"),
          (else_try),
            (presentation_set_duration, 0),
          (try_end),
        (try_end),
    ]),
  ]),
##

  ("all_items", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (create_combo_label_overlay, "$g_presentation_obj_1"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 675),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_add_item, "$g_presentation_obj_1", "@One-Handed Weapons"),
        (overlay_add_item, "$g_presentation_obj_1", "@Two-Handed Weapons"),
        (overlay_add_item, "$g_presentation_obj_1", "@Polearms"),
        (overlay_add_item, "$g_presentation_obj_1", "@Ranged Weapons"),
        (overlay_add_item, "$g_presentation_obj_1", "@Shields"),
        (overlay_add_item, "$g_presentation_obj_1", "@Helmets"),
        (overlay_add_item, "$g_presentation_obj_1", "@Armors"),
        (overlay_add_item, "$g_presentation_obj_1", "@Boots"),
        (overlay_add_item, "$g_presentation_obj_1", "@Gauntlets"),
        (overlay_add_item, "$g_presentation_obj_1", "@Horses"),
#        (overlay_add_item, "$g_presentation_obj_1", "@Goods"), ##Floris: Disabled the view of goods, because there are quite some items that shouldn't be seen, like trees.
        (overlay_set_val, "$g_presentation_obj_1", "$temp"),

        ## back
        (create_game_button_overlay, "$g_presentation_obj_5", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_5", pos1),

        (str_clear, s0),
        (create_text_overlay, "$g_presentation_obj_6", s0, tf_scrollable),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 100),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (position_set_x, pos1, 890),
        (position_set_y, pos1, 560),
        (overlay_set_area_size, "$g_presentation_obj_6", pos1),
        (set_container_overlay, "$g_presentation_obj_6"),

        (assign, ":num_items", len(items)),
        (assign, "$temp_2", 0),
        ## types
        (try_begin),
          (eq, "$temp", 0), # one-handed weapons
          (try_for_range, ":item_no", 0, ":num_items"),
            (item_get_type, ":type", ":item_no"),
            (eq, ":type", itp_type_one_handed_wpn),
            (val_add, "$temp_2", 1),
          (try_end),
        (else_try),
          (eq, "$temp", 1), # two-handed weapons
          (try_for_range, ":item_no", 0, ":num_items"),
            (item_get_type, ":type", ":item_no"),
            (eq, ":type", itp_type_two_handed_wpn),
            (val_add, "$temp_2", 1),
          (try_end),
        (else_try),
          (eq, "$temp", 2), # polearms
          (try_for_range, ":item_no", 0, ":num_items"),
            (item_get_type, ":type", ":item_no"),
            (eq, ":type", itp_type_polearm),
            (val_add, "$temp_2", 1),
          (try_end),
        (else_try),
          (eq, "$temp", 3), # ranged weapons
          (try_for_range, ":item_no", 0, ":num_items"),
            (item_get_type, ":type", ":item_no"),
            (this_or_next|eq, ":type", itp_type_bolts),
            (this_or_next|eq, ":type", itp_type_bow),
            (this_or_next|eq, ":type", itp_type_crossbow),
            (this_or_next|eq, ":type", itp_type_thrown),
            (this_or_next|eq, ":type", itp_type_pistol),
            (this_or_next|eq, ":type", itp_type_musket),
            (eq, ":type", itp_type_bullets),
            (val_add, "$temp_2", 1),
          (try_end),
        (else_try),
          (eq, "$temp", 4), # shields
          (try_for_range, ":item_no", 0, ":num_items"),
            (item_get_type, ":type", ":item_no"),
            (eq, ":type", itp_type_shield),
            (val_add, "$temp_2", 1),
          (try_end),
        (else_try),
          (eq, "$temp", 5), # helmets
          (try_for_range, ":item_no", 0, ":num_items"),
            (item_get_type, ":type", ":item_no"),
            (eq, ":type", itp_type_head_armor),
            (val_add, "$temp_2", 1),
          (try_end),
        (else_try),
          (eq, "$temp", 6), # armors
          (try_for_range, ":item_no", 0, ":num_items"),
            (item_get_type, ":type", ":item_no"),
            (eq, ":type", itp_type_body_armor),
            (val_add, "$temp_2", 1),
          (try_end),
        (else_try),
          (eq, "$temp", 7), # boots
          (try_for_range, ":item_no", 0, ":num_items"),
            (item_get_type, ":type", ":item_no"),
            (eq, ":type", itp_type_foot_armor),
            (val_add, "$temp_2", 1),
          (try_end),
        (else_try),
          (eq, "$temp", 8), # gauntlets
          (try_for_range, ":item_no", 0, ":num_items"),
            (item_get_type, ":type", ":item_no"),
            (eq, ":type", itp_type_hand_armor),
            (val_add, "$temp_2", 1),
          (try_end),
        (else_try),
          (eq, "$temp", 9), # horses
          (try_for_range, ":item_no", 0, ":num_items"),
            (item_get_type, ":type", ":item_no"),
            (eq, ":type", itp_type_horse),
            (val_add, "$temp_2", 1),
          (try_end),
##Floris: disabled the view of goods, because there are quite some items that shouldn't be seen, like trees.
#        (else_try),
#          (eq, "$temp", 10), # goods
#          (try_for_range, ":item_no", 0, ":num_items"),
#            (item_get_type, ":type", ":item_no"),
#            (this_or_next|eq, ":type", itp_type_goods),
#            (this_or_next|eq, ":type", itp_type_animal),
#            (eq, ":type", itp_type_book),
#            (val_add, "$temp_2", 1),
#          (try_end),
##
        (try_end),

        (store_div, ":height", "$temp_2", 11),
        (store_mod, ":offset", "$temp_2", 11),
        (val_min, ":offset", 1),
        (val_add, ":height", ":offset"),
        (store_mul, ":pos_y", ":height", 80),
        (val_sub, ":pos_y", 80),
        (assign, ":pos_x", 0),
        (assign, ":slot_no", 0),
        (try_for_range, ":item_no", 0, ":num_items"),
          (item_get_type, ":type", ":item_no"),
          (try_begin),
            (eq, "$temp", 0), # one-handed weapons
            (try_begin),
              (eq, ":type", itp_type_one_handed_wpn),
              (assign, ":continue", 1),
            (else_try),
              (assign, ":continue", 0),
            (try_end),
          (else_try),
            (eq, "$temp", 1), # two-handed weapons
            (try_begin),
              (eq, ":type", itp_type_two_handed_wpn),
              (assign, ":continue", 1),
            (else_try),
              (assign, ":continue", 0),
            (try_end),
          (else_try),
            (eq, "$temp", 2), # polearms
            (try_begin),
              (eq, ":type", itp_type_polearm),
              (assign, ":continue", 1),
            (else_try),
              (assign, ":continue", 0),
            (try_end),
          (else_try),
            (eq, "$temp", 3), # ranged weapons
            (try_begin),
              (this_or_next|eq, ":type", itp_type_bolts),
              (this_or_next|eq, ":type", itp_type_bow),
              (this_or_next|eq, ":type", itp_type_crossbow),
              (this_or_next|eq, ":type", itp_type_thrown),
              (this_or_next|eq, ":type", itp_type_pistol),
              (this_or_next|eq, ":type", itp_type_musket),
              (eq, ":type", itp_type_bullets),
              (assign, ":continue", 1),
            (else_try),
              (assign, ":continue", 0),
            (try_end),
          (else_try),
            (eq, "$temp", 4), # shields
            (try_begin),
              (eq, ":type", itp_type_shield),
              (assign, ":continue", 1),
            (else_try),
              (assign, ":continue", 0),
            (try_end),
          (else_try),
            (eq, "$temp", 5), # helmets
            (try_begin),
              (eq, ":type", itp_type_head_armor),
              (assign, ":continue", 1),
            (else_try),
              (assign, ":continue", 0),
            (try_end),
          (else_try),
            (eq, "$temp", 6), # armors
            (try_begin),
              (eq, ":type", itp_type_body_armor),
              (assign, ":continue", 1),
            (else_try),
              (assign, ":continue", 0),
            (try_end),
          (else_try),
            (eq, "$temp", 7), # boots
            (try_begin),
              (eq, ":type", itp_type_foot_armor),
              (assign, ":continue", 1),
            (else_try),
              (assign, ":continue", 0),
            (try_end),
          (else_try),
            (eq, "$temp", 8), # gauntlets
            (try_begin),
              (eq, ":type", itp_type_hand_armor),
              (assign, ":continue", 1),
            (else_try),
              (assign, ":continue", 0),
            (try_end),
          (else_try),
            (eq, "$temp", 9), # horses
            (try_begin),
              (eq, ":type", itp_type_horse),
              (assign, ":continue", 1),
            (else_try),
              (assign, ":continue", 0),
            (try_end),
          (else_try),
            (eq, "$temp", 10), # goods
            (try_begin),
              (this_or_next|eq, ":type", itp_type_goods),
              (this_or_next|eq, ":type", itp_type_animal),
              (eq, ":type", itp_type_book),
              (assign, ":continue", 1),
            (else_try),
              (assign, ":continue", 0),
            (try_end),
          (try_end),
          (eq, ":continue", 1),
          ## item slot
          (create_mesh_overlay, reg1, "mesh_inv_slot"),
          (position_set_x, pos1, 800),
          (position_set_y, pos1, 800),
          (overlay_set_size, reg1, pos1),
          (position_set_x, pos1, ":pos_x"),
          (position_set_y, pos1, ":pos_y"),
          (overlay_set_position, reg1, pos1),
          (create_mesh_overlay, reg1, "mesh_mp_inventory_choose"),
          (position_set_x, pos1, 640),
          (position_set_y, pos1, 640),
          (overlay_set_size, reg1, pos1),
          (position_set_x, pos1, ":pos_x"),
          (position_set_y, pos1, ":pos_y"),
          (overlay_set_position, reg1, pos1),
          (troop_set_slot, "trp_temp_array_a", ":slot_no", reg1),
          ## item
          (create_mesh_overlay_with_item_id, reg1, ":item_no"),
          (position_set_x, pos1, 800),
          (position_set_y, pos1, 800),
          (overlay_set_size, reg1, pos1),
          (store_add, ":item_x", ":pos_x", 40),
          (store_add, ":item_y", ":pos_y", 40),
          (position_set_x, pos1, ":item_x"),
          (position_set_y, pos1, ":item_y"),
          (overlay_set_position, reg1, pos1),
          (troop_set_slot, "trp_temp_array_b", ":slot_no", reg1),
          (troop_set_slot, "trp_temp_array_c", ":slot_no", ":item_no"),
          (val_add, ":pos_x", 80),
          (val_add, ":slot_no", 1),
          (try_begin),
            (ge, ":pos_x", 880),
            (assign, ":pos_x", 0),
            (val_sub, ":pos_y", 80),
          (try_end),
        (try_end),

        (set_container_overlay, -1),
        ## items

#        ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_ready"),
#        ####### mouse fix pos system #######
      ]),

#    (ti_on_presentation_run,
#      [
#        ####### mouse fix pos system #######
#        (call_script, "script_mouse_fix_pos_run"),
#        ####### mouse fix pos system #######
#    ]),

    (ti_on_presentation_mouse_enter_leave,
      [
      (store_trigger_param_1, ":object"),
      (store_trigger_param_2, ":enter_leave"),

      (try_begin),
        (eq, ":enter_leave", 0),
        (try_for_range, ":slot_no", 0, "$temp_2"),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (troop_get_slot, ":item_no", "trp_temp_array_c", ":slot_no"),
          (troop_get_slot, ":target_obj", "trp_temp_array_b", ":slot_no"),
          (overlay_get_position, pos0, ":target_obj"),
          (show_item_details, ":item_no", pos0, 100),
          (assign, "$g_current_opened_item_details", ":slot_no"),
        (try_end),
      (else_try),
        (try_for_range, ":slot_no", 0, "$temp_2"),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (try_begin),
            (eq, "$g_current_opened_item_details", ":slot_no"),
            (close_item_details),
          (try_end),
        (try_end),
      (try_end),
    ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (assign, "$temp", ":value"),
          (start_presentation, "prsnt_all_items"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_5"),
          (presentation_set_duration, 0),
        (try_end),
    ]),
  ]),

  ("change_commander", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (position_set_x, pos1, 400),
        (position_set_y, pos1, 670),
        (str_store_troop_name, s0, "$g_player_troop"),
        (str_store_string, s1, "@Please reselect a companion as the commander for the comming battle.^^Current commander: {s0}."),

        (create_text_overlay, "$g_presentation_obj_1", "@{s1}", tf_center_justify|tf_vertical_align_center),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        
        (create_game_button_overlay, "$g_presentation_obj_2", "@Done"),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 40),
        (overlay_set_position, "$g_presentation_obj_2", pos1),

##CC 1.324
        (str_clear, s0),
        (create_text_overlay, "$g_presentation_obj_6", s0, tf_scrollable),
        (position_set_x, pos1, 750), #800
        (position_set_y, pos1, 150),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (position_set_x, pos1, 200), #100
        (position_set_y, pos1, 400),
        (overlay_set_area_size, "$g_presentation_obj_6", pos1),
        (set_container_overlay, "$g_presentation_obj_6"),
  
        (assign, ":num_of_heros", 0),
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id,":stack_troop","p_main_party",":i_stack"),
          (troop_is_hero, ":stack_troop"),
          (neg|troop_is_wounded, ":stack_troop"),
          (val_add, ":num_of_heros", 1),
        (try_end),
        (try_begin),
          (le, ":num_of_heros", 10),
          (assign, ":pos_y", 400),
        (else_try),
          (store_mul, ":pos_y", ":num_of_heros", 40),
        (try_end),
        (val_sub, ":pos_y", 40),
        (assign, ":pos_x", 0), #50 
##
        (assign, ":num_of_heros", 0),
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id,":stack_troop","p_main_party",":i_stack"),
          (troop_is_hero, ":stack_troop"),
          (neg|troop_is_wounded, ":stack_troop"),
          (str_store_troop_name, s1, ":stack_troop"),
          (position_set_x, pos1, ":pos_x"),
          (position_set_y, pos1, ":pos_y"),
          (val_sub, ":pos_y", 40), ##CC 1.324
          (create_button_overlay, reg0, "@{s1}"), # tf_center_justify), ##CC 1.324
          (overlay_set_position, reg0, pos1),

          (assign, ":trp_slot_prsnt_no", ":num_of_heros"),
          (troop_set_slot, "trp_temp_array_a", ":trp_slot_prsnt_no", reg0),
          (troop_set_slot, "trp_temp_array_b", ":trp_slot_prsnt_no", ":stack_troop"),
          (val_add, ":num_of_heros", 1),
        (try_end),

        (set_container_overlay, -1), ##CC 1.324

        ################
        (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_troop_note_mesh", "$g_player_troop"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_size, reg0, pos1),
        (position_set_x, pos1, 150),
        (position_set_y, pos1, 450),
        (overlay_set_position, reg0, pos1),

        (str_store_troop_name, s1, "$g_player_troop"),
        (store_character_level, ":troop_level", "$g_player_troop"),
        (assign, reg1, ":troop_level"),
        (str_store_string, s1, "@Name: {s1}^Level: {reg1}"),

        (store_troop_health, ":cur_hp", "$g_player_troop", 1),
        (call_script, "script_get_troop_max_hp", "$g_player_troop"),
        (assign, reg1, ":cur_hp"),
        (assign, reg2, reg0),
        (str_store_string, s1, "@{s1}^HP: {reg1}/{reg2}"),

        (create_text_overlay, reg0, "@{s1}", tf_double_space),
        (position_set_x, pos1, 380),
        (position_set_y, pos1, 450),
        (overlay_set_position, reg0, pos1),

        (str_store_string, s2, "@Arms:"),
        (try_for_range, ":cur_slot", 0, 4),#weapon slots
          (troop_get_inventory_slot, ":item", "$g_player_troop", ":cur_slot"),
          (troop_get_inventory_slot_modifier, ":imod", "$g_player_troop", ":cur_slot"),
          (try_begin),
            (lt, ":item", 0),
            (str_store_string, s2, "@{s2}^None"),
          (else_try),
            (str_store_item_name, s3, ":item"),
            (store_sub, ":out_string", ":imod", imod_plain),
            (val_add, ":out_string", "str_imod_plain"),
            (str_store_string, s4, ":out_string"),
            (try_begin),
              (eq, ":imod", imod_plain),
              (str_store_string, s2, "@{s2}^{s3}"),
            (else_try),
              (str_store_string, s2, "@{s2}^{s4}{s3}"),
            (try_end),
          (try_end),
        (try_end),
        (str_store_string, s2, "@{s2}^^Outfits:"),
        (try_for_range, ":cur_slot", 4, 8),#outfit slots
          (troop_get_inventory_slot, ":item", "$g_player_troop", ":cur_slot"),
          (troop_get_inventory_slot_modifier, ":imod", "$g_player_troop", ":cur_slot"),
          (try_begin),
            (lt, ":item", 0),
            (str_store_string, s2, "@{s2}^None"),
          (else_try),
            (str_store_item_name, s3, ":item"),
            (store_sub, ":out_string", ":imod", imod_plain),
            (val_add, ":out_string", "str_imod_plain"),
            (str_store_string, s4, ":out_string"),
            (try_begin),
              (eq, ":imod", imod_plain),
              (str_store_string, s2, "@{s2}^{s3}"),
            (else_try),
              (str_store_string, s2, "@{s2}^{s4}{s3}"),
            (try_end),
          (try_end),
        (try_end),
        (str_store_string, s2, "@{s2}^^Horse:"),
        (troop_get_inventory_slot, ":item", "$g_player_troop", 8),
        (troop_get_inventory_slot_modifier, ":imod", "$g_player_troop", 8),
        (try_begin),
          (lt, ":item", 0),
          (str_store_string, s2, "@{s2}^None"),
        (else_try),
          (str_store_item_name, s3, ":item"),
          (store_sub, ":out_string", ":imod", imod_plain),
          (val_add, ":out_string", "str_imod_plain"),
          (str_store_string, s4, ":out_string"),
          (str_store_string, s2, "@{s2}^{s4}{s3}"),
        (try_end),
        (create_text_overlay, reg0, "@{s2}", tf_center_justify|tf_double_space),
        (position_set_x, pos1, 190),
        (position_set_y, pos1, 50),
        (overlay_set_position, reg0, pos1),

        (str_store_string, s3, "@Attributes:"),
        (store_attribute_level, reg1, "$g_player_troop", ca_strength),
        (store_attribute_level, reg2, "$g_player_troop", ca_intelligence),
        (str_store_string, s3, "@{s3}^STR: {reg1}^INT: {reg2}^^Skills:"),
        (store_skill_level, reg1, skl_power_strike, "$g_player_troop"),
        (store_skill_level, reg2, skl_power_draw, "$g_player_troop"),
        (store_skill_level, reg3, skl_power_throw, "$g_player_troop"),
        (store_skill_level, reg4, skl_horse_archery, "$g_player_troop"),
        (str_store_string, s3, "@{s3}^Power Strike: {reg1}^Power Draw: {reg2}^Power Throw: {reg3}^Horse Archery: {reg4}^^Weapon Proficiencies:"),
        (store_proficiency_level, reg1, "$g_player_troop", wpt_one_handed_weapon),
        (store_proficiency_level, reg2, "$g_player_troop", wpt_two_handed_weapon),
        (store_proficiency_level, reg3, "$g_player_troop", wpt_polearm),
        (str_store_string, s3, "@{s3}^1 Hand Wpns: {reg1}^2 Hand Wpns: {reg2}^Polearms: {reg3}"),
        (create_text_overlay, reg0, "@{s3}", tf_double_space),
        (position_set_x, pos1, 380),
        (position_set_y, pos1, 50),
        (overlay_set_position, reg0, pos1),

        (str_store_string, s4, "str_empty_string"),
        (store_attribute_level, reg1, "$g_player_troop", ca_agility),
        (store_attribute_level, reg2, "$g_player_troop", ca_charisma),
        (str_store_string, s4, "@{s4}^AGI: {reg1}^CHA: {reg2}^^"),
        (store_skill_level, reg1, skl_ironflesh, "$g_player_troop"),
        (store_skill_level, reg2, skl_athletics, "$g_player_troop"),
        (store_skill_level, reg3, skl_shield, "$g_player_troop"),
        (store_skill_level, reg4, skl_riding, "$g_player_troop"),
        (str_store_string, s4, "@{s4}^Ironflesh: {reg1}^Athletics: {reg2}^Shield: {reg3}^Riding: {reg4}^^"),
        (store_proficiency_level, reg1, "$g_player_troop", wpt_archery),
        (store_proficiency_level, reg2, "$g_player_troop", wpt_crossbow),
        (store_proficiency_level, reg3, "$g_player_troop", wpt_throwing),
        (str_store_string, s4, "@{s4}^Archery: {reg1}^Crossbows: {reg2}^Throwing: {reg3}"),
        (create_text_overlay, reg0, "@{s4}", tf_double_space),
        (position_set_x, pos1, 590),
        (position_set_y, pos1, 50),
        (overlay_set_position, reg0, pos1),
        ################
        
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_ready"),
        ####### mouse fix pos system #######
      ]),

      #(ti_on_presentation_run,
        #[
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_run"),
        ####### mouse fix pos system #######
      #]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_2"),
          (presentation_set_duration, 0),
        (try_end),

        (assign, ":num_of_heros", 0),
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id,":stack_troop","p_main_party",":i_stack"),
          (troop_is_hero, ":stack_troop"),
          (neg|troop_is_wounded, ":stack_troop"),
          (assign, ":trp_slot_prsnt_no", ":num_of_heros"),
          (val_add, ":num_of_heros", 1),
          (troop_slot_eq, "trp_temp_array_a", ":trp_slot_prsnt_no", ":object"),
          (troop_get_slot, ":cur_troop", "trp_temp_array_b", ":trp_slot_prsnt_no"),
          (assign, "$g_player_troop", ":cur_troop"),
          (start_presentation, "prsnt_change_commander"),
        (try_end),
      ]),
    ]),

  ("deposit_withdraw_money", 0, 0, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (party_get_slot, ":chest_troop", "$current_town", slot_town_seneschal),
        (store_troop_gold, ":account_money", ":chest_troop"),
        (store_troop_gold, ":player_money", "trp_player"),

        (create_mesh_overlay, reg0, "mesh_message_window"),
        (position_set_x, pos1, 224),
        (position_set_y, pos1, 230),
        (overlay_set_position, reg0, pos1),
        
        (assign, reg1, ":account_money"),
        (create_text_overlay, reg0, "@{reg1}^money in the chest", tf_center_justify|tf_vertical_align_center),
        (position_set_x, pos1, 370),
        (position_set_y, pos1, 320),
        (overlay_set_position, reg0, pos1),

        (assign, reg2, ":player_money"),
        (create_text_overlay, reg0, "@{reg2}^money in your inventory", tf_center_justify|tf_vertical_align_center),
        (position_set_x, pos1, 630),
        (position_set_y, pos1, 320),
        (overlay_set_position, reg0, pos1),

        (create_combo_button_overlay, "$g_presentation_obj_1"),
        (position_set_x, pos1, 480),
        (position_set_y, pos1, 380),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_1", pos1),
        (overlay_add_item, "$g_presentation_obj_1", "@Withdraw"),
        (overlay_add_item, "$g_presentation_obj_1", "@Deposit"),
        (overlay_set_val, "$g_presentation_obj_1", 1),
        
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 380),
        (val_add, ":player_money", 1),
        (create_number_box_overlay, "$g_presentation_obj_2", 0, ":player_money"),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_val, "$g_presentation_obj_2", 0),
        (overlay_set_display, "$g_presentation_obj_2", 1),
        (val_add, ":account_money", 1),
        (create_number_box_overlay, "$g_presentation_obj_3", 0, ":account_money"),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (overlay_set_val, "$g_presentation_obj_3", 0),
        (overlay_set_display, "$g_presentation_obj_3", 0),
        
        (create_game_button_overlay, "$g_presentation_obj_5", "@Done"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 250),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (try_begin),
            (eq, ":value", 1),
            (overlay_set_display, "$g_presentation_obj_2", 1),
            (overlay_set_display, "$g_presentation_obj_3", 0),
          (else_try),
            (overlay_set_display, "$g_presentation_obj_2", 0),
            (overlay_set_display, "$g_presentation_obj_3", 1),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_2"),
          (party_get_slot, ":chest_troop", "$current_town", slot_town_seneschal),
          (gt, ":value", 0),
          (troop_remove_gold, "trp_player",":value"),
          (troop_add_gold, ":chest_troop", ":value"),
          (start_presentation, "prsnt_deposit_withdraw_money"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_3"),
          (party_get_slot, ":chest_troop", "$current_town", slot_town_seneschal),
          (gt, ":value", 0),
          (troop_remove_gold, ":chest_troop",":value"),
          (troop_add_gold, "trp_player", ":value"),
          (start_presentation, "prsnt_deposit_withdraw_money"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_5"),
          (presentation_set_duration, 0),
        (try_end),
    ]),
  ]),

  ("recruit_plan", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
  
        (call_script, "script_get_town_faction_for_recruiting", "$current_town"),
        (assign, ":party_faction", reg0),
        (str_store_faction_name, s1, ":party_faction"),
        (party_get_slot, reg1, "$current_town", slot_town_recruit_gold),
        (store_div, reg2, reg1, reinforcement_cost_player),
        (store_sub, reg3, reg2, 1),
        (assign, reg4, reinforcement_cost_player),
        (store_troop_gold, reg5, "trp_player"),
        (party_get_slot, ":party_type", "$current_town", slot_party_type),
        (assign, reg6, 0),
        (try_begin),
          (eq, ":party_type", spt_castle),
          (assign, reg6, 1),
        (try_end),
        
        (create_text_overlay, reg0, "@You can recruit troops of {s1} for this {reg6?castle:town}. Recruiting will costs {reg4} denars and will require at least one day. You have {reg1} denars left here (can recruit for {reg2} {reg3?times:time}) and have {reg5} denars in your coffers.", tf_scrollable),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 300),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 300),
        (overlay_set_area_size, reg0, pos1),
        
        (create_combo_button_overlay, "$g_presentation_obj_1"),
        (position_set_x, pos1, 380),
        (position_set_y, pos1, 280),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_presentation_obj_1", pos1),
        (overlay_add_item, "$g_presentation_obj_1", "@Decrease times of recruiting"),
        (overlay_add_item, "$g_presentation_obj_1", "@Increase times of recruiting"),
        (overlay_set_val, "$g_presentation_obj_1", 1),
        
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 280),
        # Increase
        (store_troop_gold, ":player_gold", "trp_player"),
        (val_div, ":player_gold", reinforcement_cost_player),
        (val_add, ":player_gold", 1),
        (create_number_box_overlay, "$g_presentation_obj_2", 0, ":player_gold"),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_val, "$g_presentation_obj_2", 0),
        (overlay_set_display, "$g_presentation_obj_2", 1),
        # Decrease
        (party_get_slot, ":recruit_gold", "$current_town", slot_town_recruit_gold),
        (val_div, ":recruit_gold", reinforcement_cost_player),
        (val_add, ":recruit_gold", 1),
        (create_number_box_overlay, "$g_presentation_obj_3", 0, ":recruit_gold"),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (overlay_set_val, "$g_presentation_obj_3", 0),
        (overlay_set_display, "$g_presentation_obj_3", 0),
        
        (create_game_button_overlay, "$g_presentation_obj_5", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
      ]),
  
    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
  
        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (try_begin),
            (eq, ":value", 1),
            (overlay_set_display, "$g_presentation_obj_2", 1),
            (overlay_set_display, "$g_presentation_obj_3", 0),
          (else_try),
            (overlay_set_display, "$g_presentation_obj_2", 0),
            (overlay_set_display, "$g_presentation_obj_3", 1),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_2"),
          (gt, ":value", 0),
          (store_mul, ":cost_money", ":value", reinforcement_cost_player),
          (troop_remove_gold, "trp_player", ":cost_money"),
          (party_get_slot, ":recruit_gold", "$current_town", slot_town_recruit_gold),
          (val_add, ":recruit_gold", ":cost_money"),
          (party_set_slot, "$current_town", slot_town_recruit_gold, ":recruit_gold"),
          (start_presentation, "prsnt_recruit_plan"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_3"),
          (gt, ":value", 0),
          (store_mul, ":cancle_money", ":value", reinforcement_cost_player),
          (troop_add_gold, "trp_player", ":cancle_money"),
          (party_get_slot, ":recruit_gold", "$current_town", slot_town_recruit_gold),
          (val_sub, ":recruit_gold", ":cancle_money"),
          (party_set_slot, "$current_town", slot_town_recruit_gold, ":recruit_gold"),
          (start_presentation, "prsnt_recruit_plan"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_5"),
          (presentation_set_duration, 0),
        (try_end),
    ]),
  ]),
  
  ("change_all_factions_color", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
        
        (create_combo_button_overlay, "$g_presentation_obj_1"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 680),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        
        # faction list
        (troop_set_slot, "trp_temp_array_a", 0, "fac_deserters"),
        (troop_set_slot, "trp_temp_array_a", 1, "fac_outlaws"),
        (troop_set_slot, "trp_temp_array_a", 2, "fac_player_supporters_faction"),
        (troop_set_slot, "trp_temp_array_a", 3, "fac_kingdom_6"),
        (troop_set_slot, "trp_temp_array_a", 4, "fac_kingdom_5"),
        (troop_set_slot, "trp_temp_array_a", 5, "fac_kingdom_4"),
        (troop_set_slot, "trp_temp_array_a", 6, "fac_kingdom_3"),
        (troop_set_slot, "trp_temp_array_a", 7, "fac_kingdom_2"),
        (troop_set_slot, "trp_temp_array_a", 8, "fac_kingdom_1"),
        # default color list
        (troop_set_slot, "trp_temp_array_b", 0, 0xff8080),
        (troop_set_slot, "trp_temp_array_b", 1, 0xcc66cc),
        (troop_set_slot, "trp_temp_array_b", 2, 0xFF4433),
        (troop_set_slot, "trp_temp_array_b", 3, 0xDDDD33),
        (troop_set_slot, "trp_temp_array_b", 7, 0x33DD33),
        (troop_set_slot, "trp_temp_array_b", 5, 0x33DDDD),
        (troop_set_slot, "trp_temp_array_b", 6, 0xCC99FF),
        (troop_set_slot, "trp_temp_array_b", 7, 0x3344FF),
        (troop_set_slot, "trp_temp_array_b", 8, 0xEE7744),
##
        
        (try_for_range, ":cur_slot", 0, 9),
          (troop_get_slot, ":cur_faction", "trp_temp_array_a", ":cur_slot"),
          (str_store_faction_name, s0, ":cur_faction"),
          (overlay_add_item, "$g_presentation_obj_1", s0),
        (try_end),
		(val_clamp, "$temp", 0, 9),
        (overlay_set_val, "$g_presentation_obj_1", "$temp"),
        
        ## name and color
        (troop_get_slot, ":cur_faction", "trp_temp_array_a", "$temp"),
        (str_store_faction_name, s0, ":cur_faction"),
        (create_text_overlay, reg1, "@Sovereign color of the {s0}:", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg1, pos1),
        (create_mesh_overlay, "$g_presentation_obj_2", "mesh_white_plane"),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 480),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (position_set_x, pos1, 5000),
        (position_set_y, pos1, 5000),
        (overlay_set_size, "$g_presentation_obj_2", pos1),
        (faction_get_color, ":faction_color", ":cur_faction"),
        (overlay_set_color, "$g_presentation_obj_2", ":faction_color"),
        
        ## sliders
        (position_set_x, pos1, 500),
        (create_slider_overlay, "$g_presentation_obj_3", 0, 255),
        (position_set_y, pos1, 400),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (create_slider_overlay, "$g_presentation_obj_4", 0, 255),
        (position_set_y, pos1, 350),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (create_slider_overlay, "$g_presentation_obj_5", 0, 255),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (store_mod, ":blue", ":faction_color", 0x100),
        (val_div, ":faction_color", 0x100),
        (store_mod, ":green", ":faction_color", 0x100),
        (val_div, ":faction_color", 0x100),
        (store_mod, ":red", ":faction_color", 0x100),
        (overlay_set_val, "$g_presentation_obj_3", ":red"),
        (overlay_set_val, "$g_presentation_obj_4", ":green"),
        (overlay_set_val, "$g_presentation_obj_5", ":blue"),
        ## num boxes
        (position_set_x, pos1, 650),
        (create_number_box_overlay, "$g_presentation_obj_6", 0, 256),
        (position_set_y, pos1, 400),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (create_number_box_overlay, "$g_presentation_obj_7", 0, 256),
        (position_set_y, pos1, 350),
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (create_number_box_overlay, "$g_presentation_obj_8", 0, 256),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_8", pos1),
        (overlay_set_val, "$g_presentation_obj_6", ":red"),
        (overlay_set_val, "$g_presentation_obj_7", ":green"),
        (overlay_set_val, "$g_presentation_obj_8", ":blue"),
        (assign, reg2, ":red"),
        (assign, reg3, ":green"),
        (assign, reg4, ":blue"),
        ## text: r g b
        (position_set_x, pos1, 330),
        (create_text_overlay, reg1, "@Red:", tf_center_justify),
        (position_set_y, pos1, 400),
        (overlay_set_position, reg1, pos1),
        (create_text_overlay, reg1, "@Green:", tf_center_justify),
        (position_set_y, pos1, 350),
        (overlay_set_position, reg1, pos1),
        (create_text_overlay, reg1, "@Blue:", tf_center_justify),
        (position_set_y, pos1, 300),
        (overlay_set_position, reg1, pos1),
        
        ## HTML code
        (create_text_overlay, "$g_presentation_obj_9", "@ ", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 450),
        (overlay_set_position, "$g_presentation_obj_9", pos1),
        (call_script, "script_convert_rgb_code_to_html_code", reg2, reg3, reg4),
        (overlay_set_text, "$g_presentation_obj_9", "@HTML code: {s0}"),
        
        ## default and random
        (create_game_button_overlay, "$g_presentation_obj_11", "@Default"),
        (position_set_x, pos1, 420),
        (position_set_y, pos1, 230),
        (overlay_set_position, "$g_presentation_obj_11", pos1),
        (create_game_button_overlay, "$g_presentation_obj_12", "@Randomize"),
        (position_set_x, pos1, 580),
        (position_set_y, pos1, 230),
        (overlay_set_position, "$g_presentation_obj_12", pos1),
        
        ## color picker
        (create_mesh_overlay, reg1, "mesh_white_plane"),
        (position_set_x, pos1, 138),
        (position_set_y, pos1, 78),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 36100),
        (position_set_y, pos1, 6100),
        (overlay_set_size, reg1, pos1),
        (overlay_set_color, reg1, 0),
        
        (assign, ":pos_x", 140),
        (assign, ":pos_y", 80),
        (try_for_range, ":cur_slot", 0, 216),
          (create_image_button_overlay, reg1, "mesh_white_plane", "mesh_white_plane"),
          (position_set_x, pos1, ":pos_x"),
          (position_set_y, pos1, ":pos_y"),
          (overlay_set_position, reg1, pos1),
          (position_set_x, pos1, 900),
          (position_set_y, pos1, 900),
          (overlay_set_size, reg1, pos1),
          (assign, ":cur_color", ":cur_slot"),
          (call_script, "script_convert_slot_no_to_color", ":cur_color"),
          (assign, ":dest_color", reg0),
          (overlay_set_color, reg1, ":dest_color"),
          (val_add, ":pos_x", 20),
          (try_begin),
            (eq, ":pos_x", 860),
            (assign, ":pos_x", 140),
            (val_add, ":pos_y", 20),
          (try_end),
          (troop_set_slot, "trp_temp_array_c", ":cur_slot", reg1),
        (try_end),
        
        ## done
        (create_game_button_overlay, "$g_presentation_obj_10", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_10", pos1),
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_ready"),
        ####### mouse fix pos system #######
      ]),

      #(ti_on_presentation_run,
        #[
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_run"),
        ####### mouse fix pos system #######
      #]),
  
    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        
        (try_for_range, ":cur_slot", 0, 216),
          (troop_slot_eq, "trp_temp_array_c", ":cur_slot", ":object"),
          (assign, ":cur_color", ":cur_slot"),
          (call_script, "script_convert_slot_no_to_color", ":cur_color"),
          (assign, ":dest_color", reg0),
          (troop_get_slot, ":cur_faction", "trp_temp_array_a", "$temp"),
          (faction_set_color, ":cur_faction", ":dest_color"),
          (overlay_set_color, "$g_presentation_obj_2", ":dest_color"),
          (store_mod, ":blue", ":dest_color", 0x100),
          (val_div, ":dest_color", 0x100),
          (store_mod, ":green", ":dest_color", 0x100),
          (val_div, ":dest_color", 0x100),
          (store_mod, ":red", ":dest_color", 0x100),
          (overlay_set_val, "$g_presentation_obj_3", ":red"),
          (overlay_set_val, "$g_presentation_obj_4", ":green"),
          (overlay_set_val, "$g_presentation_obj_5", ":blue"),
          (overlay_set_val, "$g_presentation_obj_6", ":red"),
          (overlay_set_val, "$g_presentation_obj_7", ":green"),
          (overlay_set_val, "$g_presentation_obj_8", ":blue"),
          (assign, reg2, ":red"),
          (assign, reg3, ":green"),
          (assign, reg4, ":blue"),
          (call_script, "script_convert_rgb_code_to_html_code", reg2, reg3, reg4),
          (overlay_set_text, "$g_presentation_obj_9", "@HTML code: {s0}"),
        (try_end),
        
        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (assign, "$temp", ":value"),
          (start_presentation, "prsnt_change_all_factions_color"),
        (else_try),
          (this_or_next|eq, ":object", "$g_presentation_obj_3"),
          (eq, ":object", "$g_presentation_obj_6"),
          (overlay_set_val, "$g_presentation_obj_3", ":value"),
          (overlay_set_val, "$g_presentation_obj_6", ":value"),
          (assign, reg2, ":value"),
          (call_script, "script_get_dest_color_from_rgb", reg2, reg3, reg4),
          (assign, ":cur_color", reg0),
          (overlay_set_color, "$g_presentation_obj_2", ":cur_color"),
          (troop_get_slot, ":cur_faction", "trp_temp_array_a", "$temp"),
          (faction_set_color, ":cur_faction", ":cur_color"),
          (call_script, "script_convert_rgb_code_to_html_code", reg2, reg3, reg4),
          (overlay_set_text, "$g_presentation_obj_9", "@HTML code: {s0}"),
        (else_try),
          (this_or_next|eq, ":object", "$g_presentation_obj_4"),
          (eq, ":object", "$g_presentation_obj_7"),
          (overlay_set_val, "$g_presentation_obj_4", ":value"),
          (overlay_set_val, "$g_presentation_obj_7", ":value"),
          (assign, reg3, ":value"),
          (call_script, "script_get_dest_color_from_rgb", reg2, reg3, reg4),
          (assign, ":cur_color", reg0),
          (overlay_set_color, "$g_presentation_obj_2", ":cur_color"),
          (troop_get_slot, ":cur_faction", "trp_temp_array_a", "$temp"),
          (faction_set_color, ":cur_faction", ":cur_color"),
          (call_script, "script_convert_rgb_code_to_html_code", reg2, reg3, reg4),
          (overlay_set_text, "$g_presentation_obj_9", "@HTML code: {s0}"),
        (else_try),
          (this_or_next|eq, ":object", "$g_presentation_obj_5"),
          (eq, ":object", "$g_presentation_obj_8"),
          (overlay_set_val, "$g_presentation_obj_5", ":value"),
          (overlay_set_val, "$g_presentation_obj_8", ":value"),
          (assign, reg4, ":value"),
          (call_script, "script_get_dest_color_from_rgb", reg2, reg3, reg4),
          (assign, ":cur_color", reg0),
          (overlay_set_color, "$g_presentation_obj_2", ":cur_color"),
          (troop_get_slot, ":cur_faction", "trp_temp_array_a", "$temp"),
          (faction_set_color, ":cur_faction", ":cur_color"),
          (call_script, "script_convert_rgb_code_to_html_code", reg2, reg3, reg4),
          (overlay_set_text, "$g_presentation_obj_9", "@HTML code: {s0}"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_11"),
          (troop_get_slot, ":cur_faction", "trp_temp_array_a", "$temp"),
          (troop_get_slot, ":default_color", "trp_temp_array_b", "$temp"),
          (faction_set_color, ":cur_faction", ":default_color"),
          (overlay_set_color, "$g_presentation_obj_2", ":default_color"),
          (store_mod, ":blue", ":default_color", 0x100),
          (val_div, ":default_color", 0x100),
          (store_mod, ":green", ":default_color", 0x100),
          (val_div, ":default_color", 0x100),
          (store_mod, ":red", ":default_color", 0x100),
          (overlay_set_val, "$g_presentation_obj_3", ":red"),
          (overlay_set_val, "$g_presentation_obj_4", ":green"),
          (overlay_set_val, "$g_presentation_obj_5", ":blue"),
          (overlay_set_val, "$g_presentation_obj_6", ":red"),
          (overlay_set_val, "$g_presentation_obj_7", ":green"),
          (overlay_set_val, "$g_presentation_obj_8", ":blue"),
          (assign, reg2, ":red"),
          (assign, reg3, ":green"),
          (assign, reg4, ":blue"),
          (call_script, "script_convert_rgb_code_to_html_code", reg2, reg3, reg4),
          (overlay_set_text, "$g_presentation_obj_9", "@HTML code: {s0}"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_12"),
          (store_random_in_range, reg2, 0, 256),
          (store_random_in_range, reg3, 0, 256),
          (store_random_in_range, reg4, 0, 256),
          (overlay_set_val, "$g_presentation_obj_3", reg2),
          (overlay_set_val, "$g_presentation_obj_4", reg3),
          (overlay_set_val, "$g_presentation_obj_5", reg4),
          (overlay_set_val, "$g_presentation_obj_6", reg2),
          (overlay_set_val, "$g_presentation_obj_7", reg3),
          (overlay_set_val, "$g_presentation_obj_8", reg4),
          (call_script, "script_get_dest_color_from_rgb", reg2, reg3, reg4),
          (assign, ":cur_color", reg0),
          (overlay_set_color, "$g_presentation_obj_2", ":cur_color"),
          (troop_get_slot, ":cur_faction", "trp_temp_array_a", "$temp"),
          (faction_set_color, ":cur_faction", ":cur_color"),
          (call_script, "script_convert_rgb_code_to_html_code", reg2, reg3, reg4),
          (overlay_set_text, "$g_presentation_obj_9", "@HTML code: {s0}"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_10"),
          (presentation_set_duration, 0),
        (try_end),
    ]),
  ]),
  
  ("sort_the_defenders", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
        
        ## next presentation
        (assign, "$g_presentation_next_presentation", -1),
      
        (str_clear, s0),
        (create_text_overlay, "$g_presentation_obj_1", s0, tf_scrollable),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 50),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 600),
        (overlay_set_area_size, "$g_presentation_obj_1", pos1),
        (set_container_overlay, "$g_presentation_obj_1"),
        
        (assign, ":pos_x", 150),
        (party_get_num_companion_stacks, ":num_stacks", "$current_town"),
        (store_mul, ":pos_y", ":num_stacks", 40),
        (val_sub, ":pos_y", 40),
        (val_max, ":pos_y", 560),
        (try_for_range, ":slot_no", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":troop_no", "$current_town", ":slot_no"),
          (party_stack_get_size, ":stack_size", "$current_town", ":slot_no"),
          (party_stack_get_num_wounded, ":num_wounded", "$current_town", ":slot_no"),
          (str_store_troop_name, s1, ":troop_no"),
          (assign, reg2, ":stack_size"),
          (try_begin),
            (gt, ":num_wounded", 0),
            (store_sub, reg3, ":stack_size", ":num_wounded"),
            (str_store_string, s1, "@{s1}({reg3}/{reg2})"),
          (else_try),
            (str_store_string, s1, "@{s1}({reg2})"),
          (try_end),
          (create_game_button_overlay, reg1, "@{s1}"),
          (position_set_x, pos1, ":pos_x"),
          (position_set_y, pos1, ":pos_y"),
          (overlay_set_position, reg1, pos1),
          (position_set_x, pos1, 240),
          (position_set_y, pos1, 32),
          (overlay_set_size, reg1, pos1),
          (troop_set_slot, "trp_temp_array_a", ":slot_no", reg1),
          (val_sub, ":pos_y", 40),
        (try_end),
        (try_begin),
          (gt, "$g_cur_stack", -1),
          (troop_get_slot, ":dest_obj", "trp_temp_array_a", "$g_cur_stack"),
          (overlay_set_alpha, ":dest_obj", 0x80),
        (try_end),
        (set_container_overlay, -1),
        
        # Move up - Move Down
        (position_set_x, pos1, 750),
        (create_button_overlay, "$g_presentation_obj_2", "@Move to Top", tf_center_justify),
        (position_set_y, pos1, 600),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (create_button_overlay, "$g_presentation_obj_3", "@Move Up", tf_center_justify),
        (position_set_y, pos1, 525),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (create_button_overlay, "$g_presentation_obj_4", "@Move Down", tf_center_justify),
        (position_set_y, pos1, 450),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (create_button_overlay, "$g_presentation_obj_5", "@Move to Bottom", tf_center_justify),
        (position_set_y, pos1, 375),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        
        # cur troop
        (try_begin),
          (gt, "$g_cur_stack", -1),
          (party_stack_get_troop_id, ":troop_no", "$current_town", "$g_cur_stack"),
          (store_mul, ":cur_troop", ":troop_no", 2), #with weapons
          (create_image_button_overlay_with_tableau_material, "$g_presentation_obj_6", -1, "tableau_game_party_window", ":cur_troop"),
          (position_set_x, pos1, 400),
          (position_set_y, pos1, 300),
          (overlay_set_position, "$g_presentation_obj_6", pos1),
        (else_try),
          (create_mesh_overlay, "$g_presentation_obj_6", "mesh_white_plane"),
          (overlay_set_display, "$g_presentation_obj_6", 0),
        (try_end),
        
        # done
        (create_game_button_overlay, "$g_presentation_obj_10", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_10", pos1),
        
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_ready"),
        ####### mouse fix pos system #######
      ]),
    #(ti_on_presentation_run,
      #[
      ####### mouse fix pos system #######
      #(call_script, "script_mouse_fix_pos_run"),
      ####### mouse fix pos system #######
    #]),
    
    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),

        (party_get_num_companion_stacks, ":num_stacks", "$current_town"),
        (try_for_range, ":slot_no", 0, ":num_stacks"),
          (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
          (assign, "$g_cur_stack", ":slot_no"),
          (start_presentation, "prsnt_sort_the_defenders"),
        (try_end),
        
        (try_begin),
          (eq, ":object", "$g_presentation_obj_2"), # top
          (try_begin),
            (gt, "$g_cur_stack", 0),
            (store_sub, ":times", ":num_stacks", 1),
            (call_script, "script_move_one_stack_to_the_bottom", "$current_town", "$g_cur_stack", 1),
            (call_script, "script_move_one_stack_to_the_bottom", "$current_town", 0, ":times"),
            (assign, "$g_cur_stack", 0),
            (start_presentation, "prsnt_sort_the_defenders"),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_3"), # up
          (try_begin),
            (gt, "$g_cur_stack", 0),
            (store_sub, ":pre_stack", "$g_cur_stack", 1),
            (store_sub, ":times", ":num_stacks", "$g_cur_stack"),
            (call_script, "script_move_one_stack_to_the_bottom", "$current_town", "$g_cur_stack", 1),
            (call_script, "script_move_one_stack_to_the_bottom", "$current_town", ":pre_stack", ":times"),
            (val_sub, "$g_cur_stack", 1),
            (start_presentation, "prsnt_sort_the_defenders"),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_4"), # down
          (try_begin),
            (store_sub, ":last_stack", ":num_stacks", 1),
            (lt, "$g_cur_stack", ":last_stack"),
            (gt, "$g_cur_stack", -1),
            (store_add, ":next_stack", "$g_cur_stack", 1),
            (store_sub, ":times", ":last_stack", "$g_cur_stack"),
            (call_script, "script_move_one_stack_to_the_bottom", "$current_town", ":next_stack", 1),
            (call_script, "script_move_one_stack_to_the_bottom", "$current_town", "$g_cur_stack", ":times"),
            (val_add, "$g_cur_stack", 1),
            (start_presentation, "prsnt_sort_the_defenders"),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_5"), # bottom
          (try_begin),
            (store_sub, ":last_stack", ":num_stacks", 1),
            (lt, "$g_cur_stack", ":last_stack"),
            (gt, "$g_cur_stack", -1),
            (call_script, "script_move_one_stack_to_the_bottom", "$current_town", "$g_cur_stack", 1),
            (assign, "$g_cur_stack", ":last_stack"),
            (start_presentation, "prsnt_sort_the_defenders"),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_6"), # troop note
          (assign, "$g_presentation_next_presentation", "prsnt_sort_the_defenders"),
          (party_stack_get_troop_id, "$temp", "$current_town", "$g_cur_stack"),
          (start_presentation, "prsnt_troop_note"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_10"),
          (presentation_set_duration, 0),
        (try_end),
    ]),
  ]),
  
  ("shopping_list_of_food", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
        
        ## back
        (create_game_button_overlay, "$g_presentation_obj_1", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_1", pos1),

        ## buy foos automaticly when leaving
        (create_text_overlay, reg0, "@Buy foods automaticly when leaving:", tf_vertical_align_center),
        (position_set_x, pos1, 150),
        (position_set_y, pos1, 690),
        (overlay_set_position, reg0, pos1),

        (create_check_box_overlay, "$g_presentation_obj_2", "mesh_checkbox_off", "mesh_checkbox_on"),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 682),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_val, "$g_presentation_obj_2", "$g_buy_foods_when_leaving"),

        (assign, ":pos_x", 60),
        (assign, ":pos_y", 550),
        (try_for_range, ":cur_food", food_begin, food_end),
          # frame
          (create_mesh_overlay, reg1, "mesh_inv_slot"),
          (position_set_x, pos1, 800),
          (position_set_y, pos1, 800),
          (overlay_set_size, reg1, pos1),
          (position_set_x, pos1, ":pos_x"),
          (position_set_y, pos1, ":pos_y"),
          (overlay_set_position, reg1, pos1),
          # back ground
          (create_mesh_overlay, reg1, "mesh_mp_inventory_choose"),
          (position_set_x, pos1, 640),
          (position_set_y, pos1, 640),
          (overlay_set_size, reg1, pos1),
          (position_set_x, pos1, ":pos_x"),
          (position_set_y, pos1, ":pos_y"),
          (overlay_set_position, reg1, pos1),
          # item overlay
          (troop_set_slot, "trp_temp_array_a", ":cur_food", reg1),
          (create_mesh_overlay_with_item_id, reg1, ":cur_food"),
          (position_set_x, pos1, 800),
          (position_set_y, pos1, 800),
          (overlay_set_size, reg1, pos1),
          (store_add, ":item_x", ":pos_x", 40),
          (store_add, ":item_y", ":pos_y", 40),
          (position_set_x, pos1, ":item_x"),
          (position_set_y, pos1, ":item_y"),
          (overlay_set_position, reg1, pos1),
          (troop_set_slot, "trp_temp_array_b", ":cur_food", reg1),
          # text *
          (create_text_overlay, reg1, "@*", tf_center_justify|tf_vertical_align_center),
          (store_add, ":text_x", ":pos_x", 100),
          (store_add, ":text_y", ":pos_y", 40),
          (position_set_x, pos1, ":text_x"),
          (position_set_y, pos1, ":text_y"),
          (overlay_set_position, reg1, pos1),
          # number_box
          (create_number_box_overlay, reg1, 0, 5),
          (store_add, ":number_box_x", ":pos_x", 115),
          (store_add, ":number_box_y", ":pos_y", 30),
          (position_set_x, pos1, ":number_box_x"),
          (position_set_y, pos1, ":number_box_y"),
          (overlay_set_position, reg1, pos1),
          (item_get_slot, ":food_portion", ":cur_food", slot_item_food_portion),
          (overlay_set_val, reg1, ":food_portion"),
          (troop_set_slot, "trp_temp_array_c", ":cur_food", reg1),
          # next
          (val_add, ":pos_x", 240),
          (try_begin),
            (eq, ":pos_x", 1020),
            (assign, ":pos_x", 60),
            (val_sub, ":pos_y", 120),
          (try_end),
        (try_end),

        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_ready"),
        ####### mouse fix pos system #######
      ]),

    #(ti_on_presentation_run,
      #[
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_run"),
        ####### mouse fix pos system #######
    #]),

    (ti_on_presentation_mouse_enter_leave,
      [
      (store_trigger_param_1, ":object"),
      (store_trigger_param_2, ":enter_leave"),

      (try_begin),
        (eq, ":enter_leave", 0),
        (try_for_range, ":cur_food", food_begin, food_end),
          (troop_slot_eq, "trp_temp_array_a", ":cur_food", ":object"),
          (troop_get_slot, ":target_obj", "trp_temp_array_b", ":cur_food"),
          (overlay_get_position, pos0, ":target_obj"),
          (show_item_details, ":cur_food", pos0, 100),
          (assign, "$g_current_opened_item_details", ":cur_food"),
        (try_end),
      (else_try),
        (try_for_range, ":cur_food", food_begin, food_end),
          (troop_slot_eq, "trp_temp_array_a", ":cur_food", ":object"),
          (try_begin),
            (eq, "$g_current_opened_item_details", ":cur_food"),
            (close_item_details),
          (try_end),
        (try_end),
      (try_end),
    ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_for_range, ":cur_food", food_begin, food_end),
          (troop_slot_eq, "trp_temp_array_c", ":cur_food", ":object"),
          (item_set_slot, ":cur_food", slot_item_food_portion, ":value"),
        (try_end),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_2"),
          (assign, "$g_buy_foods_when_leaving", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_1"),
          (presentation_set_duration, 0),
        (try_end),
    ]),
  ]),
  
  
  ("character_creation", 0, mesh_load_window, [ 
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
        
        ## done
        (create_game_button_overlay, "$g_presentation_obj_1", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_1", pos1),

        (create_game_button_overlay, "$g_presentation_obj_2", "@Default"),
        (position_set_x, pos1, 730),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_2", pos1),

        (create_game_button_overlay, "$g_presentation_obj_3", "@Randomize"),
        (position_set_x, pos1, 560),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_3", pos1),

        (create_text_overlay, reg1, "@Character Background", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 630),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 2000),
        (position_set_y, pos1, 2000),
        (overlay_set_size, reg1, pos1),
        (create_text_overlay, reg1, "@Your story:", tf_left_align),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 550),
        (overlay_set_position, reg1, pos1),

        ## options
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 550),
        (create_text_overlay, reg1, "@Your gender:", tf_center_justify),
        (overlay_set_position, reg1, pos1),
        (position_set_y, pos1, 470),
        (create_text_overlay, reg1, "@Your father was:", tf_center_justify),
        (overlay_set_position, reg1, pos1),
        (position_set_y, pos1, 390),
        (create_text_overlay, reg1, "@You spent your early life as:", tf_center_justify),
        (overlay_set_position, reg1, pos1),
        (position_set_y, pos1, 310),
        (create_text_overlay, reg1, "@Later you became:", tf_center_justify),
        (overlay_set_position, reg1, pos1),
        (position_set_y, pos1, 230),
        (create_text_overlay, reg1, "@The reason for an adventure:", tf_center_justify),
        (overlay_set_position, reg1, pos1),
        ## combo button
        # gender
        (position_set_y, pos1, 510),
        (create_combo_button_overlay, "$g_presentation_obj_11"),
        (overlay_set_position, "$g_presentation_obj_11", pos1),
        (overlay_add_item, "$g_presentation_obj_11", "@female"),
        (overlay_add_item, "$g_presentation_obj_11", "@male"),
        (try_begin),
          (eq, "$character_gender", tf_female),
          (overlay_set_val, "$g_presentation_obj_11", 0),
        (else_try),
          (eq, "$character_gender", tf_male),
          (overlay_set_val, "$g_presentation_obj_11", 1),
        (try_end),
        
        # father
        (position_set_y, pos1, 430),
        (create_combo_button_overlay, "$g_presentation_obj_12"),
        (overlay_set_position, "$g_presentation_obj_12", pos1),
        (overlay_add_item, "$g_presentation_obj_12", "@a thief"),
        (overlay_add_item, "$g_presentation_obj_12", "@a steppe nomad"),
        (overlay_add_item, "$g_presentation_obj_12", "@a hunter"),
        (overlay_add_item, "$g_presentation_obj_12", "@a veteran warrior"),
        (overlay_add_item, "$g_presentation_obj_12", "@a travelling merchant"),
        (overlay_add_item, "$g_presentation_obj_12", "@an impoverished noble"),
        (try_begin),
          (eq, "$background_type", cb_thief),
          (overlay_set_val, "$g_presentation_obj_12", 0),
        (else_try),
          (eq, "$background_type", cb_nomad),
          (overlay_set_val, "$g_presentation_obj_12", 1),
        (else_try),
          (eq, "$background_type", cb_forester),
          (overlay_set_val, "$g_presentation_obj_12", 2),
        (else_try),
          (eq, "$background_type", cb_guard),
          (overlay_set_val, "$g_presentation_obj_12", 3),
        (else_try),
          (eq, "$background_type", cb_merchant),
          (overlay_set_val, "$g_presentation_obj_12", 4),
        (else_try),
          (eq, "$background_type", cb_noble),
          (overlay_set_val, "$g_presentation_obj_12", 5),
        (try_end),
        
        # early life
        (position_set_y, pos1, 350),
        (create_combo_button_overlay, "$g_presentation_obj_13"),
        (overlay_set_position, "$g_presentation_obj_13", pos1),
        (overlay_add_item, "$g_presentation_obj_13", "@a steppe child"),
        (overlay_add_item, "$g_presentation_obj_13", "@a street urchin"),
        (overlay_add_item, "$g_presentation_obj_13", "@a shop assistant"),
        (overlay_add_item, "$g_presentation_obj_13", "@a craftsman's apprentice"),
        (overlay_add_item, "$g_presentation_obj_13", "@a page at a nobleman's court"),
        (try_begin),
          (eq, "$background_answer_2", cb2_steppe_child),
          (overlay_set_val, "$g_presentation_obj_13", 0),
        (else_try),
          (eq, "$background_answer_2", cb2_urchin),
          (overlay_set_val, "$g_presentation_obj_13", 1),
        (else_try),
          (eq, "$background_answer_2", cb2_merchants_helper),
          (overlay_set_val, "$g_presentation_obj_13", 2),
        (else_try),
          (eq, "$background_answer_2", cb2_apprentice),
          (overlay_set_val, "$g_presentation_obj_13", 3),
        (else_try),
          (eq, "$background_answer_2", cb2_page),
          (overlay_set_val, "$g_presentation_obj_13", 4),
        (try_end),
        
        # later
        (position_set_y, pos1, 270),
        (create_combo_button_overlay, "$g_presentation_obj_14"),
        (overlay_set_position, "$g_presentation_obj_14", pos1),
        (overlay_add_item, "$g_presentation_obj_14", "@a game poacher"),
        (overlay_add_item, "$g_presentation_obj_14", "@a smith"),
        (overlay_add_item, "$g_presentation_obj_14", "@a goods peddler"),
        (overlay_add_item, "$g_presentation_obj_14", "@a university student"),
        (overlay_add_item, "$g_presentation_obj_14", "@a troubadour"),
        (try_begin),
          (eq,"$character_gender",tf_male),
          (overlay_add_item, "$g_presentation_obj_14", "@a squire"),
        (else_try),
          (eq,"$character_gender",tf_female),
          (overlay_add_item, "$g_presentation_obj_14", "@a lady-in-waiting"),
        (try_end),
        (try_begin),
          (eq, "$background_answer_3", cb3_poacher),
          (overlay_set_val, "$g_presentation_obj_14", 0),
        (else_try),
          (eq, "$background_answer_3", cb3_craftsman),
          (overlay_set_val, "$g_presentation_obj_14", 1),
        (else_try),
          (eq, "$background_answer_3", cb3_peddler),
          (overlay_set_val, "$g_presentation_obj_14", 2),
        (else_try),
          (eq, "$background_answer_3", cb3_student),
          (overlay_set_val, "$g_presentation_obj_14", 3),
        (else_try),
          (eq, "$background_answer_3", cb3_troubadour),
          (overlay_set_val, "$g_presentation_obj_14", 4),
        (else_try),
          (this_or_next|eq, "$background_answer_3", cb3_squire),
          (eq, "$background_answer_3", cb3_lady_in_waiting),
          (overlay_set_val, "$g_presentation_obj_14", 5),
        (try_end),
        
        # reason
        (position_set_y, pos1, 190),
        (create_combo_button_overlay, "$g_presentation_obj_15"),
        (overlay_set_position, "$g_presentation_obj_15", pos1),
        (overlay_add_item, "$g_presentation_obj_15", "@lust for money and power"),
        (overlay_add_item, "$g_presentation_obj_15", "@being forced out of your home"),
        (overlay_add_item, "$g_presentation_obj_15", "@wanderlust"),
        (overlay_add_item, "$g_presentation_obj_15", "@the loss of a loved one"),
        (overlay_add_item, "$g_presentation_obj_15", "@personal revenge"),
        (try_begin),
          (eq, "$background_answer_4", cb4_greed),
          (overlay_set_val, "$g_presentation_obj_15", 0),
        (else_try),
          (eq, "$background_answer_4", cb4_disown),
          (overlay_set_val, "$g_presentation_obj_15", 1),
        (else_try),
          (eq, "$background_answer_4", cb4_wanderlust),
          (overlay_set_val, "$g_presentation_obj_15", 2),
        (else_try),
          (eq, "$background_answer_4", cb4_loss),
          (overlay_set_val, "$g_presentation_obj_15", 3),
        (else_try),
          (eq, "$background_answer_4", cb4_revenge),
          (overlay_set_val, "$g_presentation_obj_15", 4),
        (try_end),
        
        ## story
        (call_script, "script_get_character_background_text"),
        (create_text_overlay, reg1, "@{s1}", tf_double_space|tf_scrollable),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 450),
        (overlay_set_area_size, reg1, pos1),
        
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_ready"),
        ####### mouse fix pos system #######
      ]),

    #(ti_on_presentation_run,
      #[
        ####### mouse fix pos system #######
        #(call_script, "script_mouse_fix_pos_run"),
        ####### mouse fix pos system #######
    #]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_11"),
          (try_begin),
            (eq, ":value", 0),
            (assign, "$character_gender", tf_female),
          (else_try),
            (eq, ":value", 1),
            (assign, "$character_gender", tf_male),
          (try_end),
          (start_presentation, "prsnt_character_creation"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_12"),
          (try_begin),
            (eq, ":value", 0),
            (assign, "$background_type", cb_thief),
          (else_try),
            (eq, ":value", 1),
            (assign, "$background_type", cb_nomad),
          (else_try),
            (eq, ":value", 2),
            (assign, "$background_type", cb_forester),
          (else_try),
            (eq, ":value", 3),
            (assign, "$background_type", cb_guard),
          (else_try),
            (eq, ":value", 4),
            (assign, "$background_type", cb_merchant),
          (else_try),
            (eq, ":value", 5),
            (assign, "$background_type", cb_noble),
          (try_end),
          (start_presentation, "prsnt_character_creation"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_13"),
          (try_begin),
            (eq, ":value", 0),
            (assign, "$background_answer_2", cb2_steppe_child),
          (else_try),
            (eq, ":value", 1),
            (assign, "$background_answer_2", cb2_urchin),
          (else_try),
            (eq, ":value", 2),
            (assign, "$background_answer_2", cb2_merchants_helper),
          (else_try),
            (eq, ":value", 3),
            (assign, "$background_answer_2", cb2_apprentice),
          (else_try),
            (eq, ":value", 4),
            (assign, "$background_answer_2", cb2_page),
          (try_end),
          (start_presentation, "prsnt_character_creation"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_14"),
          (try_begin),
            (eq, ":value", 0),
            (assign, "$background_answer_3", cb3_poacher),
          (else_try),
            (eq, ":value", 1),
            (assign, "$background_answer_3", cb3_craftsman),
          (else_try),
            (eq, ":value", 2),
            (assign, "$background_answer_3", cb3_peddler),
          (else_try),
            (eq, ":value", 3),
            (assign, "$background_answer_3", cb3_student),
          (else_try),
            (eq, ":value", 4),
            (assign, "$background_answer_3", cb3_troubadour),
          (else_try),
            (eq, ":value", 5),
            (try_begin),
              (eq, "$character_gender", tf_male),
              (assign, "$background_answer_3", cb3_squire),
            (else_try),
              (eq, "$character_gender", tf_female),
              (assign, "$background_answer_3", cb3_lady_in_waiting),
            (try_end),
          (try_end),
          (start_presentation, "prsnt_character_creation"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_15"),
          (try_begin),
            (eq, ":value", 0),
            (assign, "$background_answer_4", cb4_greed),
          (else_try),
            (eq, ":value", 1),
            (assign, "$background_answer_4", cb4_disown),
          (else_try),
            (eq, ":value", 2),
            (assign, "$background_answer_4", cb4_wanderlust),
          (else_try),
            (eq, ":value", 3),
            (assign, "$background_answer_4", cb4_loss),
          (else_try),
            (eq, ":value", 4),
            (assign, "$background_answer_4", cb4_revenge),
          (try_end),
          (start_presentation, "prsnt_character_creation"),
        (else_try), ## Randomize
          (eq, ":object", "$g_presentation_obj_3"),
          # gender
          (store_random_in_range, ":player_gender", 0, 2),
          (assign, "$character_gender", ":player_gender"),
          # father
          (store_random_in_range, ":r_value", 0, 6),
          (try_begin),
            (eq, ":r_value", 0),
            (assign, "$background_type", cb_thief),
          (else_try),
            (eq, ":r_value", 1),
            (assign, "$background_type", cb_nomad),
          (else_try),
            (eq, ":r_value", 2),
            (assign, "$background_type", cb_forester),
          (else_try),
            (eq, ":r_value", 3),
            (assign, "$background_type", cb_guard),
          (else_try),
            (eq, ":r_value", 4),
            (assign, "$background_type", cb_merchant),
          (else_try),
            (eq, ":r_value", 5),
            (assign, "$background_type", cb_noble),
          (try_end),
          # early life
          (store_random_in_range, ":r_value", 0, 5),
          (try_begin),
            (eq, ":r_value", 0),
            (assign, "$background_answer_2", cb2_steppe_child),
          (else_try),
            (eq, ":r_value", 1),
            (assign, "$background_answer_2", cb2_urchin),
          (else_try),
            (eq, ":r_value", 2),
            (assign, "$background_answer_2", cb2_merchants_helper),
          (else_try),
            (eq, ":r_value", 3),
            (assign, "$background_answer_2", cb2_apprentice),
          (else_try),
            (eq, ":r_value", 4),
            (assign, "$background_answer_2", cb2_page),
          (try_end),
          # later
          (store_random_in_range, ":r_value", 0, 6),
          (try_begin),
            (eq, ":r_value", 0),
            (assign, "$background_answer_3", cb3_poacher),
          (else_try),
            (eq, ":r_value", 1),
            (assign, "$background_answer_3", cb3_craftsman),
          (else_try),
            (eq, ":r_value", 2),
            (assign, "$background_answer_3", cb3_peddler),
          (else_try),
            (eq, ":r_value", 3),
            (assign, "$background_answer_3", cb3_student),
          (else_try),
            (eq, ":r_value", 4),
            (assign, "$background_answer_3", cb3_troubadour),
          (else_try),
            (eq, ":r_value", 5),
            (try_begin),
              (eq, "$character_gender", tf_male),
              (assign, "$background_answer_3", cb3_squire),
            (else_try),
              (eq, "$character_gender", tf_female),
              (assign, "$background_answer_3", cb3_lady_in_waiting),
            (try_end),
          (try_end),
          # reason
          (store_random_in_range, ":r_value", 0, 5),
          (try_begin),
            (eq, ":r_value", 0),
            (assign, "$background_answer_4", cb4_greed),
          (else_try),
            (eq, ":r_value", 1),
            (assign, "$background_answer_4", cb4_disown),
          (else_try),
            (eq, ":r_value", 2),
            (assign, "$background_answer_4", cb4_wanderlust),
          (else_try),
            (eq, ":r_value", 3),
            (assign, "$background_answer_4", cb4_loss),
          (else_try),
            (eq, ":r_value", 4),
            (assign, "$background_answer_4", cb4_revenge),
          (try_end),
          (start_presentation, "prsnt_character_creation"),
        (else_try), ## Default
          (eq, ":object", "$g_presentation_obj_2"),
          (assign, "$character_gender", tf_male),
          (assign,"$background_type",cb_noble),
          (assign,"$background_answer_2", cb2_page),
          (assign,"$background_answer_3",cb3_squire),
          (assign,"$background_answer_4", cb4_revenge),
          (start_presentation, "prsnt_character_creation"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_1"),
          # skill
          (call_script, "script_start_adventuring_raise_skills"),
          # gender
          (try_begin),
            (eq,"$character_gender",tf_male),
            (troop_set_type,"trp_player", 0),
          (else_try),
            (eq,"$character_gender",tf_female),
            (troop_set_type,"trp_player", 1),
          (try_end),
          (try_begin),
            (eq, "$background_type", cb_noble),
            (jump_to_menu, "mnu_auto_return"),
#normal_banner_begin
            (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
#             (start_presentation, "prsnt_custom_banner"),
          (else_try),
            (presentation_set_duration, 0),
            (jump_to_menu, "mnu_auto_return"),
          (try_end),
        (try_end),
    ]),
  ]),
## CC


##diplomacy begin
    ("dplmc_policy_management",0,mesh_load_window,[
      (ti_on_presentation_load,
       [
        (set_fixed_point_multiplier, 1000),
        (presentation_set_duration, 999999),
       
        # done
        (create_game_button_overlay, "$g_presentation_obj_10", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_10", pos1),
        
        # title
        (create_text_overlay, reg1, "@Select your domestic policy", tf_center_justify|tf_vertical_align_center),
        (position_set_x, pos1, 445),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg1, pos1),

        (create_slider_overlay, "$g_presentation_obj_sliders_1", -3, 3),
        (create_slider_overlay, "$g_presentation_obj_sliders_2", -3, 3),
        (create_slider_overlay, "$g_presentation_obj_sliders_3", -3, 3),
        (create_slider_overlay, "$g_presentation_obj_sliders_4", -3, 3),
        (assign, reg1, 25),
        (create_text_overlay, "$g_presentation_obj_sliders_5", "str_dplmc_neither_centralize_nor_decentralized"),
        (create_text_overlay, "$g_presentation_obj_sliders_6", "str_dplmc_neither_aristocratic_nor_plutocratic"),
        (create_text_overlay, "$g_presentation_obj_sliders_7", "str_dplmc_mixture_serfs"),
        (create_text_overlay, "$g_presentation_obj_sliders_8", "str_dplmc_mediocre_quality"),
        
        (create_text_overlay, "$g_presentation_obj_1", "@Centralization:"),
        (create_text_overlay, "$g_presentation_obj_2", "@Aristocracy:"),
        (create_text_overlay, "$g_presentation_obj_3", "@Serfdom:"),
        (create_text_overlay, "$g_presentation_obj_4", "@Conscript quality:"),  
        (create_text_overlay, "$g_presentation_obj_5", "@High centralization reduces tax inefficiency for the sovereign and raises it for vassals. This will interfere  the relations between ruler and vassals."),
        (create_text_overlay, "$g_presentation_obj_6", "@High aristocracy will improve the relations between the sovereign and his vassals who will be able to raise larger armies but it will decreased trade capabilities with a disenfranchised merchant class."),
        (create_text_overlay, "$g_presentation_obj_7", "@High serfdom reduces tax inefficiency for the sovereign and his vassals and vassals can maintain larger armies but soldiers lose morale."),
        (create_text_overlay, "$g_presentation_obj_8", "@High troop quality increases the strength of troops but decreases army size."),    
        
        (faction_get_slot, ":centralization", "fac_player_supporters_faction", dplmc_slot_faction_centralization),
        (faction_get_slot, ":aristocratcy", "fac_player_supporters_faction", dplmc_slot_faction_aristocracy),
        (faction_get_slot, ":serfdom", "fac_player_supporters_faction", dplmc_slot_faction_serfdom),
        (faction_get_slot, ":quality", "fac_player_supporters_faction", dplmc_slot_faction_quality),

        (overlay_set_val, "$g_presentation_obj_sliders_1", ":centralization"),
        (overlay_set_val, "$g_presentation_obj_sliders_2", ":aristocratcy"),
        (overlay_set_val, "$g_presentation_obj_sliders_3", ":serfdom"),
        (overlay_set_val, "$g_presentation_obj_sliders_4", ":quality"),
        (position_set_x, pos1, 200),
        (position_set_y, pos1, 600),
        (overlay_set_position, "$g_presentation_obj_sliders_1", pos1),
        (position_set_y, pos1, 450),
        (overlay_set_position, "$g_presentation_obj_sliders_2", pos1),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_sliders_3", pos1),
        (position_set_y, pos1, 150),
        (overlay_set_position, "$g_presentation_obj_sliders_4", pos1),
        
        (position_set_x, pos1, 100),
        (position_set_y, pos1, 650),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (position_set_y, pos1, 500),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (position_set_y, pos1, 350),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (position_set_y, pos1, 200),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 550),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (position_set_y, pos1, 400),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (position_set_y, pos1, 250),
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (position_set_y, pos1, 100),
        (overlay_set_position, "$g_presentation_obj_8", pos1),
        
        (position_set_x, pos1, 775),
        (position_set_y, pos1, 775),
        (overlay_set_size, "$g_presentation_obj_5", pos1),
        (overlay_set_size, "$g_presentation_obj_6", pos1),
        (overlay_set_size, "$g_presentation_obj_7", pos1),
        (overlay_set_size, "$g_presentation_obj_8", pos1),

        (position_set_x, pos1, 400),
        (position_set_y, pos1, 600),
        (overlay_set_position, "$g_presentation_obj_sliders_5", pos1),
        (position_set_y, pos1, 450),
        (overlay_set_position, "$g_presentation_obj_sliders_6", pos1),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_sliders_7", pos1),
        (position_set_y, pos1, 150),
        (overlay_set_position, "$g_presentation_obj_sliders_8", pos1),
        
        (position_set_x, pos1, 925),
        (position_set_y, pos1, 925),
        (overlay_set_size, "$g_presentation_obj_sliders_5", pos1),
        (overlay_set_size, "$g_presentation_obj_sliders_6", pos1),
        (overlay_set_size, "$g_presentation_obj_sliders_7", pos1),
        (overlay_set_size, "$g_presentation_obj_sliders_8", pos1),
        ]),
      (ti_on_presentation_run,
       [
        ]),
      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        
        (try_begin),
          (eq, ":object", "$g_presentation_obj_sliders_1"),
          (faction_set_slot,  "fac_player_supporters_faction", dplmc_slot_faction_centralization, ":value"),
          (val_add, ":value", "str_dplmc_neither_centralize_nor_decentralized"),
          (overlay_set_text, "$g_presentation_obj_sliders_5", ":value"),
        (else_try),          
          (eq, ":object", "$g_presentation_obj_sliders_2"),
          (faction_set_slot,  "fac_player_supporters_faction", dplmc_slot_faction_aristocracy, ":value"),
          (val_add, ":value", "str_dplmc_neither_aristocratic_nor_plutocratic"),
          (overlay_set_text, "$g_presentation_obj_sliders_6", ":value"),
        (else_try),          
          (eq, ":object", "$g_presentation_obj_sliders_3"),
          (faction_set_slot,  "fac_player_supporters_faction", dplmc_slot_faction_serfdom, ":value"),
          (val_add, ":value", "str_dplmc_mixture_serfs"),
          (overlay_set_text, "$g_presentation_obj_sliders_7", ":value"),
        (else_try),          
          (eq, ":object", "$g_presentation_obj_sliders_4"),
          (faction_set_slot,  "fac_player_supporters_faction", dplmc_slot_faction_quality, ":value"),
          (val_add, ":value", "str_dplmc_mediocre_quality"),
          (overlay_set_text, "$g_presentation_obj_sliders_8", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_10"),
          (assign, "$g_players_policy_set", 1),
          (presentation_set_duration, 0),
        (try_end),
    ]),
  ]),
  
    ("dplmc_peace_terms",0,mesh_load_window,[
      (ti_on_presentation_load,
       [
        (set_fixed_point_multiplier, 1000),
        (presentation_set_duration, 999999),
       
        # done
        (create_game_button_overlay, "$g_presentation_obj_10", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_10", pos1),
  
        #cancel
        (create_game_button_overlay, "$g_presentation_obj_9", "@Cancel"),
        (position_set_x, pos1, 100),
        (overlay_set_position, "$g_presentation_obj_9", pos1),
        
        # title
        (create_text_overlay, reg1, "@Dictate the peace terms", tf_center_justify|tf_vertical_align_center),
        (position_set_x, pos1, 445),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg1, pos1),

        (position_set_y, pos1, 550),
        (create_text_overlay, "$g_presentation_obj_2", "@Select the castle and the amount of money and check the boxes to activate the demand. The demands are combined if both boxes are checked."),
        (position_set_x, pos1, 50),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        
        (create_slider_overlay, "$g_presentation_obj_sliders_1", 1, 10),
        (overlay_set_val, "$g_presentation_obj_sliders_1", 1),
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 350),
        (overlay_set_position, "$g_presentation_obj_sliders_1", pos1),
        (assign, "$demanded_money", 1000),
        (assign, "$diplomacy_var", 1),

        (create_text_overlay, "$g_presentation_obj_sliders_2", "@1000 denars"),
        (position_set_x, pos1, 500),
        (overlay_set_position, "$g_presentation_obj_sliders_2", pos1),
        
        (create_check_box_overlay, "$g_presentation_obj_battle_check0", "mesh_checkbox_off", "mesh_checkbox_on"),
        (position_set_x, pos1, 700),
        (overlay_set_position, "$g_presentation_obj_battle_check0", pos1),
        (overlay_set_val, "$g_presentation_obj_battle_check0", 1),  

        (assign, "$demanded_castle", 0), 
        (assign, ":castle_count", 0),
        (create_combo_button_overlay, "$g_presentation_obj_1"),     
        (try_for_range, ":castle", castles_begin, castles_end),
          (store_faction_of_party, ":castle_faction", ":castle"),
          (eq, ":castle_faction", "$g_notification_menu_var1"),
          (str_store_party_name, s2, ":castle"),
          (overlay_add_item, "$g_presentation_obj_1", s2),   
          (assign, "$demanded_castle", ":castle"),   
          (val_add, ":castle_count", 1),         
        (end_try),       
        (assign, "$diplomacy_var2", 0),                 
        (position_set_x, pos1, 300),
        (position_set_y, pos1, 250),
        (overlay_set_position, "$g_presentation_obj_1", pos1), 
        (overlay_set_val, "$g_presentation_obj_1", ":castle_count"), 
              
        (create_check_box_overlay, "$g_presentation_obj_battle_check1", "mesh_checkbox_off", "mesh_checkbox_on"),
        (position_set_x, pos1, 700),
        (overlay_set_position, "$g_presentation_obj_battle_check1", pos1),  

        ]),
      (ti_on_presentation_run,
       [
        ]),
      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
        
        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
   
          (assign, ":cur", 0),
          (try_for_range, ":castle", castles_begin, castles_end),
            (store_faction_of_party, ":castle_faction", ":castle"),
            (eq, ":castle_faction", "$g_notification_menu_var1"),
            (try_begin),
              (eq, ":cur", ":value"),
              (assign, "$demanded_castle", ":castle"),
            (try_end),
            (val_add, ":cur", 1),              
          (try_end),       
          
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_check0"), 
          (assign, "$diplomacy_var", ":value"),
          
        (else_try),
          (eq, ":object", "$g_presentation_obj_battle_check1"),
          (assign, "$diplomacy_var2", ":value"),
          
        (else_try),
          (eq, ":object", "$g_presentation_obj_sliders_1"),
          (store_mul, "$demanded_money",":value", 1000),
          (assign, reg0, "$demanded_money"),
          (overlay_set_text, "$g_presentation_obj_sliders_2", "@{reg0} denars"),
                   
        (else_try),    
          (eq, ":object", "$g_presentation_obj_9"),
          (presentation_set_duration, 0),
        (else_try),      
          (eq, ":object", "$g_presentation_obj_10"),
          (presentation_set_duration, 0),

          (try_begin),
            (eq, "$diplomacy_var", 0),
            (assign, "$demanded_money", 0),                 
          (try_end),

          (try_begin),
            (eq, "$diplomacy_var2", 0),
            (assign, "$demanded_castle", 0),                 
          (try_end),
          
          (assign, ":demand", 0),
          (try_begin),
            (gt, "$demanded_money", 0),
            (store_div, ":demand", "$demanded_money", 1000),
          (try_end),
          (try_begin),
            (is_between, "$demanded_castle", castles_begin, castles_end),
            (val_add, ":demand", 12),
          (try_end),
  
          (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
          (assign, ":goodwill", reg0), 
          (val_mul, ":goodwill", 2),     
          (store_random_in_range, ":random", 0, ":demand"),
          
          (val_div, ":demand", -2),        
    
          (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", ":demand"),
          (try_begin),
            (le, ":random", ":goodwill"),
            (try_begin),
              (is_between, "$demanded_castle", castles_begin, castles_end),
              (call_script, "script_give_center_to_faction", "$demanded_castle", "fac_player_supporters_faction"),
            (try_end),
            (try_begin),
              (gt, "$demanded_money", 0),
              (call_script, "script_dplmc_pay_into_treasury", "$demanded_money"),
            (try_end),
            (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),    
            (presentation_set_duration, 0),
            (change_screen_return),
          (else_try),       
            (jump_to_menu,"mnu_dplmc_deny_terms"),
          (try_end),  
         
        (try_end),
    ]),
  ]),

  # Jrider +
  # REPORTS PRESENTATIONS 1.2 :
  # Factions relations presentation report
  ("jrider_faction_relations_report", 0,
   mesh_message_window,
   [
     (ti_on_presentation_load,
      [
    (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        # Embed picture upper right
        (create_mesh_overlay, reg1, "mesh_pic_castledes"),
        (position_set_x, pos1, 180),
        (position_set_y, pos1, 180),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 795),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg1, pos1),

        # Embed picture upper left
        (create_mesh_overlay, reg1, "mesh_pic_looted_village"),
        (position_set_x, pos1, 170),
        (position_set_y, pos1, 170),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, -15),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg1, pos1),

    # Presentation title, centered at the top
        (create_text_overlay, reg1, "@_Sovereignty Relations Report_", tf_center_justify),
    (position_set_x, pos1, 500), # Higher, means more toward the right
        (position_set_y, pos1, 670), # Higher, means more toward the top
        (overlay_set_position, reg1, pos1),
    (position_set_x, pos1, 1500),
        (position_set_y, pos1, 1500),
    (overlay_set_size, reg1, pos1),

    # Back to menu - graphical button
    (create_game_button_overlay, reg1, "@_Return to menu_"),
    (position_set_x, pos1, 500),
        (position_set_y, pos1, 23),
        (overlay_set_position, reg1, pos1),
        (assign, "$g_jrider_faction_report_Return_to_menu", reg1),

    # Set Headlines
#set column title
          (assign, ":x_poshl", 250),  
          (assign, ":y_pos", 620),
          (position_set_y, pos1, ":y_pos"),
    (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
            (faction_slot_eq, ":faction", slot_faction_state, sfs_active), # continue if active
            (try_begin),
              (is_between, ":faction", npc_kingdoms_begin, npc_kingdoms_end),
              (store_sub, ":offset", ":faction", "fac_kingdom_1"),
              (val_add, ":offset", "str_swadians"),
              (str_store_string, s1, ":offset"),    
            (else_try),
              (str_store_string, s1, "@Your sovereignty"),    
            (try_end),
            
            (str_store_string, s11, ":offset"),  
            (create_text_overlay, reg10, s1, tf_left_align|tf_with_outline),
            (faction_get_color, ":faction_color", ":faction"),
            (overlay_set_color, reg10, ":faction_color"),
      
            (position_set_x, pos3, 650),
            (position_set_y, pos3, 800),
            (overlay_set_size, reg10, pos3),

            (position_set_x, pos1, ":x_poshl"),
            (overlay_set_position, reg10, pos1),
            (val_add, ":x_poshl", 90),
    (try_end),


    (assign, ":x_poshl", 215),
     (assign, ":y_pos", 597),
     (assign, ":headline_size", 0),
    (position_set_x, ":headline_size", 720),
        (position_set_y, ":headline_size", 775),
       
        (assign, ":hl_columnsep_size", 50),
        (position_set_x, ":hl_columnsep_size", 60),
        (position_set_y, ":hl_columnsep_size", 28000),

        (create_text_overlay, reg2, "@Player^Relation", tf_center_justify),
        (overlay_set_size, reg2, ":headline_size"),
        (position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, reg2, pos1),

        (val_add, ":x_poshl", 45),
        (try_for_range, ":count", 0, 7),
          # create a separator column
          (create_mesh_overlay, reg1, "mesh_white_plane"),
          (overlay_set_color, reg1, 0x000000),
          (overlay_set_size, reg1, ":hl_columnsep_size"),      
          (store_sub, ":line_x", ":x_poshl", 15), # set it 21 pix left of current column start
          (store_sub, ":y_pos2", ":y_pos", 500), # set it 21 pix left of current column start
          (position_set_x, pos2, ":line_x"),
          (position_set_y, pos2, ":y_pos2"),
          (overlay_set_position, reg1, pos2),
          (val_add, ":x_poshl", 90),
          
          (try_begin),
            (eq, "$cheat_mode", 1),
            (assign, reg20, ":count"),
            (display_message, "@{!}DEBUG - Drawing line {reg20}"),
          (try_end),
        (try_end),

        # clear the string globals that we'll use
         (str_clear, s9),
    (str_clear, s8),
    (str_clear, s3),
    (str_clear, s60),
    (str_clear, s61),
    (str_clear, s0),

        # Scrollable area (all the next overlay will be contained in this, s0 sets the scrollbar)
        (create_text_overlay, reg1, s0, tf_scrollable_style_2),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 70),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 860),
        (position_set_y, pos1, 527),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        # set base position and size for lines
        (assign, ":line_size", 0),
        (assign, ":y_pos", 0),

        # set base color for line
    (assign, ":line_color", 0x000000),

        # Line faction loop begins here - fetching corresponding informations and printing the line title
        (try_for_range_backwards, ":faction_line", kingdoms_begin, kingdoms_end),
            (faction_slot_eq, ":faction_line", slot_faction_state, sfs_active), # continue if active

            # Base position for subheaders
            (assign, ":x_posfhl", 220),

            # Loop other factions (columns)
            (try_for_range, ":faction_column", kingdoms_begin, kingdoms_end),
                (faction_slot_eq, ":faction_column", slot_faction_state, sfs_active), # continue if active

                (try_begin), # not same faction
                  (neq, ":faction_column", ":faction_line"),
                 
                  (str_store_faction_name, s8, ":faction_column"),
  
                  # sub-faction excluding current faction line
                  (try_begin),
                      # different from faction line, display status and relation with faction line
                      (neq, ":faction_column", ":faction_line"),
                      (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":faction_line", ":faction_column"),
                      (assign, ":global_diplomatic_status", reg0),
                      (assign, ":extended_diplomatic_status", reg1),
  
                      (try_begin), # War
                          (eq, ":global_diplomatic_status", -2),
                          (str_store_string, s60, "@War"),
                          (assign, reg60, 0xDD0000),
                          (assign, reg59, 0),
                      (else_try), # Border incident
                          (eq, ":global_diplomatic_status", -1),
                          (str_store_string, s60, "@Casus Belli"),
                          (assign, reg60, 0xDD8000),
                          (assign, reg59, ":extended_diplomatic_status"),
                      (else_try), # Peace
                          (eq, ":global_diplomatic_status", 0),
                          (str_store_string, s60, "@Peace"),
                          (assign, reg60, 0xFFFFFF),
                          (assign, reg59, 0),
                      (else_try), # Truce (non aggression)
                          (eq, ":global_diplomatic_status", 1),
                          (str_store_string, s60, "@Truce"),
                          (assign, reg60, 0xDDDDDD),
                          (assign, reg59, ":extended_diplomatic_status"),
  
                          # for Diplomacy, comment if not using
                          (try_begin),
                              (ge, ":extended_diplomatic_status", 61),
                              (str_store_string, s60, "@Alliance"),
                              (assign, reg60, 0x00FF00),
                              (store_sub, reg59, ":extended_diplomatic_status", 60),
                          (else_try),
                              (ge, ":extended_diplomatic_status", 41),
                              (str_store_string, s60, "@Defense"),
                              (assign, reg60, 0x00FFAA),
                              (store_sub, reg59, ":extended_diplomatic_status", 40),
                          (else_try),
                              (ge, ":extended_diplomatic_status", 21),
                              (str_store_string, s60, "@Trade"),
                              (assign, reg60, 0x00FFCC),
                              (store_sub, reg59, ":extended_diplomatic_status", 20),
                          (try_end),
                      (try_end),
  
                      (val_add, ":x_poshl", 50),
  
                      # diplomatic status and duration block (set at current line)
                      (create_text_overlay, reg10, s60, tf_left_align|tf_with_outline),
                      (overlay_set_size, reg10, ":line_size"),
                      (overlay_set_color, reg10, reg60),
                      (store_sub, ":line_x", ":x_posfhl", 20),
                      (store_add, ":line_y", ":y_pos", 54),
                      (position_set_x, pos3, ":line_x"),
                      (position_set_y, pos3, ":line_y"),
                      (overlay_set_position, reg10, pos3),
                      
                      (create_text_overlay, reg10, "@{reg59?{reg59} days:}", tf_center_justify),
                      (overlay_set_size, reg10, ":line_size"),                      
                      (store_add, ":line_y", ":y_pos", 36),
                      (store_add, ":line_x", ":x_posfhl", 10),
                      (position_set_x, pos3, ":line_x"),
                      (position_set_y, pos3, ":line_y"),                      
                      (overlay_set_position, reg10, pos3),
                      
  
                      # add diplomatic status
                      (store_relation, ":kingdom_relation", ":faction_line", ":faction_column"),

                      # kingdom relation (same line as faction name)
                      (assign, reg61, ":kingdom_relation"),
                      (create_text_overlay, reg10, "@{reg61}", tf_center_justify),
                      (overlay_set_size, reg10, ":line_size"),
  
                      (store_add, ":line_y", ":y_pos", 18),
                      (store_add, ":line_x", ":x_posfhl", 10),
                      (position_set_x, pos3, ":line_x"),
                      (position_set_y, pos3, ":line_y"),
                      (overlay_set_position, reg10, pos3),
                  (try_end), # end select alternate display
                (try_end),

                # increase column x position
                (val_add, ":x_posfhl", 90), # valid values 220, 385, 550, 715
            (try_end), # end of column faction loop

            # Faction line information, this is a 4 line block
            # reset x postion for next beginning column and decrease y position according to line count
            (assign, ":x_poshl", 165),

            (val_add, ":y_pos", 54), # linebreak

            # create a separator for faction line
            (create_mesh_overlay, reg1, "mesh_white_plane"),
            (overlay_set_color, reg1, 0x000000),
            (position_set_x, pos1, 42000),
            (position_set_y, pos1, 60),
            (overlay_set_size, reg1, pos1),
            (position_set_x, pos1, 17),
            (store_add, ":line_y", ":y_pos", 20), # set it 20 pix above current line
            (position_set_y, pos1, ":line_y"),
            (overlay_set_position, reg1, pos1),

            # Set line title
            (str_store_faction_name, s9, ":faction_line"),
			## WINDYPLAINS+ ## - Shrink size of Vaegirs faction name so it doesn't cover the player relation value.
			(try_begin),
				(eq, ":faction_line", "fac_kingdom_2"),
				(str_store_string, s9, "@Grand Principality"),
			(try_end),
			## WINDYPLAINS- ##
           (str_store_string, s1, "@{s9}"),
            (create_text_overlay, reg10, s1, tf_left_align|tf_with_outline),
            (faction_get_color, ":faction_color", ":faction_line"),
            (overlay_set_color, reg10, ":faction_color"),

            (position_set_x, pos3, 750),
            (position_set_y, pos3, 850),
            (overlay_set_size, reg10, pos3),

            (position_set_x, pos3, 10),
            (position_set_y, pos3, ":y_pos"),
            (overlay_set_position, reg10, pos3),

            # set position for columns
            (assign, ":x_poshl", 165),
            (assign, ":line_size", 0),
            (position_set_x, ":line_size", 700),
            (position_set_y, ":line_size", 800),

            ## Player relation (first column)
            (store_relation, reg1, "fac_player_supporters_faction", ":faction_line"),

            # no clean strings existing, doing it the same way it's done in game_menu
            (try_begin),
                (ge, reg1, 90),
                (str_store_string, s3, "@Loyal"),
            (else_try),
                (ge, reg1, 80),
                (str_store_string, s3, "@Devoted"),
            (else_try),
                (ge, reg1, 70),
                (str_store_string, s3, "@Fond"),
            (else_try),
                (ge, reg1, 60),
                (str_store_string, s3, "@Gracious"),
            (else_try),
                (ge, reg1, 50),
                (str_store_string, s3, "@Friendly"),
            (else_try),
                (ge, reg1, 40),
                (str_store_string, s3, "@Supportive"),
            (else_try),
                (ge, reg1, 30),
                (str_store_string, s3, "@Favorable"),
            (else_try),
                (ge, reg1, 20),
                (str_store_string, s3, "@Cooperative"),
            (else_try),
                (ge, reg1, 10),
                (str_store_string, s3, "@Accepting"),
            (else_try),
                (ge, reg1, 0),
                (str_store_string, s3, "@Indifferent"),
            (else_try),
                (ge, reg1, -10),
                (str_store_string, s3, "@Suspicious"),
            (else_try),
                (ge, reg1, -20),
                (str_store_string, s3, "@Grumbling"),
            (else_try),
                (ge, reg1, -30),
                (str_store_string, s3, "@Hostile"),
            (else_try),
                (ge, reg1, -40),
                (str_store_string, s3, "@Resentful"),
            (else_try),
                (ge, reg1, -50),
                (str_store_string, s3, "@Angry"),
            (else_try),
                (ge, reg1, -60),
                (str_store_string, s3, "@Hateful"),
            (else_try),
                (ge, reg1, -70),
                (str_store_string, s3, "@Revengeful"),
            (else_try),
                (str_store_string, s3, "@Vengeful"),
            (try_end),

            # Set relation to player numerical value (same line)
            (create_text_overlay, reg10, "@{reg1}", tf_right_align),
            (overlay_set_size, reg10, ":line_size"),
            (store_add, ":line_x", ":x_poshl", 20),
            (position_set_x, pos1, ":line_x"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, reg10, pos1),
            (overlay_set_color, reg10, ":line_color"),

            # Set relation to player string value (second line)
            (create_text_overlay, reg10, "@{s3}", tf_right_align),
            (overlay_set_size, reg10, ":line_size"),
            (position_set_x, pos1, ":line_x"),
            (store_sub, ":line_y", ":y_pos", 20),
            (position_set_y, pos1, ":line_y"),
            (overlay_set_position, reg10, pos1),
            (overlay_set_color, reg10, ":line_color"),

            # Set Faction Coat of Arm for standard faction (left of relation string)
            (try_begin),
                (neq, ":faction_line", "fac_player_supporters_faction"),
                (store_sub, ":mesh_index", ":faction_line", kingdoms_begin),
                (val_add, ":mesh_index", "mesh_pic_recruits"),
                (create_mesh_overlay, reg10, ":mesh_index"),
                (position_set_x, pos1, 75),
                (position_set_y, pos1, 75),
                (overlay_set_size, reg10, pos1),
                (position_set_x, pos1, 165),
                (store_sub, ":line_y", ":y_pos", 37),
                (position_set_y, pos1, ":line_y"),
                (overlay_set_position, reg10, pos1),
            (try_end),

            # for current line_faction count lords and centers
            (assign, ":num_lords", 0),
            (assign, ":num_caravans", 0),
            (assign, ":num_centers", 0),
            (assign, ":unassigned_centers", 0),
            (try_for_parties, ":cur_party"),
                (store_faction_of_party, ":cur_faction", ":cur_party"),
                (eq, ":cur_faction", ":faction_line"),

                (try_begin),
                    (party_slot_eq, ":cur_party", slot_party_type, spt_kingdom_hero_party),
                    (val_add, ":num_lords", 1),
                (else_try),
                    (party_slot_eq, ":cur_party", slot_party_type, spt_kingdom_caravan),
                    (val_add, ":num_caravans", 1),
                (else_try),
                    (this_or_next|party_slot_eq, ":cur_party", slot_party_type, spt_town),
                    (this_or_next|party_slot_eq, ":cur_party", slot_party_type, spt_castle),
                    (party_slot_eq, ":cur_party", slot_party_type, spt_village),
                    (val_add, ":num_centers", 1),

                    (try_begin),
                        (party_slot_eq, ":cur_party", slot_town_lord, stl_unassigned),
                        (val_add, ":unassigned_centers", 1),
                    (try_end),
                (try_end),
            (try_end), # end of parties loop

            # Count prisoners
            (assign, ":prisoners", 0),
            (try_for_range, ":lord_id", active_npcs_begin, active_npcs_end),
                (troop_slot_eq, ":lord_id", slot_troop_occupation, slto_kingdom_hero),
                (troop_slot_ge, ":lord_id", slot_troop_prisoner_of_party, 0),
                (store_troop_faction, ":lord_faction", ":lord_id"),
                (eq, ":lord_faction", ":faction_line"),
                (val_add, ":prisoners", 1),
            (try_end),

            # add count to last line for faction line report (second, third and fourth line)
            (assign, reg61, ":num_centers"),
            (assign, reg58, ":unassigned_centers"),
            (create_text_overlay, reg10, "@{reg61} {reg58?({reg58} U) :}Centers", tf_left_align),
            (overlay_set_size, reg10, ":line_size"),
            (position_set_x, pos1, 15),
            (store_sub, ":line_y", ":y_pos", 17),
            (position_set_y, pos1, ":line_y"),
            (overlay_set_position, reg10, pos1),
            (overlay_set_color, reg10, 0x000000),

            (assign, reg62, ":num_caravans"),
            (create_text_overlay, reg10, "@{reg62} Caravans", tf_left_align),
            (overlay_set_size, reg10, ":line_size"),
            (position_set_x, pos1, 15),
            (val_sub, ":line_y", 17),
            (position_set_y, pos1, ":line_y"),
            (overlay_set_position, reg10, pos1),
            (overlay_set_color, reg10, 0x000000),

            (assign, reg60, ":num_lords"),
            (assign, reg59, ":prisoners"),
            (create_text_overlay, reg10, "@{reg60} {reg59?({reg59} P) :}Lords", tf_left_align),
            (overlay_set_size, reg10, ":line_size"),
            (position_set_x, pos1, 15),
            (val_sub, ":line_y", 17),
            (position_set_y, pos1, ":line_y"),
            (overlay_set_position, reg10, pos1),
            (overlay_set_color, reg10, 0x000000),

            # increase line for next faction block
            (val_add, ":y_pos", 18),#linebreak

        (try_end), # end of faction loop
        (set_container_overlay, -1),
   ]),
   ## END on load trigger

   ## Check for buttonpress
   (ti_on_presentation_event_state_change,
    [
        (store_trigger_param_1, ":button_pressed_id"),
        (try_begin),
             (eq, ":button_pressed_id", "$g_jrider_faction_report_Return_to_menu"), # pressed  (Return to menu)
        (presentation_set_duration, 0),
    (try_end),
    ]),
   ## END presentation event state change trigger

   ## Event to process when running the presentation
   (ti_on_presentation_run,
    [
        (try_begin),
      (this_or_next|key_clicked, key_escape),
      (key_clicked, key_right_mouse_button),
      (presentation_set_duration, 0),
      (jump_to_menu, "mnu_reports"),
        (try_end),

        ]),
   ]),
  # END presentation run trigger
  # END Faction relation presentation
  # Jrider -

##diplomacy end

# Jrider +
  ##############################################################################
  # REPORT PRESENTATIONS v1.2
  ## Character relations report
  ("jrider_character_relation_report", 0,
   mesh_message_window,
   [
     ## Load Presentation
     (ti_on_presentation_load,
      # generic_ti_on_load +
      [
		(presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (str_clear, s0),
        (str_clear, s1),

        # Character presentation type variations
        (try_begin),
            ###############################
            ## Courtship Relations presentation
            (eq, "$g_character_presentation_type", 0),

            # Set presentation title string
            (str_store_string, s0, "@_Courtships in progress_"),

            # Set size of listbox
            (assign, ":base_scroll_y", 160),
            (assign, ":base_scroll_size_y", 480),
            (assign, ":base_candidates_y", 0), # scrollable area size minus (one line size + 2) 430

            # Set storage index
            (assign, "$g_base_character_presentation_storage_index", 1000),

            # presentation specific extra overlays
            (call_script, "script_generate_knonwn_poems_string"),

            # Extra text area for knowns poems (filling once so we use a register), filled from s1 generated in script call
            (create_text_overlay, reg1, s1, tf_left_align),
            (position_set_x, pos1, 590), # position
            (position_set_y, pos1, 55),
            (overlay_set_position, reg1, pos1),
            (position_set_x, pos1, 750), # size
            (position_set_y, pos1, 850),
            (overlay_set_size, reg1, pos1),
            (overlay_set_color, reg1, 0xFF66CC), # color
        (else_try),
            ###############################
            ## Lord Relations presentation
            (eq, "$g_character_presentation_type", 1),

            # Set presentation title string
            (str_store_string, s0, "@_Known Lords by Relation_"),

            # Set size of listbox
            (assign, ":base_scroll_y", 110),
            (assign, ":base_scroll_size_y", 550),
            (assign, ":base_candidates_y", 0), # scrollable area size minus 530

            # Set storage index
            (assign, "$g_base_character_presentation_storage_index", 2000),
        (else_try),
            ###############################
            ## Player and Companions presentation
            (eq, "$g_character_presentation_type", 2),

            # Set presentation title string
            (str_store_string, s0, "@_Character & Companions_"),

            # Set size of listbox
            (assign, ":base_scroll_y", 110),
            (assign, ":base_scroll_size_y", 550),
            (assign, ":base_candidates_y", 0), # scrollable area size minus (one line size + 2) 530

            # Set storage index
            (assign, "$g_base_character_presentation_storage_index", 3000),

            # Extra area for equipment display
            (assign, ":inv_bar_size", 0),
            (position_set_x, ":inv_bar_size", 400),
            (position_set_y, ":inv_bar_size", 400),

            (create_mesh_overlay, reg1, "mesh_mp_inventory_left"),
            (position_set_x, pos1, 67),
            (position_set_y, pos1, 300),
            (overlay_set_position, reg1, pos1),
            (overlay_set_size, reg1, ":inv_bar_size"),

            (create_mesh_overlay, reg1, "mesh_mp_inventory_right"),
            (position_set_x, pos1, 450),
            (position_set_y, pos1, 330),
            (overlay_set_position, reg1, pos1),
            (overlay_set_size, reg1, ":inv_bar_size"),
        (try_end),
        # END of presentation type specific init and static overlay

        ###############################
        # Create common overlays
        # set foreground mesh overlay (has some transparency in it, so can't use it directly)
        (create_mesh_overlay, reg1, "mesh_face_gen_window"),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),
		(position_set_x, pos1, 1000),
        (position_set_y, pos1, 1000),
		(overlay_set_size, reg1, pos1),

    # Presentation title overlay, centered at the top of right pane (from s0, presentation type specific)
        (create_text_overlay, reg1, s0, tf_center_justify),
        (overlay_set_color, reg1, 0xDDDDDD),
		(position_set_x, pos1, 740), # Higher, means more toward the right
        (position_set_y, pos1, 680), # Higher, means more toward the top
        (overlay_set_position, reg1, pos1),
		(position_set_x, pos1, 1200),
        (position_set_y, pos1, 1200),
		(overlay_set_size, reg1, pos1),

    # Done button
        (create_game_button_overlay, "$g_jrider_character_report_Return_to_menu", "@_Done_"),
		(position_set_x, pos1, 290),
        (position_set_y, pos1, 10),
        (overlay_set_position, "$g_jrider_character_report_Return_to_menu", pos1),

        # Character Information text to fill when an entry is clicked in the list
        (create_text_overlay, "$g_jrider_character_information_text", "str_space", tf_left_align),
        (overlay_set_color, "$g_jrider_character_information_text", 0xFFFFFF),
        (position_set_x, pos1, 55), # Higher, means more toward the right
        (position_set_y, pos1, 60), # Higher, means more toward the top
        (overlay_set_position, "$g_jrider_character_information_text", pos1),
        (position_set_x, pos1, 700), # smaller means smaller font
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_jrider_character_information_text", pos1),

        # Character selection listbox overlay
        # use scrollable text area with global reference so objects can be put inside using overlay_set_container
        (create_text_overlay, "$g_jrider_character_relation_listbox", "str_empty_string", tf_scrollable_style_2),
        (position_set_x, pos1, 590),
        (position_set_y, pos1, ":base_scroll_y"),
        (overlay_set_position, "$g_jrider_character_relation_listbox", pos1),
        (position_set_x, pos1, 335),
        (position_set_y, pos1, ":base_scroll_size_y"),
        (overlay_set_area_size, "$g_jrider_character_relation_listbox", pos1),

        # Faction filter
        (create_combo_button_overlay, "$g_jrider_character_faction_filter", "str_empty_string",0),
        (position_set_x, pos1, 507),
        (position_set_y, pos1, 709),
        (overlay_set_position, "$g_jrider_character_faction_filter", pos1),
        (position_set_x, pos1, 550),
        (position_set_y, pos1, 650),
        (overlay_set_size, "$g_jrider_character_faction_filter", pos1),

        # add elements to filter button
        (overlay_add_item, "$g_jrider_character_faction_filter", "@Your supporters"),
        (overlay_add_item, "$g_jrider_character_faction_filter", "@Swadians"),
        (overlay_add_item, "$g_jrider_character_faction_filter", "@Vaegirs"),
        (overlay_add_item, "$g_jrider_character_faction_filter", "@Khergits"),
        (overlay_add_item, "$g_jrider_character_faction_filter", "@Nords"),
        (overlay_add_item, "$g_jrider_character_faction_filter", "@Rhodoks"),
        (overlay_add_item, "$g_jrider_character_faction_filter", "@Sarranids"),
        (overlay_add_item, "$g_jrider_character_faction_filter", "@All Sovereignties"),

        # Set initial value for selection box
        (try_begin),
            (this_or_next|eq, "$g_jrider_pres_called_from_menu", 1),
            (eq, "$g_jrider_faction_filter", -1),

            (assign, "$g_jrider_faction_filter", -1),
            (overlay_set_val, "$g_jrider_character_faction_filter", 7),
        (else_try),
            (overlay_set_val, "$g_jrider_character_faction_filter", "$g_jrider_faction_filter"),
        (try_end),

        ###############################
        # Populate lists
        # Init presentation common global variables
        (assign, "$num_charinfo_candidates", 0),

        # Fill listbox (overlay_add_item and extra storage)
        (call_script, "script_fill_relation_canditate_list_for_presentation", "$g_character_presentation_type", ":base_candidates_y"),
        (assign, "$g_jrider_reset_selected_on_faction", 0),
        # stop if there's no candidate
        (gt, "$num_charinfo_candidates", 0),

        # get extra information from storage
        (store_add, ":current_storage_index", "$g_base_character_presentation_storage_index", "$g_latest_character_relation_entry"),
        (troop_get_slot, "$character_info_id", "trp_temp_array_c", ":current_storage_index"),
        (this_or_next|eq, "$character_info_id", "trp_player"), #CABA #Floris 2.52 bugfix --rather brute force, but I didn't see any real reason trp_temp_array_c would be giving a -1 from the scripts above
		(is_between, "$character_info_id", heroes_begin, heroes_end), #CABA #Floris 2.52 bugfix
		
        # Fill text information for current entry and update text information overlay
        (call_script, "script_generate_extended_troop_relation_information_string", "$character_info_id"),
        (overlay_set_text, "$g_jrider_character_information_text", s1),

        # color selected entry
        (overlay_set_color, "$g_jrider_last_checked_indicator", 0xFF6666FF), ####FLORIS 2.53 - was bugged should be fixed
        (overlay_set_alpha, "$g_jrider_last_checked_indicator", 0x44), ####FLORIS 2.53 - was bugged should be fixed

        # Begin common dynamic overlay
        # mesh Overlay for character portrait (global not needed)
        (create_image_button_overlay_with_tableau_material, "$g_jrider_character_portrait", -1, "tableau_troop_note_mesh", "$character_info_id"),
        (position_set_x, pos2, 100),
        (position_set_y, pos2, 280),
        (overlay_set_position, "$g_jrider_character_portrait", pos2),
        (position_set_x, pos2, 1100), #1150
        (position_set_y, pos2, 1100), #1150
        (overlay_set_size, "$g_jrider_character_portrait", pos2),

        # mesh Overlay for faction coat of arms
        (try_begin),
            (store_troop_faction, ":troop_faction", "$character_info_id"),
            (neq, ":troop_faction", "fac_player_supporters_faction"),
            (is_between, ":troop_faction", kingdoms_begin, kingdoms_end),
            (store_sub, ":faction_mesh_index", ":troop_faction", kingdoms_begin),
            (val_add, ":faction_mesh_index", "mesh_pic_recruits"),

            (create_mesh_overlay, "$g_jrider_faction_coat_of_arms", ":faction_mesh_index"),
            (position_set_x, pos3, 150),
            (position_set_y, pos3, 600),
            (overlay_set_position, "$g_jrider_faction_coat_of_arms", pos3),
            (position_set_x, pos3, 250),
            (position_set_y, pos3, 250),
            (overlay_set_size, "$g_jrider_faction_coat_of_arms", pos3),
        (try_end),

        # Begin presentation type specific dynamic overlay
        # equipement meshes for character/companions
        (try_begin),
            (eq, "$g_character_presentation_type", 2),

            (assign, ":base_inv_slot_x", 452),
            (assign, ":base_inv_slot_y", 536),

            (try_for_range, ":item_eq", 0, 9),
            # loop equipment slots
                (troop_get_inventory_slot, reg1, "$character_info_id", ":item_eq"),
       
                (try_begin),
                    (eq, ":item_eq", 4),
                    (assign, ":base_inv_slot_x", 68),
                    (assign, ":base_inv_slot_y", 557),
                (try_end),
                (try_begin),
                    (lt, reg1, 1),
                    # empty... assign default mesh
                   (try_begin),
                       (lt, ":item_eq", 4),
                       (assign, ":mesh_id", "mesh_mp_inventory_slot_equip"),
                   (else_try),
                       (eq, ":item_eq", 4),
                       (assign, ":mesh_id", "mesh_mp_inventory_slot_helmet"),
                   (else_try),
                       (eq, ":item_eq", 5),
                       (assign, ":mesh_id", "mesh_mp_inventory_slot_armor"),
                   (else_try),
                       (eq, ":item_eq", 6),
                       (assign, ":mesh_id", "mesh_mp_inventory_slot_boot"),
                   (else_try),
                       (eq, ":item_eq", 7),
                       (assign, ":mesh_id", "mesh_mp_inventory_slot_glove"),
                   (else_try),
                       (eq, ":item_eq", 8),
                       (assign, ":mesh_id", "mesh_mp_inventory_slot_horse"),
                   (try_end),
       
                   (create_mesh_overlay, reg11, ":mesh_id"),
                   (overlay_set_size, reg11, ":inv_bar_size"),

                   (position_set_x, pos1, ":base_inv_slot_x"),
                   (position_set_y, pos1, ":base_inv_slot_y"),
                   (overlay_set_position, reg11, pos1),
       
                   (troop_set_slot, "trp_temp_array_a", ":item_eq", -1),
                   (store_add, ":item_eq_id", ":item_eq", 10),
                   (troop_set_slot, "trp_temp_array_a", ":item_eq_id", -1),
                # end missing item
                (else_try),
                    (create_mesh_overlay_with_item_id, reg10, reg1),
                    (position_set_x, pos1, 450),
                    (position_set_y, pos1, 450),
                    (overlay_set_size, reg10, pos1),

                    (store_add, ":item_inv_slot_x", ":base_inv_slot_x", 25),
                    (store_add, ":item_inv_slot_y", ":base_inv_slot_y", 25),

                    (position_set_x, pos1, ":item_inv_slot_x"),
                    (position_set_y, pos1, ":item_inv_slot_y"),
                    (overlay_set_position, reg10, pos1),

                    # save id for reuse
                    (troop_set_slot, "trp_temp_array_a", ":item_eq", reg10),
                    (store_add, ":item_eq_id", ":item_eq", 10),
                    (troop_set_slot, "trp_temp_array_a", ":item_eq_id", reg1),
                # real items
                (try_end),
                (val_sub, ":base_inv_slot_y", 51),
            (try_end),
            # end loop equipments slots
        (try_end),

        # do an update if called from menu and reset init variable
        (try_begin),
            (eq, "$g_jrider_pres_called_from_menu", 1),
            (assign, "$g_jrider_pres_called_from_menu", 0),
        (try_end),
    ]),
    # end presentation load

    ## Mouse-over
    (ti_on_presentation_mouse_enter_leave,
      [
      (store_trigger_param_1, ":object"),
      (store_trigger_param_2, ":enter_leave"),

      (try_begin),
          (eq, "$g_character_presentation_type", 2),
          (try_begin),
              (eq, ":enter_leave", 0),
              (try_for_range, ":slot_no", 0, 9),
                  (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
                  (store_add, ":slot_no_eq", ":slot_no", 10),
                  (troop_get_slot, ":item_no", "trp_temp_array_a", ":slot_no_eq"),

                  (set_fixed_point_multiplier, 1000),

                  (position_set_x,pos0,740),
                  (position_set_y,pos0,235),
                  (show_item_details, ":item_no", pos0, 100),
              (try_end),
          (else_try),
              (try_for_range, ":slot_no", 0, 9),
                (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
                (close_item_details),
              (try_end),
          (try_end),
      (try_end),
    ]),
    # end mouseover

    ## Check for buttonpress
    (ti_on_presentation_event_state_change,
     [
        (store_trigger_param_1, ":object"), # object
        (store_trigger_param_2, ":value"),  # value

        (try_begin),
            # pressed  (Return to menu)
            (eq, ":object", "$g_jrider_character_report_Return_to_menu"),

            (try_begin),
                (neq, "$num_charinfo_candidates", 0),
                (overlay_set_text, "$g_jrider_character_information_text", "str_empty_string"),
                (overlay_set_alpha, "$g_jrider_last_checked_indicator", 0), ####FLORIS 2.53 - was bugged should be fixed
            (try_end),
            (presentation_set_duration, 0),

        (else_try),
            # Faction filter
            (eq, ":object", "$g_jrider_character_faction_filter"),
            (try_begin),
                (eq, ":value", 7),
                (assign, "$g_jrider_faction_filter", -1),
            (else_try),
                (assign, "$g_jrider_faction_filter", ":value"),
            (try_end),

            # reset selected to first
            (assign, "$g_jrider_reset_selected_on_faction", 1000),

            # restart presentation to take filters into account
            (start_presentation, "prsnt_jrider_character_relation_report"),

        (else_try),
            (neq, ":object", "$g_jrider_character_information_text"),
            (neq, ":object", "$g_jrider_character_portrait"),
            (neq, ":object", "$g_jrider_character_relation_listbox"),
            #(neq, ":object", "$g_jrider_faction_coat_of_arms"),
            # clicked on list entry
            # get storage index + base storage index
            (store_add, ":storage_button_id", ":object", "$g_base_character_presentation_storage_index"),
            (troop_get_slot, ":character_number", "trp_temp_array_b", ":storage_button_id"),

            (overlay_set_alpha, "$g_jrider_last_checked_indicator", 0),
            (overlay_set_color, "$g_jrider_last_checked_indicator", 0xDDDDDD),

            # update last entry and check variables
            (assign, "$g_latest_character_relation_entry", ":character_number"),
            (assign, "$g_jrider_last_checked_indicator", ":object"),

            # color selected entry
            (overlay_set_color, "$g_jrider_last_checked_indicator", 0xFF6666FF),
            (overlay_set_alpha, "$g_jrider_last_checked_indicator", 0x44),

            # get troop information from storage to update text
            (val_add, ":character_number", "$g_base_character_presentation_storage_index"),
            (troop_get_slot, "$character_info_id", "trp_temp_array_c", ":character_number"),

            # restart presentation to update picture and text
            (start_presentation, "prsnt_jrider_character_relation_report"),
    (try_end),
     ] # + generic_ti_on_presentation_event_state_change
     ),
     # end event state change

    ## Event to process when running the presentation
    (ti_on_presentation_run,
     # generic_ti_on_presentation_run +
     [
        (try_begin),
      (this_or_next|key_clicked, key_escape),
      (key_clicked, key_right_mouse_button),
      (presentation_set_duration, 0),
      (jump_to_menu, "mnu_reports"),
        (try_end),

        ]),
     # end presentation run
     ]),
    ###################################
    # Character relation presentation end
# Jrider -


## Companions Overview, by Jedediah Q, modified by lazeras
  ("jq_companions_quickview", 0, mesh_companion_overview, #mesh_companion_overview
   [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
        (assign, "$jq_just_visited_CO", 0),
        #(assign, "$jq_slot", 0),
        #(assign, "$g_jq_Return_to_menu", 1013),#jibberish value, just for button assign
        #(assign, "$g_jq_Back_to_shop", 1013),#jibberish value, just for button assign
    
        #Back to menu - graphical button
        (create_game_button_overlay, "$g_jq_Return_to_menu", "@_Return to menu_"),     
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 23),
        (overlay_set_position, "$g_jq_Return_to_menu", pos1),

        #Back to shop - graphical button
        (create_game_button_overlay, "$g_jq_Back_to_shop", "@_Back to shop_"),     
        (position_set_x, pos1, 100),
        (position_set_y, pos1, -180),#hide this and show only if any store has been visited in this town
        (overlay_set_position, "$g_jq_Back_to_shop", pos1),

        #show 'Back to shop'-button if any store has been visited in this town
        (try_begin),
            (eq, "$jq_current_town", "$current_town"),
            (eq, "$jq_in_market_menu", 1),
            (position_set_x, pos1, 100), 
            (position_set_y, pos1, 23),
            (overlay_set_position, "$g_jq_Back_to_shop", pos1),
        (try_end),

        ###HEADLINES###
        (assign, ":x_poshl", 165),
        (assign, ":y_pos", 581),
        (assign, ":jq_size", pos0),
        (position_set_x, ":jq_size", 720),
        (position_set_y, ":jq_size", 775),

        (create_text_overlay, reg2, "@Strength", tf_center_justify),
        (overlay_set_size, reg2, ":jq_size"),
        (position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@Riding", tf_center_justify),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 55),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@Pdraw", tf_center_justify),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 55),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@Pthrow", tf_center_justify),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 55),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@1-hand", tf_center_justify),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 55),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@2-hand", tf_center_justify),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 55),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@Polearm", tf_center_justify),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 55),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@Archery", tf_center_justify),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 55),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@ X-bow ", tf_center_justify),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 55),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@Throwing ", tf_center_justify),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 55),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@  Firearms", tf_center_justify),
        (position_set_x, ":jq_size", 640),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 55),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@ Mode", tf_center_justify),
        (position_set_x, ":jq_size", 700),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 55),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (create_text_overlay, reg2, "@(to next lvl)", tf_center_justify),
        (position_set_x, ":jq_size", 640),
        (position_set_y, ":jq_size", 750),
        (overlay_set_size, reg2, ":jq_size"),
        (val_add, ":x_poshl", 60),
        (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg2, pos1),

        (assign, ":jq_value", 100),
        (assign, "$jq_nr", 0),
        (assign, ":jq_size", 0),
        (assign, ":x_pos", 25),
        (assign, ":y_pos", 547),
        (str_clear, s9),    
        (assign, ":jq_col", 0x000000),
        (str_clear, s8),
    
        #Version info
        (create_text_overlay, "$g_jq_version", "@_1.3_", tf_left_align),
        (position_set_x, pos1, 963),
        (position_set_y, pos1, 735),
        (overlay_set_position, "$g_jq_version", pos1),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 700),
        (overlay_set_size, "$g_jq_version", pos1),
        (overlay_set_color, "$g_jq_version", 0xFFFFFFFF), 

        #Equipment info
        (create_text_overlay, "$g_jq_equipment_status", "@If you can see this, buy a new cpu.", tf_center_justify), #Hero name
        #(create_text_overlay, "$g_jq_equip_hlines", "@-Weapons-                                                                 -Armor-", tf_left_align),
        (create_text_overlay, "$g_jq_equip_hline1", "@_-Weapons-", tf_left_align),
        (create_text_overlay, "$g_jq_equip_hline2", "@_-Armor-", tf_left_align),
        (create_text_overlay, "$g_jq_equipment_item0", "@________________n/a________________", tf_center_justify), #item 0
        (create_text_overlay, "$g_jq_equipment_item1", "@________________n/a________________", tf_center_justify), #item 1
        (create_text_overlay, "$g_jq_equipment_item2", "@________________n/a________________", tf_center_justify), #item 2
        (create_text_overlay, "$g_jq_equipment_item3", "@________________n/a________________", tf_center_justify), #item 3
        (create_text_overlay, "$g_jq_equipment_item4", "@________________n/a________________", tf_center_justify), #head
        (create_text_overlay, "$g_jq_equipment_item5", "@________________n/a________________", tf_center_justify), #body
        (create_text_overlay, "$g_jq_equipment_item6", "@________________n/a________________", tf_center_justify), #feet
        (create_text_overlay, "$g_jq_equipment_item7", "@________________n/a________________", tf_center_justify), #hands
        #(create_text_overlay, "$g_jq_equipment_item8", "@________________n/a________________", tf_center_justify), #horse - not in use for now.

        #Hero name centered at the top
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 630),
        (overlay_set_position, "$g_jq_equipment_status", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 850),
        (overlay_set_size, "$g_jq_equipment_status", pos1),
    
        # Weapons and Armor headlines
        (position_set_x, pos1, 210),
        (position_set_y, pos1, 700),
        (overlay_set_position, "$g_jq_equip_hline1", pos1),
        (overlay_set_color, "$g_jq_equip_hline1", 0xFFAAAAFF),
        (position_set_x, pos1, 700),
        (overlay_set_position, "$g_jq_equip_hline2", pos1),
        (overlay_set_color, "$g_jq_equip_hline2", 0xFFAAAAFF),
        (position_set_x, pos1, 1000),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_jq_equip_hline1", pos1),
        (overlay_set_size, "$g_jq_equip_hline2", pos1),
    
        # item 0-3
        (position_set_x, pos1, 255),
        (position_set_y, pos1, 681),
        (overlay_set_position, "$g_jq_equipment_item0", pos1),
        (position_set_y, pos1, 664),
        (overlay_set_position, "$g_jq_equipment_item1", pos1),
        (position_set_y, pos1, 647),
        (overlay_set_position, "$g_jq_equipment_item2", pos1),
        (position_set_y, pos1, 630),
        (overlay_set_position, "$g_jq_equipment_item3", pos1),

        #new column head, body, feet, hands
        (position_set_x, pos1, 740),
        (position_set_y, pos1, 681),
        (overlay_set_position, "$g_jq_equipment_item4", pos1),
        (position_set_y, pos1, 664),
        (overlay_set_position, "$g_jq_equipment_item5", pos1),
        (position_set_y, pos1, 647),
        (overlay_set_position, "$g_jq_equipment_item6", pos1),
        (position_set_y, pos1, 630),
        (overlay_set_position, "$g_jq_equipment_item7", pos1),

        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_jq_equipment_status", pos1),
        (overlay_set_size, "$g_jq_equipment_item0", pos1),
        (overlay_set_color, "$g_jq_equipment_item0", 0xFFFFFFFF),
        (overlay_set_size, "$g_jq_equipment_item1", pos1),
        (overlay_set_color, "$g_jq_equipment_item1", 0xFFFFFFFF),
        (overlay_set_size, "$g_jq_equipment_item2", pos1),
        (overlay_set_color, "$g_jq_equipment_item2", 0xFFFFFFFF),
        (overlay_set_size, "$g_jq_equipment_item3", pos1),
        (overlay_set_color, "$g_jq_equipment_item3", 0xFFFFFFFF),
        (overlay_set_size, "$g_jq_equipment_item4", pos1),
        (overlay_set_color, "$g_jq_equipment_item4", 0xFFFFFFFF),
        (overlay_set_size, "$g_jq_equipment_item5", pos1),
        (overlay_set_color, "$g_jq_equipment_item5", 0xFFFFFFFF),
        (overlay_set_size, "$g_jq_equipment_item6", pos1),
        (overlay_set_color, "$g_jq_equipment_item6", 0xFFFFFFFF),
        (overlay_set_size, "$g_jq_equipment_item7", pos1),
        (overlay_set_color, "$g_jq_equipment_item7", 0xFFFFFFFF), 

    ### Loop begins here. Printing out hero names and stats. ####################################
        (try_for_range, "$jq_dude", companions_begin, companions_end),
            (main_party_has_troop, "$jq_dude"),
            (troop_set_slot, "trp_temp_array_c", "$jq_nr", "$jq_dude"),
            (val_add, "$jq_nr", 1),

            #Do the morale-script call at the beginning, instead of every single mouseover
            (call_script, "script_npc_morale", "$jq_dude"),
            (assign, ":troop_morale", reg0),
            (assign, reg1, ":troop_morale"),
            (troop_set_slot, "trp_temp_array_c", ":jq_value", reg1),
            (val_add, ":jq_value", 1),

            (str_store_troop_name, s9, "$jq_dude"),
            (str_store_string, s1, "@{s9}"),
            (create_text_overlay, reg1, s1, tf_left_align),
            (position_set_x, pos3, ":x_pos"),
            (position_set_y, pos3, ":y_pos"),
            (overlay_set_position, reg1, pos3),
            (position_set_x, pos3, 750),
            (position_set_y, pos3, 850),
            (overlay_set_size, reg1, pos3),
            

            #Same name, right margin
            (create_text_overlay, reg2, s1, tf_left_align),
            (position_set_x, pos3, 880),
            (position_set_y, pos3, ":y_pos"),
            (overlay_set_position, reg2, pos3),
            (position_set_x, pos3, 750),
            (position_set_y, pos3, 850),
            (overlay_set_size, reg2, pos3),

            (assign, ":x_poshl", 165),
            (assign, ":jq_size", 0),    
            (position_set_x, ":jq_size", 750),
            (position_set_y, ":jq_size", 850), 

            #STRENGTH
            (store_attribute_level, reg1, "$jq_dude", ca_strength),
            (create_text_overlay, ":jqreg", "@{reg1}", tf_center_justify),
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),
            (overlay_set_color, ":jqreg", ":jq_col"), 
            #RIDING
            (store_skill_level, reg1, "skl_riding", "$jq_dude"), 
            (val_add, ":x_poshl", 55),
            (create_text_overlay, ":jqreg", "@{reg1}", tf_center_justify),
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),
            (overlay_set_color, ":jqreg", ":jq_col"), 
            #POWERDRAW
            (store_skill_level, reg1, "skl_power_draw", "$jq_dude"), 
            (val_add, ":x_poshl", 55),
            (create_text_overlay, ":jqreg", "@{reg1}", tf_center_justify),
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),
            (overlay_set_color, ":jqreg", ":jq_col"), 
            #POWERTHROW
            (store_skill_level, reg1, "skl_power_throw", "$jq_dude"), 
            (val_add, ":x_poshl", 55),
            (create_text_overlay, ":jqreg", "@{reg1}", tf_center_justify),
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),
            (overlay_set_color, ":jqreg", ":jq_col"), 
            #ONE-HANDED WEAPS
            (store_proficiency_level,  reg1, "$jq_dude", wpt_one_handed_weapon),
            (val_add, ":x_poshl", 55),
            (create_text_overlay, ":jqreg", "@{reg1}", tf_center_justify),    
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),
            (overlay_set_color, ":jqreg", ":jq_col"), 

            #TWO-HANDED WEAPS
            (store_proficiency_level,  reg1, "$jq_dude", wpt_two_handed_weapon),
            (val_add, ":x_poshl", 55),
            (create_text_overlay, ":jqreg", "@{reg1}", tf_center_justify),    
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),
            (overlay_set_color, ":jqreg", ":jq_col"), 
            #POLEARMS
            (store_proficiency_level,  reg1, "$jq_dude", wpt_polearm),
            (val_add, ":x_poshl", 55),
            (create_text_overlay, ":jqreg", "@{reg1}", tf_center_justify),    
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),
            (overlay_set_color, ":jqreg", ":jq_col"), 
            #ARCHERY
            (store_proficiency_level,  reg1, "$jq_dude", wpt_archery),
            (val_add, ":x_poshl", 55),
            (create_text_overlay, ":jqreg", "@{reg1}", tf_center_justify),    
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),
            (overlay_set_color, ":jqreg", ":jq_col"), 
            #CROSSBOW
            (store_proficiency_level,  reg1, "$jq_dude", wpt_crossbow),
            (val_add, ":x_poshl", 55),
            (create_text_overlay, ":jqreg", "@{reg1}", tf_center_justify),    
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),
            (overlay_set_color, ":jqreg", ":jq_col"), 
            #THROWING
            (store_proficiency_level,  reg1, "$jq_dude", wpt_throwing),
            (val_add, ":x_poshl", 55),
            (create_text_overlay, ":jqreg", "@{reg1}", tf_center_justify),    
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),  
            (overlay_set_color, ":jqreg", ":jq_col"), 
            #FIREARMS
            (store_proficiency_level,  reg1, "$jq_dude", wpt_firearm),
            (val_add, ":x_poshl", 55),
            (create_text_overlay, ":jqreg", "@{reg1}", tf_center_justify),    
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),  
            (overlay_set_color, ":jqreg", ":jq_col"),                  
            #WALKSorRIDES
            (try_begin), 
                (troop_is_mounted,  "$jq_dude"),
                (str_store_string, s1, "@Rides"),
                (assign, ":jq_col", 0x0000FF),
                (else_try),
                (str_store_string, s1, "@Walks"),
            (try_end),
            (val_add, ":x_poshl", 41),
            (create_text_overlay, ":jqreg", s1, tf_left_align),    
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),  
            (overlay_set_color, ":jqreg", ":jq_col"),  
            (assign, ":jq_col", 0x000000),     
            #POINTS 2 NEXT LVL
            (troop_get_xp, ":jqreg", "$jq_dude"),
            (call_script, "script_jq_xp_to_next_lvl", ":jqreg"),
            (val_add, ":x_poshl", 64),
            (create_text_overlay, ":jqreg", s1, tf_left_align),    
            (overlay_set_size, ":jqreg", ":jq_size"),
            (position_set_x, pos1, ":x_poshl"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, ":jqreg", pos1),

            (assign, ":x_pos", 25),
            (assign, ":x_poshl", 165),
            (val_sub, ":y_pos", 23),#linebreak 
            (ge, ":x_pos", 950),
            (assign, ":x_pos", 25),
            (val_sub, ":y_pos", 23),
        (try_end),
    #try-for-companions-loop ends here #################################### 

    #--TROOP SELECTORS--------------------------------------------------------------------------------------------# 

        (position_set_x, ":jq_size", 49350),
        (position_set_y, ":jq_size", 1000),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, -200),

        #Create buttons (even if the equiv. hero doesn't exist) 
        #If I don't do this, the 'Return'-button will take over the memory adress. Yup i suck at this.

        (create_image_button_overlay, "$g_jq_selector_1", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_1", pos1), 
        (create_image_button_overlay, "$g_jq_selector_2", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_2", pos1), 
        (create_image_button_overlay, "$g_jq_selector_3", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_3", pos1), 
        (create_image_button_overlay, "$g_jq_selector_4", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_4", pos1), 
        (create_image_button_overlay, "$g_jq_selector_5", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_5", pos1),  
        (create_image_button_overlay, "$g_jq_selector_6", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_6", pos1), 
        (create_image_button_overlay, "$g_jq_selector_7", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_7", pos1),  
        (create_image_button_overlay, "$g_jq_selector_8", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_8", pos1), 
        (create_image_button_overlay, "$g_jq_selector_9", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_9", pos1), 
        (create_image_button_overlay, "$g_jq_selector_10", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_10", pos1), 
        (create_image_button_overlay, "$g_jq_selector_11", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_11", pos1), 
        (create_image_button_overlay, "$g_jq_selector_12", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_12", pos1), 
        (create_image_button_overlay, "$g_jq_selector_13", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_13", pos1), 
        (create_image_button_overlay, "$g_jq_selector_14", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_14", pos1), 
        (create_image_button_overlay, "$g_jq_selector_15", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_15", pos1),  
        (create_image_button_overlay, "$g_jq_selector_16", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_16", pos1), 
        (create_image_button_overlay, "$g_jq_selector_17", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_17", pos1),  
        (create_image_button_overlay, "$g_jq_selector_18", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_18", pos1), 
        (create_image_button_overlay, "$g_jq_selector_19", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_19", pos1), 
        (create_image_button_overlay, "$g_jq_selector_20", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_position, "$g_jq_selector_20", pos1),
         

        #create buttons end ### create buttons end ### create buttons end ###

        (try_begin),
            (gt, "$jq_nr", 0),
            (position_set_x, pos1, 5),
            (position_set_y, pos1, 547),
            (overlay_set_position, "$g_jq_selector_1", pos1),
            (overlay_set_size, "$g_jq_selector_1", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_1", 0),
            (overlay_set_color, "$g_jq_selector_1", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 1),
            (position_set_y, pos1, 524),
            (overlay_set_position, "$g_jq_selector_2", pos1),
            (overlay_set_size, "$g_jq_selector_2", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_2", 0),
            (overlay_set_color, "$g_jq_selector_2", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 2),
            (position_set_y, pos1, 501),
            (overlay_set_position, "$g_jq_selector_3", pos1),
            (overlay_set_size, "$g_jq_selector_3", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_3", 0),
            (overlay_set_color, "$g_jq_selector_3", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 3),
            (position_set_y, pos1, 478),
            (overlay_set_position, "$g_jq_selector_4", pos1),
            (overlay_set_size, "$g_jq_selector_4", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_4", 0),
            (overlay_set_color, "$g_jq_selector_4", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 4),
            (position_set_y, pos1, 455),
            (overlay_set_position, "$g_jq_selector_5", pos1),
            (overlay_set_size, "$g_jq_selector_5", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_5", 0),
            (overlay_set_color, "$g_jq_selector_5", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 5), 
            (position_set_y, pos1, 432),
            (overlay_set_position, "$g_jq_selector_6", pos1),
            (overlay_set_size, "$g_jq_selector_6", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_6", 0),
            (overlay_set_color, "$g_jq_selector_6", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 6), 
            (position_set_y, pos1, 409),
            (overlay_set_position, "$g_jq_selector_7", pos1),
            (overlay_set_size, "$g_jq_selector_7", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_7", 0),
            (overlay_set_color, "$g_jq_selector_7", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 7), 
            (position_set_y, pos1, 386),
            (overlay_set_position, "$g_jq_selector_8", pos1),
            (overlay_set_size, "$g_jq_selector_8", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_8", 0),
            (overlay_set_color, "$g_jq_selector_8", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 8),
            (position_set_y, pos1, 363),
            (overlay_set_position, "$g_jq_selector_9", pos1),
            (overlay_set_size, "$g_jq_selector_9", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_9", 0),
            (overlay_set_color, "$g_jq_selector_9", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 9),
            (position_set_y, pos1, 340),
            (overlay_set_position, "$g_jq_selector_10", pos1),
            (overlay_set_size, "$g_jq_selector_10", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_10", 0),
            (overlay_set_color, "$g_jq_selector_10", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 10),
            (position_set_y, pos1, 317),
            (overlay_set_position, "$g_jq_selector_11", pos1),
            (overlay_set_size, "$g_jq_selector_11", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_11", 0),
            (overlay_set_color, "$g_jq_selector_11", 0xFFFF00),
        (try_end),
        (try_begin),
        (gt, "$jq_nr", 11),
            (position_set_y, pos1, 294),
            (overlay_set_position, "$g_jq_selector_12", pos1),
            (overlay_set_size, "$g_jq_selector_12", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_12", 0),
            (overlay_set_color, "$g_jq_selector_12", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 12),
            (position_set_y, pos1, 271),
            (overlay_set_position, "$g_jq_selector_13", pos1),
            (overlay_set_size, "$g_jq_selector_13", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_13", 0),
            (overlay_set_color, "$g_jq_selector_13", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 13),
            (position_set_y, pos1, 248),
            (overlay_set_position, "$g_jq_selector_14", pos1),
            (overlay_set_size, "$g_jq_selector_14", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_14", 0),
            (overlay_set_color, "$g_jq_selector_14", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 14),
            (position_set_y, pos1, 225),
            (overlay_set_position, "$g_jq_selector_15", pos1),
            (overlay_set_size, "$g_jq_selector_15", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_15", 0),
            (overlay_set_color, "$g_jq_selector_15", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 15), 
            (position_set_y, pos1, 202),
            (overlay_set_position, "$g_jq_selector_16", pos1),
            (overlay_set_size, "$g_jq_selector_16", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_16", 0),
            (overlay_set_color, "$g_jq_selector_16", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 16), 
            (position_set_y, pos1, 179),
            (overlay_set_position, "$g_jq_selector_17", pos1),
            (overlay_set_size, "$g_jq_selector_17", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_17", 0),
            (overlay_set_color, "$g_jq_selector_17", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 17), 
            (position_set_y, pos1, 156),
            (overlay_set_position, "$g_jq_selector_18", pos1),
            (overlay_set_size, "$g_jq_selector_18", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_18", 0),
            (overlay_set_color, "$g_jq_selector_18", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 18),
            (position_set_y, pos1, 133),
            (overlay_set_position, "$g_jq_selector_19", pos1),
            (overlay_set_size, "$g_jq_selector_19", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_19", 0),
            (overlay_set_color, "$g_jq_selector_19", 0xFFFF00),
        (try_end),
        (try_begin),
            (gt, "$jq_nr", 19),
            (position_set_y, pos1, 110),
            (overlay_set_position, "$g_jq_selector_20", pos1),
            (overlay_set_size, "$g_jq_selector_20", ":jq_size"),
            (overlay_set_alpha, "$g_jq_selector_20", 0),
            (overlay_set_color, "$g_jq_selector_20", 0xFFFF00),
        (try_end),
    #TROOP SELECTORS END #-----------------------------------------------------------------------------------------------#
        (position_set_x, ":jq_size", 49350),
        (position_set_y, ":jq_size", 1000),
        (assign, ":y_poshl", 547),
        (create_mesh_overlay, "$g_jq_last_checked_indicator", "mesh_white_plane", "mesh_white_plane"),
        (overlay_set_size, "$g_jq_last_checked_indicator", ":jq_size"),
        (overlay_set_color, "$g_jq_last_checked_indicator", 0xFF6666FF),
        (overlay_animate_to_alpha, "$g_jq_last_checked_indicator", 0, 0),
    
    #Automatically shows last checked hero's stats. Defaults back to 1st troop in list if this is the 1st visit.

        (assign, "$jq_nr", 0),    
        (try_for_range, "$jq_dude", companions_begin, companions_end),
            (main_party_has_troop, "$jq_dude"),
            (try_begin),
                (eq, "$jq_last_checked_hero", "$jq_dude"),
                (assign, ":jq_slt", "$jq_nr"),
                (assign, reg2, "$jq_nr"),
                (val_add, reg2, 100),
                (assign, ":y_pos", ":y_poshl"),
            (try_end),
            (val_add, "$jq_nr", 1),
            (val_sub, ":y_poshl", 23), 
        (try_end), 
        (troop_get_slot, "$jq_dude", "trp_temp_array_c", ":jq_slt"),  ##CABA - This looks messed up.
        (call_script, "script_jq_extra_stats", "$jq_dude", reg2),
        (position_set_x, pos1, 5),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, "$g_jq_last_checked_indicator", pos1),
        (overlay_animate_to_alpha, "$g_jq_last_checked_indicator", 50, 0x44), 
       ]),

      #Check for buttonpress
    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, "$espresso"), ##CABA - no need for global
        (try_begin),
            (eq, "$espresso", "$g_jq_Return_to_menu"), # pressed  (Return to menu)
            (assign, "$jq_just_visited_CO", 0),#do NOT autoreturn to store
            (assign, "$jq_override",0), #use default anim and camera settings in 'module_scripts'
            (presentation_set_duration, 0),
        (else_try),
            (eq, "$espresso", "$g_jq_Back_to_shop"), # pressed 'Back to shop' 
            (assign, "$jq_just_visited_CO", 1), #autoreturn to latest visited store 
            (assign, "$jq_override",0),
            (presentation_set_duration, 0),                  
        (else_try),
            (try_begin),
                (eq, "$espresso", "$g_jq_selector_1"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 0),
                (assign, "$jq_slot", 0),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_2"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 1),
                (assign, "$jq_slot", 1),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_3"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 2),
                (assign, "$jq_slot", 2),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_4"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 3),
                (assign, "$jq_slot", 3),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_5"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 4),
                (assign, "$jq_slot", 4),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_6"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 5),
                (assign, "$jq_slot", 5),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_7"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 6),
                (assign, "$jq_slot", 6),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_8"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 7),
                (assign, "$jq_slot", 7),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_9"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 8),
                (assign, "$jq_slot", 8),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_10"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 9),
                (assign, "$jq_slot", 9),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_11"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 10),
                (assign, "$jq_slot", 10),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_12"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 11),
                (assign, "$jq_slot", 10),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_13"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 12),
                (assign, "$jq_slot", 12),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_14"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 13),
                (assign, "$jq_slot", 13),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_15"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 14),
                (assign, "$jq_slot", 14),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_16"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 15),
                (assign, "$jq_slot", 15),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_17"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 16),
                (assign, "$jq_slot", 16),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_18"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 17),
                (assign, "$jq_slot", 17),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_19"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 18),
                (assign, "$jq_slot", 18),
            (else_try),
                (eq, "$espresso", "$g_jq_selector_20"),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 19),
                (assign, "$jq_slot", 19),         
            (try_end),
            (start_presentation, "prsnt_jq_extended_info"),
        (try_end),
       ]), 
    #IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII#
    ## mouse-over start ##
    # Trigger Param 1: id of the object that mouse enters/leaves
    # Trigger Param 2: 0 if mouse enters, 1 if mouse leaves

    (ti_on_presentation_mouse_enter_leave,
       [(store_trigger_param_1, "$espresso"),
        (store_trigger_param_2, ":jq_enter_leave"),
        (overlay_animate_to_alpha, "$g_jq_last_checked_indicator", 1500, 0),
        (try_begin),
            (eq, "$espresso", "$g_jq_selector_1"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_1", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 0),
                (call_script, "script_jq_extra_stats", "$jq_dude", 100),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_1", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_2"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_2", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 1),
                (call_script, "script_jq_extra_stats", "$jq_dude", 101),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_2", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_3"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_3", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 2),
                (call_script, "script_jq_extra_stats", "$jq_dude", 102),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_3", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_4"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_4", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 3),
                (call_script, "script_jq_extra_stats", "$jq_dude", 103),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_4", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_5"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_5", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 4),
                (call_script, "script_jq_extra_stats", "$jq_dude", 104),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_5", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_6"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_6", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 5),
                (call_script, "script_jq_extra_stats", "$jq_dude", 105),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_6", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_7"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_7", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 6),
                (call_script, "script_jq_extra_stats", "$jq_dude", 106),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_7", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_8"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_8", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 7),
                (call_script, "script_jq_extra_stats", "$jq_dude", 107),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_8", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_9"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_9", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 8),
                (call_script, "script_jq_extra_stats", "$jq_dude", 108),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_9", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_10"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_10", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 9),
                (call_script, "script_jq_extra_stats", "$jq_dude", 109),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_10", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_11"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_11", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 10),
                (call_script, "script_jq_extra_stats", "$jq_dude", 110),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_11", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_12"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_12", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 11),
                (call_script, "script_jq_extra_stats", "$jq_dude", 111),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_12", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_13"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_13", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 12),
                (call_script, "script_jq_extra_stats", "$jq_dude", 112),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_13", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_14"),
              (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_14", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 13),
                (call_script, "script_jq_extra_stats", "$jq_dude", 113),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_14", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_15"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_15", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 14),
                (call_script, "script_jq_extra_stats", "$jq_dude", 114),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_15", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_16"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_16", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 15),
                (call_script, "script_jq_extra_stats", "$jq_dude", 115),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_16", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_17"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_17", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 16),
                (call_script, "script_jq_extra_stats", "$jq_dude", 116),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_17", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_18"),
              (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_18", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 17),
                (call_script, "script_jq_extra_stats", "$jq_dude", 117),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_18", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_19"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_19", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 18),
                (call_script, "script_jq_extra_stats", "$jq_dude", 118),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_19", 10, 0),
            (try_end),
        (else_try),
            (eq, "$espresso", "$g_jq_selector_20"),
            (try_begin),
                (eq, ":jq_enter_leave", 0),
                (overlay_animate_to_alpha, "$g_jq_selector_20", 5, 0x44),
                (troop_get_slot, "$jq_dude", "trp_temp_array_c", 19),
                (call_script, "script_jq_extra_stats", "$jq_dude", 119),
            (else_try),
                (overlay_animate_to_alpha, "$g_jq_selector_20", 10, 0),
            (try_end),

        (try_end),
       ]),
    ## mouse-over end ##
    #IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII#
    (ti_on_presentation_run,
       [(try_begin),
            (this_or_next|key_clicked, key_escape),
            (key_clicked, key_right_mouse_button),
            (eq, "$jq_in_market_menu", 0),
            (assign, "$jq_override",0), 
            (presentation_set_duration, 0),
            (jump_to_menu, "mnu_reports"),
        (else_try),
            (this_or_next|key_clicked, key_escape),
            (key_clicked, key_right_mouse_button),
            (eq, "$jq_in_market_menu", 1),
            (assign, "$jq_override",0),
            (presentation_set_duration, 0),      
            (jump_to_menu,"mnu_town_trade"),
        (else_try),
            (key_clicked, key_back_space),
            (eq, "$jq_in_market_menu", 1),
            (eq, "$jq_current_town", "$current_town"),
            (assign, "$jq_just_visited_CO", 1),
            (assign, "$jq_override",0), 
            (presentation_set_duration, 0),      
            (jump_to_menu,"mnu_town_trade"),
        (else_try),
            (key_clicked, key_home),
            (assign, "$jq_startpage", 1),    
            (play_sound, "snd_put_back_sword"),
            (display_message,"@Startpage set (Quick View)",0xFFAAFFAA),        
        (try_end),
       ]),
   ]),

###########################################################################################################################
###########################################################################################################################
################## EXTENDED INFO ##########################################################################################

  ("jq_extended_info", 0, mesh_companion_overview_details,
   [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (try_begin),
            (gt,  "$jq_dude", 0), 
            (assign, "$jq_last_checked_hero", "$jq_dude"),
        (else_try),
            (assign, "$jq_nr", 0),
            (try_for_range, "$jq_dude", companions_begin, companions_end),
                (main_party_has_troop, "$jq_dude"),
                (troop_set_slot, "trp_temp_array_c", "$jq_nr", "$jq_dude"),
                (val_add, "$jq_nr", 1),
            (try_end),
            (assign, "$jq_last_checked_hero", "$jq_dude"),
        (try_end),

        (assign, "$jq_override", 1),  

        #Back to menu - graphical button
        (create_game_button_overlay, "$g_jq_Return_to_menu", "@_Return to menu_"),     
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 20),
        (overlay_set_position, "$g_jq_Return_to_menu", pos1),

        #Back to shop - graphical button
        (create_game_button_overlay, "$g_jq_Back_to_shop", "@Back to shop"),     
        (position_set_x, pos1, 100),
        (position_set_y, pos1, -180),#hide this and show only if any store been visited in current town
        (overlay_set_position, "$g_jq_Back_to_shop", pos1),

        #show 'Back to shop'- graphical button (visible if you arrived from or recently visited any of the stores)
        (try_begin),
            (eq, "$jq_current_town", "$current_town"),
            (eq, "$jq_in_market_menu", 1),
            (position_set_x, pos1, 100), 
            (position_set_y, pos1, 20),
            (overlay_set_position, "$g_jq_Back_to_shop", pos1),
        (try_end),
        
        #Help button
        (assign, "$jq_helptoggle", 0),
        (create_button_overlay, "$g_jqhelp", "@_[?]_", tf_left_align), 
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 28),
        (overlay_set_position,  "$g_jqhelp", pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_jqhelp", pos1),
        (overlay_set_color, "$g_jqhelp", 0xFFFFFFFF),

        (create_text_overlay, "$g_jqhelptxt", "@Hotkeys:^HOME = Set startpage^RMB = Exit to menu^ESCAPE = Quick View^BACKSPACE = Back to shop (if visited)", tf_left_align),
        (position_set_x, pos1, 707),
        (position_set_y, pos1, 80), 
        (overlay_set_position,  "$g_jqhelptxt", pos1),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_jqhelptxt", pos1),
        (overlay_set_color, "$g_jqhelptxt", 0xFFFFFFFF),
        (overlay_set_alpha, "$g_jqhelptxt" , 0),       

        #Quit2 - debug button
        (create_button_overlay, "$g_quitdebug2", "@- Quit2 -", tf_left_align), 
        (position_set_x, pos1, 330),
        #(position_set_y, pos1, 25),
        (position_set_y, pos1, -50),
        (overlay_set_position, "$g_quitdebug2", pos1),

        #Previous page - graphical button
        (create_game_button_overlay, "$g_presentation_obj_1", "@_Quick View_"),     
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 20),
        (overlay_set_position, "$g_presentation_obj_1", pos1),

        #prevTroop - graphical button
        (assign, "$g_jq_prevtroop", 1),
        (create_game_button_overlay, "$g_jq_prevtroop", "@ ____ "),     
        (position_set_x, pos1, 90),
        (position_set_y, pos1, 710),
        (overlay_set_position, "$g_jq_prevtroop", pos1),
        (position_set_x, pos1, 25),
        (position_set_y, pos1, 20),
        (overlay_set_size, "$g_jq_prevtroop", pos1),

        #nextTroop - graphical button
        (assign, "$g_jq_nexttroop", 1),
        (create_game_button_overlay, "$g_jq_nexttroop", "@ ____ "),     
        (position_set_x, pos1, 350),
        (position_set_y, pos1, 710),
        (overlay_set_position, "$g_jq_nexttroop", pos1),
        (position_set_x, pos1, 25),
        (position_set_y, pos1, 20),
        (overlay_set_size, "$g_jq_nexttroop", pos1),

        #Draw hero character mesh
        (create_mesh_overlay_with_tableau_material, "$jq_portrait", -1, "tableau_game_character_sheet", "$jq_dude"),
        (position_set_x, pos1, 1150),
        (position_set_y, pos1, 1150),
        (overlay_set_size, "$jq_portrait", pos1),
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 295),
        (position_set_z, pos1, 170),
        (overlay_set_position, "$jq_portrait", pos1),
    
        ###HEADLINES###
        (assign, ":x_poshl", 35),
        (assign, ":jq_size", 0),
        (position_set_x, ":jq_size", 1250),
        (position_set_y, ":jq_size", 1200),

        (str_store_troop_name, s9, "$jq_dude"),
        (str_store_string, s1, "@{s9}"),
        (create_text_overlay, "$jq_troop_name", s1, tf_center_justify),
        (position_set_x, pos3, 160),
        (position_set_y, pos3, 705),
        (overlay_set_position, "$jq_troop_name", pos3),
        (position_set_x, pos3, 900),
        (position_set_y, pos3, 1000),
        (overlay_set_size, "$jq_troop_name", pos3),

        (create_text_overlay, reg2, "@Attributes", tf_left_align),
        (overlay_set_size, reg2, ":jq_size"),
        (position_set_x, pos1, 78),
        (position_set_y, pos1, 243),
        (overlay_set_position, reg2, pos1),
        (overlay_set_color, reg2, 0xFF000033),

        (create_text_overlay, reg2, "@Skills", tf_left_align),
        (overlay_set_size, reg2, ":jq_size"),
        (position_set_x, pos1, 388),
        (position_set_y, pos1, 503),
        (overlay_set_position, reg2, pos1),
        (overlay_set_color, reg2, 0xFF003300),

        (create_text_overlay, reg2, "@Proficiencies", tf_left_align),
        (overlay_set_size, reg2, ":jq_size"),
        (position_set_x, pos1, 740),
        (position_set_y, pos1, 403),
        (overlay_set_position, reg2, pos1),
        (overlay_set_color, reg2, 0xFF330000),

        (position_set_x, ":jq_size", 975),
        (position_set_y, ":jq_size", 975),
        (position_set_x, pos1, 42),

        (create_text_overlay, reg2, "@STR:", tf_left_align),
        (position_set_y, pos1, 212),
        (overlay_set_position, reg2, pos1),
        (overlay_set_size, reg2, ":jq_size"),

        (create_text_overlay, reg2, "@AGI:", tf_left_align),
        (position_set_y, pos1, 187),
        (overlay_set_position, reg2, pos1),
        (overlay_set_size, reg2, ":jq_size"),

        (create_text_overlay, reg2, "@INT:", tf_left_align),
        (position_set_y, pos1, 162),
        (overlay_set_position, reg2, pos1),
        (overlay_set_size, reg2, ":jq_size"),

        (create_text_overlay, reg2, "@CHA:", tf_left_align),
        (position_set_y, pos1, 137),
        (overlay_set_position, reg2, pos1),
        (position_set_x, ":jq_size", 900),
        (overlay_set_size, reg2, ":jq_size"),

        (create_text_overlay, reg2, "@Health:", tf_left_align),
        (position_set_y, pos1, 105),
        (overlay_set_position, reg2, pos1),
        (position_set_x, ":jq_size", 1250),
        (position_set_y, ":jq_size", 1250),
        (overlay_set_size, reg2, ":jq_size"),

        (create_text_overlay, reg2, "@Level:", tf_left_align),
        (position_set_y, pos1, 76),
        (overlay_set_position, reg2, pos1),
        (position_set_x, ":jq_size", 1250),
        (position_set_y, ":jq_size", 1250),
        (overlay_set_size, reg2, ":jq_size"),

        (create_text_overlay, reg2, "@To next lvl: ", tf_left_align),
        (position_set_y, pos1, 60),
        (overlay_set_position, reg2, pos1),
        (position_set_x, ":jq_size", 700),
        (position_set_y, ":jq_size", 800),
        (overlay_set_size, reg2, ":jq_size"),

        #Skills Labels
        (assign, ":x_poshl", 585),
        (assign, ":y_poshl", 374),
        (position_set_x, ":jq_size", 900),
        (position_set_y, ":jq_size", 1000),

        (create_text_overlay, reg2, "@Ironflesh^Power Strike^Power Throw^Power Draw^Weapon Master^Shield^Athletics^Riding^Horse Archery^Looting^Trainer^Tracking^", tf_left_align),
        (create_text_overlay, reg3, "@Tactics^Path-finding^Spotting^Inventory Management^Wound Treatment^Surgery^First Aid^Engineer^Persuasion^Prisoner Management^Leadership^Trade", tf_left_align),    
        (position_set_x, pos1, 353),
        (position_set_y, pos1, 284),
        (overlay_set_position, reg2, pos1),
        (position_set_y, pos1, 68),
        (overlay_set_position, reg3, pos1),
        (overlay_set_size, reg2, ":jq_size"),
        (overlay_set_size, reg3, ":jq_size"),

        # Skills Values
        (assign, ":x_poshl", 625),
        (assign, ":y_poshl", 68),
        (str_clear, s1),
        (create_text_overlay, "$jq_allskills",  "@10", tf_center_justify), 
        (position_set_x, ":jq_size", 850),
        (position_set_y, ":jq_size", 1000),
        (position_set_x, pos2, ":x_poshl"),
        (position_set_y, pos2, ":y_poshl"),
        (overlay_set_position,"$jq_allskills", pos2),    
        (overlay_set_size,"$jq_allskills", ":jq_size"),

        #Proficiencies Labels
        (create_text_overlay, ":jqreg", "@One Handed Weapons:^^Two Handed Weapons:^^Polearms:^^Archery:^^Crossbows:^^Throwing:^^Firearms:", tf_left_align),    
        (create_text_overlay, "$jq_allprofs", "@350^^350^^350^^350^^350^^350^^350", tf_left_align),    
        (position_set_x, pos1, 707),
        (position_set_y, pos1, 155),
        (overlay_set_position, ":jqreg", pos1),
        (position_set_x, pos1, 900),
        (overlay_set_position, "$jq_allprofs", pos1),
        (position_set_x, ":jq_size", 950),
        (position_set_y, ":jq_size", 1000),
        (overlay_set_size, ":jqreg", ":jq_size"),
        (overlay_set_size, "$jq_allprofs", ":jq_size"),

        ## STR, AGI, INT, CHA, LVL ##
        (assign, ":x_poshl", 115),
        (assign, ":y_pos", 500),
        (position_set_x, ":jq_size", 975),
        (position_set_y, ":jq_size", 975),

        (position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, 212),

        (create_text_overlay, "$jqregstr", "@_{reg1}_", tf_center_justify),
        (overlay_set_position, "$jqregstr", pos1),
        (overlay_set_size, "$jqregstr", ":jq_size"),

        (create_text_overlay, "$jqregagi", "@_{reg1}_", tf_center_justify),
        (position_set_y, pos1, 187),
        (overlay_set_position, "$jqregagi", pos1),
        (overlay_set_size, "$jqregagi", ":jq_size"),

        (create_text_overlay, "$jqregint", "@_{reg1}_", tf_center_justify),
        (position_set_y, pos1, 162),
        (overlay_set_position, "$jqregint", pos1),
        (overlay_set_size, "$jqregint", ":jq_size"),

        (create_text_overlay, "$jqregcha", "@_{reg1}_", tf_center_justify),
        (position_set_y, pos1, 137),
        (overlay_set_position, "$jqregcha", pos1),
        (overlay_set_size, "$jqregcha", ":jq_size"),

        (create_text_overlay,  "$jqhealth", "@_100%__", tf_center_justify),
        (position_set_x, pos1, 142),
        (position_set_y, pos1, 105),
        (overlay_set_position,  "$jqhealth", pos1),
        (position_set_x, ":jq_size", 1250),
        (position_set_y, ":jq_size", 1250),
        (overlay_set_size,  "$jqhealth", ":jq_size"),

        (create_text_overlay,  "$jqreglvl", "@_30_", tf_center_justify),
        (position_set_x, pos1, 122),
        (position_set_y, pos1, 76),
        (overlay_set_position,  "$jqreglvl", pos1),
        (position_set_x, ":jq_size", 1250),
        (position_set_y, ":jq_size", 1250),
        (overlay_set_size,  "$jqreglvl", ":jq_size"),

        (create_text_overlay,  "$jqtonextlvl", "@_3333333333_", tf_center_justify),
        (position_set_x, pos1, 124),
        (position_set_y, pos1, 60),
        (overlay_set_position,  "$jqtonextlvl", pos1),
        (position_set_x, ":jq_size", 800),
        (position_set_y, ":jq_size", 800),
        (overlay_set_size,  "$jqtonextlvl", ":jq_size"),

        # Weapons and Armor headlines
        (position_set_x, pos1, 353),
        (position_set_y, pos1, 707),
        (create_text_overlay, "$g_jq_equip_hline1", "@-Weapons-"),
        (overlay_set_position, "$g_jq_equip_hline1", pos1),
        (overlay_set_color, "$g_jq_equip_hline1", 0xFF000066),

        (position_set_y, pos1, 622),
        (create_text_overlay, "$g_jq_equip_hline2", "@-Armor-"),
        (overlay_set_position, "$g_jq_equip_hline2", pos1),
        (overlay_set_color, "$g_jq_equip_hline2", 0xFF000099),

        # items
        (create_text_overlay, "$g_jq_equipment_item0", "@n/a________________________________", tf_left_align), #item 0
        (create_text_overlay, "$g_jq_equipment_item1", "@n/a________________________________", tf_left_align), #item 1
        (create_text_overlay, "$g_jq_equipment_item2", "@n/a________________________________", tf_left_align), #item 2
        (create_text_overlay, "$g_jq_equipment_item3", "@n/a________________________________", tf_left_align), #item 3
        (create_text_overlay, "$g_jq_equipment_item4", "@n/a________________________________", tf_left_align), #head
        (create_text_overlay, "$g_jq_equipment_item5", "@n/a________________________________", tf_left_align), #body
        (create_text_overlay, "$g_jq_equipment_item6", "@n/a________________________________", tf_left_align), #feet
        (create_text_overlay, "$g_jq_equipment_item7", "@n/a________________________________", tf_left_align), #hands

        (position_set_x, pos1, 353),
        (position_set_y, pos1, 690),
        (overlay_set_position, "$g_jq_equipment_item0", pos1),
        (position_set_y, pos1, 673),
        (overlay_set_position, "$g_jq_equipment_item1", pos1),
        (position_set_y, pos1, 656),
        (overlay_set_position, "$g_jq_equipment_item2", pos1),
        (position_set_y, pos1, 639),
        (overlay_set_position, "$g_jq_equipment_item3", pos1),

        (position_set_y, pos1, 605),
        (overlay_set_position, "$g_jq_equipment_item4", pos1),
        (position_set_y, pos1, 588),
        (overlay_set_position, "$g_jq_equipment_item5", pos1),
        (position_set_y, pos1, 571),
        (overlay_set_position, "$g_jq_equipment_item6", pos1),
        (position_set_y, pos1, 554),
        (overlay_set_position, "$g_jq_equipment_item7", pos1),

        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, "$g_jq_equip_hline1", pos1),
        (overlay_set_size, "$g_jq_equip_hline2", pos1),
        (overlay_set_size, "$g_jq_equipment_item0", pos1),
        (overlay_set_size, "$g_jq_equipment_item1", pos1),
        (overlay_set_size, "$g_jq_equipment_item2", pos1),
        (overlay_set_size, "$g_jq_equipment_item3", pos1),
        (overlay_set_size, "$g_jq_equipment_item4", pos1),
        (overlay_set_size, "$g_jq_equipment_item5", pos1),
        (overlay_set_size, "$g_jq_equipment_item6", pos1),
        (overlay_set_size, "$g_jq_equipment_item7", pos1),

    # MORALE REPORT ETC ########################
        #  Colorcoded - perhaps later on...
        #  ("happy", "happy about"), # Green 
        #  ("content", "content with"), # Green/Yellow
        #  ("concerned", "concerned about"), # Yellow
        #  ("not_happy", "not at all happy about"), # orange
        #  ("miserable", "downright appalled at"),   #red

        (assign, ":x_poshl", 840),
        (assign, ":y_pos", 690),
        (position_set_x, ":jq_size", 850),
        (position_set_y, ":jq_size", 875),
        (position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, ":y_pos"),
        (str_store_troop_name, s9, "$jq_dude"),

        (create_text_overlay, "$jq_mrlc", "@{s9} feels...", tf_center_justify),
        (overlay_set_size, "$jq_mrlc", ":jq_size"),
        (position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, "$jq_mrlc", pos1),
        (overlay_set_color, "$jq_mrlc", 0xFFFFFFFF),
        (val_sub, ":y_pos", 27),

        (call_script, "script_npc_morale", "$jq_dude"),
        (assign, reg1, reg0),
        (create_text_overlay, "$jq_feeling1", "@{s6}", tf_center_justify),
        (create_text_overlay, ":jqreg2", "@your choice of companions,", tf_center_justify),
        (overlay_set_size, ":jqreg2", ":jq_size"),
        (overlay_set_size, "$jq_feeling1", ":jq_size"),
        (position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, "$jq_feeling1", pos1),
        (val_sub, ":y_pos", 19),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, ":jqreg2", pos1),
        (overlay_set_color,"$jq_feeling1",  0xFFFFFF00),
        (overlay_set_color, ":jqreg2", 0xFFFFFFFF),
        (val_sub, ":y_pos", 19),

        #(str_store_string, 7, "@{s7}"),
        (create_text_overlay, "$jq_feeling2", "@{s7}", tf_center_justify),
        (create_text_overlay,  ":jqreg2", "@your style of leadership and...", tf_center_justify),
        (overlay_set_size, ":jqreg2", ":jq_size"),
        (overlay_set_size, "$jq_feeling2", ":jq_size"),
        (position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, "$jq_feeling2", pos1),
        (val_sub, ":y_pos", 19),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, ":jqreg2", pos1),
        (overlay_set_color,"$jq_feeling2",  0xFFFFFF00),
        (overlay_set_color, ":jqreg2", 0xFFFFFFFF),
        (val_sub, ":y_pos", 19),
 
        (create_text_overlay, "$jq_feeling3", "@{s8}", tf_center_justify),
        (create_text_overlay, ":jqreg2", "@the general state of affairs.^------------------------------", tf_center_justify),
        (overlay_set_size, ":jqreg2", ":jq_size"),
        (overlay_set_size, "$jq_feeling3", ":jq_size"),
        (position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, "$jq_feeling3", pos1),
        (val_sub, ":y_pos", 36),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, ":jqreg2", pos1),
        (overlay_set_color,"$jq_feeling3",  0xFFFFFF00),
        (overlay_set_color, ":jqreg2", 0xFFFFFFFF),

        (val_sub, ":y_pos", 51),
        (create_text_overlay, "$jq_comphome", "@Morale:_______________________^^Origin: _________", tf_center_justify),
        (overlay_set_size, "$jq_comphome", ":jq_size"),
        (position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, "$jq_comphome", pos1),
        (overlay_set_color, "$jq_comphome", 0xFFFFFFFF),

        (val_sub, ":y_pos", 27),
        (create_text_overlay, "$jq_state", "@State:_______________________", tf_center_justify),
        (overlay_set_size, "$jq_state", ":jq_size"),
        (position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, "$jq_state", pos1),
        (overlay_set_color, "$jq_state", 0xFFFFFFFF),
    # MORALE REPORT ETC END ########################

        (call_script, "script_jq_browse", "$jq_dude", 150),
       ]),
    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (try_begin),
            (eq, ":object", "$g_jq_Return_to_menu"), 
            (assign, "$jq_just_visited_CO", 0),#do NOT autoreturn to store
            (assign, "$jq_override",0), #use default anim and camera settings in 'module-scripts'
            (presentation_set_duration, 0),
        (else_try),
            (eq, ":object", "$g_presentation_obj_1"),# pressed 'Quick View'
            (start_presentation, "prsnt_jq_companions_quickview"),
        (else_try),
        # BROWSE BUTTONS #############
            # Left btn -----------------------------#
            (eq, ":object", "$g_jq_prevtroop"),
            #(is_between, "$jq_slot", 1, "$jq_nr"),
            (val_sub, "$jq_slot", 1),
            (try_begin),
                (lt, "$jq_slot", 0),
                (val_sub, "$jq_nr", 1),
                (assign, "$jq_slot", "$jq_nr"),# Cycle when min reached 
                (val_add, "$jq_nr", 1),
            (try_end),
            (troop_get_slot, "$jq_dude", "trp_temp_array_c", "$jq_slot"),
            (overlay_set_alpha, "$jq_portrait", 0), 
            (create_mesh_overlay_with_tableau_material, "$jq_portrait", -1, "tableau_game_character_sheet", "$jq_dude"),
            (call_script, "script_jq_browse", "$jq_dude", 150),
        (else_try),
            # Right btn ---------------------------#
            (eq, ":object", "$g_jq_nexttroop"),
            #(is_between, "$jq_slot", 0, "$jq_nr"),
            (val_add, "$jq_slot", 1),
            (try_begin),
                (eq, "$jq_slot", "$jq_nr"),
                (assign, "$jq_slot", 0),# Cycle when max reached 
                #(val_sub, "$jq_slot", 1),
            (try_end),
            (troop_get_slot, "$jq_dude", "trp_temp_array_c", "$jq_slot"),
            (overlay_set_alpha, "$jq_portrait", 0), 
            (create_mesh_overlay_with_tableau_material, "$jq_portrait", -1, "tableau_game_character_sheet", "$jq_dude"),
            (call_script, "script_jq_browse", "$jq_dude", 150),
        # BROWSE BUTTONS END ###########
        (else_try),
            (eq, ":object", "$g_jqhelp"),
            (eq, "$jq_helptoggle", 0),
            (assign, "$jq_helptoggle", 1),
            (overlay_animate_to_alpha, "$g_jqhelptxt", 400, 0xFF),
        (else_try),
            (eq, ":object", "$g_jqhelp"),
            (eq, "$jq_helptoggle", 1),
            (assign, "$jq_helptoggle", 0),
            (overlay_animate_to_alpha, "$g_jqhelptxt", 400, 0),    
        (else_try),
            (eq, ":object", "$g_quitdebug2"),#quit - only for debug        
            (presentation_set_duration, 0),
            (jump_to_menu, "mnu_end_game"),
        (else_try),
            (eq, ":object", "$g_jq_Back_to_shop"),
            (assign, "$jq_just_visited_CO", 1),
            (assign, "$jq_override",0), 
            (presentation_set_duration, 0),
        (try_end),
       ]),
    (ti_on_presentation_run,
       [(try_begin),
            (key_clicked, key_right_mouse_button),
            (eq, "$jq_in_market_menu", 0),
            (assign, "$jq_override",0), 
            (presentation_set_duration, 0),
            (jump_to_menu, "mnu_reports"),
        (else_try),
            (key_clicked, key_right_mouse_button),
            (eq, "$jq_in_market_menu", 1),
            (assign, "$jq_override",0), 
            (presentation_set_duration, 0),      
            (jump_to_menu,"mnu_town_trade"),
        (else_try),
            (key_clicked, key_back_space),    
            (eq, "$jq_in_market_menu", 1),
            (eq, "$jq_current_town", "$current_town"),
            (assign, "$jq_just_visited_CO", 1),
            (assign, "$jq_override",0),
            (presentation_set_duration, 0),      
            (jump_to_menu,"mnu_town_trade"),
        (else_try),
            (key_clicked, key_escape),
            (start_presentation, "prsnt_jq_companions_quickview"),
        (else_try),
            (key_clicked, key_home),
            (assign, "$jq_startpage", 2),    
            (play_sound, "snd_put_back_sword"),    
            (display_message,"@Startpage set (Extended View)",0xFFAAFFAA),    
        (try_end),
       ]),
   ]),
##


##Custom Player Kingdom Vassal Titles by Caba@ Drin
  ("set_vassal_title",0,mesh_load_window,[
      (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
	    (str_clear, s0),
        (str_clear, s1),
        (str_clear, s2),
		(str_clear, s3),
       
        (create_text_overlay, reg0, "@How will your male vassals be known?", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg0, pos1),
        (create_text_overlay, reg0, "@How will your female vassals be known?", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 400),
        (overlay_set_position, reg0, pos1),
        
        (create_simple_text_box_overlay, "$g_presentation_obj_name_kingdom_1"),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 500),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),
        (try_begin),
          (troop_slot_eq, "trp_heroes_end", 0, 1), #Pick a slot
          (str_store_troop_name, s3, "trp_heroes_end"),
        (else_try),
          (str_store_string, s3, "@Default title."),
        (try_end),
        (overlay_set_text, "$g_presentation_obj_name_kingdom_1", s3),
        
        (create_simple_text_box_overlay, reg0),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 300),
        (overlay_set_position, reg0, pos1),
        (try_begin),
          (troop_slot_eq, "trp_heroes_end", 1, 1), #Pick a slot
          (str_store_troop_name_plural, s3, "trp_heroes_end"),
        (else_try),
          (str_store_string, s3, "@Default title."),
        (try_end),
        (overlay_set_text, reg0, s3),
		(str_clear, s3),
          
        (create_button_overlay, reg0, "@Set Custom Titles.", tf_center_justify),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 150),
        (overlay_set_position, reg0, pos1),
		
		(create_button_overlay, reg0, "@Use fief-based titles (Default).", tf_center_justify),
        (position_set_x, pos1, 600),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg0, pos1),
		
        (presentation_set_duration, 999999),
        ]),
      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
          (eq, ":object", "$g_presentation_obj_name_kingdom_1"),
          (str_store_string, s1, s0), #Male Title
        (else_try),
          (store_add, ":overlay", "$g_presentation_obj_name_kingdom_1", 1),
          (eq, ":object", ":overlay"), 
          (str_store_string, s2, s0), ##Female Title          
        (else_try),
          (val_add, ":overlay", 1), 
          (eq, ":object", ":overlay"), #Set Custom Titles button
		  (assign, ":change", 0),
          (try_begin),
            (neg|str_is_empty, s1),
            (troop_set_name, "trp_heroes_end", s1),
            (troop_set_slot, "trp_heroes_end", 0, 1),
            (try_for_range, ":lord_lady", lords_begin, lords_end),
                (store_troop_faction, ":faction", ":lord_lady"),
                (eq, ":faction", "fac_player_supporters_faction"),
                (call_script, "script_troop_set_title_according_to_faction", ":lord_lady", ":faction"),
            (try_end),
			(assign, ":change", 1),
          (try_end),
          (try_begin),
            (neg|str_is_empty, s2),
            (troop_set_plural_name, "trp_heroes_end", s2),
            (troop_set_slot, "trp_heroes_end", 1, 1),
            (try_for_range, ":lord_lady", kingdom_ladies_begin, kingdom_ladies_end),
                (store_troop_faction, ":faction", ":lord_lady"),
                (eq, ":faction", "fac_player_supporters_faction"),
                (call_script, "script_troop_set_title_according_to_faction", ":lord_lady", ":faction"),
            (try_end),
			(assign, ":change", 1),
          (try_end),
          (try_begin),
            (eq, ":change", 1),
            (try_for_range, ":lord_lady", companions_begin, companions_end),
                (store_troop_faction, ":faction", ":lord_lady"),
                (eq, ":faction", "fac_player_supporters_faction"),
                (troop_slot_eq, ":lord_lady", slot_troop_occupation, slto_kingdom_hero),
                (call_script, "script_troop_set_title_according_to_faction", ":lord_lady", ":faction"),
            (try_end),
          (try_end),          
          (presentation_set_duration, 0),
		(else_try),
          (val_add, ":overlay", 1), 
          (eq, ":object", ":overlay"), #Use Expanded Pack
          (troop_set_slot, "trp_heroes_end", 0, 0),
          (troop_set_slot, "trp_heroes_end", 1, 0),
          (try_for_range, ":lord_lady", lords_begin, kingdom_ladies_end),
            (neg|is_between, ":lord_lady", pretenders_begin, pretenders_end),
            (store_troop_faction, ":faction", ":lord_lady"),
            (eq, ":faction", "fac_player_supporters_faction"),
            (call_script, "script_troop_set_title_according_to_faction", ":lord_lady", ":faction"),
          (try_end),
          (try_for_range, ":lord_lady", companions_begin, companions_end),
            (store_troop_faction, ":faction", ":lord_lady"),
            (eq, ":faction", "fac_player_supporters_faction"),
            (troop_slot_eq, ":lord_lady", slot_troop_occupation, slto_kingdom_hero),
            (call_script, "script_troop_set_title_according_to_faction", ":lord_lady", ":faction"),
          (try_end),
          (presentation_set_duration, 0),
        (try_end),
        ]),
      ]),
##

##Custom Player Party Name by Caba`Drin
  ("set_party_name",0,mesh_load_window,[
     (ti_on_presentation_load,
       [(set_fixed_point_multiplier, 1000),
	    (str_clear, s0), ##BUGFIX - Caba
		(str_clear, s5), ##BUGFIX - Caba
		(str_clear, s7), ##BUGFIX - Caba
        (str_store_string, s1, "@What will your party be known as?"),
        (create_text_overlay, reg1, s1, tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 500),
        (overlay_set_position, reg1, pos1),
        (overlay_set_text, reg1, s1),
        (create_simple_text_box_overlay, "$g_presentation_obj_name_kingdom_1"),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 400),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),        
        (str_store_party_name, s7, "p_main_party"),
        (overlay_set_text, "$g_presentation_obj_name_kingdom_1", s7),
        
        (create_button_overlay, "$g_presentation_obj_name_kingdom_2", "@By the name entered above."),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_2", pos1),
          
        (str_store_troop_name, s5, "trp_player"),
        (create_button_overlay, reg1, "@Simply by my name: {s5}."),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 275),
        (overlay_set_position, reg1, pos1),  
          
        (presentation_set_duration, 999999),
        ]),
      (ti_on_presentation_event_state_change,
       [(store_trigger_param_1, ":object"),
        (try_begin),
          (eq, ":object", "$g_presentation_obj_name_kingdom_1"),
          (str_store_string, s7, s0),
        (else_try),
          (eq, ":object", "$g_presentation_obj_name_kingdom_2"),
          (party_set_name, "p_main_party", s7),
          (party_set_slot, 0, 1, 1),
          (presentation_set_duration, 0),
        (else_try),
          (store_add, ":overlay", "$g_presentation_obj_name_kingdom_2", 1),
          (eq, ":overlay", ":object"),
          (party_set_name, "p_main_party", s5),
          (party_set_slot, 0, 1, 0),
          (presentation_set_duration, 0),
        (try_end),
        ]),
      ]),    
##

##TEMPERED scene picker siege camps, castles, towns                                                                                                                                                                                                          ############ skirmisher slider##################
   ("scene_picker",0,mesh_load_window,[
      (ti_on_presentation_load,
       [	(presentation_set_duration,99999),
			(set_fixed_point_multiplier, 1000),
			(assign,"$g_presentation_obj_15_val","p_town_1"),
			(str_store_party_name,s2,"$g_presentation_obj_15_val"),
#hero slider        
			(create_slider_overlay, "$g_presentation_obj_15", "p_town_1", "p_castle_48"),               
			(position_set_x, pos1, 500),
			(position_set_y, pos1, 500),
			(overlay_set_position, "$g_presentation_obj_15", pos1),
			(overlay_set_val, "$g_presentation_obj_15",  "$g_presentation_obj_15_val"),

			(create_text_overlay, "$g_presentation_obj_17","@ {s2} siege camp.",tf_center_justify),
			(position_set_x, pos1, 500),
			(position_set_y, pos1, 600),
			(overlay_set_position, "$g_presentation_obj_17", pos1),
			(position_set_x, pos2,1000),
			(position_set_y, pos2,1000),
			(overlay_set_size,"$g_presentation_obj_17",pos2),

			#CONTINUE BUTTON
			(create_game_button_overlay,"$g_presentation_obj_19","@_Continue_",tf_center_justify),
			(position_set_x, pos1, 500),
			(position_set_y, pos1, 30),
			(overlay_set_position, "$g_presentation_obj_19", pos1),			

		]),
		
      (ti_on_presentation_event_state_change,
       [	(store_trigger_param_1, ":object"),
			(store_trigger_param_2, ":value"),
			(try_begin),
				(eq,"$g_presentation_obj_19",":object"),
				(assign,"$temp_presentation_shown",1),				
				(presentation_set_duration,0),
			(else_try),
				(eq,":object","$g_presentation_obj_15"),
				(assign,"$g_presentation_obj_15_val",":value"),
				(str_store_party_name, s2,":value"),
				(overlay_set_text,"$g_presentation_obj_17", "@ {s2} siege camp.",tf_center_justify),
			(try_end),
        ]),		
	]),
##

##Floris Sea Trade - Name your ship

  ("manage_ships", 0, mesh_load_window, [ 
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
		
		(str_clear, s0), #just in case
		(try_for_range, ":i", 0, 100), #be sure the temp slots are empty
		    (troop_set_slot, "trp_temp_array_a", ":i", 0),
			(troop_set_slot, "trp_temp_array_b", ":i", 0),
		(try_end),
        		
		(create_text_overlay, reg0, "@Manage Ship", tf_center_justify),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 680),
        (overlay_set_position, reg0, pos1),
		(position_set_x, pos1, 1500),
        (position_set_y, pos1, 1500),
        (overlay_set_size, reg0, pos1),
		
		(str_store_string, s11, "@{s12}\
Cogs are large sailing ships with their bows and sterns built at a higher level than the rest of the ship in order to form a castle like structure,\
which is used to defend the ship from enemies using archers. The Cog was the first type of boat that used the new idea of a rudder mounted on the stern\
for steering purpose. However as this is still a rather new idea, many cogs are still equipped with steering oars, which were also known as side rudders.\
The early cogs, weren't very large and had open hulls which didnt offer much sailing capability.^^\
Nowadays the cogs are used for sailing through rough waters and their hull is made from clinker construction, which provides them with\
added strength and robustness. Their hulls also grew in size as they evolved into large cargo carriers.^^\
Cog are ships with flat bottoms. They have a ridge or keel that runs along the lower side of the ship. On both sides of the keel, there\
is lapstrake planking, firmly fixed by iron nails. The stern and stern posts are both straight in shape and attached to the keel plate\
by means of hooks. The plank of the keel is thicker than the lapstrake and planking at the sites and moreover, the stern mounted central\
rudder is an integral part of the cog construction. It is this design, that makes cogs more stable than any other type of ship.^^\
Generally built from oak wood, cogs have only a single long mast, which carries a massive square sail. The size of the sail depends \
on the size of the hull. This means that as the size of cog hull became bigger, the size of sails also increased. The only drawback of this construction\
was that it prevented sailing directly into the wind. However it facilitated the yacht so far, that it could be handled by a small crew,\
reducing the overall operational cost."),
		
		(create_text_overlay, reg0, s11, tf_double_space|tf_scrollable),  ##Describes the ship
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 80),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 550),
        (position_set_y, pos1, 500),
        (overlay_set_area_size, reg0, pos1),
		
		
        (create_text_overlay, reg0, "@Select ship:", tf_center_justify),
        (position_set_x, pos1, 150),
        (position_set_y, pos1, 550),
        (overlay_set_position, reg0, pos1),
		
		(position_set_x, pos1, 160),
		(position_set_y, pos1, 510),
        (create_combo_button_overlay, "$g_presentation_obj_11"),	#Combo Button for ships
        (overlay_set_position, "$g_presentation_obj_11", pos1),
		
		(assign, ":slot", 0),
		(try_for_parties, ":ship_no"),
			(party_slot_eq, ":ship_no", slot_ship_center, "$current_town"),
			(str_store_party_name, s1, ":ship_no"),
			(overlay_add_item, "$g_presentation_obj_11", s1),
			(overlay_set_val, "$g_presentation_obj_11", reg6),
			(troop_set_slot, "trp_temp_array_a", ":slot", ":ship_no"), #this way the troop slot # = overlay combo box index #
			(val_add, ":slot", 1),
		(try_end),
		
	    (create_text_overlay, reg0, "@Name your ship:", tf_center_justify),
        (position_set_x, pos1, 150),
        (position_set_y, pos1, 475),
        (overlay_set_position, reg0, pos1),
		
		(create_simple_text_box_overlay, "$g_presentation_obj_name_kingdom_1"), #Text box
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 440),
        (overlay_set_position, "$g_presentation_obj_name_kingdom_1", pos1),	
				
        (create_button_overlay, "$g_presentation_obj_13", "@Rename Ship."),
        (position_set_x, pos1, 75),
        (position_set_y, pos1, 400),
        (overlay_set_position, "$g_presentation_obj_13", pos1),
	
	
		(create_text_overlay, reg0, "@Send ship to port:", tf_center_justify),
        (position_set_x, pos1, 150),
        (position_set_y, pos1, 250),
        (overlay_set_position, reg0, pos1),
		
		(position_set_x, pos1, 160),
		(position_set_y, pos1, 210),
        (create_combo_button_overlay, "$g_presentation_obj_12"),	#Combo Button for towns
        (overlay_set_position, "$g_presentation_obj_12", pos1),
      
		(assign, ":slot", 0),
		(try_for_range, ":town_no", towns_begin, towns_end),
			(neq, ":town_no", "$current_town"),
			(party_slot_ge, ":town_no", slot_town_is_coastal, 1),
			(store_faction_of_party, ":faction_1", "p_main_party"),
			(store_faction_of_party, ":faction_2", ":town_no"),
			(store_relation, ":relation", ":faction_1", ":faction_2"), #Cant send to enemy ports
			(ge, ":relation", 0),
			(str_store_party_name, s1, ":town_no"),
			(overlay_add_item, "$g_presentation_obj_12", s1),
			(troop_set_slot, "trp_temp_array_b", ":slot", ":town_no"), #this way the troop slot # = overlay combo box index #
			(val_add, ":slot", 1),
		(try_end),   	

		(try_begin), 
         (neq, reg6, -1),
         (overlay_set_val, "$g_presentation_obj_11", reg6),
		 (troop_get_slot, ":ship_no", "trp_temp_array_a", reg6),
		 (str_store_party_name, s13, ":ship_no"),
         (overlay_set_text, "$g_presentation_obj_name_kingdom_1", s13),	
        (try_end),	
		(try_begin),
         (neq, reg8, -1),
         (overlay_set_val, "$g_presentation_obj_12", reg8),
        (try_end),	
##TO MAKE THIS WORK, add:
# (assign, reg6, -1),
# (assign, reg8, -1),
##right before the presentation call in the menu		

		
		(create_button_overlay, "$g_presentation_obj_14", "@Verify."), ##Duh - renamed
        (position_set_x, pos1, 75),
        (position_set_y, pos1, 175),
        (overlay_set_position, "$g_presentation_obj_14", pos1),

		(create_button_overlay, "$g_presentation_obj_2", "@Manage the crew."),
        (position_set_x, pos1, 75),
        (position_set_y, pos1, 365),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
		
		(create_button_overlay, "$g_presentation_obj_15", "@View the ship registry."),
        (position_set_x, pos1, 75),
        (position_set_y, pos1, 330),
        (overlay_set_position, "$g_presentation_obj_15", pos1),		
		
		
		(create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_19", "@Done", 0),
        (position_set_x, pos1, 880),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_custom_battle_designer_19", pos1),
        ]),
		
	(ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
			(eq, ":object", "$g_presentation_obj_11"), #Combo Box - Ship Select
			(assign, reg6, ":value"),
			(troop_get_slot, ":ship_no", "trp_temp_array_a", reg6),
			(str_store_party_name, s13, ":ship_no"),
			(party_get_num_companions, reg7, ":ship_no"),
			(str_store_string, s12, "@This is your ship '{s13}'. The crew is currently made up of {reg7} men.^^"),
            (overlay_set_text, "$g_presentation_obj_name_kingdom_1", s13),
			(start_presentation, "prsnt_manage_ships"),
        (else_try),
			(eq, ":object", "$g_presentation_obj_name_kingdom_1"), #Text Box - Ship Name
			(str_store_string, s14, s0),
		(else_try),
		    (eq, ":object", "$g_presentation_obj_13"), # Rename Ship
			(neq, reg6, -1),
			(troop_get_slot, ":ship_no", "trp_temp_array_a", reg6),
			(party_set_name, ":ship_no", s14),
			(str_store_party_name, s13, ":ship_no"),
			(party_get_num_companions, reg7, ":ship_no"),
			(str_store_string, s12, "@This is your ship '{s13}'. The crew is currently made up of {reg7} men.^^"),
			(start_presentation, "prsnt_manage_ships"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_2"), #Manage crew
			(try_begin),
				(party_get_slot, ":num_ships_current", "$current_town", slot_town_has_ship),
				(ge, ":num_ships_current", 1),	
				(troop_get_slot, ":ship_no", "trp_temp_array_a", reg6),
				(party_get_slot, ":loc_no", ":ship_no", slot_ship_center),
				(eq, ":loc_no", "$current_town"),
				(assign, "$ship", ":ship_no"),
				(assign, "$crew_screen_state", 1),
				(presentation_set_duration, 0),
			(else_try),
				(display_message, "@Make sure you selected a ship"),
			(try_end),
		(else_try),
			(eq, ":object", "$g_presentation_obj_15"), #Registry
			(assign, "$crew_screen_state", 3),
			(presentation_set_duration, 0),
		(else_try),
			(eq, ":object", "$g_presentation_obj_12"), #Combo Box - Port to Send
			(assign, reg8, ":value"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_14"), # Send Ship
			(neq, reg6, -1),
			(neq, reg8, -1),
			(troop_get_slot, ":town_no", "trp_temp_array_b", reg8),
			(troop_get_slot, ":ship_no", "trp_temp_array_a", reg6),
			(try_begin),
				(party_get_num_companions, reg7, ":ship_no"),
				#(ge, reg7, 30),
				#(le, reg7, 90),
				(is_between, reg7, 30, 91),
				(party_get_slot, ":num_ships_current", "$current_town", slot_town_has_ship),
				(ge, ":num_ships_current", 1),												#Making sure there is a ship to send
				(party_get_slot, ":num_ships_target", ":town_no", slot_town_has_ship),
				(lt, ":num_ships_target", 5),												#Making sure the target town has space for another ship
				(val_add, ":num_ships_target", 1),	
				(val_sub, ":num_ships_current", 1),
				(party_set_slot, "$current_town", slot_town_has_ship, ":num_ships_current"),
				(party_set_slot, ":town_no", slot_town_has_ship, ":num_ships_target"),
				(party_set_slot, ":ship_no", slot_ship_center, ":town_no"),
				(str_store_party_name, s15, ":ship_no"),
				(str_store_party_name, s16, ":town_no"),
				(start_presentation, "prsnt_manage_ships"),
				(str_clear, s12),
				(display_message, "@Your ship {s15} succesfully set sail for {s16}."),
			(else_try),
				(display_message, "@Make sure a ship is selected, it has a sufficient crew and there is room for another ship in the target town."),
			(try_end),			
		(else_try),
		    (eq, ":object", "$g_presentation_obj_custom_battle_designer_19"),
			(presentation_set_duration, 0),
		(try_end),       
		
		]),
      ]),

   ("bank", 0, mesh_load_window, [ 													#	Floris Overhaul
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
		
		(try_begin),
			(party_get_slot, ":assets", "$current_town", slot_town_bank_assets),
			(troop_add_gold, "trp_player", ":assets"),
			(party_set_slot, "$current_town", slot_town_bank_assets, 0),
		(try_end),
			
		(str_store_party_name, s1, "$current_town"),

		
	    (create_text_overlay, reg0, 
"@This area of {s1} can best be described as the very core of the town.^^\
 You can almost see the strings that are being pulled from here, the money that comes and goes at seemingly endless rates. \
 Here you can buy the land that is cultivated outside the towns gates and benefit from the ones working hard.\
 Of course you might not have the denars required to do so, but the moneylenders are known to have some spare change.",tf_center_justify),
        (position_set_x, pos1, 475),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg0, pos1),
		
        (position_set_x, pos2, 800),
        (position_set_y, pos2, 900),		
		(overlay_set_size, reg0, pos2),
		
		(party_get_slot, ":population", "$current_town", slot_center_population),
		(party_get_slot, ":land_town", "$current_town", slot_town_acres),
		(party_get_slot, ":land_player", "$current_town", slot_town_player_acres),
		(store_add, ":land_total", ":land_town", ":land_player"),
		(assign, reg1, ":population"),
		(assign, reg2, ":land_total"),
		(assign, reg3, ":land_player"),
		
		(party_get_slot, ":debt", "$current_town", slot_town_bank_debt),
		(assign, reg4, ":debt"),
		
		(assign, reg5, 0),														#Slider storage / acres		Buy
		(assign, reg6, 0),														#Slider storage / money		Borrow
		(assign, reg7, 0),														#Slider storage / acres		Build
		(assign, reg8, 0),														#Slider storage / money		Pay back
		
		(party_get_slot, ":prosp_mod", "$current_town", slot_town_prosperity),
		(store_mul, ":price_mod", ":prosp_mod", 10),
		(val_sub, ":price_mod", 500),
		(store_add, reg9, 1000, ":price_mod"),									#Buy Price 
		(store_add, reg10, 750, ":price_mod"),									#Sell Price 
		(store_add, reg11, 2000, ":price_mod"),									#Build Price
		#reg12 used for buy/sell switch
		(store_sub, ":rent_mod", ":prosp_mod", 50),
		(store_add, reg13, ":rent_mod", 100),									#Rent Revenue

		(create_text_overlay, "$g_presentation_obj_19", "@{reg1} people live in {s1}. There are currently {reg2} acres of land available for cultivation to provide them with \
 food and other goods. You own {reg3} acres of land in this town. You currently owe the moneylenders of {s1} {reg4} denars. The interest rate is 20% and the contract period amounts \
 to 2 weeks. If you dont manage to pay off your debt until the deadline, the interest is raised to 40%. Buying an existing acre costs {reg9} denars, while it sells for {reg10} denars. Building a new one requires {reg11} denars.\
 The rent paid to landowners currently accumulates to {reg13} denars per acre every 2 weeks and has to be collected in the town. Land wont be rented if a town is already well supplied.",tf_center_justify),
        (position_set_x, pos1, 475),
        (position_set_y, pos1, 450),
        (overlay_set_position, "$g_presentation_obj_19", pos1),
		
        (position_set_x, pos2, 900),
        (position_set_y, pos2, 1000),		
		(overlay_set_size, "$g_presentation_obj_19", pos2),	
		
		(try_begin),
			(eq, reg12, 2222),	
			(str_store_string, s2, "@Choose how many acres you wish to sell :"),
		(else_try),
			(str_store_string, s2, "@Choose how many acres you wish to buy :"),
		(try_end),
			
		(create_button_overlay, "$g_presentation_obj_16", "@{s2}",tf_center_justify),				#	Landlords buy
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 350),
        (overlay_set_position, "$g_presentation_obj_16", pos1),
		
		(store_troop_gold, ":funds", "trp_player"),
		(store_div, ":funds_build", ":funds", reg11),
		(val_div, ":funds", reg9),
		(val_min, ":funds", ":land_town"),

		(try_begin),
			(eq, reg12, 2222),
			(party_get_slot, ":sell_no", "$current_town", slot_town_player_acres),
			(assign, ":funds", ":sell_no"),
		(try_end),
		
		(create_slider_overlay, "$g_presentation_obj_1", 0, ":funds"),
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 310),
        (overlay_set_position, "$g_presentation_obj_1", pos1),

		(create_text_overlay, "$g_presentation_obj_2", "@0"),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_2", pos1),			

		(create_button_overlay, "$g_presentation_obj_3", "@Verify",tf_center_justify),		
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 275),
        (overlay_set_position, "$g_presentation_obj_3", pos1),	
		

		
		(create_text_overlay, reg0, "@Choose how much money you wish to borrow :",tf_center_justify),			#	Moneylenders borrow
        (position_set_x, pos1, 725),
        (position_set_y, pos1, 350),
        (overlay_set_position, reg0, pos1),
		
		(assign, ":fief_count", 0),																				#	Money = 250*Prosperity + Relationship*100 - Debt, IF Player owns fief or is renowned,
		(try_for_range, ":cur_center", centers_begin, centers_end),												#	otherwise not more than 5000 + Relationship*100 - Debt
			(party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
			(val_add, ":fief_count", 1),
		(try_end),
		(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
		(party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		(store_mul, ":money", ":prosperity", 250),
		(try_begin),
			(lt, ":fief_count", 1),
			(lt, ":renown", 500),
			(gt, ":money", 5000),
			(assign, ":money", 5000),
		(try_end),
		(party_get_slot, ":player_relation", "$current_town", slot_center_player_relation),
		(store_mul, ":trust", ":player_relation", 100),
		(val_add, ":money", ":trust"),
		(val_sub, ":money", ":debt"),
		(try_begin),																							#	Money lending cant turn negative
			(lt, ":money", 0),	
			(assign, ":money", 0),
		(try_end),
		
		(try_begin),
			(assign, reg25, 0),
			(try_for_range, ":town_no", towns_begin, towns_end),													#	Too much debt overall or in a single bank will stop banks from lending you money
				(party_get_slot, ":debt_all", ":town_no", slot_town_bank_debt),
				(val_add, reg25, ":debt_all"),
			(try_end),
			(ge, reg25, 50000),
			(assign, ":money", 0),
		(try_end),
		
		(create_slider_overlay, "$g_presentation_obj_4", 0, ":money"),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 310),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
		
		(create_text_overlay, "$g_presentation_obj_5", "@0"),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
		
		(create_button_overlay, "$g_presentation_obj_6", "@Verify",tf_center_justify),		
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 275),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
		
		
		
		(create_text_overlay, "$g_presentation_obj_7", "@Buy and prepare uncultivated land :",tf_center_justify),		#	Landlord / Buy and Build
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 200),
        (overlay_set_position, "$g_presentation_obj_7", pos1),
		
		
		(create_slider_overlay, "$g_presentation_obj_8", 0, ":funds_build"),											#	Choose acres to build 
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 160),
        (overlay_set_position, "$g_presentation_obj_8", pos1),		
		
		(create_text_overlay, "$g_presentation_obj_9", "@0"),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 150),
        (overlay_set_position, "$g_presentation_obj_9", pos1),			

		(create_button_overlay, "$g_presentation_obj_10", "@Verify",tf_center_justify),		
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 125),
        (overlay_set_position, "$g_presentation_obj_10", pos1),	
		
		
		(create_text_overlay, "$g_presentation_obj_11", "@Pay off your debt :",tf_center_justify),		#	Pay off your debt
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 200),
        (overlay_set_position, "$g_presentation_obj_11", pos1),		
		
		(store_troop_gold, ":funds", "trp_player"),
		(try_begin),
			(lt, ":debt", ":funds"),
			(assign, ":funds", ":debt"),
		(try_end),
		
		(create_slider_overlay, "$g_presentation_obj_12", 0, ":funds"),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 160),
        (overlay_set_position, "$g_presentation_obj_12", pos1),		
		
		(create_text_overlay, "$g_presentation_obj_13", "@0"),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 150),
        (overlay_set_position, "$g_presentation_obj_13", pos1),			

		(create_button_overlay, "$g_presentation_obj_14", "@Verify",tf_center_justify),		
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 125),
        (overlay_set_position, "$g_presentation_obj_14", pos1),	
		
		
		
		(create_game_button_overlay, "$g_presentation_obj_15", "@Done", 0),										#	Leave
        (position_set_x, pos1, 880),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_15", pos1),		
		
        ]),
		
	(ti_on_presentation_event_state_change, 
		[
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
		
		(try_begin),
			(eq, ":object", "$g_presentation_obj_1"),															#	Show chosen amount of land
			(assign, reg5, ":value"),
			(overlay_set_text, "$g_presentation_obj_2", "@{reg5}"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_3"),															#	Sell/Buy chosen amount of land
			(try_begin),
				(eq, reg12, 2222),
				(try_begin),
					(gt, reg5, 0),
					(store_mul, ":price", reg5, reg10),
					(troop_add_gold, "trp_player", ":price"),					
					(party_get_slot, ":land_town", "$current_town", slot_town_acres),
					(val_add, ":land_town", reg5),
					(party_set_slot, "$current_town", slot_town_acres, ":land_town"),
					(party_get_slot, ":land_player", "$current_town", slot_town_player_acres),
					(val_sub, ":land_player", reg5),
					(party_set_slot, "$current_town", slot_town_player_acres, ":land_player"),
					(start_presentation, "prsnt_bank"),					
				(else_try),	
					(display_message, "@You cant sell 0 acres of land."),
				(try_end),
			(else_try),
				(try_begin),
					(gt, reg5, 0),
					(store_mul, ":cost", reg5, reg9),
					(troop_remove_gold, "trp_player", ":cost"),
					(party_get_slot, ":land_town", "$current_town", slot_town_acres),
					(val_sub, ":land_town", reg5),
					(party_set_slot, "$current_town", slot_town_acres, ":land_town"),
					(party_get_slot, ":land_player", "$current_town", slot_town_player_acres),
					(val_add, ":land_player", reg5),
					(party_set_slot, "$current_town", slot_town_player_acres, ":land_player"),
					(start_presentation, "prsnt_bank"),
				(else_try),
					(display_message, "@You cant buy 0 acres of land."),
				(try_end),
			(try_end),
		(else_try),
			(eq, ":object", "$g_presentation_obj_4"),															#	Show chosen amount of money
			(assign, reg6, ":value"),
			(overlay_set_text, "$g_presentation_obj_5", "@{reg6}"),
		(else_try),		
			(eq, ":object", "$g_presentation_obj_6"),															#	Borrow chosen amount of money
			(try_begin),
				(gt, reg6, 0),
				(party_get_slot, ":debt", "$current_town", slot_town_bank_debt),
				(try_begin),
					(le, ":debt", 0),
					(store_current_hours, ":date"),
					(val_add, ":date", 24*14*2), 								#	First Deadline / 4 weeks / then 2 weeks (see simple_triggers)
					(party_set_slot, "$current_town", slot_town_bank_deadline, ":date"),
				(try_end),
				(troop_add_gold, "trp_player", reg6),
				(val_mul, reg6, 120),
				(val_div, reg6, 100),
				(val_add, ":debt", reg6),
				(party_set_slot, "$current_town", slot_town_bank_debt, ":debt"),
				(start_presentation, "prsnt_bank"),
			(else_try),
				(display_message, "@You cant borrow 0 denars."),
			(try_end),
		(else_try),
			(eq, ":object", "$g_presentation_obj_8"),															#	Show chosen amount of land	//	2nd Option
			(assign, reg7, ":value"),
			(overlay_set_text, "$g_presentation_obj_9", "@{reg7}"),			
		(else_try),
			(eq, ":object", "$g_presentation_obj_10"),															#	Buy chosen amount of land	//	2nd Option
			(try_begin),
				(gt, reg7, 0),
				(store_mul, ":cost", reg7, reg11),
				(troop_remove_gold, "trp_player", ":cost"),
				(party_get_slot, ":land_player", "$current_town", slot_town_player_acres),
				(val_add, ":land_player", reg7),
				(party_set_slot, "$current_town", slot_town_player_acres, ":land_player"),
				(start_presentation, "prsnt_bank"),
			(else_try),
				(display_message, "@You cant buy 0 acres of land."),
			(try_end),		
		(else_try),
			(eq, ":object", "$g_presentation_obj_12"),															#	Show chosen amount of money
			(assign, reg8, ":value"),
			(overlay_set_text, "$g_presentation_obj_13", "@{reg8}"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_14"),															#	Pay back chosen amount of money
			(try_begin),
				(gt, reg8, 0),
				(troop_remove_gold, "trp_player", reg8),
				(party_get_slot, ":debt", "$current_town", slot_town_bank_debt),
				(val_sub, ":debt", reg8),
				(party_set_slot, "$current_town", slot_town_bank_debt, ":debt"),
				(try_begin),
					(le, ":debt", 0),
					(party_set_slot, "$current_town", slot_town_bank_deadline, 0),
				(try_end),
				(start_presentation, "prsnt_bank"),
			(else_try),
				(display_message, "@You cant pay back 0 denars."),
			(try_end),
		(else_try),																								#	Switch Buy/Sell
			(eq, ":object", "$g_presentation_obj_16"),
			(try_begin),
				(neq, reg12, 2222),
				(assign, reg12, 2222),
				(start_presentation, "prsnt_bank"),
			(else_try),
				(assign, reg12, 0),
				(start_presentation, "prsnt_bank"),
			(try_end),
		(else_try),
			(eq, ":object", "$g_presentation_obj_15"),															#	Leave
			(presentation_set_duration, 0),
		(try_end),       
		
		]),
      ]),	  
	  
	 #	Floris Bank
  ("bank_quickview", 0, mesh_companion_overview, #mesh_companion_overview
   [
     (ti_on_presentation_load,
      [
	    (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
		
#		(str_clear, s0),
 #       (create_text_overlay, reg0, "@Hello, {s0}", tf_scrollable),
 #       (position_set_x, pos1, 50),
  #      (position_set_y, pos1, 50),
 ###       (overlay_set_position, reg0, pos1),
 #       (position_set_x, pos1, 550),
 #       (position_set_y, pos1, 630),
  #      (overlay_set_area_size, reg0, pos1),
 #       (set_container_overlay, reg0),
		

		

		###HEADLINES###
		(assign, ":x_poshl", 155),
		(assign, ":y_pos", 581),
		(assign, ":jq_size", pos0),
		(position_set_x, ":jq_size", 720),
		(position_set_y, ":jq_size", 775),

        (create_text_overlay, reg1, "@Town", tf_center_justify),
    	(overlay_set_size, reg1, ":jq_size"),
 		(position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, reg1, pos1),
		
        (create_text_overlay, reg1, "@Acres", tf_center_justify),
       	(overlay_set_size, reg1, ":jq_size"),
		(val_add, ":x_poshl", 120),
 		(position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),	

        (create_text_overlay, reg1, "@Owned", tf_center_justify),
       	(overlay_set_size, reg1, ":jq_size"),
		(val_add, ":x_poshl", 108),
 		(position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),
		
        (create_text_overlay, reg1, "@Balance", tf_center_justify),
       	(overlay_set_size, reg1, ":jq_size"),
		(val_add, ":x_poshl", 112),
 		(position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),
		
		(create_text_overlay, reg1, "@Assets", tf_center_justify),
       	(overlay_set_size, reg1, ":jq_size"),
		(val_add, ":x_poshl", 105),
 		(position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),

        (create_text_overlay, reg1, "@Debt", tf_center_justify),
       	(overlay_set_size, reg1, ":jq_size"),
		(val_add, ":x_poshl", 105),
 		(position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),	

        (create_text_overlay, reg1, "@Deadline", tf_center_justify),
       	(overlay_set_size, reg1, ":jq_size"),
		(val_add, ":x_poshl", 120),
 		(position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),			
		
		
		(str_clear, s0),
		(create_text_overlay, reg0, s0, tf_scrollable),
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 450),
        (overlay_set_area_size, reg0, pos1),
		(set_container_overlay, reg0),		
		
		(assign, ":jq_value", 100),
		(assign, ":jq_size", 0),
		(assign, ":x_pos", 0),
		(assign, ":y_pos", 547),
		(str_clear, s9),	
		(str_clear, s8),
		
		
        (assign, reg2, 0),#total_acres
        (assign, reg3, 0),#player_acres
        (assign, reg4, 0),#balance
        (assign, reg5, 0),#assets
		(assign, reg6, 0),#debt
		(assign, reg7, 0),#deadline
		
		(try_for_range, ":center_no", towns_begin, towns_end),
			(party_get_slot, ":land_town", ":center_no", slot_town_acres),
			(party_get_slot, ":land_player", ":center_no", slot_town_player_acres),
			(party_get_slot, ":assets", ":center_no", slot_town_bank_assets),
			(party_get_slot,":debt",":center_no",slot_town_bank_debt),
			(party_get_slot, ":deadline", ":center_no", slot_town_bank_deadline),
			(party_get_slot, ":population", ":center_no", slot_center_population),
			(party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
			
			(store_add, ":land_total", ":land_town", ":land_player"),
			
			(store_div, ":acres_needed", ":population", 200),
			(store_sub, ":surplus", ":land_total", ":acres_needed"),
			(store_sub, ":revenue", ":prosperity", 50),
			(val_add, ":revenue", 100),
			(assign, ":rent_player", 0),			
			(assign, ":upkeep_player", 0),
			(try_begin),
				(gt, ":land_player", 0),												# 	Fix 
				(try_begin),															#	Player Balance
					(le, ":land_total", ":acres_needed"),
					(store_mul, ":rent_player", ":land_player", ":revenue"),										
				(else_try),
					(store_mul, ":penalty", ":surplus", -1),
					(val_add, ":penalty", ":revenue"),
					(try_begin),
						(ge, ":penalty", 85),
						(store_mul, ":rent_player", ":land_player", ":penalty"),
					(else_try),
						(store_sub, ":non_rented", ":surplus", 15),
						(store_sub, ":land_rented", ":land_player", ":non_rented"),					# Fixed, wrong display # if player owned too much land due to val_sub usage
						(store_mul, ":rent_player", ":land_rented", 85),
						(store_mul, ":upkeep_player", ":non_rented", -50),
					(try_end),
				(try_end),
			(try_end),
			
			(store_add, ":balance", ":rent_player", ":upkeep_player"),
			
			(val_add, ":jq_value", 1),   
				 
			#center center name
			(val_add, ":x_pos", 118), 
			(str_store_party_name,s9, ":center_no"),
			(str_store_string, s1, "@{s9}"),
			(create_text_overlay, reg1, s1, tf_left_align),
			(position_set_x, pos3, ":x_pos"),
			(position_set_y, pos3, ":y_pos"),
			(overlay_set_position, reg1, pos3),
			(position_set_x, pos3, 750),
			(position_set_y, pos3, 850),
			(overlay_set_size, reg1, pos3),

			#center land in acres
			(val_add, ":x_pos", 135),  
			(assign, reg2, ":land_total"),
			(create_text_overlay, reg1, "@{reg2}", tf_left_align),
			(position_set_x, pos3, ":x_pos"),
			(position_set_y, pos3, ":y_pos"),
			(overlay_set_position, reg1, pos3),
			(position_set_x, pos3, 750),
			(position_set_y, pos3, 850),
			(overlay_set_size, reg1, pos3),

			#Player land in city
			(val_add, ":x_pos", 113),  
			(assign, reg3, ":land_player"),
			(str_store_string, s1, "@{reg3}"),
			(create_text_overlay, reg1, s1, tf_left_align),
			(position_set_x, pos3, ":x_pos"),
			(position_set_y, pos3, ":y_pos"),
			(overlay_set_position, reg1, pos3),
			(position_set_x, pos3, 750),
			(position_set_y, pos3, 850),
			(overlay_set_size, reg1, pos3),

			#city Balance
			(val_add, ":x_pos", 110),  
			(assign, reg4, ":balance"),
			(str_store_string, s1, "@{reg4}"),
			(create_text_overlay, reg1, s1, tf_left_align),
			(position_set_x, pos3, ":x_pos"),
			(position_set_y, pos3, ":y_pos"),
			(overlay_set_position, reg1, pos3),
			(position_set_x, pos3, 750),
			(position_set_y, pos3, 850),
			(overlay_set_size, reg1, pos3),
			
			#Player assets in city
			(val_add, ":x_pos", 110),  
			(assign, reg4, ":assets"),
			(str_store_string, s1, "@{reg4}"),
			(create_text_overlay, reg1, s1, tf_left_align),
			(position_set_x, pos3, ":x_pos"),
			(position_set_y, pos3, ":y_pos"),
			(overlay_set_position, reg1, pos3),
			(position_set_x, pos3, 750),
			(position_set_y, pos3, 850),
			(overlay_set_size, reg1, pos3),

			#city Debt
			(val_add, ":x_pos", 105),  
			(assign, reg5, ":debt"),
			(str_store_string, s1, "@{reg5}"),
			(create_text_overlay, reg1, s1, tf_left_align),
			(position_set_x, pos3, ":x_pos"),
			(position_set_y, pos3, ":y_pos"),
			(overlay_set_position, reg1, pos3),
			(position_set_x, pos3, 750),
			(position_set_y, pos3, 850),
			(overlay_set_size, reg1, pos3),

			#city Deadline
			(val_add, ":x_pos", 105),
			(try_begin),
				(gt, ":deadline", 0),
				(call_script, "script_game_get_date_text", 1, ":deadline"),
			(else_try),
				(str_store_string, s1, "@None"),
			(try_end),
			(create_text_overlay, reg1, s1, tf_left_align),
			(position_set_x, pos3, ":x_pos"),
			(position_set_y, pos3, ":y_pos"),
			(overlay_set_position, reg1, pos3),
			(position_set_x, pos3, 750),
			(position_set_y, pos3, 850),
			(overlay_set_size, reg1, pos3),

			(assign, ":x_pos", 0),
			(assign, ":x_poshl", 165),
			(val_sub, ":y_pos", 23),#linebreak 
			(ge, ":x_pos", 950),
			(assign, ":x_pos", 0),
			(val_sub, ":y_pos", 23),
		(try_end), #Center-Bank Loop End

	  (set_container_overlay, -1),
	  
	  		 #Back to menu - graphical button
	    (create_game_button_overlay, "$g_jq_Return_to_menu", "@_Return to menu_"),	 
	    (position_set_x, pos1, 500),
        (position_set_y, pos1, 23),
        (overlay_set_position, "$g_jq_Return_to_menu", pos1),
		(assign, "$g_jq_Back_to_shop", 0), ##BUGFIX - savegame compatability 
		(assign, "$jq_nr", 0), ##BUGFIX - savegame compatability 
	  
	  ]),
	 (ti_on_presentation_event_state_change,
     [
        (store_trigger_param_1, ":object"),
		(try_begin), 
			(eq, ":object", "$g_jq_Return_to_menu"),
			(presentation_set_duration, 0),
		(try_end),
		]),
	]),
]
