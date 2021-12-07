import csv 
data=[]
with open("dataset_2.csv","r") as f:
    r=csv.reader(f)
    for row in r :
        data.append(row)

headers=data[0]
planet_data=data[1:]
for d in planet_data:
    d[2]=d[2].lower()
planet_data.sort(key=lambda planet_data:planet_data[2])
with open("dataset_sorted.csv","w") as f:
    writer=csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planet_data)
