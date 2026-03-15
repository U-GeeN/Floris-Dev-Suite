from module_info import *

import shutil, os, glob

export_dir_music = export_dir_main + export_dir_gameplay + "./Music/"
export_dir_resource = export_dir_main + export_dir_gameplay + "./Resource/"
export_dir_sceneobj = export_dir_main + export_dir_gameplay + "./SceneObj/"
export_dir_sounds = export_dir_main + export_dir_gameplay + "./Sounds/"
export_dir_textures = export_dir_main + export_dir_gameplay + "./Textures/"

if os.path.exists(export_dir_music):
    shutil.rmtree(export_dir_music)

if os.path.exists(export_dir_resource):
    shutil.rmtree(export_dir_resource)

if os.path.exists(export_dir_sceneobj):
    shutil.rmtree(export_dir_sceneobj)

if os.path.exists(export_dir_sounds):
    shutil.rmtree(export_dir_sounds)

if os.path.exists(export_dir_textures):
    shutil.rmtree(export_dir_textures)

print "Copying Music..."
shutil.copytree("../Files/Music/",export_dir_music,ignore=shutil.ignore_patterns("ext*"))
print "Copying Resources..."
shutil.copytree("../Files/Resource/",export_dir_resource,ignore=shutil.ignore_patterns("exp*","ext*"))
print "Copying Scenes..."
shutil.copytree("../Files/SceneObj/Native/",export_dir_sceneobj,ignore=shutil.ignore_patterns("*arena.sco","scn_castle_*_exterior.sco","scn_training_ground_*"))

files1 = glob.iglob(os.path.join("../Files/SceneObj/Arena Overhaul Mod v1.0/", "*.sco"))
for file in files1:
    if os.path.isfile(file):
        shutil.copy2(file,export_dir_sceneobj)

files2 = glob.iglob(os.path.join("../Files/SceneObj/El Arte De La Guerra UNOFFICIAL Siege Fix v1.5.3/", "*.sco"))
for file in files2:
    if os.path.isfile(file):
        shutil.copy2(file,export_dir_sceneobj)

files3 = glob.iglob(os.path.join("../Files/SceneObj/Historic Castles Project - the British Isles v1.2/", "*.sco"))
for file in files3:
    if os.path.isfile(file):
        shutil.copy2(file,export_dir_sceneobj)

files4 = glob.iglob(os.path.join("../Files/SceneObj/Training Fields v1.0/", "*.sco"))
for file in files4:
    if os.path.isfile(file):
        shutil.copy2(file,export_dir_sceneobj)

files5 = glob.iglob(os.path.join("../Files/SceneObj/Utrehd's Castle Pack v.0.32/", "*.sco"))
for file in files5:
    if os.path.isfile(file):
        shutil.copy2(file,export_dir_sceneobj)

files6 = glob.iglob(os.path.join("../Files/SceneObj/Outposts kit v0.8/", "*.sco"))
for file in files6:
    if os.path.isfile(file):
        shutil.copy2(file,export_dir_sceneobj)

files7 = glob.iglob(os.path.join("../Files/SceneObj/Sea Battles Mk. II & Misc Scenes v1.0/", "*.sco"))
for file in files7:
    if os.path.isfile(file):
        shutil.copy2(file,export_dir_sceneobj)

files8 = glob.iglob(os.path.join("../Files/SceneObj/Warband Entrenched v1.1/", "*.sco"))
for file in files8:
    if os.path.isfile(file):
        shutil.copy2(file,export_dir_sceneobj)

print "Copying Sounds..."
shutil.copytree("../Files/Sounds",export_dir_sounds,ignore=shutil.ignore_patterns("ext*"))
print "Copying Textures..."
shutil.copytree("../Files/Textures",export_dir_textures,ignore=shutil.ignore_patterns("exp*","ext*"))
