import csv 
data1=[]
data2=[]
with open("dataset_1.csv","r") as f:
    r=csv.reader(f)
    for row in r :
        data1.append(row)

headers1=data1[0]
planet_data1=data1[1:]

with open("dataset_sorted.csv","r") as f:
    r=csv.reader(f)
    for row in r :
        data2.append(row)

headers2=data2[0]
planet_data2=data2[1:]
headers=headers1+headers2
planet_data=[]
for i,row in enumerate(planet_data1):
    planet_data.append(planet_data1[i]+planet_data2[i])
with open("finaldata.csv","a+") as f:
    writer=csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planet_data)

