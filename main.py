import jpype
import jpype.imports

import jpype
import jpype.imports

jpype.startJVM(classpath = ['build/libs/*'])

from dummy.kt.jpype import IterablesJava, IterablesKt

iterable = IterablesJava.intRange(1, 10) # works
iterator = iterable.iterator() # works
print(iterator.next()) # 1

for x in IterablesJava.intRange(1, 10): # works
    print('java', x)

iterable = IterablesKt.intRange(1, 10) # doesn't work
iterator = iterable.iterator() # doesn't work
print(iterator.next()) # doesn't work

for x in IterablesKt.intRange(1, 10): # doesn't work
    print('kotlin', x) 
