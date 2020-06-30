from cec17_functions import cec17_test_func
from cma import *

class Wrapper:
	def __init__(self, dims, func):
		self.dims = dims
		self.func = func
	
	def compute(self, arg):
		f = [0]
		cec17_test_func(arg, f, self.dims, 1, self.func)
		return f[0]

# x: Solution vector
x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# nx: Number of dimensions
nx = 10
# mx: Number of objective functions
mx = 1
# func_num: Function number
func_num = 1
# Pointer for the calculated fitness
f = [0]

cec17_test_func(x, f, nx, mx, func_num)
print(f[0])

wrapper = Wrapper(10, 1)

res = fmin(
		wrapper.compute, # funkcja minimalizowana
		10 * [0], # początkowe rozwiązanie
		1, # długość kroku sigma
		options = {'verbose':-9} # słownik z opcjami algorytmu
	  )

print("Best solution: %s" % res[0])
print("Best value: %s" % res[1])


