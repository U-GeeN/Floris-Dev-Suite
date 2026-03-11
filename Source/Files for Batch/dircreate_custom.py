from module_info import *

import shutil
import os

export_dir_main_custom = export_dir_main + "/Modules/" + export_dir_custom

if not os.path.exists(export_dir_main_custom):
    os.makedirs(export_dir_main_custom)

export_dir_data = export_dir_main + "/Modules/" + export_dir_custom + "/Data/"

if not os.path.exists(export_dir_data):
    os.makedirs(export_dir_data)