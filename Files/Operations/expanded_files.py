from module_info import *

import shutil
import os

export_dir_music = export_dir_main + export_dir_expanded + "./Music/"
export_dir_resource = export_dir_main + export_dir_expanded + "./Resource/"
export_dir_sceneobj = export_dir_main + export_dir_expanded + "./SceneObj/"
export_dir_sounds = export_dir_main + export_dir_expanded + "./Sounds/"
export_dir_textures = export_dir_main + export_dir_expanded + "./Textures/"

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
shutil.copytree("../Files/Music/",export_dir_music)
print "Copying Resources..."
shutil.copytree("../Files/Resource/",export_dir_resource)
print "Copying Scenes..."
shutil.copytree("../Files/SceneObj/Expanded/",export_dir_sceneobj)
print "Copying Sounds..."
shutil.copytree("../Files/Sounds",export_dir_sounds)
print "Copying Textures..."
shutil.copytree("../Files/Textures",export_dir_textures)
