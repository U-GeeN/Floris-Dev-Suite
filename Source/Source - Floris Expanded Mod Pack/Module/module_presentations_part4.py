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

presentations_part4 = [

	##	Floris Bank End
	  
	## Floris - Trade Ledger
  ("trade_ledger_basic", 0, mesh_game_log_window, [ #mesh_game_log_window
    (ti_on_presentation_load,
     [(set_fixed_point_multiplier, 1000),
	 
	  (assign, ":pref_date", "$g_date"), #Floris Date fix
	  (assign, "$g_date",  1), #Floris Date fix
	 
	  (create_text_overlay, reg0, "@Merchant Ledger", tf_center_justify|tf_single_line|tf_with_outline),
      (overlay_set_color, reg0, 0xFFFFFFFF),
      (position_set_x, pos1, 1500),
      (position_set_y, pos1, 1500),
      (overlay_set_size, reg0, pos1),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 680),
      (overlay_set_position, reg0, pos1),

	  (create_text_overlay, reg0, "@____Assessed Profit by Subtitle Here", tf_center_justify|tf_single_line), #Subtitle
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 650),
      (overlay_set_position, reg0, pos1),
	  
	  ##Ledger Pane
      (str_clear, s0),
      (create_text_overlay, "$g_presentation_obj_bugdet_report_container", s0, tf_scrollable_style_2),
      (position_set_x, pos1, 50),
      (position_set_y, pos1, 100),
      (overlay_set_position, "$g_presentation_obj_bugdet_report_container", pos1),
      (position_set_x, pos1, 600),
      (position_set_y, pos1, 500), 
      (overlay_set_area_size, "$g_presentation_obj_bugdet_report_container", pos1),
      (set_container_overlay, "$g_presentation_obj_bugdet_report_container"),
	  
	  (troop_get_slot, ":ledger", "trp_player", slot_troop_trade_ledger),
	  (ge, ":ledger", 1),
	  (call_script, "script_cf_array_is_array", ":ledger"),
	  (call_script, "script_array_get_element", ":ledger", date_array),
	  (assign, ":date_array", reg0),
	  (call_script, "script_array_get_element", ":ledger", town_array),
	  (assign, ":town_array", reg0),
	  (call_script, "script_array_get_element", ":ledger", item_array),
	  (assign, ":item_array", reg0),
	  (call_script, "script_array_get_element", ":ledger", destination_array),
	  (assign, ":destination_array", reg0),
	  (call_script, "script_array_get_element", ":ledger", profit_array),
	  (assign, ":profit_array", reg0),
		
	  (call_script, "script_array_get_size", ":date_array"),
	  (assign, ":ledger_length", reg0),
	  (store_mul, ":cur_y", ":ledger_length", 30),

	  (try_begin),
	      (eq, reg60, 0), #Default (Chronological) View
		  (assign, ":next_entry", 0),
		  (try_for_range, ":i", 0, ":ledger_length"),
			(eq, ":i", ":next_entry"),
			
			(call_script, "script_cf_array_get_element", ":date_array", ":i"),
			(assign, ":date", reg0),
			(str_store_date, s0, ":date"),
			(call_script, "script_cf_array_get_element", ":town_array", ":i"),
			(assign, ":town", reg0),
			(str_store_party_name, s1, ":town"),
			#DISPLAY DAY, TOWN in one overlay
			(create_text_overlay, reg0, "@{s0}, products from {s1}:"),
			(position_set_x, pos1, 1000),
			(position_set_y, pos1, 1000),
			(overlay_set_size, reg0, pos1),
			(position_set_x, pos1, 25),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),
			
			(assign, ":end", ":ledger_length"),
			(assign, ":end_index", ":end"), #Should get overwritten in below loop
			#(store_add, ":next_entry", ":i", 1), #Should get overwritten in below loop #necessary fail-safe?
			(try_for_range, ":n", ":i", ":end"), #This loop finds the end of the current set of entries
				(call_script, "script_cf_array_get_element", ":date_array", ":n"),
				(assign, ":test_date", reg0),
				(call_script, "script_cf_array_get_element", ":town_array", ":n"),
				(this_or_next|neq, ":town", reg0), #Once the date OR the town change, it is a new entry
				(neq, ":date", ":test_date"),
				(assign, ":end_index", ":n"),
				(assign, ":next_entry", ":n"),
				(assign, ":end", 0), #Break
			(try_end),

			(assign, ":line_count", 0),
			(str_clear, s3),
			(try_for_range, ":n", ":i", ":end_index"),
			    (val_add, ":line_count", 1),
				(call_script, "script_cf_array_get_element", ":item_array", ":n"),
				(str_store_item_name, s1, reg0),
				(call_script, "script_cf_array_get_element", ":destination_array", ":n"),
				(str_store_party_name, s2, reg0),
				(call_script, "script_cf_array_get_element", ":profit_array", ":n"),
				(str_store_string, s3, "@^{s1} sold in {s2} would earn {reg0} denars.{s3}"),	
			(try_end), #Item Loop	
			
			(val_mul, ":line_count", 14),
			(val_sub, ":cur_y", ":line_count"),
			#CREATE ITEM, DEST, PROFIT for all items in one overlay
			(create_text_overlay, reg0, s3),
			(position_set_x, pos1, 800),
			(position_set_y, pos1, 800),
			(overlay_set_size, reg0, pos1),
			(position_set_x, pos1, 50),
			(position_set_y, pos1, ":cur_y"),
			(overlay_set_position, reg0, pos1),
			(val_sub, ":cur_y", 30),			
		  (try_end), #Town Entry Loop
		  (store_sub, reg0, "$g_presentation_obj_bugdet_report_container", 1),
		  (overlay_set_text, reg0, "@__Assessed Profit by Log Entry Date"),
	    (else_try),
	      (eq, reg60, 1), #Origin View
		  (try_for_range, ":cur_town", towns_begin, towns_end),
		    (assign, ":line_count", 0),
			(assign, ":profit", 0),
			(try_for_range, ":i", 0, ":ledger_length"),
				(call_script, "script_cf_array_get_element", ":town_array", ":i"),
				(eq, ":cur_town", reg0),
				(call_script, "script_cf_array_get_element", ":profit_array", ":i"),
				(val_add, ":profit", reg0),	
				(val_add, ":line_count", 1),
			(try_end),
			(val_max, ":line_count", 1), #Ensure no Div-by-0
			(val_div, ":profit", ":line_count"),
			(troop_set_slot, "trp_temp_array_b", ":cur_town", ":profit"),
		  (try_end),
		  (assign, ":max_profit", 0),
		  (try_for_range, ":i", towns_begin, towns_end),
			(troop_get_slot, reg0, "trp_temp_array_b", ":i"),
			(lt, ":max_profit", reg0),
			(assign, ":max_profit", reg0),
		  (try_end),
		  (val_add, ":max_profit", 1),
		  (try_for_range_backwards, ":profit", 0, ":max_profit"),
			(try_for_range, ":cur_town", towns_begin, towns_end),
				(troop_slot_eq, "trp_temp_array_b", ":cur_town", ":profit"),

				(assign, ":line_count", 0),
				(str_clear, s3),
				(try_for_range, ":i", 0, ":ledger_length"),
					(call_script, "script_cf_array_get_element", ":town_array", ":i"),
					(eq, ":cur_town", reg0),
					(val_add, ":line_count", 1),

					(call_script, "script_cf_array_get_element", ":date_array", ":i"),
					(str_store_date, s0, reg0),
					(call_script, "script_cf_array_get_element", ":item_array", ":i"),
					(str_store_item_name, s1, reg0),
					(call_script, "script_cf_array_get_element", ":destination_array", ":i"),
					(str_store_party_name, s2, reg0),
					(call_script, "script_cf_array_get_element", ":profit_array", ":i"),
					(str_store_string, s3, "@^{s1} sold in {s2} would earn {reg0} denars (as of {s0}).{s3}"),			
				(try_end), #Entry Loop
				(ge, ":line_count", 1),
				
				#DISPLAY TOWN header in one overlay
				(str_store_party_name, s1, ":cur_town"),
				(str_store_string, s1, "@Production in {s1}"),
				(create_text_overlay, reg0, s1),
				(position_set_x, pos1, 1000),
				(position_set_y, pos1, 1000),
				(overlay_set_size, reg0, pos1),
				(position_set_x, pos1, 25),
				(position_set_y, pos1, ":cur_y"),
				(overlay_set_position, reg0, pos1),

				
				(val_mul, ":line_count", 14),
				(val_sub, ":cur_y", ":line_count"),
				
				#ITEM, DEST, PROFIT, and DATE for all items in one overlay
				(create_text_overlay, reg0, s3),
				(position_set_x, pos1, 800),
				(position_set_y, pos1, 800),
				(overlay_set_size, reg0, pos1),
				(position_set_x, pos1, 50),
				(position_set_y, pos1, ":cur_y"),
				(overlay_set_position, reg0, pos1),
				(val_sub, ":cur_y", 30),	
		  	(try_end), #Town-Profit Loop
		  (try_end), #Profit Values Loop
		  
		  (store_sub, reg0, "$g_presentation_obj_bugdet_report_container", 1),
		  (overlay_set_text, reg0, "@Assessed Profit by Town of Production"),
		(else_try),
		  (eq, reg60, 2), #Destination View
		  (try_for_range, ":cur_town", towns_begin, towns_end),
		    (assign, ":line_count", 0),
			(assign, ":profit", 0),
			(try_for_range, ":i", 0, ":ledger_length"),
				(call_script, "script_cf_array_get_element", ":destination_array", ":i"),
				(eq, ":cur_town", reg0),
				(call_script, "script_cf_array_get_element", ":profit_array", ":i"),
				(val_add, ":profit", reg0),	
				(val_add, ":line_count", 1),
			(try_end),
			(val_max, ":line_count", 1), #Ensure no Div-by-0
			(val_div, ":profit", ":line_count"),
			(troop_set_slot, "trp_temp_array_b", ":cur_town", ":profit"),
		  (try_end),
		  (assign, ":max_profit", 0),
		  (try_for_range, ":i", towns_begin, towns_end),
			(troop_get_slot, reg0, "trp_temp_array_b", ":i"),
			(lt, ":max_profit", reg0),
			(assign, ":max_profit", reg0),
		  (try_end),
		  (val_add, ":max_profit", 1),
		  (try_for_range_backwards, ":profit", 0, ":max_profit"),
			(try_for_range, ":cur_town", towns_begin, towns_end),
				(troop_slot_eq, "trp_temp_array_b", ":cur_town", ":profit"),

				(assign, ":line_count", 0),
				(str_clear, s3),
				(try_for_range, ":i", 0, ":ledger_length"),
					(call_script, "script_cf_array_get_element", ":destination_array", ":i"),
					(eq, ":cur_town", reg0),
					(val_add, ":line_count", 1),

					(call_script, "script_cf_array_get_element", ":date_array", ":i"),
					(str_store_date, s0, reg0),
					(call_script, "script_cf_array_get_element", ":item_array", ":i"),
					(str_store_item_name, s1, reg0),
					(call_script, "script_cf_array_get_element", ":town_array", ":i"),
					(str_store_party_name, s2, reg0),
					(call_script, "script_cf_array_get_element", ":profit_array", ":i"),
					(str_store_string, s3, "@^{s1} purchased in {s2} would earn {reg0} denars (as of {s0}).{s3}"),			
				(try_end), #Entry Loop
				(ge, ":line_count", 1),
				
				#DISPLAY TOWN header in one overlay
				(str_store_party_name, s1, ":cur_town"),
				(str_store_string, s1, "@Demand in {s1}"),
				(create_text_overlay, reg0, s1),
				(position_set_x, pos1, 1000),
				(position_set_y, pos1, 1000),
				(overlay_set_size, reg0, pos1),
				(position_set_x, pos1, 25),
				(position_set_y, pos1, ":cur_y"),
				(overlay_set_position, reg0, pos1),

				(val_mul, ":line_count", 14),
				(val_sub, ":cur_y", ":line_count"),
				
				#ITEM, DEST, PROFIT, and DATE for all items in one overlay
				(create_text_overlay, reg0, s3),
				(position_set_x, pos1, 800),
				(position_set_y, pos1, 800),
				(overlay_set_size, reg0, pos1),
				(position_set_x, pos1, 50),
				(position_set_y, pos1, ":cur_y"),
				(overlay_set_position, reg0, pos1),
				(val_sub, ":cur_y", 30),	
		  	(try_end), #Town-Profit Loop
		  (try_end), #Profit Values Loop
		  (store_sub, reg0, "$g_presentation_obj_bugdet_report_container", 1),
		  (overlay_set_text, reg0, "@Assessed Profit by Town of Demand"),
		(else_try),
		  (eq, reg60, 3), #Item View
		  (try_for_range, ":cur_item", trade_goods_begin, trade_goods_end),
		    (assign, ":line_count", 0),
			(assign, ":profit", 0),
			(try_for_range, ":i", 0, ":ledger_length"),
				(call_script, "script_cf_array_get_element", ":item_array", ":i"), 
				(eq, ":cur_item", reg0),
				(call_script, "script_cf_array_get_element", ":profit_array", ":i"),
				(val_add, ":profit", reg0),	
				(val_add, ":line_count", 1),
			(try_end),
			(val_max, ":line_count", 1), #Ensure no Div-by-0
			(val_div, ":profit", ":line_count"),
			(troop_set_slot, "trp_temp_array_b", ":cur_item", ":profit"),
		  (try_end),
		  (assign, ":max_profit", 0),
		  (try_for_range, ":i", trade_goods_begin, trade_goods_end),
			(troop_get_slot, reg0, "trp_temp_array_b", ":i"),
			(lt, ":max_profit", reg0),
			(assign, ":max_profit", reg0),
		  (try_end),
		  (val_add, ":max_profit", 1),
		  (try_for_range_backwards, ":profit", 0, ":max_profit"),
			(try_for_range, ":cur_item", trade_goods_begin, trade_goods_end),
				(troop_slot_eq, "trp_temp_array_b", ":cur_item", ":profit"),

				(assign, ":line_count", 0),
				(str_clear, s3),
				(try_for_range, ":i", 0, ":ledger_length"),
					(call_script, "script_cf_array_get_element", ":item_array", ":i"),
					(eq, ":cur_item", reg0),
					(val_add, ":line_count", 1),

					(call_script, "script_cf_array_get_element", ":date_array", ":i"),
					(str_store_date, s0, reg0),
					(call_script, "script_cf_array_get_element", ":town_array", ":i"),
					(str_store_party_name, s1, reg0),
					(call_script, "script_cf_array_get_element", ":destination_array", ":i"),
					(str_store_party_name, s2, reg0),
					(call_script, "script_cf_array_get_element", ":profit_array", ":i"),
					(str_store_string, s3, "@^Buy in: {s1} - sell in: {s2} for {reg0} denars profit (as of {s0}).{s3}"),			
				(try_end), #Entry Loop
				(ge, ":line_count", 1),
				
				#DISPLAY ITEM header in one overlay
				(str_store_item_name, s1, ":cur_item"),
				(str_store_string, s1, "@Supply and Demand of {s1}"),
				(create_text_overlay, reg0, s1),
				(position_set_x, pos1, 1000),
				(position_set_y, pos1, 1000),
				(overlay_set_size, reg0, pos1),
				(position_set_x, pos1, 25),
				(position_set_y, pos1, ":cur_y"),
				(overlay_set_position, reg0, pos1),

				(val_mul, ":line_count", 14),
				(val_sub, ":cur_y", ":line_count"),
				
				#Origin, DEST, PROFIT, and DATE for all towns in one overlay
				(create_text_overlay, reg0, s3),
				(position_set_x, pos1, 800),
				(position_set_y, pos1, 800),
				(overlay_set_size, reg0, pos1),
				(position_set_x, pos1, 50),
				(position_set_y, pos1, ":cur_y"),
				(overlay_set_position, reg0, pos1),
				(val_sub, ":cur_y", 30),	
		  	(try_end), #Item-Profit Loop
          (try_end), #Profit Values Loop
		  (store_sub, reg0, "$g_presentation_obj_bugdet_report_container", 1),
		  (overlay_set_text, reg0, "@____Assessed Profit by Trade Good"),
		(else_try),
		  (eq, reg60, 4),
		  (assign, ":cur_y", 750),
		  
		  (create_text_overlay, reg0, "@Trim ledger entries older than:______________days:"),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 50),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  
		  (create_number_box_overlay, "$g_presentation_obj_custom_battle_designer_17", 3, 1001),
		  (position_set_x, pos1, 285),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, "$g_presentation_obj_custom_battle_designer_17", pos1),
		  (overlay_set_val, "$g_presentation_obj_custom_battle_designer_17", 3),
		  (val_sub, ":cur_y", 30),
		  
		  (create_button_overlay, reg0, "@Remove entries."),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 290),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  (val_sub, ":cur_y", 40),
		  
		  (create_text_overlay, reg0, "@Trim ledger entries covering the following trade good:"),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 50),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  (val_sub, ":cur_y", 40),
		  
		  (create_slider_overlay, "$g_presentation_obj_custom_battle_designer_16", trade_goods_begin, trade_goods_end),
		  (position_set_x, pos1, 200),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, "$g_presentation_obj_custom_battle_designer_16", pos1),
				
		  (create_text_overlay, reg0, "@Use slider to choose item"),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 350),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  (val_sub, ":cur_y", 30),
		  
		  (create_button_overlay, reg0, "@Remove entries."),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 290),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  (val_sub, ":cur_y", 40),
		  
		  (create_text_overlay, reg0, "@Trim ledger entries for goods tied to this town:"),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 50),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  (val_sub, ":cur_y", 40),
		  
		  (create_slider_overlay, "$g_presentation_obj_custom_battle_designer_15", towns_begin, towns_end),
		  (position_set_x, pos1, 200),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, "$g_presentation_obj_custom_battle_designer_15", pos1),
				
		  (create_text_overlay, reg0, "@Use slider to choose town"),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 350),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  (val_sub, ":cur_y", 30),
		  		  
		  (create_button_overlay, reg0, "@Remove entries (Production)."),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 290),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  (val_sub, ":cur_y", 20),
		  
		  (create_button_overlay, reg0, "@Remove entries (Demand)."),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 290),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  (val_sub, ":cur_y", 40),
		  
		  (create_text_overlay, reg0, "@Trim ledger entries with less than:______________denar profit:"),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 50),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  
		  (create_number_box_overlay, "$g_presentation_obj_custom_battle_designer_14", 10, 1001),
		  (position_set_x, pos1, 305),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, "$g_presentation_obj_custom_battle_designer_14", pos1),
		  (overlay_set_val, "$g_presentation_obj_custom_battle_designer_14", 10),
		  (val_sub, ":cur_y", 30),
		  
		  (create_button_overlay, reg0, "@Remove entries."),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 290),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  (val_sub, ":cur_y", 60),
		  		  
		  (create_text_overlay, reg0, "@Ask about the potential profit of the following items^____every time you assess prices in a marketplace:"),
		  (position_set_x, pos1, 900),
		  (position_set_y, pos1, 900),
		  (overlay_set_size, reg0, pos1),
		  (position_set_x, pos1, 50),
		  (position_set_y, pos1, ":cur_y"),
		  (overlay_set_position, reg0, pos1),
		  (val_sub, ":cur_y", 40),
		  
		  (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
          (assign, ":max_skill", reg0),
		  (val_max, ":max_skill", 1), #at least 1
		  (store_add, ":array_size", ":max_skill", custom_assess_begin),
		  (assign, ":ledger_length", ":array_size"),
		  (try_begin),
		    (call_script, "script_array_get_size", ":ledger"),
			(lt, reg0, ":array_size"), #array not big enough
			(val_sub, ":array_size", reg0),
			(try_for_range, ":unused", 0, ":array_size"),
			    (call_script, "script_array_pushback", ":ledger", -1), #Increase array's size
			(try_end),		  
		  (try_end),
		  
		  (try_for_range, ":i", custom_assess_begin, ":ledger_length"),
				(create_slider_overlay, ":overlay", trade_goods_begin, trade_goods_end),
				(position_set_x, pos1, 200),
				(position_set_y, pos1, ":cur_y"),
				(overlay_set_position, ":overlay", pos1),
				
				(create_text_overlay, reg0, s0),
				(position_set_x, pos1, 900),
				(position_set_y, pos1, 900),
				(overlay_set_size, reg0, pos1),
				(position_set_x, pos1, 350),
				(position_set_y, pos1, ":cur_y"),
				(overlay_set_position, reg0, pos1),
				(val_sub, ":cur_y", 40),
				
				(troop_set_slot, "trp_temp_array_c", ":i", ":overlay"),
				(try_begin),
				    (call_script, "script_cf_array_get_element", ":ledger", ":i"),
					(is_between, reg0, trade_goods_begin, trade_goods_end),
					(str_store_item_name, s0, reg0),
					(overlay_set_val, ":overlay", reg0),
				(else_try),
				    (str_store_string, s0, "@Use slider to choose item"),
				(try_end),
				(val_add, ":overlay", 1),
				(overlay_set_text, ":overlay", s0),
		  (try_end),
		   
		  (store_sub, reg0, "$g_presentation_obj_bugdet_report_container", 1),
		  (overlay_set_text, reg0, "@___________Log Entry Options"),
	  (try_end),	  
	  (set_container_overlay, -1),
	  
	  ##Note Pad Pane
	  (create_mesh_overlay, reg0, "mesh_white_plane"),
	  (overlay_set_alpha, reg0, 0x30),
	  (position_set_x, pos1, 11550),
	  (position_set_y, pos1, 19500),
	  (overlay_set_size, reg0, pos1),
	  (position_set_x, pos1, 700),
	  (position_set_y, pos1, 210),
	  (overlay_set_position, reg0, pos1),	  
	  
	  (str_store_party_name, s0, ":date_array"),
	  (create_text_overlay, "$g_presentation_obj_custom_battle_designer_18", s0, tf_scrollable_style_2),
	  (position_set_x, pos1, 800),
	  (position_set_y, pos1, 800),
	  (overlay_set_size, "$g_presentation_obj_custom_battle_designer_18", pos1),
	  (position_set_x, pos1, 700),
	  (position_set_y, pos1, 210),
	  (overlay_set_position, "$g_presentation_obj_custom_battle_designer_18", pos1),
	  (position_set_x, pos1, 230),
	  (position_set_y, pos1, 390),
	  (overlay_set_area_size, "$g_presentation_obj_custom_battle_designer_18", pos1),
	  
	  (create_button_overlay, reg0, "@Add Note"),
	  (position_set_x, pos1, 900),
	  (position_set_y, pos1, 900),
	  (overlay_set_size, reg0, pos1),
	  (position_set_x, pos1, 700),
      (position_set_y, pos1, 150),
	  (overlay_set_position, reg0, pos1),	
	  
	  (create_button_overlay, reg0, "@Clear Notes"),
	  (position_set_x, pos1, 900),
	  (position_set_y, pos1, 900),
	  (overlay_set_size, reg0, pos1),
	  (position_set_x, pos1, 830),
      (position_set_y, pos1, 150),
	  (overlay_set_position, reg0, pos1),
    
	  (create_simple_text_box_overlay, reg0),
	  (position_set_x, pos1, 228),
	  (position_set_y, pos1, 800),
	  (overlay_set_size, reg0, pos1),
	  (position_set_x, pos1, 700),
	  (position_set_y, pos1, 180),
	  (overlay_set_position, reg0, pos1),

	  (create_text_overlay, reg0, "@Use a /\ (caret) for a line break."), # \%^
	  (position_set_x, pos1, 700),
	  (position_set_y, pos1, 700),
	  (overlay_set_size, reg0, pos1),
	  (position_set_x, pos1, 730),
	  (position_set_y, pos1, 120),
	  (overlay_set_position, reg0, pos1),	  
	  
	  ##Bottom Row Buttons	  
	  (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_19", "@Chronological Log", 0),
      (position_set_x, pos1, 260),
      (position_set_y, pos1, 10),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_19", pos1),
	  
	  (create_game_button_overlay, reg0, "@Production Towns", 0),
      (position_set_x, pos1, 420),
      (position_set_y, pos1, 10),
      (overlay_set_position, reg0, pos1),	  
	  	  
	  (create_game_button_overlay, reg0, "@Purchasing Towns", 0),
      (position_set_x, pos1, 580),
      (position_set_y, pos1, 10),
      (overlay_set_position, reg0, pos1),		  
	  	  
	  (create_game_button_overlay, reg0, "@Trade Goods", 0),
      (position_set_x, pos1, 740),
      (position_set_y, pos1, 10),
      (overlay_set_position, reg0, pos1),	
	  
	  (create_game_button_overlay, reg0, "@Manage Ledger", 0), #On Far Left
      (position_set_x, pos1, 100),
      (position_set_y, pos1, 10),
      (overlay_set_position, reg0, pos1),

	  (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_20", "@Done", 0),
      (position_set_x, pos1, 900),
      (position_set_y, pos1, 10),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_20", pos1),
	  
	  (str_clear, s0),
	  (assign, reg56, 10),
	  (assign, reg57, -1),
	  (assign, reg58, -1),
	  (assign, reg59, 3),
	  (assign, "$g_date", ":pref_date"), #Floris Date fix
	  (presentation_set_duration, 999999),
      ]),
	(ti_on_presentation_run,
      [	
		(key_clicked, key_escape),
		(try_begin),
			(eq, reg60, 4),#Leaving Config/Options Page
			(call_script, "script_cf_trade_ledger_custom_assess_duplicates"),
	    (try_end),
		(presentation_set_duration, 0),
      ]),
    (ti_on_presentation_event_state_change,
     [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),
	    (try_begin),
		   (eq, ":object", "$g_presentation_obj_custom_battle_designer_20"),
		   (try_begin),
			    (eq, reg60, 4),#Leaving Config/Options Page
				(call_script, "script_cf_trade_ledger_custom_assess_duplicates"),
		   (try_end),
		   (presentation_set_duration, 0),
		(else_try),  #Add Note
		    (store_add, ":overlay", "$g_presentation_obj_custom_battle_designer_18", 1),
			(eq, ":object", ":overlay"),
			(neg|str_is_empty, s0),
			(troop_get_slot, ":ledger", "trp_player", slot_troop_trade_ledger),
	        (ge, ":ledger", 1),
		    (call_script, "script_array_get_element", ":ledger", 0),
			(str_store_party_name, s1, reg0),
			(str_store_string, s1, "@{s1}^+{s0}"),
			(party_set_name, reg0, s1),
			(overlay_set_text, "$g_presentation_obj_custom_battle_designer_18", s1),
			(str_clear, s0),
			(val_add, ":overlay", 2),
			(overlay_set_text, ":overlay", s0),
		(else_try), #Clear Notes
		    (store_add, ":overlay", "$g_presentation_obj_custom_battle_designer_18", 2),
			(eq, ":object", ":overlay"),
			(troop_get_slot, ":ledger", "trp_player", slot_troop_trade_ledger),
	        (ge, ":ledger", 1),
		    (call_script, "script_array_get_element", ":ledger", 0),
			(str_clear, s0),
			(party_set_name, reg0, s0),
			(overlay_set_text, "$g_presentation_obj_custom_battle_designer_18", s0),
		(else_try), #Log View Changes
			(is_between, ":object", "$g_presentation_obj_custom_battle_designer_19", "$g_presentation_obj_custom_battle_designer_20"),
			(store_sub, ":view", ":object", "$g_presentation_obj_custom_battle_designer_19"), #Results in a value 0-4
			(try_begin),
			    (eq, reg60, 4), #Leaving Config/Options Page
				(call_script, "script_cf_trade_ledger_custom_assess_duplicates"),
			(try_end),
			(assign, reg60, ":view"),
			(start_presentation, "prsnt_trade_ledger_basic"),
		(else_try), #Set Date Threshold for Removal
		    (eq, ":object", "$g_presentation_obj_custom_battle_designer_17"),
			(assign, reg59, ":value"),
		(else_try), #Remove Entries - Date
		    (store_add, ":overlay", "$g_presentation_obj_custom_battle_designer_17", 1),
		    (eq, ":object", ":overlay"),
			(gt, reg59, 0),
			(call_script, "script_cf_trade_ledger_trim_entries", "trp_player", reg59, date_array),
			(display_message, "@{reg0} entries removed from ledger."),
		(else_try), #Set Item for Removal
		    (eq, ":object", "$g_presentation_obj_custom_battle_designer_16"),
			(is_between, ":value", trade_goods_begin, trade_goods_end),
			(assign, reg58, ":value"),
			(str_store_item_name, s0, ":value"),
			(overlay_set_val, ":object", ":value"), #looks cleaner
			(val_add, ":object", 1),
			(overlay_set_text, ":object", s0),
		(else_try), #Remove Entries - Item
		    (store_add, ":overlay", "$g_presentation_obj_custom_battle_designer_16", 2),
		    (eq, ":object", ":overlay"),
			(is_between, reg58, trade_goods_begin, trade_goods_end),
			(call_script, "script_cf_trade_ledger_trim_entries", "trp_player", reg58, item_array),
			(display_message, "@{reg0} entries removed from ledger."),
		(else_try), #Set Town for Removal
		    (eq, ":object", "$g_presentation_obj_custom_battle_designer_15"),
			(is_between, ":value", towns_begin, towns_end),
			(assign, reg57, ":value"),
			(str_store_party_name, s0, ":value"),
			(overlay_set_val, ":object", ":value"), #looks cleaner
			(val_add, ":object", 1),
			(overlay_set_text, ":object", s0),
		(else_try), #Remove Entries - Production Town
		    (store_add, ":overlay", "$g_presentation_obj_custom_battle_designer_15", 2),
		    (eq, ":object", ":overlay"), 
			(is_between, reg57, towns_begin, towns_end),
			(store_sub, ":overlay", ":object", "$g_presentation_obj_custom_battle_designer_15"),
			(call_script, "script_cf_trade_ledger_trim_entries", "trp_player", reg57, town_array),
			(display_message, "@{reg0} entries removed from ledger."),	
		(else_try), #Remove Entries - Demand Town
		    (val_add, ":overlay", 1),
		    (eq, ":object", ":overlay"), 
			(is_between, reg57, towns_begin, towns_end),
			(store_sub, ":overlay", ":object", "$g_presentation_obj_custom_battle_designer_15"),
			(call_script, "script_cf_trade_ledger_trim_entries", "trp_player", reg57, destination_array),
			(display_message, "@{reg0} entries removed from ledger."),	
		(else_try), #Set Profit Level for Removal
		    (eq, ":object", "$g_presentation_obj_custom_battle_designer_14"),
			(assign, reg56, ":value"),
		(else_try), #Remove Entries - Proft Level
		    (store_add, ":overlay", "$g_presentation_obj_custom_battle_designer_14", 1),
		    (eq, ":object", ":overlay"),
			(gt, reg56, 0),
			(call_script, "script_cf_trade_ledger_trim_entries", "trp_player", reg56, profit_array),
			(display_message, "@{reg0} entries removed from ledger."),			
		(else_try), #Assess Custom Item		
			(troop_get_slot, ":slider_1", "trp_temp_array_c", 5),
			(is_between, ":object", ":slider_1", "$g_presentation_obj_custom_battle_designer_18"),
			(is_between, ":value", trade_goods_begin, trade_goods_end),
			(troop_get_slot, ":ledger", "trp_player", slot_troop_trade_ledger),
			(call_script, "script_array_get_size", ":ledger"),
			(val_add, reg0, 1),
			(try_for_range, ":i", custom_assess_begin, reg0),
			    (troop_slot_eq, "trp_temp_array_c", ":i", ":object"),
				(assign, ":index", ":i"),
				(assign, reg0, 0), #break
			(try_end),
			(call_script, "script_cf_trade_ledger_custom_assess_item", ":value", ":index"),
			(str_store_item_name, s0, ":value"),
			(overlay_set_val, ":object", ":value"), #looks cleaner
			(val_add, ":object", 1),
			(overlay_set_text, ":object", s0),
		(try_end),
	 ]),
    ]),
    ## Floris - Trade Ledger end	
	  
	##	Floris Reports
		 
  ("reports", 0, mesh_report_screen,		 #mesh_note_window_bottom
   [
     (ti_on_presentation_load,
      [
	    (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),
		
		#g_presentation_obj_1 -> 16
		
		#Headers
		
		(create_text_overlay, reg0, "@Personal Reports"),
		(position_set_x, pos1, 50),
        (position_set_y, pos1, 670),
        (overlay_set_position, reg0, pos1),
		
		(create_text_overlay, reg0, "@Party Reports"),
		(position_set_x, pos1, 310),
        (position_set_y, pos1, 670),
        (overlay_set_position, reg0, pos1),
		
		(create_text_overlay, reg0, "@Kingdom Reports"),
		(position_set_x, pos1, 50),
        (position_set_y, pos1, 340),
        (overlay_set_position, reg0, pos1),
		
		(create_text_overlay, reg0, "@Reference Material"),
		(position_set_x, pos1, 280),
        (position_set_y, pos1, 340),
        (overlay_set_position, reg0, pos1),
		
		#Lines
		
#		(call_script, "script_prsnt_lines", 4, 610, 260, 90), #	width, height, starting x coordinate, startung y coordinate
#		(call_script, "script_prsnt_lines", 4, 610, 510, 90), 
#		(call_script, "script_prsnt_lines", 500, 4, 45, 660),
#		(call_script, "script_prsnt_lines", 480, 4, 45, 330),
		#(call_script, "script_gpu_create_mesh", "mesh_character_creator", 0, 0, 1000, 1325),
		#(overlay_set_alpha, reg1, 0x00),
		
		### Reports ###
		
		#Personal Reports
		
		(create_button_overlay, "$g_presentation_obj_2", "@Character Reports",tf_center_justify),		
        (position_set_x, pos1, 140),
        (position_set_y, pos1, 630),
        (overlay_set_position, "$g_presentation_obj_2", pos1),	

		(create_button_overlay, "$g_presentation_obj_3", "@Courtship Relations",tf_center_justify),		
        (position_set_x, pos1, 140),
        (position_set_y, pos1, 610),
        (overlay_set_position, "$g_presentation_obj_3", pos1),	
		
		(create_button_overlay, "$g_presentation_obj_4", "@Weekly Budget",tf_center_justify),		
        (position_set_x, pos1, 140),
        (position_set_y, pos1, 590),
        (overlay_set_position, "$g_presentation_obj_4", pos1),			
		
		(create_button_overlay, "$g_presentation_obj_5", "@Financial Report",tf_center_justify),		
        (position_set_x, pos1, 140),
        (position_set_y, pos1, 570),
        (overlay_set_position, "$g_presentation_obj_5", pos1),			
		
		#Party Reports
		
		(create_button_overlay, "$g_presentation_obj_6", "@Force Size Report",tf_center_justify),		
        (position_set_x, pos1, 380),
        (position_set_y, pos1, 630),
        (overlay_set_position, "$g_presentation_obj_6", pos1),		
		
		(create_button_overlay, "$g_presentation_obj_7", "@Morale Report",tf_center_justify),		
        (position_set_x, pos1, 375),
        (position_set_y, pos1, 610),
        (overlay_set_position, "$g_presentation_obj_7", pos1),		

		(create_button_overlay, "$g_presentation_obj_8", "@Companion Overview",tf_center_justify),		
        (position_set_x, pos1, 385),
        (position_set_y, pos1, 590),
        (overlay_set_position, "$g_presentation_obj_8", pos1),
		
		(create_button_overlay, "$g_presentation_obj_9", "@Character&Companions",tf_center_justify),		
        (position_set_x, pos1, 385),
        (position_set_y, pos1, 570),
        (overlay_set_position, "$g_presentation_obj_9", pos1),				
		
		(create_button_overlay, "$g_presentation_obj_10", "@Companion Missions",tf_center_justify),		
        (position_set_x, pos1, 387),
        (position_set_y, pos1, 550),
        (overlay_set_position, "$g_presentation_obj_10", pos1),	
		
		#Kingdom Reports
		
		(create_button_overlay, "$g_presentation_obj_11", "@Sovereign Relations",tf_center_justify),		
        (position_set_x, pos1, 150),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_11", pos1),	

		(create_button_overlay, "$g_presentation_obj_12", "@Lord Holdings",tf_center_justify),		
        (position_set_x, pos1, 140),
        (position_set_y, pos1, 278),
        (overlay_set_position, "$g_presentation_obj_12", pos1),	
		
		(create_button_overlay, "$g_presentation_obj_13", "@Known Lords",tf_center_justify),		
        (position_set_x, pos1, 140),
        (position_set_y, pos1, 256),
        (overlay_set_position, "$g_presentation_obj_13", pos1),			
		
		#Reference Material
		
		(create_button_overlay, "$g_presentation_obj_14", "@Upgrade Trees",tf_center_justify),		
        (position_set_x, pos1, 380),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_14", pos1),		
		
		(create_button_overlay, "$g_presentation_obj_15", "@All Items",tf_center_justify),		
        (position_set_x, pos1, 375),
        (position_set_y, pos1, 275),
        (overlay_set_position, "$g_presentation_obj_15", pos1),
		
		(create_button_overlay, "$g_presentation_obj_16", "@Other Information",tf_center_justify),		
        (position_set_x, pos1, 375),
        (position_set_y, pos1, 255),
        (overlay_set_position, "$g_presentation_obj_16", pos1),
		
		(try_begin),
			(ge,"$cheat_mode",1),
			(create_button_overlay, "$g_presentation_obj_19", "@Debug&Cheats",tf_center_justify),		
			(position_set_x, pos1, 375),
			(position_set_y, pos1, 235),
			(overlay_set_position, "$g_presentation_obj_19", pos1),
		(try_end),
		
		### Reports Over ###

		
		
		### Text for short reports ###
		
		(str_clear, s10),
		(str_store_string, s10, "@{s11}"),
		
		(create_text_overlay, reg0, s10, tf_double_space|tf_scrollable),  ##Short report
        (position_set_x, pos1, 525),
        (position_set_y, pos1, 120),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 450),
        (position_set_y, pos1, 500),
        (overlay_set_area_size, reg0, pos1),		
		
		
  		 #Back to menu - graphical button
	    (create_game_button_overlay, "$g_jq_Return_to_menu", "@_Return to world_"),	 
	    (position_set_x, pos1, 500),
        (position_set_y, pos1, 23),
        (overlay_set_position, "$g_jq_Return_to_menu", pos1),
	  
	  ]),
	 (ti_on_presentation_event_state_change,
     [
        (store_trigger_param_1, ":object"),													#Leave
		(try_begin), 
			(eq, ":object", "$g_jq_Return_to_menu"),
			(party_set_slot, "p_main_party", slot_screen_state, 1),
			(presentation_set_duration, 0),
		(else_try),															
			(eq, ":object", "$g_presentation_obj_3"),										# Courtship Relations
			(assign, "$g_jrider_pres_called_from_menu", 1),
			(assign, "$g_character_presentation_type", 0),
			(start_presentation, "prsnt_jrider_character_relation_report"),
		(else_try),															
			(eq, ":object", "$g_presentation_obj_4"),										# Weekly Budget
			(assign, "$g_apply_budget_report_to_gold", 0),
			(start_presentation, "prsnt_budget_report"),
		(else_try),															
			(eq, ":object", "$g_presentation_obj_5"),										# Financial Report
			(start_presentation, "prsnt_bank_quickview"),
		(else_try),															
			(eq, ":object", "$g_presentation_obj_8"),										# Companion Overview
			(assign, "$jq_in_market_menu", 0), # player is not in market menu
			#Exit if no companions 
			(assign, ":heroes_in_party", 0),
			(try_for_range, reg3, companions_begin, companions_end),
				(main_party_has_troop, reg3),
				(val_add, ":heroes_in_party", 1),
			(try_end),
			(try_begin),
				(eq, ":heroes_in_party", 0),
				(display_message,"@No companions in party!",0xFFFF0000),
			(else_try),
				(gt, "$jq_startpage", 1),
				(start_presentation, "prsnt_jq_extended_info"),
			(else_try),
				(start_presentation, "prsnt_jq_companions_quickview"),
			(try_end),			
		(else_try),															
			(eq, ":object", "$g_presentation_obj_9"),										# Character+Companions
			(assign, "$g_jrider_pres_called_from_menu", 1),
			(assign, "$g_character_presentation_type", 2),
			(start_presentation, "prsnt_jrider_character_relation_report"),	
		(else_try),															
			(eq, ":object", "$g_presentation_obj_11"),										# Sovereign relations
			(start_presentation, "prsnt_jrider_faction_relations_report"),
		(else_try),															
			(eq, ":object", "$g_presentation_obj_12"),										# Lord Holdings
			(start_presentation, "prsnt_kmt_lord_holdings"),
		(else_try),															
			(eq, ":object", "$g_presentation_obj_13"),										# Known Lords
			(assign, "$g_jrider_pres_called_from_menu", 1),
			(assign, "$g_character_presentation_type", 1),
			(start_presentation, "prsnt_jrider_character_relation_report"),			
		(else_try),	
			(eq, ":object", "$g_presentation_obj_14"),										# Troop Tree Viewer
			##Floris MTT begin
			(val_clamp, "$temp_2", 0, 10), #ensure valid number
			(try_begin),
				(eq, "$troop_trees", troop_trees_0),
				(store_add, ":cur_presentation", "$temp_2", "prsnt_upgrade_tree_1"),
			(else_try),
				(eq, "$troop_trees", troop_trees_1),
				(store_add, ":cur_presentation", "$temp_2", "prsnt_upgrade_tree_11"),
			(else_try),
				(eq, "$troop_trees", troop_trees_2),
				(store_add, ":cur_presentation", "$temp_2", "prsnt_upgrade_tree_21"),
			(try_end),
			##Floris MTT end
            (start_presentation, ":cur_presentation"),			
		(else_try),	
			(eq, ":object", "$g_presentation_obj_15"),										# View all items
			(assign, "$temp", 0),
			(start_presentation, "prsnt_all_items"),			
		(else_try),	
			(eq, ":object", "$g_presentation_obj_2"),										# Character Report			NOTE: The reports that are included within this presentation are bundled in a script.
			(call_script, "script_initialize_reports", 1),
		(else_try),	
			(eq, ":object", "$g_presentation_obj_6"),										# Force Size Report
			(call_script, "script_initialize_reports", 2),
		(else_try),
			(eq, ":object", "$g_presentation_obj_7"),										#Morale Report
			(call_script, "script_initialize_reports", 3),
		(else_try),																			##	Companion Mission Report
			(eq, ":object", "$g_presentation_obj_10"),
			(call_script, "script_initialize_reports", 4),
		(else_try),
			(eq, ":object", "$g_presentation_obj_16"),								# Other Information // Arguments made for Right to Rule // Fiefs Owned
			(call_script, "script_initialize_reports", 5),
		(else_try),
			(eq, ":object", "$g_presentation_obj_19"),
			(presentation_set_duration, 0),
			(jump_to_menu, "mnu_cheat_reports"),
		(try_end),
		
		]),
	]),	  
	#	Reports Over
	  
 
]
