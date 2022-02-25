import os
import logging

path = os.path.join(os.getcwd(),'scan_dir')
logging.basicConfig(filename="scaned_dirs_treeview.log", 
					format='%(message)s', 
					filemode='a+')
logger=logging.getLogger()
logger.setLevel(logging.INFO)
for dirpath, dirnames, filenames in os.walk(path):
    directory_level = dirpath.replace(path, "")
    directory_level = directory_level.count(os.sep)
    indent = " " * 4
    print("{}{}/".format(indent*directory_level, os.path.basename(dirpath)))
    for f in filenames:
        logger.info("{}{}".format(indent*(directory_level+1), f))