from module_info import *

import shutil
import os

if not os.path.exists(export_dir):
    os.makedirs(export_dir)

export_dir_data = export_dir_main + export_dir_expanded + "./Data/"
export_dir_music = export_dir_main + export_dir_expanded + "./Music/"
export_dir_resource = export_dir_main + export_dir_expanded + "./Resource/"
export_dir_sceneobj = export_dir_main + export_dir_expanded + "./SceneObj/"
export_dir_sounds = export_dir_main + export_dir_expanded + "./Sounds/"
export_dir_textures = export_dir_main + export_dir_expanded + "./Textures/"

if not os.path.exists(export_dir_data):
    os.makedirs(export_dir_data)

if not os.path.exists(export_dir_music):
    os.makedirs(export_dir_music)

if not os.path.exists(export_dir_resource):
    os.makedirs(export_dir_resource)

if not os.path.exists(export_dir_sceneobj):
    os.makedirs(export_dir_sceneobj)

if not os.path.exists(export_dir_sounds):
    os.makedirs(export_dir_sounds)

if not os.path.exists(export_dir_textures):
    os.makedirs(export_dir_textures)