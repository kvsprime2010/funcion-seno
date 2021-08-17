import numpy as np
import matplotlib.pyplot as plt
import xlrd
from xlrd import open_workbook, sheet
vector=[]



filepath = "data2.xls"
openfile=xlrd.open_workbook(filepath)
sheet=openfile.sheet_by_name("Hoja1")

for i in range(sheet.nrows):
    vector.append(sheet.cell_value(i,0))

y=np.zeros(sheet.nrows)
plt.plot(vector,y)
plt.show()