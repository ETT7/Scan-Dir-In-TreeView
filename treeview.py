import os
import logging

path = os.path.join(os.getcwd(),'scan\\')
logging.basicConfig(filename="scaned_dirs_treeview.log", 
					format='%(message)s', 
					filemode='a+')
logger=logging.getLogger()
logger.setLevel(logging.INFO)
f = open("scaned_dirs_treeview.log","w+")
f.write("***Dirs In TreeViews***\n\n")
f.close()
for dirpath, dirnames, filenames in os.walk(path):
    directory_level = dirpath.replace(path, "")
    directory_level = directory_level.count(os.sep)
    indent = " " * 4
    print("{}{}\\".format(indent*directory_level, os.path.basename(dirpath)))
    logger.info("{}{}\\".format(indent*directory_level, os.path.basename(dirpath)))
    for f in filenames:
        print("{}{}".format(indent*(directory_level+1), f))
        logger.info("{}{}".format(indent*(directory_level+1), f))
