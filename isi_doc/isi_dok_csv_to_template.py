#!/usr/bin/env python3

# pip install python-docx
# pip install pandas
# pip install docxtpl
# pip install docx2pdf

#-------------------Modules-----------------#

import random
import time
import csv
import pandas as pd
from docxtpl import DocxTemplate
from docx2pdf import convert
from pathlib import Path

# Source CSV - column names that must match the *** that are {{***}} inside "template.docx"
csvfn = "output.csv"

print("test")

#-------------------Function make docx----------------#

def mkw():
    tpl = DocxTemplate("template.docx") # In same directory
    df = pd.read_csv(csvfn)
    df_to_doct = df.to_dict() # dataframe -> dict for the template render
    x = df.to_dict(orient='records')
    context = x
    tpl.render(context)
    tpl.save("%s.docx" %str(1))


def mkw2():
    tpl = DocxTemplate("template.docx") # In same directory
    with open(csvfn, 'r') as f:
        reader=csv.DictReader(f)
        headers=reader.fieldnames
        print(headers[0])
    df_to_doct = .to_dict() 
    context = headers
    tpl.render(context)
    tpl.save("%s.docx" %str(1))

# wait = time.sleep(random.randint(300,400))

#-------------------Function make pdf----------------#
def mpdf(n):
    file=(str(n+1)+".docx")
    #file=("1.docx")
    convert(file)    

#-------------------Main-----------------------------#

df2 = len(pd.read_csv(csvfn))

while True:
    
    docxcreate = input('Create Cluster documentation from template (Docx)? (y/n): ')
    if docxcreate == 'y':
        for i in range(0,1):
            print ("There will be ", df2, "Docx files")
            print("Making file: ",f"{i}," ,"..Please Wait...")
            mkw2()
            print ("")
            print("Done Docx! - Now check your files")
            print ("")
            print ("")
            print ("")
        break
    elif docxcreate == 'n':
            print ('ciao, without Docx no PDF')
            break
    else:
        docxcreate = input('Wrong input - Try again y or n : ')
        if docxcreate== 'n':
            print('ciao')
            break
        continue


while True:

    pdfcreate = input('Create PDF? (y/n): ')
    if pdfcreate == 'y':
        for i in range(0,df2):
            print ("There will be ", df2, "PDF files")
            print ("Making file: ",f"{i}," ,"..Please Wait...")
            mpdf(i)
            print ("")
            print ("Done PDF! - Now check your files")
            print ("")
            print ("")
            print ("")
        break
    elif pdfcreate == 'n':
        print('ciao')
        break
    else:
        pdfcreate = input('Wrong input - Try again y or n : ')
        if pdfcreate== 'n':
            print('ciao')
        break
