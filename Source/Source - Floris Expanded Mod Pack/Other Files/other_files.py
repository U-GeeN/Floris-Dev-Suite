from module_info import *

import shutil

print " "
print "______________________________"
print " "
print "Copying source files to internal directory..."

# Main Files
shutil.copy("./actions.txt",intern_dir_expanded + "./actions.txt")
shutil.copy("./conversation.txt",intern_dir_expanded + "./conversation.txt")
shutil.copy("./dialog_states.txt",intern_dir_expanded + "./dialog_states.txt")
shutil.copy("./factions.txt",intern_dir_expanded + "./factions.txt")
shutil.copy("./info_pages.txt",intern_dir_expanded + "./info_pages.txt")
shutil.copy("./item_kinds1.txt",intern_dir_expanded + "./item_kinds1.txt")
shutil.copy("./map_icons.txt",intern_dir_expanded + "./map_icons.txt")
shutil.copy("./menus.txt",intern_dir_expanded + "./menus.txt")
shutil.copy("./meshes.txt",intern_dir_expanded + "./meshes.txt")
shutil.copy("./mission_templates.txt",intern_dir_expanded + "./mission_templates.txt")
shutil.copy("./music.txt",intern_dir_expanded + "./music.txt")
shutil.copy("./particle_systems.txt",intern_dir_expanded + "./particle_systems.txt")
shutil.copy("./parties.txt",intern_dir_expanded + "./parties.txt")
shutil.copy("./party_templates.txt",intern_dir_expanded + "./party_templates.txt")
shutil.copy("./postfx.txt",intern_dir_expanded + "./postfx.txt")
shutil.copy("./presentations.txt",intern_dir_expanded + "./presentations.txt")
shutil.copy("./quests.txt",intern_dir_expanded + "./quests.txt")
shutil.copy("./quick_strings.txt",intern_dir_expanded + "./quick_strings.txt")
shutil.copy("./scene_props.txt",intern_dir_expanded + "./scene_props.txt")
shutil.copy("./scenes.txt",intern_dir_expanded + "./scenes.txt")
shutil.copy("./scripts.txt",intern_dir_expanded + "./scripts.txt")
shutil.copy("./simple_triggers.txt",intern_dir_expanded + "./simple_triggers.txt")
shutil.copy("./skills.txt",intern_dir_expanded + "./skills.txt")
shutil.copy("./skins.txt",intern_dir_expanded + "./skins.txt")
shutil.copy("./sounds.txt",intern_dir_expanded + "./sounds.txt")
shutil.copy("./strings.txt",intern_dir_expanded + "./strings.txt")
shutil.copy("./tableau_materials.txt",intern_dir_expanded + "./tableau_materials.txt")
shutil.copy("./tag_uses.txt",intern_dir_expanded + "./tag_uses.txt")
shutil.copy("./triggers.txt",intern_dir_expanded + "./triggers.txt")
shutil.copy("./troops.txt",intern_dir_expanded + "./troops.txt")
shutil.copy("./variable_uses.txt",intern_dir_expanded + "./variable_uses.txt")
shutil.copy("./variables.txt",intern_dir_expanded + "./variables.txt")
# Data Files
shutil.copy("./flora_kinds.txt",intern_dir_expanded + "./Data/flora_kinds.txt")
shutil.copy("./ground_specs.txt",intern_dir_expanded + "./Data/ground_specs.txt")
shutil.copy("./skyboxes.txt",intern_dir_expanded + "./Data/skyboxes.txt")
# Other Files
shutil.copy("./game_variables.txt",intern_dir_expanded + "./game_variables.txt")
shutil.copy("./main.bmp",intern_dir_expanded + "./main.bmp")
shutil.copy("./map.txt",intern_dir_expanded + "./map.txt")
shutil.copy("./module.ini",intern_dir_expanded + "./module.ini")

print "Moving source files to custom mod directory..."

