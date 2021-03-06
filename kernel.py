import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import scipy
import math
import statistics
import string
import re
import pyopencl as cl
import time
from pyopencl.elementwise import ElementwiseKernel
from pyopencl.reduction import ReductionKernel
import pyopencl.array
import pyopencl.array as cl_array  # Import PyOpenCL Array (a Numpy array plus an OpenCL buffer object)



pVar=0
X=[]
Y=[]
arrY=[]
arrX=[]


# a_np=np.asarray(X)
# b_np=np.asarray(Y)

class DataSets(object):
    def __init__(self,A=[],B=[]):
        self.A=A
        self.B=B

# DataSet=DataSets(list(a_np),list(b_np))
DataSet=DataSets(arrX,arrY)
#DataSet=DataSets(list(a_np),list(b_np))


def Pearson(X,Y):
    len1=len(X)
    Xsum=sum(X)
    Ysum=sum(Y)

    # Mx=AVERAGE(Xsum,len1)
    # My=AVERAGE(Ysum,len1)
    #print(Mx,"___",My)
    dX=[]
    sumpowX=0
    sumpowY=0
    DxDy=0
    Rxy=0
    for i in range(len(X)):
        dX=X[i]-Mx
        sumpowX+=math.pow(dX,2)
        dY=Y[i]-My
        sumpowY+=math.pow(dY,2)
        DxDy+=dX*dY
       
    Rxy=(DxDy)/math.sqrt(sumpowX*sumpowY) 
    return(Rxy)


def descriptiveX(X):
    lenX=len(X)
    meanX=np.mean(X)
    minX=min(X)
    maxX=max(X)
    stdX=np.std(X)
    KvartilsA=[]
    KvartilsA.append((np.percentile(X, 25), np.percentile(X, 50), np.percentile(X, 75))) # квартили A
    modaX=st.mode(X)
    excessX=st.kurtosis(X)
    assymX=st.skew(X)
    resultX=[]
    resultX.append("Len_A="+str(lenX))
    resultX.append("Mean_A="+str(meanX))
    resultX.append("Min_A="+str(minX))
    resultX.append("Max_A="+str(maxX))
    resultX.append("Std_A="+str(stdX))
    resultX.append("Kvartils_A="+str(KvartilsA))
    resultX.append("Moda_A="+str(modaX))
    resultX.append("Excess_A="+str(excessX))
    resultX.append("Assym_A="+str(assymX))
    return resultX

def descriptiveY(Y):
    lenY=len(Y)
    meanY=np.mean(Y)
    minY=min(Y)
    maxY=max(Y)
    stdY=np.std(Y)
    KvartilsB=[]
    KvartilsB.append((np.percentile(Y, 25), np.percentile(Y, 50), np.percentile(Y, 75))) # квартили B
    modaY=st.mode(Y)
    excessY=st.kurtosis(Y)
    assymY=st.skew(Y)
    resultY=[]
    resultY.append("Len_B="+str(lenY))
    resultY.append("Mean_B="+str(meanY))
    resultY.append("Min_B="+str(minY))
    resultY.append("Max_B="+str(maxY))
    resultY.append("Std_B="+str(stdY))
    resultY.append("Kvartils_B="+str(KvartilsB))
    resultY.append("Moda_B="+str(modaY))
    resultY.append("Excess_B="+str(excessY))
    resultY.append("Assym_B="+str(assymY))
    return resultY



#----------------------------CRITERIA--------------------------------
def Pirson(X,Y):
    
    result= scipy.stats.pearsonr(X,Y)

    print(Y)
    print(st.shapiro(X))
    print(st.shapiro(Y))
    return('PearsonResult('+'correlation='+str(result[0])+', pvalue='+str(result[1])+')')

def PirsonGraph(event):
    Pirson(X,Y)

def Spirmen(X,Y):
    return(scipy.stats.spearmanr(X,Y))

def PointCorr(X,Y):
    return(scipy.stats.pointbiserialr(X,Y))

def miniMax(X1,Y1):
    global arrX
    global arrY
    Xmax=max(X1)
    Xmin=min(X1)
    Ymax=max(Y1)
    Ymin=min(Y1)
    denumX=Xmax-Xmin
    denumY=Ymax-Ymin

    for i in X1:
        arrX.append((i-Xmin)/(Xmax-Xmin))

    for i in Y1:
        arrY.append((i-Ymin)/(Ymax-Ymin))

    global DataSet
   
    return DataSet.A,DataSet.B
    




def scale(X,Y):
    scaleArrY=[]
    scaleArrX=[]
    for i in Y:
        scaleArrY.append(i/pow(10,8))
    for i in X:
        scaleArrX.append(i/pow(10,8))
        
    print (scaleArrY)
    print (scaleArrX)






def PointCorrGraph(event):
    PointCorr(X,Y)

def PearsonGraph(event):
    Pearson(X,Y)



