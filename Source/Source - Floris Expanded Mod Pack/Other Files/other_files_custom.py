from module_info import *
import shutil
import os

print "Moving source files to custom mod directory..."

def safe_move(src, dst_dir, filename):
	full_dst = os.path.join(dst_dir, filename)
	if not os.path.exists(dst_dir):
		try:
			os.makedirs(dst_dir)
		except:
			print "Warning: Could not create directory %s. Skipping move for %s." % (dst_dir, filename)
			return
	
	if os.path.exists(src):
		shutil.move(src, full_dst)
	else:
		print "Warning: Source file %s not found. Skipping move." % src

export_dir_full = os.path.join(export_dir_main, "Modules", export_dir_custom)
export_dir_data = os.path.join(export_dir_full, "Data")

# Main Files
safe_move("./actions.txt", export_dir_full, "actions.txt")
safe_move("./conversation.txt", export_dir_full, "conversation.txt")
safe_move("./dialog_states.txt", export_dir_full, "dialog_states.txt")
safe_move("./factions.txt", export_dir_full, "factions.txt")
safe_move("./info_pages.txt", export_dir_full, "info_pages.txt")
safe_move("./item_kinds1.txt", export_dir_full, "item_kinds1.txt")
safe_move("./map_icons.txt", export_dir_full, "map_icons.txt")
safe_move("./menus.txt", export_dir_full, "menus.txt")
safe_move("./meshes.txt", export_dir_full, "meshes.txt")
safe_move("./mission_templates.txt", export_dir_full, "mission_templates.txt")
safe_move("./music.txt", export_dir_full, "music.txt")
safe_move("./particle_systems.txt", export_dir_full, "particle_systems.txt")
safe_move("./parties.txt", export_dir_full, "parties.txt")
safe_move("./party_templates.txt", export_dir_full, "party_templates.txt")
safe_move("./postfx.txt", export_dir_full, "postfx.txt")
safe_move("./presentations.txt", export_dir_full, "presentations.txt")
safe_move("./quests.txt", export_dir_full, "quests.txt")
safe_move("./quick_strings.txt", export_dir_full, "quick_strings.txt")
safe_move("./scene_props.txt", export_dir_full, "scene_props.txt")
safe_move("./scenes.txt", export_dir_full, "scenes.txt")
safe_move("./scripts.txt", export_dir_full, "scripts.txt")
safe_move("./simple_triggers.txt", export_dir_full, "simple_triggers.txt")
safe_move("./skills.txt", export_dir_full, "skills.txt")
safe_move("./skins.txt", export_dir_full, "skins.txt")
safe_move("./sounds.txt", export_dir_full, "sounds.txt")
safe_move("./strings.txt", export_dir_full, "strings.txt")
safe_move("./tableau_materials.txt", export_dir_full, "tableau_materials.txt")
safe_move("./tag_uses.txt", export_dir_full, "tag_uses.txt")
safe_move("./triggers.txt", export_dir_full, "triggers.txt")
safe_move("./troops.txt", export_dir_full, "troops.txt")
safe_move("./variable_uses.txt", export_dir_full, "variable_uses.txt")
safe_move("./variables.txt", export_dir_full, "variables.txt")

# Data Files
safe_move("./flora_kinds.txt", export_dir_data, "flora_kinds.txt")
safe_move("./ground_specs.txt", export_dir_data, "ground_specs.txt")
safe_move("./skyboxes.txt", export_dir_data, "skyboxes.txt")

# Other Files
safe_move("./game_variables.txt", export_dir_full, "game_variables.txt")
safe_move("./main.bmp", export_dir_full, "main.bmp")
safe_move("./map.txt", export_dir_full, "map.txt")
safe_move("./module.ini", export_dir_full, "module.ini")

print "Copying static asset folders..."
try:
	from distutils.dir_util import copy_tree
	asset_mappings = {
		"Music": "Music",
		"Resource": "Resource",
		"SceneObj/Expanded": "SceneObj",
		"Sounds": "Sounds",
		"Textures": "Textures",
		"Specific Textures/Expanded": "Textures",
		"languages": "languages"
	}
	for src_rel, dst_rel in asset_mappings.items():
		src_folder = os.path.join(".", "Files", src_rel)
		dst_folder = os.path.join(export_dir_full, dst_rel)
		if os.path.exists(src_folder):
			print "Copying %s to %s" % (src_folder, dst_folder)
			copy_tree(src_folder, dst_folder)
		else:
			print "Warning: Source folder %s not found." % src_folder
except Exception as e:
	print "Error copying static assets: ", e

print "Moving Process Log..."
