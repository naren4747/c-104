import csv

with open(r"heightWeight.csv",newline='') as df:
    reader=csv.reader(df)
    fileData=list(reader)

fileData.pop(0)

newData=[]

for i in range(len(fileData)):
    height=fileData[i][1]
    newData.append(float(height))

n=len(newData)
sum=0

for x in newData:
    sum+=x

mean=sum/n

print(mean)
