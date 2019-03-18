import matplotlib.pyplot as plt
#import pyopencl as ocl
import numpy as np
import scipy.stats as st
import scipy

#import seaborn
import math
from tkinter import Tk,END,Frame,BOTH,Button,scrolledtext, ttk
from tkinter import *



def MULT(X,Y):
    return list(map(lambda a,b:a*b,X,Y)) 
def SUM(X,Y):
    return list(map(lambda a,b:a+b,X,Y)) 
    
def AVERAGE(a,n):
    return a/n

mu=0.5
sigma=0.01

X= np.random.normal(mu,sigma,1000000)

Y= np.random.normal(mu,sigma,1000000)
#----------------------PLOTTING---------------------------
def Graphical(X,Y):
    data=np.concatenate((X,Y))
    bins=20
    #fig,axs=plt.subplots(1,3,figsize=(9,3))
    plt.subplot(2,2,1)
    plt.hist(data,bins)
    plt.subplot(2,2,2)
    plt.boxplot(data)
    
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
    S=0
    DxDy=0
    Rxy=0
    for i in range(len(X)):
        dX=X[i]-Mx
        #print("dX",i,"=",dX)
        sumpowX+=math.pow(dX,2)
        #print("d2X",i,"=",math.pow(dX,2))
        dY=Y[i]-My
        #print("dY",i,"=",dY,2)
        #print("d2Y",i,"=",math.pow(dY,2))
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
    print(scipy.stats.f_oneway(X,Y))

def OneWayTestGraph(event):
    OneWayTest(X,Y)


def Graph():
    Graphical(X,Y)


#--------------------------------------------------------------------









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

'''
with open("x.txt") as file:
    Xx = [row.strip() for row in file]

with open("y.txt") as file:
    Yy = [row.strip() for row in file]'''
'''
with open("x.txt") as f:
    for line in f:
        Xx.append([float(x) for x in line.split()])

with open("y.txt") as f:
    for line in f:
        Xx.append([float(x) for x in line.split()])
'''
#print(Xx)



   
  

     
#Pearson(X,Y)
#Spirmen(X,Y)
#PearsonInt(X,Y)
#Graphical(X,Y) 

#Spirmen()

'''
def dataWriting():
    f=open("X.txt","w")
    f1=open("Y.txt","w")
    for i in range(len(X)):
        f.writelines(str(X[i])+'\n')
    for i in range(len(Y)):
        f1.writelines(str(Y[i])+'\n')
'''