# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:47:39 2020

@author: shantanu
"""
import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path,header=None,index=False)
    space=[1,4,2,13,13,30,15,1,35,35,10,1,2,4,2,3,1,8,20,2,1,20,2,1,20,2,1,20,2,1,20,2,1,20,2,1,20,2,1,20,2,1,20,2,1,20,2,1]
    for i in range(1,len(df.columns)):
        spaces='{:<'+str(space[i])+'}'
        col=df.iloc[:,i]
        for j in range(1,len(col)):
            col[j]=spaces.format(col[j])[:space[i]]
    df=df.iloc[1:]
    
    txt_file =  os.path.join(os.path.dirname(import_file_path), 'records.txt')
    open(txt_file, 'w').close()
    df.to_csv(txt_file,index=False, sep='\t', mode='w')
    with open(txt_file, 'r') as fin:
        data = []
        for line in (fin.readlines()):
            data.append(line.replace("\t", ""))
    with open(txt_file, 'w') as fout:
        fout.writelines(data[1:])
    print("Your file has been saved in {0}. You may close this window now".format(txt_file))

browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()
