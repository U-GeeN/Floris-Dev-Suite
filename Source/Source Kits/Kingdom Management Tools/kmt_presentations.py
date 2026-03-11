# Kingdom Management Tools (1.0) by Windyplains

from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
from header_items import *   # Added for Show all Items presentation.
from module_items import *   # Added for Show all Items presentation.
import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

# script_gpu_create_checkbox     - pos_x, pos_y, label, storage_slot, value_slot
# script_gpu_create_mesh         - mesh_id, pos_x, pos_y, size_x, size_y
# script_gpu_create_portrait     - troop_id, pos_x, pos_y, size, storage_id
# script_gpu_create_button       - title, pos_x, pos_y, storage_id
# script_gpu_create_text_label   - title, pos_x, pos_y, storage_id, design
# script_gpu_resize_object       - storage_id, percent size
# script_gpu_draw_line           - x length, y length, pos_x, pos_y, color
# script_gpu_container_heading   - pos_x, pos_y, size_x, size_y, storage_id
# script_gpu_create_slider       - min, max, pos_x, pos_y, storage_id, value_id

presentations = [
###########################################################################################################################
#####                                                KMT Lord Holdings                                                #####
###########################################################################################################################
("kmt_lord_holdings", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
		
		(assign, ":x_names", 25),
		(store_add, ":x_relations", ":x_names",  190),
		(store_add, ":x_towns", ":x_relations",   55),
		(store_add, ":x_castles", ":x_towns",    105),
		(store_add, ":x_villages", ":x_castles", 150),
		(store_add, ":x_friends", ":x_villages", 110),
		(store_add, ":x_enemies", ":x_friends",  165),
		
		(assign, "$gpu_storage", kmt_objects),
		
		(try_begin),
			(troop_slot_eq, kmt_objects, kmt_val_remove_backgrounds, 0),
			(call_script, "script_gpu_create_mesh", "mesh_pic_map_calradia_half", 0, 0, 1000, 1300),
			(overlay_set_alpha, reg1, 0x00),
		(try_end),
		(call_script, "script_gpu_draw_line", 950, 510, 25, 115, 10526880), # White background above the map.
		(overlay_set_alpha, reg1, 0x77),
		(call_script, "script_gpu_draw_line", 950, 30, 25, 625, gpu_brown), # Brown header background above the map.
		(overlay_set_alpha, reg1, 0xCC),
		(call_script, "script_gpu_draw_line", 950, 30, 25, 85, gpu_brown), # Brown footer background above the map.
		(overlay_set_alpha, reg1, 0xCC),
		
		
		
		(call_script, "script_gpu_create_game_button", "str_kmt_done_button", 500, 25, kmt_obj_button_done), # DONE Button @ 895, 35
		
		(call_script, "script_gpu_create_text_label", "str_kmt_title_holdings", 837, 693, kmt_obj_main_title, gpu_center_with_outline), # Estates of the Realm
		(overlay_set_color, reg1, gpu_white),
		(call_script, "script_gpu_resize_object", kmt_obj_main_title, 150),
		
		# script_gpu_create_checkbox     - pos_x, pos_y, label, storage_slot, value_slot
		(call_script, "script_gpu_create_checkbox", 30, 56, "str_kmt_opt_remove_background", kmt_obj_remove_backgrounds, kmt_val_remove_backgrounds),
		
		# Header
		(assign, ":pos_y", 655),
		(call_script, "script_gpu_draw_line", 950, 2, 25, ":pos_y", gpu_black),
		(store_sub, ":pos_y_titles", ":pos_y", 13),
		(call_script, "script_gpu_create_text_label", "str_kmt_title_names", ":x_names", ":pos_y_titles", 0, gpu_left_with_outline),
		(call_script, "script_gpu_resize_object", 0, kmt_text_size),
		(overlay_set_color, reg1, gpu_white),
		(call_script, "script_gpu_create_text_label", "str_kmt_title_relations", ":x_relations", ":pos_y_titles", 0, gpu_center_with_outline),
		(call_script, "script_gpu_resize_object", 0, kmt_text_size),
		(overlay_set_color, reg1, gpu_white),
		(call_script, "script_gpu_create_text_label", "str_kmt_title_towns", ":x_towns", ":pos_y_titles", 0, gpu_left_with_outline),
		(call_script, "script_gpu_resize_object", 0, kmt_text_size),
		(overlay_set_color, reg1, gpu_white),
		(call_script, "script_gpu_create_text_label", "str_kmt_title_castles", ":x_castles", ":pos_y_titles", 0, gpu_left_with_outline),
		(call_script, "script_gpu_resize_object", 0, kmt_text_size),
		(overlay_set_color, reg1, gpu_white),
		(call_script, "script_gpu_create_text_label", "str_kmt_title_villages", ":x_villages", ":pos_y_titles", 0, gpu_left_with_outline),
		(call_script, "script_gpu_resize_object", 0, kmt_text_size),
		(overlay_set_color, reg1, gpu_white),
		(call_script, "script_gpu_create_text_label", "str_kmt_title_friends", ":x_friends", ":pos_y_titles", 0, gpu_left_with_outline),
		(call_script, "script_gpu_resize_object", 0, kmt_text_size),
		(overlay_set_color, reg1, gpu_white),
		(call_script, "script_gpu_create_text_label", "str_kmt_title_enemies", ":x_enemies", ":pos_y_titles", 0, gpu_left_with_outline),
		(call_script, "script_gpu_resize_object", 0, kmt_text_size),
		(overlay_set_color, reg1, gpu_white),
		(val_sub, ":pos_y", 30),
		(call_script, "script_gpu_draw_line", 950, 2, 25, ":pos_y", gpu_black),
		
		# OBJ - Faction Menu
		(position_set_x, pos1, 190),
        (position_set_y, pos1, 675),
		(create_combo_label_overlay, reg1),
        (overlay_set_position, reg1, pos1),
		(assign, ":valid_kingdoms", 0),
		(try_for_range, ":kingdom_no", kingdoms_begin, kingdoms_end),
			(faction_slot_eq, ":kingdom_no", slot_faction_state, sfs_active),
			(str_store_faction_name, s21, ":kingdom_no"),
			(overlay_add_item, reg1, "@{s21}"),
			#(store_sub, ":storage_slot", ":kingdom_no", kingdoms_begin),
			(store_add, ":storage_slot", ":valid_kingdoms", kmt_val_kingdoms_begin),
			(troop_set_slot, kmt_objects, ":storage_slot", ":kingdom_no"),
			(val_add, ":valid_kingdoms", 1),
			# (overlay_add_item, reg1, "@Player's Kingdom"),
			# (overlay_add_item, reg1, "@Kingdom of Swadia"),
			# (overlay_add_item, reg1, "@Kingdom of Vaegirs"),
			# (overlay_add_item, reg1, "@Khergit Khanate"),
			# (overlay_add_item, reg1, "@Kingdom of Nords"),
			# (overlay_add_item, reg1, "@Kingdom of Rhodoks"),
			# (overlay_add_item, reg1, "@Sarranid Sultanate"),
			# (troop_set_slot, kmt_objects, kmt_obj_faction_menu, reg1),
		(try_end),
		(troop_set_slot, kmt_objects, kmt_obj_faction_menu, reg1),
		(troop_get_slot, ":value", kmt_objects, kmt_val_faction_menu),
		(overlay_set_val, reg1, ":value"),
		# Determine which faction we're looking at
		(store_add, ":faction_slot", ":value", kmt_val_kingdoms_begin),
		(troop_get_slot, ":faction_id", kmt_objects, ":faction_slot"),
		
		# Determine which faction we're looking at
		# (try_begin),
			# (troop_slot_eq, kmt_objects, kmt_val_faction_menu, kmt_kingdom_0),
			# (assign, ":faction_id", "fac_player_supporters_faction"),
		# (else_try),
			# (troop_slot_eq, kmt_objects, kmt_val_faction_menu, kmt_kingdom_1),
			# (assign, ":faction_id", "fac_kingdom_1"),
		# (else_try),
			# (troop_slot_eq, kmt_objects, kmt_val_faction_menu, kmt_kingdom_2),
			# (assign, ":faction_id", "fac_kingdom_2"),
		# (else_try),
			# (troop_slot_eq, kmt_objects, kmt_val_faction_menu, kmt_kingdom_3),
			# (assign, ":faction_id", "fac_kingdom_3"),
		# (else_try),
			# (troop_slot_eq, kmt_objects, kmt_val_faction_menu, kmt_kingdom_4),
			# (assign, ":faction_id", "fac_kingdom_4"),
		# (else_try),
			# (troop_slot_eq, kmt_objects, kmt_val_faction_menu, kmt_kingdom_5),
			# (assign, ":faction_id", "fac_kingdom_5"),
		# (else_try),
			# (troop_slot_eq, kmt_objects, kmt_val_faction_menu, kmt_kingdom_6),
			# (assign, ":faction_id", "fac_kingdom_6"),
		# (try_end),
		# (str_store_faction_name, s1, ":faction_id"),
		# (display_message, "@DEBUG (KMT): Selected faction is {s1}."),
		
		(call_script, "script_gpu_container_heading", 0, 115, 1000, 485, kmt_obj_main_container), # Scrolling container
		############### CONTAINER BEGIN ###############
			
			# Determine how many lords there are for spacing consideration.
			(assign, ":lord_count", 0),
			(try_for_range, ":troop_no", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
				(try_begin),
					(eq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),
					(assign, ":troop_check", "trp_player"),
					(assign, ":faction_no", "$players_kingdom"),
				(else_try),
					(assign, ":troop_check", ":troop_no"),
					(store_troop_faction, ":faction_no", ":troop_check"),
				(try_end),
				(eq, ":faction_no", ":faction_id"),
				(val_add, ":lord_count", 1),
			(try_end),
			(store_mul, ":container_length", ":lord_count", 265),
			
			(assign, ":pos_y", ":container_length"),
			(assign, ":city_count", 0),
			(assign, ":castle_count", 0),
			(assign, ":village_count", 0),
			(try_for_range, ":troop_check", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
				(assign, ":total_lines", 1),
				(try_begin),
					(eq, ":troop_check", "trp_kingdom_heroes_including_player_begin"),
					(assign, ":troop_no", "trp_player"),
					(assign, ":faction_no", "$players_kingdom"),
				(else_try),
					(assign, ":troop_no", ":troop_check"),
					(store_troop_faction, ":faction_no", ":troop_no"),
				(try_end),
				
				(eq, ":faction_no", ":faction_id"),
				
				# Add Lord Name
				(str_store_troop_name, s25, ":troop_no"),
				(call_script, "script_gpu_create_text_label", "str_kmt_s25", ":x_names", ":pos_y", 0, gpu_left),
				(call_script, "script_gpu_resize_object", 0, kmt_text_size),
				(overlay_set_color, reg1, 65547), # dark blue
			
				# Add Relation Information
				(call_script, "script_troop_get_player_relation", ":troop_no"),
				(call_script, "script_gpu_create_text_label", "str_kmt_relation_to_you_reg0", ":x_relations", ":pos_y", 0, gpu_center),
				(call_script, "script_gpu_resize_object", 0, kmt_text_size),
				# (try_begin),
					# (ge, reg0, 11),
					# (overlay_set_color, reg1, gpu_green),
				# (else_try),
					# (lt, reg0, -5),
					# (overlay_set_color, reg1, gpu_red),
				# (try_end),
				# (try_begin),
					# (faction_get_slot, ":troop_king", ":faction_no", slot_faction_leader),
					# (neq, ":troop_king", "trp_player"),
					# (assign, ":total_lines", 2),
					# (store_sub, ":pos_y_line_2", ":pos_y", kmt_line_step),
					# (call_script, "script_gpu_create_text_label", "str_kmt_relation_with_king_reg1", ":x_relations", ":pos_y_line_2", 0, gpu_left),
					# (call_script, "script_gpu_resize_object", 0, kmt_text_size),
				# (try_end),
				
				# Determine which cities are owned by troop_no
				(assign, ":line_count", 0),
				(try_for_range, ":center_no", towns_begin, towns_end),
					(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
					(str_store_party_name, s25, ":center_no"),
					(store_mul, ":y_adj", ":line_count", kmt_line_step),
					(store_sub, ":y_line", ":pos_y", ":y_adj"),
					(call_script, "script_gpu_create_text_label", "str_kmt_s25", ":x_towns", ":y_line", 0, gpu_left),
					(call_script, "script_gpu_resize_object", 0, kmt_text_size),
					(val_add, ":line_count", 1),
					(val_add, ":city_count", 1),
					(lt, ":total_lines", ":line_count"),
					(assign, ":total_lines", ":line_count"),
				(try_end),
				
				# Determine which castles are owned by troop_no
				(assign, ":line_count", 0),
				(try_for_range, ":center_no", castles_begin, castles_end),
					(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
					(str_store_party_name, s25, ":center_no"),
					(store_mul, ":y_adj", ":line_count", kmt_line_step),
					(store_sub, ":y_line", ":pos_y", ":y_adj"),
					(call_script, "script_gpu_create_text_label", "str_kmt_s25", ":x_castles", ":y_line", 0, gpu_left),
					(call_script, "script_gpu_resize_object", 0, kmt_text_size),
					(val_add, ":line_count", 1),
					(val_add, ":castle_count", 1),
					(lt, ":total_lines", ":line_count"),
					(assign, ":total_lines", ":line_count"),
				(try_end),
				
				# Determine which villages are owned by troop_no
				(assign, ":line_count", 0),
				(try_for_range, ":center_no", villages_begin, villages_end),
					(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
					(str_store_party_name, s25, ":center_no"),
					(store_mul, ":y_adj", ":line_count", kmt_line_step),
					(store_sub, ":y_line", ":pos_y", ":y_adj"),
					(call_script, "script_gpu_create_text_label", "str_kmt_s25", ":x_villages", ":y_line", 0, gpu_left),
					(call_script, "script_gpu_resize_object", 0, kmt_text_size),
					(val_add, ":line_count", 1),
					(val_add, ":village_count", 1),
					(lt, ":total_lines", ":line_count"),
					(assign, ":total_lines", ":line_count"),
				(try_end),
				
				# Determine which allies the lord has.
				(assign, ":line_count", 0),
				(try_for_range, ":lord_no", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					(neq, ":lord_no", ":troop_no"),
					(call_script, "script_troop_get_relation_with_troop", ":lord_no", ":troop_no"),
					(assign, ":relation_with_troop", reg0),
					(ge, ":relation_with_troop", kmt_ai_friend_threshold),
					
					(str_store_troop_name, s25, ":lord_no"),
					(store_mul, ":y_adj", ":line_count", kmt_line_step),
					(store_sub, ":y_line", ":pos_y", ":y_adj"),
					(call_script, "script_gpu_create_text_label", "str_kmt_s25", ":x_friends", ":y_line", 0, gpu_left),
					(call_script, "script_gpu_resize_object", 0, kmt_text_size),
					(val_add, ":line_count", 1),
					(lt, ":total_lines", ":line_count"),
					(assign, ":total_lines", ":line_count"),
				(try_end),
				
				# Determine which enemies the lord has.
				(assign, ":line_count", 0),
				(try_for_range, ":lord_no", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
					(neq, ":lord_no", ":troop_no"),
					(call_script, "script_troop_get_relation_with_troop", ":lord_no", ":troop_no"),
					(assign, ":relation_with_troop", reg0),
					(lt, ":relation_with_troop", kmt_ai_enemy_threshold),
					
					(str_store_troop_name, s25, ":lord_no"),
					(store_mul, ":y_adj", ":line_count", kmt_line_step),
					(store_sub, ":y_line", ":pos_y", ":y_adj"),
					(call_script, "script_gpu_create_text_label", "str_kmt_s25", ":x_enemies", ":y_line", 0, gpu_left),
					(call_script, "script_gpu_resize_object", 0, kmt_text_size),
					(val_add, ":line_count", 1),
					(lt, ":total_lines", ":line_count"),
					(assign, ":total_lines", ":line_count"),
				(try_end),
				
				
				
				(store_mul, ":pos_y_adjust", ":total_lines", kmt_line_step),
				(val_sub, ":pos_y", ":pos_y_adjust"),
				(call_script, "script_gpu_draw_line", 946, 2, 27, ":pos_y", 1315860),
				(val_sub, ":pos_y", kmt_line_step),
			(try_end), # End of troop_no cycle
		############### CONTAINER END ###############	
		(set_container_overlay, -1),
		
		# Footer
		(assign, ":pos_y", 115),
		(call_script, "script_gpu_draw_line", 950, 2, 25, ":pos_y", gpu_black),
		(store_sub, ":pos_y_titles", ":pos_y", 13),
		(assign, reg0, ":lord_count"),
		(call_script, "script_gpu_create_text_label", "str_kmt_footer_lords", ":x_names", ":pos_y_titles", 0, gpu_left_with_outline),
		(call_script, "script_gpu_resize_object", 0, kmt_text_size),
		(overlay_set_color, reg1, gpu_white),
		(assign, reg0, ":city_count"),
		(call_script, "script_gpu_create_text_label", "str_kmt_footer_towns", ":x_towns", ":pos_y_titles", 0, gpu_left_with_outline),
		(call_script, "script_gpu_resize_object", 0, kmt_text_size),
		(overlay_set_color, reg1, gpu_white),
		(assign, reg0, ":castle_count"),
		(call_script, "script_gpu_create_text_label", "str_kmt_footer_castles", ":x_castles", ":pos_y_titles", 0, gpu_left_with_outline),
		(call_script, "script_gpu_resize_object", 0, kmt_text_size),
		(overlay_set_color, reg1, gpu_white),
		(assign, reg0, ":village_count"),
		(call_script, "script_gpu_create_text_label", "str_kmt_footer_villages", ":x_villages", ":pos_y_titles", 0, gpu_left_with_outline),
		(call_script, "script_gpu_resize_object", 0, kmt_text_size),
		(overlay_set_color, reg1, gpu_white),
		(val_sub, ":pos_y", 30),
		(call_script, "script_gpu_draw_line", 950, 2, 25, ":pos_y", gpu_black),
		
		(call_script, "script_gpu_draw_line", 2, 570, 25, 85, gpu_black), # left border
		(call_script, "script_gpu_draw_line", 2, 570, 973, 85, gpu_black), # right border
		
		#(call_script, "script_gpu_prsnt_panel_color_chooser", 250, 475),
      ]),
	
    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
		
		(try_begin),
			(ge, kmt_debug, 2),
			(assign, reg1, ":object"),
			(assign, reg2, ":value"),
			(display_message, "@DEBUG (KMT): Object clicked is {reg1}.  Value is {reg2}."),
		(try_end),
		
		(try_begin), ####### DONE BUTTON #######
			(troop_slot_eq, kmt_objects, kmt_obj_button_done, ":object"),
			(presentation_set_duration, 0),
			
		(else_try), ####### REMOVE BACKGROUNDS CHECKBOX #######
			(troop_slot_eq, kmt_objects, kmt_obj_remove_backgrounds, ":object"),
			(troop_set_slot, kmt_objects, kmt_val_remove_backgrounds, ":value"),
			#(troop_get_slot, reg1, kmt_objects, kmt_val_remove_backgrounds),
			#(display_message, "@Objects should be {reg1?hidden:displayed}."),
			(start_presentation, "prsnt_kmt_lord_holdings"),
			
		(else_try), ####### FACTION MENU #######
			(troop_slot_eq, kmt_objects, kmt_obj_faction_menu, ":object"),
			(troop_set_slot, kmt_objects, kmt_val_faction_menu, ":value"),
			(start_presentation, "prsnt_kmt_lord_holdings"),
			
		(try_end),

		# (call_script, "script_gpu_events_panel_color_chooser", ":object", ":value"),
		# (try_begin),
			# (eq, reg0, 1),
			# (start_presentation, "prsnt_kmt_lord_holdings"),
		# (try_end),
      ]),
	  
	# (ti_on_presentation_mouse_press,
      # [
        # (store_trigger_param_1, ":object"),
        # (store_trigger_param_2, ":value"),
		
		# (call_script, "script_gpu_mouseclick_panel_color_chooser", ":object", ":value"),

      # ]),
    ]),

 ]
	
def modmerge_presentations(orig_presentations, check_duplicates = False):
    if( not check_duplicates ):
        orig_presentations.extend(presentations) # Use this only if there are no replacements (i.e. no duplicated item names)
    else:
    # Use the following loop to replace existing entries with same id
        for i in range (0,len(presentations)-1):
          find_index = find_object(orig_presentations, presentations[i][0]); # find_object is from header_common.py
          if( find_index == -1 ):
            orig_presentations.append(presentations[i])
          else:
            orig_presentations[find_index] = presentations[i]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "presentations"
        orig_presentations = var_set[var_name_1]
        modmerge_presentations(orig_presentations)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)