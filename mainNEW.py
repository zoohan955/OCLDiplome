import matplotlib.pyplot as plt
#import pyopencl as ocl
import numpy as np
import scipy.stats as st
import scipy
import math
import statistics
import string
import re
#from UI2 import *




def MULT(X,Y):
    return list(map(lambda a,b:a*b,X,Y)) 
def SUM(X,Y):
    return list(map(lambda a,b:a+b,X,Y)) 
    
def AVERAGE(a,n):
    return a/n

mu=0.5
sigma=0.2
mu1=0.1
sigma1=0.08 

#X= np.random.normal(mu,sigma,100000)
#Y= np.random.normal(mu1,sigma1,100000)
#----------------------PLOTTING---------------------------
def Graphical(X,Y):
    data=np.concatenate((X,Y))
    bins=20
    #fig,axs=plt.subplots(1,3,figsize=(9,3))
    plt.subplot(2,2,1)
    plt.hist(data,bins)
    plt.subplot(2,2,2)
    plt.boxplot(data)
    plt.subplot(2,2,3)
    plt.scatter(X,Y)
    plt.subplot(2,2,4)
    plt.plot(data)
    
    plt.show() 
#---------------------------------------------------------
def Pearson(X,Y):
    len1=len(X)
    Xsum=sum(X)
    Ysum=sum(Y)

    Mx=AVERAGE(Xsum,len1)
    My=AVERAGE(Ysum,len1)
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
    #print("Pearson =", Rxy)
    return(Rxy)
    #print(Mx)

#----------------------------CRITERIA--------------------------------
def Pirson(X,Y):
    result= scipy.stats.pearsonr(X,Y)
    return('PearsonResult('+'correlation='+str(result[0])+', pvalue='+str(result[1])+')')

def PirsonGraph(event):
    Pirson(X,Y)

def Spirmen(X,Y):
    return(scipy.stats.spearmanr(X,Y))

def PointCorr(X,Y):
    return(scipy.stats.pointbiserialr(X,Y))
    

def PointCorrGraph(event):
    PointCorr(X,Y)

def PearsonGraph(event):
    Pearson(X,Y)



def SpearmenGraph():
    Spirmen(X,Y)
def Graphics(event):
    Graphical(X,Y)

def OneWayTest(X,Y):
    return(scipy.stats.f_oneway(X,Y))

def OneWayTestGraph(event):
    OneWayTest(X,Y)

def KSSYMBOL(X,Y):
   return(scipy.stats.ks_2samp(X,Y))

def normalTest(X):
    return(scipy.stats.normaltest(X))


def Graph():

    Graphical(X,Y)

        


#--------------------------------------------------------------------




def med():
    return("Median of data-set is : % s "
        % (statistics.median(X))) 


def randomNumbers(a):
    return [np.random.choice([i for i in range(a)]) for j in range(a)]


def digression(X,L,Average):
    for i in range (len(X)):
       return X[i]-Average
       





#def PearsonInt(X,Y):
   # print("PearsonResult",scipy.stats.pearsonr(X,Y))



    '''
    ranksX = np.array(X).argsort().argsort()
    ranksY = np.array(Y).argsort().argsort()
    print(ranksX)
    print(ranksY)
    X1=X
    deltaN=0
    #X1=sorted(X1)
    n=len(X)
    dN=0
    dNPow=0
    S=0
    for i in range(len(ranksX)):
         dX=i
         dY=i
         dN+=ranksY[i]-ranksX[i]
         dNPow+=pow(ranksY[i],2)-pow(ranksX[i],2)
         S=1-(6*dNPow)/n*(pow(n,2)-1) 
         print("SPRIMEN=",dNPow)'''



#DATA READ AND CONVERT
Xx=[]
Yy=[]

A=0
B=0
file_name1='20060822_0-0.int'
file_name2='ik060822.703'
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
           



X=[]
Y=[]

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
        el=data1['DATA'][i][A]
        X.append(float(el))
        
    global Y
    Y=[]
    for i in range(0,len(data2['DATA'])-1,int(maxStep/step2)):
        el=data2['DATA'][i][B]
        Y.append(float(el))



print(X)


