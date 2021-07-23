import A2Part1
import A2Part2
import A2Part3
import A2Part4
import A2Part5

import numpy as np

print("=====A2Part1=====")
print(A2Part1.genSine(A=1.0, f=10.0, phi=1.0, fs=50.0, t=0.1))

print("=====A2Part2=====")
print(A2Part2.genComplexSine(1,5))

print("=====A2Part3=====")
print(A2Part3.DFT(np.array([1, 2, 3, 4])))

print("=====A2Part4=====")
print(A2Part4.IDFT(np.array([1 ,1 ,1 ,1])))

print("=====A2Part5=====")
print(A2Part5.genMagSpec(np.array([1, 2, 3, 4])))
