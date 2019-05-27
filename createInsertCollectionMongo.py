import pandas as pd
from pymongo import MongoClient
import pymongo



myclient = pymongo.MongoClient(u"mongodb://apsrp03693.uhc.com:27017")
print(myclient.list_database_names())
mydb = myclient["VOP"]
print(mydb.list_collection_names())
#mycol = mydb["PA_HSR_Data"]
#mycol.drop()
mycol2 = mydb['ticketsData']
cdf=pd.read_csv('C:/Users/cvikas10/Downloads/Voice-of-Providers/ticketsAPI/ticketsCSV.csv',sep=',',encoding = 'unicode_escape')
print(cdf.columns)
converterS = {col: str for col in cdf.columns}
#df = pd.read_csv('C:\\Users\\asrilekh\\Documents\\MyJabberFiles\\jnadimpa@corpimsvcs.com\\detail1.csv',sep='\t',converters=converterS,encoding = 'unicode_escape')
#print(str(len(df)))
#print(str(len(df.columns)))
data =[]
for row in range(0,len(cdf)):
    # print(str(row))
    elm = {}
    for col in range(0,len(cdf.columns)):
        elm[cdf.columns[col]]=str(cdf.iloc[row,col])
    data.append(elm)
# print(data)
x = mycol2.insert_many(data)
print(str(x.inserted_ids))
    