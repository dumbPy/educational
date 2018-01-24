# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:29:18 2018

@author: dumbPy
"""
import dependencies.files_loaded as f    #time and population as panda DataFrames
from pulp import *
import matplotlib.pyplot as plt

time = f.get_time()
population = f.get_population()
print("Q1 (b)")

def solve_for_threshold(threshold = 10):
  prob = LpProblem("Minimum Ambulances Required to Cover all Population", LpMinimize)

  #Binary indicator variable
  x = [LpVariable('X{0}'.format(i), cat = 'Binary') for i in range(1, 41)]

  #Objective
  prob += sum(x)

  #Constraints
  for Location in time.index:
      prob += (sum([time.loc[Location, Base]*x[Base-1] for Base in time.columns if time.loc[Location, Base]<=threshold])) >=1

  prob.solve()
  try:
    return(sum([v.varValue for v in prob.variables()]))
  except:
    print([v.varValue for v in prob.variables()])

def test_optimality(threshold):
  for Location in time.index:    
    flag = 0  
    for Base in time.columns:
      if time.loc[Location, Base]<=threshold:
        flag =1
    if flag == 0:
      print("Location: "+str(Location)+" cannot be served within "+str(threshold)+" minutes ever." )
      return False
  return True

ambulanceRequired = [solve_for_threshold(threshold) for threshold in range(4, 21) if test_optimality(threshold)]

plt.plot([x for x in range(6, 21)], ambulanceRequired)
plt.xlabel("Time Threshold"); plt.ylabel("Minimum Abmulances Required")
plt.title("Minimum Ambulances required vs Time Threshold")
plt.show()
