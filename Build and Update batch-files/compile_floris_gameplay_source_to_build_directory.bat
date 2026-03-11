@echo off
echo Compiling Floris Gameplay Mod Pack
copy "..\Source\Source - Floris Gameplay Mod Pack\header files\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Gameplay Mod Pack\ID files\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Gameplay Mod Pack\process files\*.*" ".\" >>Process_Log.txt
copy "..\Files\Specific Textures\Gameplay\warrider_logo.dds" ".\" >>Process_Log.txt
echo Start Processing...
copy "..\Files\Other Files\Gameplay\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Native Warband\Data\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Native Warband\Other Files\Ground_specs.py" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Data\Skyboxes.py" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Module\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Gameplay Mod Pack\Variables\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Gameplay Mod Pack\Other Files\*.*" ".\" >>Process_Log.txt
copy "..\Module Info\*.*" ".\" >>Process_Log.txt
copy "..\Source\Files for Batch\*.*" ".\" >>Process_Log.txt
python info.py
python dircreate.py
copy "..\Source\Modmerger\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Character Creation\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Companions Overview\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Dynamic Arrays\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Freelancer\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Formations\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Kingdom Management Tools\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Tournament Enhancements\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Prebattle OD\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Outposts\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Gameplay Mod Pack\Module\*.*" ".\" >>Process_Log.txt
echo ______________________________
echo.
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
copy ".\header_*.py" "..\Source\Source - Floris Gameplay Mod Pack\header files\" >>Process_Log.txt
copy ".\ID_*.py" "..\Source\Source - Floris Gameplay Mod Pack\ID files\" >>Process_Log.txt
copy ".\process_*.py" "..\Source\Source - Floris Gameplay Mod Pack\process files\" >>Process_Log.txt
python other_files.py
move ".\Process_Log.txt" "..\Compiled Files\"
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