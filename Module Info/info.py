#################################################################################
#						Welcome to the info file!								#
#																				#
# This file was formerly known as module_info.py. Don't change the name of this #
# file!																			#
#																				#
# Here you set the path where you want to compile the source to.				#
# export_dir_main_guest		is your main Warband directory. The source will		#
#							automatically create the standard Floris directory	#
#							where you compile and build to.						#
# export_dir_custom_guest	is a custom directory of your liking. If you don't	#
#							want to compile to the standard directory, the		#
#							source will compile to this one.					#
# If you need examples, please scroll down for the directories the devs use.	#
# Make sure you use forward slashes (/) and NOT backward slashes (\).			#
#################################################################################
export_dir_main_guest					= "C:/Program Files/Mount&Blade Warband/"
export_dir_custom_guest					= "./Native/"
#################################################################################
# Don't change anything below this point unless you know what you're doing.		#
#################################################################################




#################################################################################
# Here are the directories used by the devs of the Floris Mod Pack.				#
#################################################################################
# Monnikje:
export_dir_main_monnikje				= "G:/lan/Mount&Blade Warband/"
export_dir_custom_monnikje				= "./Floris/"
# Duh:
export_dir_main_duh						= "C:/Users/Duh/Desktop/Mount&Blade Warband 1.151/"
export_dir_custom_duh					= "./Floris Expanded Mod Pack 2.5/"
# Caba`Drin:
export_dir_main_caba					= "E:/Games/Mount&Blade Warband/"
export_dir_custom_caba					= "./Floris 2.5 Dev/"
# Windyplains:
export_dir_main_windy					= "D:/Games/Mount&Blade Warband/"
export_dir_custom_windy					= "./Floris Gameplay Mod Pack 2.55/"
#################################################################################
# Here are the some standard Warband directories.								#
#################################################################################
# TaleWorlds normal install:
export_dir_main_normal					= "C:/Program Files/Mount&Blade Warband/"
export_dir_custom_normal				= "./Native/"
# Steam install:
export_dir_main_steam					= "C:/Program Files (x86)/Steam/steamapps/common/mountblade warband/"
export_dir_custom_steam					= "./Native/"
#################################################################################
# These are the standard directories where the different versions are build and	#
# compiled to. Changing this will affect the directories that are automatically	#
# created, so do so with care.													#
#################################################################################
export_dir_basic						= "./Modules/Floris Basic Mod Pack 2.54/"
export_dir_expanded						= "./Modules/Floris Expanded Mod Pack 2.54/"
export_dir_gameplay						= "./Modules/Floris Gameplay Mod Pack 2.54/"
export_dir_devsuite						= "./Modules/Floris Dev Suite 2.54/"
export_dir_native						= "./Modules/Native 1.153/"
#################################################################################
# These are the directories where copies of the compiled files are copied to.	#
# It is important for the installer. Don't change this!							#
#################################################################################
intern_dir_basic						= "../Compiled Files/Basic/"
intern_dir_basic_custom					= "./Compiled Files/Basic/"
intern_dir_expanded						= "../Compiled Files/Expanded/"
intern_dir_expanded_custom				= "./Compiled Files/Expanded/"
intern_dir_gameplay						= "../Compiled Files/Gameplay/"
intern_dir_gameplay_custom				= "./Compiled Files/Gameplay/"
intern_dir_native						= "../Compiled Files/Native/"
intern_dir_native_custom				= "./Compiled Files/Native/"
#################################################################################
# This is the main folder where everything is compiled to. Don't change it!		#
#################################################################################
export_dir								= "./"
#################################################################################
# And here is the code which determines automatically what directory to use.	#
# First importing important python stuff:										#
#################################################################################
import os
import platform

# macOS Steam paths (actual folder names on macOS Steam)
export_dir_macos_steam_primary = os.path.expanduser(
    "~/Library/Application Support/Steam/steamapps/common/MountBlade Warband/")
export_dir_macos_steam_secondary = os.path.expanduser(
    "~/Library/Application Support/Steam/steamapps/common/MountBlade Warband./")

# The module name to compile to inside Warband/Modules/
export_dir_macos_custom = "./Floris Expanded Mod Pack 2.55/"

#################################################################################
# Priority: macOS Steam > Windows paths > test_build fallback
#################################################################################
f = open("./module_info.py","w")
f.write("from info import *\n")

if os.path.exists(export_dir_macos_steam_primary):
	f.write("export_dir_main		= '" + export_dir_macos_steam_primary + "'\n")
	f.write("export_dir_custom	= '" + export_dir_macos_custom + "'\n")
elif os.path.exists(export_dir_macos_steam_secondary):
	f.write("export_dir_main		= '" + export_dir_macos_steam_secondary + "'\n")
	f.write("export_dir_custom	= '" + export_dir_macos_custom + "'\n")
elif os.path.exists(export_dir_main_monnikje):
	f.write("export_dir_main		= export_dir_main_monnikje\n")
	f.write("export_dir_custom	= export_dir_custom_monnikje\n")
elif os.path.exists(export_dir_main_duh):
	f.write("export_dir_main		= export_dir_main_duh\n")
	f.write("export_dir_custom	= export_dir_custom_duh\n")
elif os.path.exists(export_dir_main_caba):
	f.write("export_dir_main		= export_dir_main_caba\n")
	f.write("export_dir_custom	= export_dir_custom_caba\n")
elif os.path.exists(export_dir_main_windy):
	f.write("export_dir_main		= export_dir_main_windy\n")
	f.write("export_dir_custom	= export_dir_custom_windy\n")
elif os.path.exists(export_dir_main_steam):
	f.write("export_dir_main		= export_dir_main_steam\n")
	f.write("export_dir_custom	= export_dir_custom_steam\n")
else:
	# Fallback to test_build
	default_dir = "./test_build/"
	if not os.path.exists(default_dir):
		os.makedirs(default_dir)
	f.write("export_dir_main		= '" + default_dir + "'\n")
	f.write("export_dir_custom	= './Native/'\n")
f.close()
