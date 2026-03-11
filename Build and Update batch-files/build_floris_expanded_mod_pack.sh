#!/bin/bash
cd "$(dirname "$0")"
shopt -s nullglob

echo "Creating Floris Expanded Mod Pack"

cp ../"Source/Source - Floris Expanded Mod Pack/header files/"*.py . >> Process_Log.txt
cp ../"Source/Source - Floris Expanded Mod Pack/ID files/"*.py . >> Process_Log.txt
cp ../"Source/Source - Floris Expanded Mod Pack/process files/"*.py . >> Process_Log.txt
cp ../"Files/Specific Textures/Expanded/warrider_logo.dds" ./ >> Process_Log.txt

echo "Start Processing..."

cp "../Files/Other Files/Expanded/"* ./ 2>/dev/null >> Process_Log.txt
cp "../Source/Source - Floris Expanded Mod Pack/Module/"* ./ >> Process_Log.txt
cp "../Source/Source - Floris Expanded Mod Pack/Data/"* ./ 2>/dev/null >> Process_Log.txt
cp "../Source/Source - Floris Expanded Mod Pack/Variables/"* ./ 2>/dev/null >> Process_Log.txt
cp "../Source/Source - Floris Expanded Mod Pack/Other Files/"* ./ 2>/dev/null >> Process_Log.txt
cp "../Module Info/"* ./ 2>/dev/null >> Process_Log.txt
cp "../Source/Files for Batch/"* ./ 2>/dev/null >> Process_Log.txt

python info.py
python dircreate.py

echo "Copy Files..."
cp "../Files/Operations/expanded_files.py" ./ >> Process_Log.txt
python expanded_files.py

cp "../Source/Modmerger/"*.py ./ >> Process_Log.txt
cp "../Source/Source Kits/Character Creation/"*.py ./ >> Process_Log.txt
cp "../Source/Source Kits/Companions Overview/"*.py ./ >> Process_Log.txt
cp "../Source/Source Kits/Dynamic Arrays/"*.py ./ >> Process_Log.txt
cp "../Source/Source Kits/Expanded Scenes/"*.py ./ >> Process_Log.txt
cp "../Source/Source Kits/Freelancer/"*.py ./ >> Process_Log.txt
cp "../Source/Source Kits/Formations/"*.py ./ >> Process_Log.txt
cp "../Source/Source Kits/Kingdom Management Tools/"*.py ./ >> Process_Log.txt
cp "../Source/Source Kits/Tournament Enhancements/"*.py ./ >> Process_Log.txt
cp "../Source/Source Kits/Prebattle OD/"*.py ./ >> Process_Log.txt
cp "../Source/Source Kits/Outposts/"*.py ./ >> Process_Log.txt

echo "______________________________"
echo

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

cp -f ./header_*.py "../Source/Source - Floris Expanded Mod Pack/header files/" 2>/dev/null >> Process_Log.txt
cp -f ./ID_*.py "../Source/Source - Floris Expanded Mod Pack/ID files/" 2>/dev/null >> Process_Log.txt
cp -f ./process_*.py "../Source/Source - Floris Expanded Mod Pack/process files/" 2>/dev/null >> Process_Log.txt

python other_files.py
mv Process_Log.txt "../Compiled Files/"

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
read -p "Press any key to exit . . ."