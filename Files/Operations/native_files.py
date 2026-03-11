from module_info import *

import shutil
import os

export_dir_sceneobj = export_dir_main + export_dir_native + "/SceneObj/"

if os.path.exists(export_dir_sceneobj):
    shutil.rmtree(export_dir_sceneobj)

print "Copying Scenes..."
shutil.copytree("../Files/SceneObj/Native/",export_dir_sceneobj)
