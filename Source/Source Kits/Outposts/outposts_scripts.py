from module_scripts import *
scripts = [
  ("setup_outpost_scene",
    [
      (party_get_current_terrain, ":terrain_type", "p_main_party"),
      (assign, ":scene_to_use", "scn_random_scene"),
      (try_begin),
        (eq, ":terrain_type", rt_steppe),
        (assign, ":scene_to_use", "scn_outpost_one_one_steppe"),
      (else_try),
        (eq, ":terrain_type", rt_plain),
        (assign, ":scene_to_use", "scn_outpost_one_one_plain"),
      (else_try),
        (eq, ":terrain_type", rt_snow),
        (assign, ":scene_to_use", "scn_outpost_one_one_snow"),
      (else_try),
        (eq, ":terrain_type", rt_desert),
        (assign, ":scene_to_use", "scn_outpost_one_one_desert"),#scn_outpost_scene_desert
      (else_try),
        (eq, ":terrain_type", rt_steppe_forest),
        (assign, ":scene_to_use", "scn_outpost_one_one_steppe_forest"),
      (else_try),
        (eq, ":terrain_type", rt_forest),
        (assign, ":scene_to_use", "scn_outpost_one_one_forest"),
      (else_try),
        (eq, ":terrain_type", rt_snow_forest),
        (assign, ":scene_to_use", "scn_outpost_one_one_snow_forest"),
      (else_try),
        (eq, ":terrain_type", rt_desert_forest),
        (assign, ":scene_to_use", "scn_outpost_one_one_desert_forest"),
      (try_end),
	  (try_begin),
	    (neq, ":scene_to_use", "scn_random_scene"),
	    (eq, "$g_encountered_party", "p_outpost_2"),
		(val_add, ":scene_to_use", 16),
	  (try_end),
	  (try_begin),
	    (neq, ":scene_to_use", "scn_random_scene"),
	    (party_slot_eq, "$g_encountered_party", slot_outpost_level, 2),
		(val_add, ":scene_to_use", 8),
	  (try_end),
      (assign, reg1, ":scene_to_use"),
      (jump_to_scene,":scene_to_use"),
  ]),
 
  ("setup_fort_scene",
    [
      (party_get_current_terrain, ":terrain_type", "p_main_party"),
      (assign, ":scene_to_use", "scn_fort"),
      (try_begin), # Lumos: Not all terrains have unique scenes yet
        (eq, ":terrain_type", rt_snow),
        (assign, ":scene_to_use", "scn_fort_snow"),
      (else_try),
        (eq, ":terrain_type", rt_forest),
        (assign, ":scene_to_use", "scn_fort_forest"),
      (try_end),
      (assign, reg1, ":scene_to_use"),
  ]),

  # script_set_walker_to_type
  # Input: arg1 = walker_id, arg2 = troop_id
  # Output: none
  ("set_walker_to_type",
   [
       (store_script_param, ":walker_id", 1),
       (store_script_param, ":troop_id", 2),
       # transfer items
       (try_for_range,":item_no", 0, "itm_items_end"), #horses_end,ranged_weapons_end),
          (store_item_kind_count,":num_items",":item_no",":walker_id"),
          (ge,":num_items",1),
          (troop_remove_items,":walker_id",":item_no",":num_items"),
       (try_end),
       (try_for_range,":item_no",  0, "itm_items_end"),  #horses_end,ranged_weapons_end),
          (store_item_kind_count,":num_items",":item_no",":troop_id"),
          (ge,":num_items",1),
          (store_item_kind_count,":num_items",":item_no",":walker_id"),
          (lt,":num_items",1),
          (troop_add_items,":walker_id",":item_no",1),
       (try_end),
       (troop_equip_items,":walker_id"),
     ]),

  # script_init_fort_patrols
  # Input: none
  # Output: none
  ("init_fort_patrols",
    [
     (try_for_agents, ":cur_agent"),
       (agent_get_troop_id, ":cur_troop", ":cur_agent"),
       (agent_get_entry_no, ":entry_no", ":cur_agent"),
	   (agent_get_party_id, ":party", ":cur_agent"), #floris
       (try_begin),
	     (party_slot_eq, "$current_town", slot_outpost_patrol, ":party"), #in a patrol
         #(eq, ":cur_troop", "trp_watchman"),
         (entry_point_get_position, pos1, ":entry_no"),
         (agent_set_position, ":cur_agent", pos1),		# force agents into the proper spot to prevent wonkyness
         (val_add, ":entry_no", 1),
         (agent_set_slot, ":cur_agent", 0, ":entry_no"),
         (entry_point_get_position, pos2, ":entry_no"),
         
         (agent_set_speed_limit, ":cur_agent", 1),
         (agent_set_scripted_destination, ":cur_agent", pos2, 0),
       (else_try),
         (this_or_next|eq, ":cur_troop", "trp_tutorial_rider_1"),  ##why????
         (eq, ":entry_no", 20),
         (agent_is_human, ":cur_agent"),
         (call_script, "script_init_mounted_patrol", ":cur_agent"),
       (try_end),
     (try_end),
  ]),
  
  # script_init_mounted_patrol
  # Input: arg1 = agent number
  # Output: none
  ("init_mounted_patrol",
    [
       (store_script_param, ":cur_agent", 1),
       (agent_get_entry_no, ":entry_no", ":cur_agent"),
       (agent_set_stand_animation, ":cur_agent", "anim_ride_0"),
       (agent_set_walk_forward_animation, ":cur_agent", "anim_ride_1"),
       (agent_set_animation, ":cur_agent", "anim_ride_0"),
       (agent_set_animation_progress, ":cur_agent", 10),
       
       (store_add, ":target_entry_point", ":entry_no", 1),
       (entry_point_get_position, pos1, ":target_entry_point"),
       (agent_set_slot, ":cur_agent", 0, ":target_entry_point"),
       (agent_set_speed_limit, ":cur_agent", mount_patrol_max_speed),
       (agent_set_scripted_destination, ":cur_agent", pos1, 0),
       
  ]),
  
  # script_tick_fort_patrol
  # Input: arg1 = agent_id, arg2 = number of way points
  # Output: none
  ("cf_tick_fort_patrol",
    [
     (store_script_param, ":agent_id", 1),
     (store_script_param, ":num_points", 2),
     
     (agent_get_entry_no, ":entry_no", ":agent_id"),
     (agent_get_slot, ":target_entry_point", ":agent_id", 0),
     (agent_get_class, ":agent_class", ":agent_id"),
     (entry_point_get_position, pos1, ":target_entry_point"),
     (agent_get_position, pos2, ":agent_id"),
     (get_distance_between_positions, ":distance", pos1, pos2),
     (try_begin),
       (eq, ":agent_class", grc_cavalry),
       (lt, ":distance", mount_patrol_closing_dist),
       (store_sub, ":speed_adjust", mount_patrol_closing_dist, ":distance"),
       (val_mul, ":speed_adjust", 100),
       (val_div, ":speed_adjust", mount_patrol_closing_dist),
       (store_sub, ":speed_limit", mount_patrol_max_speed, mount_patrol_min_speed),
       (val_mul, ":speed_limit", -1),
       (val_mul, ":speed_adjust", ":speed_limit"),
       (val_div, ":speed_adjust", 100),
       (val_add, ":speed_adjust", mount_patrol_max_speed), # maxspeed - 10*(6000-dist)/6000 scales from max to min speed as we close to destination
       (agent_set_speed_limit, ":agent_id", ":speed_adjust"), # once agent is within closing distance, it scales down from max speed to min speed as it reaches target
       (assign, reg3, ":agent_id"),
       (assign, reg4, ":speed_adjust"),
       #(display_message, "@Agent #{reg3} reducing max speed to {reg4}."),
     (try_end),
     (lt, ":distance", 400),
     (store_random_in_range, ":random_no", 0, 100),
     (lt, ":random_no", 20),
     (store_add, ":max_point", ":entry_no", ":num_points"),
     (val_add, ":target_entry_point", 1),
     (try_begin),
       (gt, ":target_entry_point", ":max_point"),
       (assign, ":target_entry_point", ":entry_no"),
     (try_end),
     (try_begin),
       (eq, ":agent_class", grc_cavalry),
       (agent_set_speed_limit, ":agent_id", 15),
     (try_end),
     (entry_point_get_position, pos1, ":target_entry_point"),
     (agent_set_slot, ":agent_id", 0, ":target_entry_point"),
     (agent_set_scripted_destination, ":agent_id", pos1, 0),
  ]),

]


