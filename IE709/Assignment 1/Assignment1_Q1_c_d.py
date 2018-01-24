# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:39:05 2018

@author: dumbPy
"""

import dependencies.files_loaded as f     #time and population as panda DataFrames
from pulp import *
time = f.get_time()
population = f.get_population()




print("Q1 (c)")
prob = LpProblem("Minimizing Population weighted coverage", LpMaximize)


#Binary indicator variable
x = [LpVariable('B{0}'.format(i), cat = 'Binary') for i in range(1, 41)]
y = [LpVariable('L{0}'.format(i), cat = 'Integer') for i in range(1, 86)]
#Objective
prob += sum([int(population.loc[Location])*y[Location-1] + 0*x[Base-1] for Location in population.index for Base in time.columns] )

#Constraints
for Location in time.index:
    prob += (sum([time.loc[Location, Base]*x[Base-1] for Base in time.columns if time.loc[Location, Base]<=10])) >=1
prob += sum(x) <= 3
for Location in time.index:
  prob += y[Location -1] >= 1
  prob += (sum([time.loc[Location, Base]*x[Base-1] for Base in time.columns if time.loc[Location, Base]<=10])) >=1
  prob += y[Location-1] <= sum([x[Base-1] for Base in time.columns if time.loc[Location, Base] <= 10])
prob.solve()
#print("Status:", LpStatus[prob.status])
print("Optimal Bases for best Coverage are: ", [x[Base-1] for Base in time.columns if x[Base-1].varValue>=1])
#print("times Coverage of each Location y: ", [y[Location-1].varValue for Location in time.index])
for n in range(1, 4):
  print(str(len([y[Location-1].varValue for Location in time.index if y[Location-1].varValue == n]))+" Locations are covered by "+str(n)+" Ambulances")


#Q1_d
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Solving the same above problem with a new constraint
#
# Total No. of Ambulances >= 8
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""
print("****************************************************************************")
print("Q1 (d) ")
prob = LpProblem("Minimizing Population weighted coverage", LpMaximize)

#Binary indicator variable
x = [LpVariable('B{0}'.format(i), cat = 'Binary') for i in range(1, 41)]
y = [LpVariable('L{0}'.format(i), cat = 'Integer') for i in range(1, 86)]
#Objective
prob += sum([int(population.loc[Location])*y[Location-1] + 0*x[Base-1] for Location in population.index for Base in time.columns] )

#Constraints
for Location in time.index:
    prob += (sum([time.loc[Location, Base]*x[Base-1] for Base in time.columns if time.loc[Location, Base]<=10])) >=1
prob += sum(x) <= 8
for Location in time.index:
  prob += y[Location -1] >= 1
  prob += (sum([time.loc[Location, Base]*x[Base-1] for Base in time.columns if time.loc[Location, Base]<=10])) >=1
  prob += y[Location-1] <= sum([x[Base-1] for Base in time.columns if time.loc[Location, Base] <= 10])
prob.solve()
#print("Status:", LpStatus[prob.status])

print("Optimal Bases for best Coverage with 8 Ambulances are: ", [x[Base-1] for Base in time.columns if x[Base-1].varValue>=1])

for n in range(1, 9):
  print(str(len([y[Location-1].varValue for Location in time.index if y[Location-1].varValue == n]))+" Locations are covered by "+str(n)+" Ambulances")
