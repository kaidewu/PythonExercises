import os
from datetime import datetime
import zipfile
from zipfile import ZipFile

date = datetime.now()
formato = date.strftime('%Y%m%d')
backup = zipfile.ZipFile(f"{formato}.zip", "w")
dir_actual = 'C:\\Users\\kayfe\\Documents\\ASO'

for directorio, subdirectorio, ficheros in os.walk('C:\\Users\\kayfe\\Documents\\ASO'):
    for f in ficheros:
        if not f.endswith(".zip"):
            backup.write(os.path.join(directorio, f), os.path.relpath(os.path.join(directorio, f), dir_actual))
            os.popen(f"attrib -a /s {f}")

backup.close()