# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:47:18 2018

@author: dumbPy
"""

import numpy as np
import pandas as pd

pairs = []

students = []
file=open("IE709_students.csv",'r')
students = file.read().splitlines()
file.close()

def find_pair(student1):   #Given 1st student(index), it finds the second student(index) for the pair.
    
    index2 = np.random.randint(len(others))   #Index of second student (uniformly distributed)
    return index2

mTech_students = []
others = []
for s in students:
    if (s[0:5] == '17319'):
        mTech_students.append(s)
    else:
        others.append(s)


while (len(mTech_students) > 1):
    index1 = np.random.randint(len(mTech_students))
    student1 = mTech_students.pop(index1)
    student2 = others.pop(find_pair(student1))
    pairs.append((student1, student2))
pairs = pd.DataFrame(pairs, columns = ['Student_1', 'Student_2'])
print(pairs)
print("One Student ("+mTech_students[0]+") remains and is randomly allotted to pair: "+str(np.random.randint(20)))
