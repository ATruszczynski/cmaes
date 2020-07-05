from cec17_functions import cec17_test_func
#import cec17_functions2
from cma import *
from cma.sigma_adaptation import *
import os
from timeit import default_timer as timer
from joblib import Parallel, delayed
import concurrent.futures


class Wrapper:
	def __init__(self, dims, func):
		self.dims = dims	
		self.func = func
	
	def compute(self, arg):
		f = [0]
		cec17_test_func(arg, f, self.dims, 1, self.func)
		return f[0]

adapt_method = [CMAAdaptSigmaMedianImprovement, CMAAdaptSigmaTPA, CMAAdaptSigmaCSA]
dims = [10, 30, 50]
funcs = [i for i in range(1, 31) if i not in [2]]
sigma = 50 # dokumentacje mówi o 1/4 przedziału w którym spodziewamy się optimum
start_point = [0]
bounds = [-100, 100]
verbosity = -1
verblog = 100
seed = None #!!! Change to 0 or None before tests
rep = range(50) # tu zmienić na swój zakres
filesToRemove = ["axlen.dat", "axlencorr.dat", "axlenprec.dat", "stddev.dat"] # tu trzeba uzupełnić to czego nie chcemy
max_proc = None

variants = [[a, b, c, d] for a in dims for b in funcs for c in adapt_method for d in rep]


#for t in tasks:
#    print(t)   

start = timer()
def job(v):
    dim = v[0]
    func = v[1]
    am = v[2]
    ams = ""
    if(am == CMAAdaptSigmaMedianImprovement):
        ams = "Med"
    if(am == CMAAdaptSigmaTPA):
        ams = "TPA"
    if(am == CMAAdaptSigmaCSA):
        ams = "CSA"
    rep = v[3]
    wrapper = Wrapper(dim, func)

    folderName = os.path.join(CMADataLogger.default_prefix, str(dim), str(func), ams, str(rep), "")
#    folderName = os.path.join(CMADataLogger.default_prefix, str(dim)+ str(func)+ ams+ str(rep))

    res = fmin(
                wrapper.compute,
                dim * start_point,
                sigma,
                options={
			    'seed': seed,
                            'AdaptSigma': am,
                            'bounds': bounds,
                            'verbose': verbosity,
                            'verb_log': verblog,
			    'verb_filenameprefix': folderName 
                        } # słownik z opcjami algorytmu
              )
    for filee in filesToRemove:
        os.remove(os.path.join(folderName, filee))

#Parallel(prefer="threads")(delayed(job)(v) for v in variants)
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_proc) as executor:
            for out1 in executor.map(job, variants):
                der = 2

#job(variants[0])
end = timer()
print("\nExecution time:")
print(end - start)





