# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:52:43 2018

@author: dumbPy
"""
import pandas as pd

population = []
if __name__ == '__main__':
  
  file=open("pop.txt",'r')
else:
  import os
  direct = os.getcwd()
  import platform
  if (platform.system()=='Linux'):
      extra = '/dependencies'
  else:
      extra = '\\dependencies'
  file=open(os.path.join(direct+extra,"pop.txt"),'r')
population = file.read().splitlines()
file.close()

time = []
if __name__ == '__main__':
  file=open("time.txt",'r')
else:
  file=open(os.path.join(direct+extra,"time.txt"),'r')
time = file.read().splitlines()
file.close()


population.remove(population[0]); population.remove(population[0])  #removes the 1st two entries

def clean(population):
    for data in population:
        tup = data.split(":  ")
        l = [int(tup[0]), int(tup[1][0:4])]
        population[population.index(data)] = l
    return population

population = clean(population)
population = pd.DataFrame(population, columns = [0, 1], index = [b for b in range(1, 86)])
del population[0]
#print(population)

time.remove(time[0]); time.remove(time[0]); time.remove(time[0]); time.remove(time[0]) #removes commented entries
for row in time:
    temp= row.split(":  ")
    temp2 = [s for s in map(int, temp[1].split())]
    temp2.insert(0, int(temp[0]))
    time[time.index(row)] = temp2
    
time = pd.DataFrame(time, columns = [a for a in range(0, 41)], index = [b for b in range(1, 86)])
del time[0]
#print(time)

def get_time():
    return time

def get_population():
    return population

