# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 10:50:53 2018

@author: dumbPy
"""

import dependencies.files_loaded as f     #time and population as panda DataFrames
from pulp import *

time = f.get_time()
population = f.get_population()

prob = LpProblem("Minimum Ambulances Required to Cover all Population", LpMinimize)

#Binary indicator variable
x = [LpVariable('X{0}'.format(i), cat = 'Binary') for i in range(1, 41)]

#Objective
prob += sum(x)

#Constraints
for Location in time.index:
    prob += (sum([time.loc[Location, Base]*x[Base-1] for Base in time.columns if time.loc[Location, Base]<=10])) >=1

prob.solve()
print("Q1(a)")
print("Status:", LpStatus[prob.status])
print("Total No. of Ambulances required for 10 mins Threshold = "+ str(int(sum([v.varValue for v in prob.variables()]))))
