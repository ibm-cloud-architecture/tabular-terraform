cat ../source/copyright.py ../source/constants.py ../source/messages.py ../source/structures.py ../source/helpers.py ../source/extractors.py ../source/genpuml.py ../source/gentf.py ../source/terraformer.py > ../build/terraformerall.py

sed -i'.bak' -e 's/from copyright import */#/g' -e 's/from constants import */#/g' -e 's/from messages import */#/g' -e 's/from structures import */#/g' -e 's/from helpers import */#/g' -e 's/from extractors import */#/g' -e 's/from genpuml import */#/g' -e 's/from gentf import */#/g' ../build/terraformerall.py

sed -i'.bak2' -e 's/import os/#/g' -e 's/import sys/#/g' -e 's/import argparse/#/g' -e 's/import json/#/g' -e 's/import yaml/#/g' -e 's/import numpy as np/#/g' -e 's/import pandas as pd/#/g' ../build/terraformerall.py

echo 'import os' > ../build/imports.py
echo 'import sys' >> ../build/imports.py
echo 'import argparse' >> ../build/imports.py
echo 'import json' >> ../build/imports.py
echo 'import yaml' >> ../build/imports.py
echo 'import numpy as np' >> ../build/imports.py
echo 'import pandas as pd' >> ../build/imports.py

cat ../build/imports.py ../build/terraformerall.py > ../build/terraformer.py

cython -o ../build/terraformer.c --embed  ../build/terraformer.py
cc -c ../build/terraformer.c -o ../build/terraformer.o -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g

cc ../build/terraformer.o -o ../build/terraformer -L/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/config-3.8-darwin -lpython3.8 -ldl -framework CoreFoundation

BINDIR="../bin"
if [ ! -d "$BINDIR" ]; then
  mkdir ../bin
fi

cp ../build/terraformer ../bin/terraformer
