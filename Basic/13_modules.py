### Modules ###

import my_module

my_module.sumValue(5, 6, 7)
my_module.printValue("Hola Python")

from my_module import sumValue, printValue

sumValue(5, 6, 7)
printValue("Hola Python")

import math

print(math.pow(2, 8))
print(math.pi)
print(math.sqrt(81))

from math import pi as PI_VALUE

print(PI_VALUE)


