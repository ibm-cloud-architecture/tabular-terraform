cython -o ../build/terraformer.c --embed  ../source/terraformer.py
cc -c ../build/terraformer.c -o ../build/terraformer.o -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g

cython -o ../build/constants.c ../source/constants.py
cc -c ../build/constants.c -o ../build/constants.o -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g

cython -o ../build/extractors.c ../source/extractors.py
cc -c ../build/extractors.c -o ../build/extractors.o -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g

cython -o ../build/generators.c ../source/generators.py
cc -c ../build/generators.c -o ../build/generators.o -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g

cython -o ../build/helpers.c ../source/helpers.py
cc -c ../build/helpers.c -o ../build/helpers.o -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g

cython -o ../build/messages.c ../source/messages.py
cc -c ../build/messages.c -o ../build/messages.o -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g

cython -o ../build/structures.c ../source/structures.py
cc -c ../build/structures.c -o ../build/structures.o -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g

cc ../build/terraformer.o ../build/constants.o ../build/extractors.o ../build/generators.o ../build/helpers.o ../build/messages.o ../build/structures.o -o ../build/terraformer -L/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/config-3.8-darwin -lpython3.8 -ldl -framework CoreFoundation

cp ../build/terraformer ../bin/terraformer
