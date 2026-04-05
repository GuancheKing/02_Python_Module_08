import sys
import os
import site

print(sys.executable)
print(os.getcwd())
print(os.path.exists("ruta"))
print(site.getsitepackages())