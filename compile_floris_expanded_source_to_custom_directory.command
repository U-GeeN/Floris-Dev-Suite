#!/bin/bash
cd "$(dirname "$0")"

echo "Compiling Floris Expanded Mod Pack to a custom directory"

LOG_FILE="Process_Log.txt"
touch "$LOG_FILE"

cp ./Source/Source\ -\ Floris\ Expanded\ Mod\ Pack/header\ files/* ./ >> "$LOG_FILE"
cp ./Source/Source\ -\ Floris\ Expanded\ Mod\ Pack/ID\ files/* ./ >> "$LOG_FILE"
cp ./Source/Source\ -\ Floris\ Expanded\ Mod\ Pack/process\ files/* ./ >> "$LOG_FILE"
cp ./Files/Other\ Files/Expanded/* ./ >> "$LOG_FILE"
cp ./Source/Source\ -\ Floris\ Expanded\ Mod\ Pack/Module/* ./ >> "$LOG_FILE"
cp ./Source/Source\ -\ Floris\ Expanded\ Mod\ Pack/Data/* ./ >> "$LOG_FILE"
cp ./Source/Source\ -\ Floris\ Expanded\ Mod\ Pack/Variables/* ./ >> "$LOG_FILE"
cp ./Source/Source\ -\ Floris\ Expanded\ Mod\ Pack/Other\ Files/* ./ >> "$LOG_FILE"
cp ./Module\ Info/* ./ >> "$LOG_FILE"
cp ./Source/Files\ for\ Batch/* ./ >> "$LOG_FILE"

python2 info.py

cp ./Source/Modmerger/*.py ./ >> "$LOG_FILE"
cp ./Source/Source\ Kits/Character\ Creation/*.py ./ >> "$LOG_FILE"
cp ./Source/Source\ Kits/Companions\ Overview/*.py ./ >> "$LOG_FILE"
cp ./Source/Source\ Kits/Dynamic\ Arrays/*.py ./ >> "$LOG_FILE"
cp ./Source/Source\ Kits/Expanded\ Scenes/*.py ./ >> "$LOG_FILE"
cp ./Source/Source\ Kits/Freelancer/*.py ./ >> "$LOG_FILE"
cp ./Source/Source\ Kits/Formations/*.py ./ >> "$LOG_FILE"
cp ./Source/Source\ Kits/Kingdom\ Management\ Tools/*.py ./ >> "$LOG_FILE"
cp ./Source/Source\ Kits/Tournament\ Enhancements/*.py ./ >> "$LOG_FILE"
cp ./Source/Source\ Kits/Prebattle\ OD/*.py ./ >> "$LOG_FILE"
cp ./Source/Source\ Kits/Outposts/*.py ./ >> "$LOG_FILE"

echo "______________________________"
echo

python2 process_init.py
python2 process_global_variables.py
python2 process_strings.py
python2 process_skills.py
python2 process_music.py
python2 process_animations.py
python2 process_meshes.py
python2 process_sounds.py
python2 process_skins.py
python2 process_map_icons.py
python2 process_factions.py
python2 process_items.py
python2 process_scenes.py
python2 process_troops.py
python2 process_particle_sys.py
python2 process_scene_props.py
python2 process_tableau_materials.py
python2 process_presentations.py
python2 process_party_tmps.py
python2 process_parties.py
python2 process_quests.py
python2 process_info_pages.py
python2 process_scripts.py
python2 process_mission_tmps.py
python2 process_game_menus.py
python2 process_simple_triggers.py
python2 process_dialogs.py
python2 process_global_variables_unused.py
python2 process_postfx.py
python2 Flora_kinds.py
python2 Ground_specs.py
python2 Skyboxes.py

cp ./header_*.py ./Source/Source\ -\ Floris\ Expanded\ Mod\ Pack/header\ files/ >> "$LOG_FILE"
cp ./ID_*.py ./Source/Source\ -\ Floris\ Expanded\ Mod\ Pack/ID\ files/ >> "$LOG_FILE"
cp ./process_*.py ./Source/Source\ -\ Floris\ Expanded\ Mod\ Pack/process\ files/ >> "$LOG_FILE"

python2 other_files_custom.py

mkdir -p "./Compiled Files"
mv "$LOG_FILE" "./Compiled Files/"

rm -f *.pyc
rm -f *.py
rm -f ground_spec_codes.h

echo
echo "______________________________"
echo
echo "All Finished ..."
echo "Cleaning up..."
echo "______________________________"
echo
echo "Script processing has ended."
echo "Press Enter to exit..."
read
