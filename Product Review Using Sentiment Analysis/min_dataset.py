import pandas as pd
import csv


input3 = open('Data.csv' , 'r')
output = open('New.csv' , 'w')
row = input3.readline()
output.write(row)
while row:
   # print(row)
    row = input3.readline()
    if row and row[0].strip() == '1' and row[1].strip()==',':
       output.write(row)
       #output.write('\n')
input3.close()
output.close()
dx = pd.read_csv('Data.csv')

distinct_list = []
for i in range(dx.shape[0]):
    if str(dx.iloc[i,1]) in distinct_list:
        continue
    else:
        distinct_list.append(dx.iloc[i,1])
print(len(distinct_list))
