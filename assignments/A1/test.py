import A1Part1
import A1Part2
import A1Part3
import A1Part4

import numpy as np

print("=====A1Part1=====")
print(A1Part1.readAudio('../../sounds/piano.wav'))

print("=====A1Part2=====")
print(A1Part2.minMaxAudio('../../sounds/oboe-A4.wav'))

print("=====A1Part3=====")
print(A1Part3.hopSamples(np.arange(10),2))

print("=====A1Part4=====")
print(A1Part4.downsampleAudio('../../sounds/vibraphone-C6.wav',16))