def SpearmenGraph():
    Spirmen(X,Y)
    
def Graphics(event):
    Graphical(X,Y)

def Shapiro(X,Y):
    return {"X_DATA":st.shapiro(X),"Y_DATA":st.shapiro(Y)}
   

def OneWayTest(X,Y):
    return(scipy.stats.f_oneway(X,Y))

def OneWayTestGraph(event):
    OneWayTest(X,Y)

def KSSYMBOL(X,Y):
   return(scipy.stats.ks_2samp(X,Y))

def normalTest(X):
    return(scipy.stats.normaltest(X))

def OCL_NORMALIZE(X1,Y1):
    global arrX
    global arrY

    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    x=np.asarray(X1)
    y=np.asarray(Y1)
    x=np.float32(X1)
    y=np.float32(Y1)
    XX=cl_array.to_device(queue,x)
    YY=cl_array.to_device(queue,y)
    mf = cl.mem_flags

    V=cl.array.empty_like(XX)
    V1=cl.array.empty_like(YY)

    Xmax=np.float(max(x))
    Ymax=np.float(max(y))
    Xmin=np.float(min(x))
    Ymin=np.float(min(y))

    miniMaxX = ElementwiseKernel(ctx, "float *x,float Xmax,float Xmin,float *v", 
"v[i] = (x[i]-Xmin)/(Xmax-Xmin);", "sum")

    miniMaxY = ElementwiseKernel(ctx, "float *y,float Ymax,float Ymin,float *v", 
"v[i] = (y[i]-Ymin)/(Ymax-Ymin);", "sum")

    start_timer = time.time()
    print('Timer: on')
    miniMaxX(XX,Xmax,Xmin,V)
    miniMaxY(YY,Ymax,Ymin,V1)

    arrX = V.T.get()
    arrY = V1.T.get()
  
    print(arrX)
    print(arrY)

    time_working = time.time()-start_timer
    print('\nTimer: stop; time: {} seconds'.format(round(time_working,3)))
    global DataSet
    DataSet=DataSets(arrX,arrY)
    return
#--------------------------------------------------------------------




def med():
    return("Median of data-set is : % s "
        % (statistics.median(X))) 


def randomNumbers(a):
    return [np.random.choice([i for i in range(a)]) for j in range(a)]


def digression(X,L,Average):
    for i in range (len(X)):
       return X[i]-Average
       



#DATA READ AND CONVERT
Xx=[]
Yy=[]
A=0
B=0
processedArr_1=[]

processedArr_2=[] 

def dataProcess(file_name):
     print(file_name)
     with open(file_name) as file:
        RAW_DATA=file.read()

        rows = RAW_DATA.split('\n')
        DATA=[]
        for row in rows:
            COL_DATA=re.compile("[\t\s]+",re.I|re.M).split(row)
            DATA.append(COL_DATA)
        

        Seconds_1_Trimmed=DATA[0][1].strip()
        Seconds_1=int(Seconds_1_Trimmed.split(':')[2])
        Seconds_2_Trimmed=DATA[1][1].strip()
        Seconds_2=int(Seconds_2_Trimmed.split(':')[2])
        step=Seconds_2-Seconds_1
       
        return{'step':step,'DATA':DATA}
           

def dataPrieview(file_name):
    print(file_name)
    with open (file_name) as file:
        RAW_DATA=file.read()
        DATA = RAW_DATA.split('\n')
        del DATA [4:]
        return(DATA)



def reduceData(file_name1,file_name2):
    data1=dataProcess(file_name1)
    data2=dataProcess(file_name2)
    print(type(data1['step']))
    step1=data1['step']
    step2=data2['step']
    maxStep=max(step1,step2)
    print(len(data1['DATA'])-1)
    print(maxStep/step1)
    print(A,B)

    global X
    X=[]
    for i in range(0,len(data1['DATA'])-1,int(maxStep/step1)):
    # for i in range(0,len(data1['DATA'])-346,int(maxStep/step1)):
        el=data1['DATA'][i][A]
        X.append(float(el))
        
    global Y
    Y=[]
    for i in range(0,len(data2['DATA'])-1,int(maxStep/step2)):
        el=data2['DATA'][i][B]
        Y.append(float(el))
    print(len(X))
    print(len(Y))


def Graphical(A,B):
    dataX=A
    dataY=B
    bins=400

    #X
    plt.subplot(2,2,2)
    plt.boxplot(dataX)
    plt.title('X Data')
    plt.grid(True)

    plt.subplot(2,2,1)
    plt.hist(dataX,bins)
    plt.title('X Data')
    plt.grid(True)

    #Y
    plt.subplot(2,2,3)
    plt.hist(dataY,bins)
    plt.title('Y Data')
    plt.grid(True)


    plt.subplot(2,2,4)
    plt.boxplot(dataY)
    plt.title('Y Data')
    plt.grid(True)
    plt.show() 

    
