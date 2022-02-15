import sys
import os
import shutil

if len(sys.argv) >= 3:
        if not os.path.exists(sys.argv[-1]):
            os.mkdir(sys.argv[-1])
            for j in range(1, (len(sys.argv) - 1)):
                if not os.path.exists(sys.argv[j]):
                    print(f"El fichero {sys.argv[j]} no existe")
                else:
                    shutil.copy(sys.argv[j],sys.argv[-1])
        else:
            for k in range(1, (len(sys.argv) - 1)):
                shutil.copy(sys.argv[k],sys.argv[-1])
else:
    print("No has puestos los valores adecuados")