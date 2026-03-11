@echo off
echo Compiling Floris Basic Mod Pack to a custom directory
copy ".\Source\Source - Native Warband\header files\*.*" ".\" >>Process_Log.txt
copy ".\Source\Source - Native Warband\ID files\*.*" ".\" >>Process_Log.txt
copy ".\Source\Source - Native Warband\process files\*.*" ".\" >>Process_Log.txt
echo Start Processing...
copy ".\Files\Other Files\Basic\*.*" ".\" >>Process_Log.txt
copy ".\Source\Modmerger\*.py" ".\" >>Process_Log.txt
copy ".\Source\Source - Native Warband\Data\*.*" ".\" >>Process_Log.txt
copy ".\Source\Source - Native Warband\Other Files\Ground_specs.py" ".\" >>Process_Log.txt
copy ".\Source\Source - Floris Expanded Mod Pack\Data\Skyboxes.py" ".\" >>Process_Log.txt
copy ".\Source\Source - Native Warband\Module\*.*" ".\" >>Process_Log.txt
copy ".\Source\Source - Floris Basic Mod Pack\Module\*.*" ".\" >>Process_Log.txt
copy ".\Source\Source - Floris Expanded Mod Pack\Module\module_skins.py" ".\" >>Process_Log.txt
copy ".\Source\Source - Floris Expanded Mod Pack\Module\music.py" ".\" >>Process_Log.txt
copy ".\Source\Source - Floris Expanded Mod Pack\Module\sounds.py" ".\" >>Process_Log.txt
copy ".\Source\Source - Floris Basic Mod Pack\Variables\*.*" ".\" >>Process_Log.txt
copy ".\Source\Source - Floris Basic Mod Pack\Other Files\*.*" ".\" >>Process_Log.txt
copy ".\Module Info\*.*" ".\" >>Process_Log.txt
copy ".\Source\Files for Batch\*.*" ".\" >>Process_Log.txt
python info.py
echo ______________________________
echo.
python mergefiles_custom.py
python process_init.py
python process_global_variables.py
python process_strings.py
python process_skills.py
python process_music.py
python process_animations.py
python process_meshes.py
python process_sounds.py
python process_skins.py
python process_map_icons.py
python process_factions.py
python process_items.py
python process_scenes.py
python process_troops.py
python process_particle_sys.py
python process_scene_props.py
python process_tableau_materials.py
python process_presentations.py
python process_party_tmps.py
python process_parties.py
python process_quests.py
python process_info_pages.py
python process_scripts.py
python process_mission_tmps.py
python process_game_menus.py
python process_simple_triggers.py
python process_dialogs.py
python process_global_variables_unused.py
python process_postfx.py
python Flora_kinds.py
python Ground_specs.py
python Skyboxes.py
python other_files_custom.py
move ".\Process_Log.txt" ".\Compiled Files\"
@del *.pyc
@del *.py
@del ground_spec_codes.h
echo.
echo ______________________________
echo.
echo All Finished ...
echo Cleaning up...
echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to exit. . .
pause>nul