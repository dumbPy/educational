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
names = []; roll = []

#seperating names and roll_numbers
for person in students:
    roll.append(person.split("    ")[0])
    names.append(person.split("    ")[1])

students = roll[:]

#Person auditing is seperated to be alloted as 3rd person in a group as per Faculty's advice. 
auditor = students.pop(students.index('174270002'))

"""
#used for debugging in terminal
def get_students():
    return(students)

def get_names():
    return names
"""

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

#This loop pairs guys from mTech 1st year IEOR with others randomly
while (len(others) > 0):
    index1 = np.random.randint(len(mTech_students))
    student1 = mTech_students.pop(index1)
    student2 = others.pop(find_pair(student1))
    pairs.append((len(pairs)+1, student1,names[roll.index(student1)], student2, names[roll.index(student2)]))

#This loops pairs the remaining (4) mTech guys among themselves randomly
while (len(mTech_students) > 0):
    index1 = np.random.randint(len(mTech_students))
    student1 = mTech_students.pop(index1-1)
    student2 = mTech_students.pop(np.random.randint(len(mTech_students))-1)    
    pairs.append((len(pairs)+1, student1,names[roll.index(student1)], student2, names[roll.index(student2)]))


pairs = pd.DataFrame(pairs, columns = ['index', 'Student_1_Roll', 'Student_1_Name', 'Student_2_Roll', 'Student_2_Name'])
pairs = pairs.set_index('index', drop = True)

#printing by roll numbers then by names
print(pairs.iloc[:, [0, 2]])
print('')
print('')
print(pairs.iloc[:, [1, 3]])
print('')
print('')

print("Auditing Student ("+auditor+", "+names[roll.index(auditor)]+") remains and is randomly allotted to pair: "+str(np.random.randint(21))+" as per faculty's advice")
print("Pair 19 and 20 are '1st year MTech IEOR' exclusive due to higher students from the same class.")

