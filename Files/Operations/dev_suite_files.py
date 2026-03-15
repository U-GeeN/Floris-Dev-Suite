from module_info import *

import shutil, os, glob

export_dir_module = export_dir_main + "./Modules/"
export_dir_devsuite = export_dir_main + export_dir_devsuite

if os.path.exists(export_dir_devsuite):
    shutil.rmtree(export_dir_devsuite)

print "Copying Dev Suite..."

files1 = glob.iglob(os.path.join("../Files/Other Files/", "Readme.txt"))
for file in files1:
    if os.path.isfile(file):
        shutil.copy2(file,export_dir_module)

shutil.copytree("../",export_dir_devsuite)