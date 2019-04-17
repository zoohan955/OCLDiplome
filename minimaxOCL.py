import numpy as np
import pyopencl as cl
import pyopencl.array as cl_array
from pyopencl.elementwise import ElementwiseKernel
from pyopencl.reduction import ReductionKernel
import time
ctx = cl.create_some_context(0)
queue = cl.CommandQueue(ctx)

X=[]
Y=[]
quantity_el = 50000000
sR_0, sR_1 = 0, 5000
step = 1000
arr1 = cl_array.to_device(queue, np.random.rand(quantity_el).astype(np.float32))
arr2 = arr1
with open("X.txt", "r") as file:
        X = file.read().splitlines() 

with open("Y.txt", "r") as file:
        Y = file.read().splitlines() 

x=np.asarray(X)
y=np.asarray(Y)
x=np.float32(x)
y=np.float32(x)
XX=cl_array.to_device(queue,x)
YY=cl_array.to_device(queue,y)
mf = cl.mem_flags

V=cl.array.empty_like(arr1)

Xmax=np.float(max(X))
Ymax=np.float(max(Y))
Xmin=np.float(min(X))
Ymin=np.float(min(Y))


miniMax = ElementwiseKernel(ctx, "float *x,float Xmax,float Xmin,float *v", 


"v[i] = (x[i]-Xmin)/(Xmax-Xmin);", "sum")

def START():
        miniMax(arr1,Xmax,Xmin,V)
        start_timer = time.time()
        print('Timer: on')
        time_working = time.time()-start_timer
        print('\nTimer: stop; time: {} seconds'.format(round(time_working,3)))




START()
print("V: {}".format(V))


