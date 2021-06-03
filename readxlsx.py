import pandas as pd

#xlsx = pd.read_excel('./sample.xlsx')
xlsx = pd.read_excel('./bmw-codes.xlsx')

#print(xlsx.head()) 
#print(xlsx)
print(xlsx.index , xlsx.columns)
print(xlsx.get('cafd_id'))
i = 0
while i < 10:
    i = i+1
    print(i, xlsx.get('cafd_id'))
    
#print() 
#print(xlsx.tail())
#print()
#print(xlsx.shape)