# Main Files
shutil.move("./actions.txt",export_dir_main + export_dir_expanded + "./actions.txt")
shutil.move("./conversation.txt",export_dir_main + export_dir_expanded + "./conversation.txt")
shutil.move("./dialog_states.txt",export_dir_main + export_dir_expanded + "./dialog_states.txt")
shutil.move("./factions.txt",export_dir_main + export_dir_expanded + "./factions.txt")
shutil.move("./info_pages.txt",export_dir_main + export_dir_expanded + "./info_pages.txt")
shutil.move("./item_kinds1.txt",export_dir_main + export_dir_expanded + "./item_kinds1.txt")
shutil.move("./map_icons.txt",export_dir_main + export_dir_expanded + "./map_icons.txt")
shutil.move("./menus.txt",export_dir_main + export_dir_expanded + "./menus.txt")
shutil.move("./meshes.txt",export_dir_main + export_dir_expanded + "./meshes.txt")
shutil.move("./mission_templates.txt",export_dir_main + export_dir_expanded + "./mission_templates.txt")
shutil.move("./music.txt",export_dir_main + export_dir_expanded + "./music.txt")
shutil.move("./particle_systems.txt",export_dir_main + export_dir_expanded + "./particle_systems.txt")
shutil.move("./parties.txt",export_dir_main + export_dir_expanded + "./parties.txt")
shutil.move("./party_templates.txt",export_dir_main + export_dir_expanded + "./party_templates.txt")
shutil.move("./postfx.txt",export_dir_main + export_dir_expanded + "./postfx.txt")
shutil.move("./presentations.txt",export_dir_main + export_dir_expanded + "./presentations.txt")
shutil.move("./quests.txt",export_dir_main + export_dir_expanded + "./quests.txt")
shutil.move("./quick_strings.txt",export_dir_main + export_dir_expanded + "./quick_strings.txt")
shutil.move("./scene_props.txt",export_dir_main + export_dir_expanded + "./scene_props.txt")
shutil.move("./scenes.txt",export_dir_main + export_dir_expanded + "./scenes.txt")
shutil.move("./scripts.txt",export_dir_main + export_dir_expanded + "./scripts.txt")
shutil.move("./simple_triggers.txt",export_dir_main + export_dir_expanded + "./simple_triggers.txt")
shutil.move("./skills.txt",export_dir_main + export_dir_expanded + "./skills.txt")
shutil.move("./skins.txt",export_dir_main + export_dir_expanded + "./skins.txt")
shutil.move("./sounds.txt",export_dir_main + export_dir_expanded + "./sounds.txt")
shutil.move("./strings.txt",export_dir_main + export_dir_expanded + "./strings.txt")
shutil.move("./tableau_materials.txt",export_dir_main + export_dir_expanded + "./tableau_materials.txt")
shutil.move("./tag_uses.txt",export_dir_main + export_dir_expanded + "./tag_uses.txt")
shutil.move("./triggers.txt",export_dir_main + export_dir_expanded + "./triggers.txt")
shutil.move("./troops.txt",export_dir_main + export_dir_expanded + "./troops.txt")
shutil.move("./variable_uses.txt",export_dir_main + export_dir_expanded + "./variable_uses.txt")
shutil.move("./variables.txt",export_dir_main + export_dir_expanded + "./variables.txt")
# Data Files
shutil.move("./flora_kinds.txt",export_dir_main + export_dir_expanded + "./Data/flora_kinds.txt")
shutil.move("./ground_specs.txt",export_dir_main + export_dir_expanded + "./Data/ground_specs.txt")
shutil.move("./skyboxes.txt",export_dir_main + export_dir_expanded + "./Data/skyboxes.txt")
# Textures
shutil.move("./warrider_logo.dds",export_dir_main + export_dir_expanded + "./Textures/warrider_logo.dds")
# Other Files
shutil.move("./game_variables.txt",export_dir_main + export_dir_expanded + "./game_variables.txt")
shutil.move("./main.bmp",export_dir_main + export_dir_expanded + "./main.bmp")
shutil.move("./map.txt",export_dir_main + export_dir_expanded + "./map.txt")
shutil.move("./module.ini",export_dir_main + export_dir_expanded + "./module.ini")

print "Moving Process Log..."