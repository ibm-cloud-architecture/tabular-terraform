cython -o ../build/tabularterraform.c --embed  ../src/tabularterraform.py
cc -c ../build/tabularterraform.c -o ../build/tabularterraform.o -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g

cc ../build/tabularterraform.o -o ../build/tabularterraform -L/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/config-3.8-darwin -lpython3.8 -ldl -framework CoreFoundation

BINDIR="../bin"
if [ ! -d "$BINDIR" ]; then
  mkdir ../bin
fi

cp ../build/tabularterraform ../bin/tabularterraform
