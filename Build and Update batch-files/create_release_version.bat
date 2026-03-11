@echo off
echo Welcome to the release creator.
echo ______________________________
echo 1. Create Alternative Files - In progress
echo 2. Floris Basic Mod Pack
echo 3. Floris Expanded Mod Pack
echo 4. Floris Gameplay Mod Pack
echo 5. Floris Dev Suite
echo 6. Creating the 7zip file
echo 7. Creating the installer
echo ______________________________
move ".\Readme.txt" "..\Compiled Files\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\header files\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\ID files\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\process files\*.*" ".\" >>Process_Log.txt
echo Start Processing...
copy "..\Source\Source - Floris Expanded Mod Pack\Module\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Data\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Variables\*.*" ".\" >>Process_Log.txt
copy "..\Module Info\*.*" ".\" >>Process_Log.txt
copy "..\Source\Files for Batch\*.*" ".\" >>Process_Log.txt
python info.py
copy "..\Source\Modmerger\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Character Creation\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Companions Overview\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Dynamic Arrays\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Expanded Scenes\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Freelancer\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Formations\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Kingdom Management Tools\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Tournament Enhancements\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Prebattle OD\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Outposts\*.py" ".\" >>Process_Log.txt
copy "..\Files\Other Files\Alternatives\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Gameplay Mod Pack\Module\module_animations.py" ".\" >>Process_Log.txt
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
copy ".\actions.txt" "..\Files\Other Files\Alternatives\"
copy ".\particle_systems.txt" "..\Files\Other Files\Alternatives\"
@del *.pyc
@del *.py
move ".\Process_Log.txt" "..\Compiled Files\"
@del *.txt
copy "..\Compiled Files\Process_Log.txt" ".\"
@del ground_spec_codes.h
move "..\Compiled Files\Readme.txt" ".\" >>Process_Log.txt
echo.
echo Cleaning up...
echo ______________________________
echo 1. Create Alternative Files - Done
echo 2. Floris Basic Mod Pack - In progress
echo 3. Floris Expanded Mod Pack
echo 4. Floris Gameplay Mod Pack
echo 5. Floris Dev Suite
echo 6. Creating the 7zip file
echo 7. Creating the installer
echo ______________________________
copy "..\Source\Source - Native Warband\header files\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Native Warband\ID files\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Native Warband\process files\*.*" ".\" >>Process_Log.txt
copy "..\Files\Specific Textures\Basic\warrider_logo.dds" ".\" >>Process_Log.txt
echo Start Processing...
copy "..\Files\Other Files\Basic\*.*" ".\" >>Process_Log.txt
copy "..\Source\Modmerger\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source - Native Warband\Data\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Native Warband\Other Files\Ground_specs.py" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Data\Skyboxes.py" ".\" >>Process_Log.txt
copy "..\Source\Source - Native Warband\Module\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Basic Mod Pack\Module\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Module\module_skins.py" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Module\music.py" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Module\sounds.py" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Basic Mod Pack\Variables\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Basic Mod Pack\Other Files\*.*" ".\" >>Process_Log.txt
copy "..\Module Info\*.*" ".\" >>Process_Log.txt
copy "..\Source\Files for Batch\*.*" ".\" >>Process_Log.txt
python info.py
python dircreate.py
echo Copy Files...
copy "..\Files\Operations\basic_files.py" ".\" >>Process_Log.txt
python basic_files.py
echo ______________________________
echo.
python mergefiles.py
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
python other_files.py
move ".\Process_Log.txt" "..\Compiled Files\"
@del *.pyc
@del *.py
@del ground_spec_codes.h
echo.
echo Cleaning up...
echo ______________________________
echo 1. Create Alternative Files - Done
echo 2. Floris Basic Mod Pack - Done
echo 3. Floris Expanded Mod Pack - In progress
echo 4. Floris Gameplay Mod Pack
echo 5. Floris Dev Suite
echo 6. Creating the 7zip file
echo 7. Creating the installer
echo ______________________________
copy "..\Source\Source - Floris Expanded Mod Pack\header files\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\ID files\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\process files\*.*" ".\" >>Process_Log.txt
copy "..\Files\Specific Textures\Expanded\warrider_logo.dds" ".\" >>Process_Log.txt
echo Start Processing...
copy "..\Files\Other Files\Expanded\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Module\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Data\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Variables\*.*" ".\" >>Process_Log.txt
copy "..\Source\Source - Floris Expanded Mod Pack\Other Files\*.*" ".\" >>Process_Log.txt
copy "..\Module Info\*.*" ".\" >>Process_Log.txt
copy "..\Source\Files for Batch\*.*" ".\" >>Process_Log.txt
python info.py
python dircreate.py
echo Copy Files...
copy "..\Files\Operations\expanded_files.py" ".\" >>Process_Log.txt
python expanded_files.py
copy "..\Source\Modmerger\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Character Creation\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Companions Overview\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Dynamic Arrays\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Expanded Scenes\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Freelancer\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Formations\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Kingdom Management Tools\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Tournament Enhancements\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Prebattle OD\*.py" ".\" >>Process_Log.txt
copy "..\Source\Source Kits\Outposts\*.py" ".\" >>Process_Log.txt
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
copy ".\header_*.py" "..\Source\Source - Floris Expanded Mod Pack\header files\" >>Process_Log.txt
copy ".\ID_*.py" "..\Source\Source - Floris Expanded Mod Pack\ID files\" >>Process_Log.txt
copy ".\process_*.py" "..\Source\Source - Floris Expanded Mod Pack\process files\" >>Process_Log.txt
python other_files.py
move ".\Process_Log.txt" "..\Compiled Files\"
@del *.pyc
@del *.py
@del ground_spec_codes.h
echo.
echo Cleaning up...
echo ______________________________
echo 1. Create Alternative Files - Done
echo 2. Floris Basic Mod Pack - Done
echo 3. Floris Expanded Mod Pack - Done
echo 4. Floris Gameplay Mod Pack - In progress
echo 5. Floris Dev Suite
echo 6. Creating the 7zip file
echo 7. Creating the installer
echo ______________________________
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
echo Copy Files...
copy "..\Files\Operations\gameplay_files.py" ".\" >>Process_Log.txt
python gameplay_files.py
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
echo Cleaning up...
echo ______________________________
echo 1. Create Alternative Files - Done
echo 2. Floris Basic Mod Pack - Done
echo 3. Floris Expanded Mod Pack - Done
echo 4. Floris Gameplay Mod Pack - Done
echo 5. Floris Dev Suite - In progress
echo 6. Creating the 7zip file
echo 7. Creating the installer
echo ______________________________
echo Copy Files...
copy "..\Module Info\*.*" ".\" >>Process_Log.txt
copy "..\Files\Operations\dev_suite_files.py" ".\" >>Process_Log.txt
python info.py
python dev_suite_files.py
@del *.pyc
@del *.py
echo.
echo Cleaning up...
echo ______________________________
echo 1. Create Alternative Files - Done
echo 2. Floris Basic Mod Pack - Done
echo 3. Floris Expanded Mod Pack - Done
echo 4. Floris Gameplay Mod Pack - Done
echo 5. Floris Dev Suite - Done
echo 6. Creating the 7zip file - In progress
echo 7. Creating the installer
echo ______________________________
"C:\Program Files\7-Zip\7z.exe" a -mx9 -t7z "G:\lan\Mount&Blade Warband\Modules\floris.7z" "G:\lan\Mount&Blade Warband\Modules\Floris*" "G:\lan\Mount&Blade Warband\Modules\Readme.txt"
move "G:\lan\Mount&Blade Warband\Modules\Floris.7z" "..\Installer\Floris.7z"
echo ______________________________
echo 1. Create Alternative Files - Done
echo 2. Floris Basic Mod Pack - Done
echo 3. Floris Expanded Mod Pack - Done
echo 4. Floris Gameplay Mod Pack - Done
echo 5. Floris Dev Suite - Done
echo 6. Creating the 7zip file - Done
echo 7. Creating the installer - In progress
echo ______________________________
"C:\Program Files (x86)\Inno Setup 5\Compil32.exe" /cc "..\Installer\floris_installer_setup.iss"
echo ______________________________
echo 1. Create Alternative Files - Done
echo 2. Floris Basic Mod Pack - Done
echo 3. Floris Expanded Mod Pack - Done
echo 4. Floris Gameplay Mod Pack - Done
echo 5. Floris Dev Suite - Done
echo 6. Creating the 7zip file - Done
echo 7. Creating the installer - Done
echo ______________________________
echo.
echo All Finished ...
echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to exit. . .
pause>nul