import glob
import logging
#from rdflib import Graph
import sys
from pyshex.utils.schema_loader import SchemaLoader
from io import StringIO

# set log level
logging.basicConfig(level=logging.INFO)

root_path = "../"

shex_file_extension = {".shex":"shex"}

for extension in shex_file_extension.keys() :
    files_to_check = "**/*" + extension
    for filename in glob.iglob(root_path + files_to_check, recursive=True):
         logging.info("Validating file " + filename)
         try:
             shex = open(filename,"r")
             log = StringIO()
             if isinstance(shex, str):
                 shex = SchemaLoader().loads(shex)
             else:
                 shex = SchemaLoader().load(shex)
                 shex['@context'] = "http://www.w3.org/ns/shex.jsonld"
         except Exception as e:
             logging.error(e)
             logging.error("Syntactic error reading ShEx file [" +filename+"]")
             sys.exit(1)
    else:
        print(f"The ShEx schema object is valid: {shex._is_valid()}")
        if not shex._is_valid(log):
            print(log.getvalue())

print("ShEx files syntactic validation is successful")
