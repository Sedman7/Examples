import numpy as np

a = np.array([0, 1, 2])			#произвольный массив
aOne = np.ones(5)				#массив из 5 элементов заполненный "1"
aZero = np.zeros(3)				#массив из 3 элементов заполненный "0"
aRnd = np.random.random(4)  	#массив из 4 элементов заполненных рандом 0..1
aRndT = np.random.random(4)*10  #рандом массив 0..10

print("\n", a, "\n", aOne, "\n", aZero, "\n", aRnd, "\n", aRndT)


