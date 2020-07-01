from cec17_functions import cec17_test_func
from cma import *
from cma.sigma_adaptation import *
import os

class Wrapper:
	def __init__(self, dims, func):
		self.dims = dims
		self.func = func
	
	def compute(self, arg):
		f = [0]
		cec17_test_func(arg, f, self.dims, 1, self.func)
		return f[0]

# x: Solution vector
x = 10*[0]
# nx: Number of dimensions
nx = 10
# mx: Number of objective functions
mx = 1
# func_num: Function number
func_num = 1
# Pointer for the calculated fitness
f = [0]
#print(os.path.abspath('cec17_test_func'))
#print()
cec17_test_func(x, f, nx, mx, func_num)
print(f[0])

wrapper = Wrapper(10, 1)

adapt_method = [CMAAdaptSigmaMedianImprovement, CMAAdaptSigmaTPA, CMAAdaptSigmaCSA]
dims = [2]
funcs = [i for i in range(1, 31) if i not in [2]]
sigma = 1
start_point = [0]
bounds = [-100, 100]
verbosity = -1
verblog = 11

variants = [(a, b, c) for a in adapt_method for b in dims for c in funcs]

for v in variants:
    am = v[0]
    ams = ""
    if(isinstance(am, CMAAdaptSigmaMedianImprovement)):
        ams = "Med"
    if(isinstance(am, CMAAdaptSigmaTPA)):
        ams = "TPA"
    if(isinstance(am, CMAAdaptSigmaCSA)):
        ams = "CSA"
    dim = v[1]
    func = v[2]

    wrapper = Wrapper(dim, func)

    res = fmin(
                wrapper.compute,
                dim * start_point,
                sigma,
                options={
                            'AdaptSigma': am,
                            'bounds': [-100, 100],
                            'verbose': verbosity,
                            'verb_log': verblog,
			                'verb_filenameprefix': os.path.join(CMADataLogger.default_prefix, "Test_" + ams + "_" + str(dim) + "_" + str(func), "") # słownik z opcjami algorytmu
                        }
              )



res = fmin(
		wrapper.compute, # funkcja minimalizowana
		10 * [-100], # początkowe rozwiązanie
		1, # długość kroku sigma
		options = {'verbose':-1, # -9 żeby się zamknął
                'bounds': [-100, 100] , # ograniczenia. Wartości recyklowane, jeśli wyjdziesz za indeks. Początkowe rozwiązanie musi się w nich mieścić, bo inaczej się obrazi
			   'verb_log': 1, 
			   'verb_filenameprefix': os.path.join(CMADataLogger.default_prefix, "Test_" + str(wrapper.func) + "_" + str(wrapper.dims), "")} # słownik z opcjami algorytmu
	  )



