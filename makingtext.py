#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:00:27 2017

@author: emadezzeldin
"""
import pandas as pd

def gettext():
    global mystring
    courses = pd.read_csv ('coursesinfo.csv', index_col = 0 , skiprows = 0)
    mytext = courses ['CourseDescription'] ['AIT 580']
    allcourses = [iteration [1] for iteration in courses.get_values() ]
    #pdftotext (mytext)
    #pdftotext (allcourses[0])
    mystring = ''
    for desc in allcourses:mystring +=desc

def writecourses():
    target = open('CourseDescription.txt', 'w')
    for word in mystring:
        target.write (word)
    target.close()

gettext()
writecourses()
