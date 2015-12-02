#start

import xlrd
import os.path

wb = xlrd.open_workbook(os.path.join('C:/Users/Matthew R Lamanque/Desktop/test0.xlsx'))
wb.sheet_names()
sh = wb.sheet_by_index(0)
i = 1
my_file = open("Output.txt", "a")

while sh.cell(i,6).value != 0:
    Load = sh.cell(i,6).value
    all_d = sh.col_values(i, 0)
    DB1 = Load+" "+(" ".join(all_d))
    my_file.write(DB1 + '\n')
    i += 1
file.close