from util_wrappers import *
from util_scripts import *

scripts_directives = [
    [SD_OP_BLOCK_INSERT, "game_event_party_encounter", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,(jump_to_menu, "mnu_cattle_herd"),0,[
	    #-## Outposts begin
           (else_try),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_outpost),
             (jump_to_menu, "mnu_outpost"),
		   (else_try),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_fort),
			 (jump_to_menu, "mnu_fort"),
		#-## Outposts end
    ]],
	[SD_OP_BLOCK_INSERT, "player_join_faction", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE,(try_for_range, ":cur_center", centers_begin, centers_end),0,[
	    #-## Outposts begin
		(store_add, ":end", "p_fort", 1),
		(try_for_range, ":cur_center", "p_outpost_1", ":end"),
		    (party_is_active, ":cur_center"),
			(party_set_faction, ":cur_center", ":faction_no"),
			(party_get_slot, ":cur_center", ":cur_center", slot_outpost_patrol),
			(party_is_active, ":cur_center"),
			(party_set_faction, ":cur_center", ":faction_no"),
		(try_end),
		#-## Outposts end
    ]],
	[SD_OP_BLOCK_INSERT, "player_leave_faction", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE,(try_begin),0,[
	    #-## Outposts begin
		(try_begin),
			(eq, ":give_back_fiefs", 0),
			(assign, ":faction_no", "fac_player_supporters_faction"),
		(else_try),
			(assign, ":faction_no", "fac_player_faction"),
		(try_end),
		(store_add, ":end", "p_fort", 1),
		(try_for_range, ":cur_center", "p_outpost_1", ":end"),
		    (party_is_active, ":cur_center"),
			(party_set_faction, ":cur_center", ":faction_no"),
			(party_get_slot, ":cur_center", ":cur_center", slot_outpost_patrol),
			(party_is_active, ":cur_center"),
			(party_set_faction, ":cur_center", ":faction_no"),
		(try_end),
		#-## Outposts end
    ]],	 
]

def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "scripts"
		orig_scripts = var_set[var_name_1]
		
		process_script_directives(orig_scripts, scripts_directives)
		# add remaining scripts
		add_scripts(orig_scripts, scripts, True)
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)

