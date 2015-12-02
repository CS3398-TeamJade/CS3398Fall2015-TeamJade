#start
#matthew lamanque
#attemptone, sprint 3, team jade
#python excel reader to .txt for processing

import xlrd
import os.path

wb = xlrd.open_workbook(os.path.join('C:/Users/Matthew R Lamanque/Desktop/test0.xlsx'))
wb.sheet_names()
sh = wb.sheet_by_index(0)
i = 0
my_file = open("Output.txt", "a")

while sh.cell(i,7).value != 0:
    Load = sh.cell(i,7).value
    all_d = sh.col_values(i, 7)
    thing = Load+" "+(" ".join(all_d))
    my_file.write(thing + '\n')
    i += 1
file.close

#end
