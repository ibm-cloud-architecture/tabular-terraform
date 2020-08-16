cython -o ../build/terraformer.c --embed  ../source/terraformer.py
cc -c ../build/terraformer.c -o ../build/terraformer.o -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g

cc ../build/terraformer.o -o ../build/terraformer -L/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/config-3.8-darwin -lpython3.8 -ldl -framework CoreFoundation

BINDIR="../bin"
if [ ! -d "$BINDIR" ]; then
  mkdir ../bin
fi

cp ../build/terraformer ../bin/terraformer
