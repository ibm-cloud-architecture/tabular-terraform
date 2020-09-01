cython -o ../build/transform.c --embed  ../source/transform.py
cc -c ../build/transform.c -o ../build/transform.o -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g

cc ../build/transform.o -o ../build/transform -L/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/config-3.8-darwin -lpython3.8 -ldl -framework CoreFoundation

BINDIR="../bin"
if [ ! -d "$BINDIR" ]; then
  mkdir ../bin
fi

cp ../build/transform ../bin/transform
