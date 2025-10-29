import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	m = len(a)
	n = len(a[0])
	o = np.zeros((n, m))
	
	for i in range(len(a)):
		for j in range(len(a[0])):
			o[j][i] = a[i][j]
	# print(o)
	return o