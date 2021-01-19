import glob
import logging
#from rdflib import Graph
import sys

# set log level
logging.basicConfig(level=logging.INFO)

root_path = "../"

shex_file_extension = {".shex":"shex"}

for extension in shex_file_extension.keys() :
    files_to_check = "**/*" + extension
    for filename in glob.iglob(root_path + files_to_check, recursive=True):
         logging.info("Validating file " + filename)
         try:
             
             
         except Exception as e:
             logging.error(e)
             logging.error("Syntaxic error reading ShEx file [" +filename+"]")
             sys.exit(1)

print("ShEx files syntaxic validation is successful")
