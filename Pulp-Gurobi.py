# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:54:54 2019

@author: cc.rojas1833
"""
#Datos
import random
random.seed(1)
nN=100
W=nN/5
N=list(range(1,nN+1))
v={i:random.randint(1,W/2)for i in N}
w={i:random.randint(1,W/10)for i in N}

#Gurobi
from gurobipy import *
m = Model("Problema Gurobi")
m.setParam('OutputFlag', False)
m.ModelSense = GRB.MAXIMIZE

x={(n):m.addVar(0, 1, v[n], GRB.BINARY) for n in N}

m.addConstr(quicksum(x[n]*w[n] for n in N) <= W)
m.optimize()

print("F.O. con Gurobi",m.objVal)

#PULP-CBC
from pulp import * 
mp = LpProblem("Problema Auxiliar", LpMaximize)
xx = LpVariable.dicts("x",N,lowBound=0,upBound=1,cat=LpBinary)  

mp+= sum([v[n]*xx[n] for n in N])#Funcion Objetivo primero

mp+= sum([w[n]*xx[n] for n in N])<=W
status=mp.solve(PULP_CBC_CMD(msg=1))

print("F.O. con CBC ",pulp.value(mp.objective))
