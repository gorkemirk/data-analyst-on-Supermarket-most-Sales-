import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("marketencoksatan/train.csv")
print(data.head(10))
print(data.shape)
print(data.describe())
print(data.columns)
data.drop(["Row ID","Order ID","Customer ID","Product ID"],axis=1,inplace=True)
print(data.head(10))
print(data.columns)
print(data.isnull().sum())#null değerleri sayar
print(data[data["Postal Code"].isnull()].City)#postal code nan olanları getirir"]]
data["Postal Code"].fillna(49029,inplace=True)
print(data.isnull().sum())#null değerleri sayar
print(data[data["City"]=="Burlington"]["Postal Code"])#Burlington şehrinin postal code değerleri
data["Month"]=data["Order Date"].str[3:5]#ayları alır
data["Month"]=data["Month"].astype(int)#int tipine çevirir
print(data.Month)
d={1:"Ocak",2:"Şubat",3:"Mart",4:"Nisan",5:"Mayıs",6:"Haziran",7:"Temmuz",8:"Ağustos",9:"Eylül",10:"Ekim",11:"Kasım",12:"Aralık"}
data["Month"]=data["Month"].map(d)
print(data.Month)
data["Order Date"]=pd.to_datetime(data["Order Date"],format="mixed")#datetime tipine çevirir
print(data["Order Date"])
data["Ship Date"]=pd.to_datetime(data["Ship Date"],format="mixed")#datetime tipine çevirir
print(data["Ship Date"])
data["Year"]=data["Order Date"].dt.year#yılları alır
print(data.Year)
print(data.Year.value_counts())#yıllara göre gruplar
print(data.groupby(["Year"]).count())#yıllara göre gruplar
print(data.groupby(["Year","Month"]).count())#yıllara göre gruplar
print(data.groupby(["Month"]).agg({"Sales":"sum"}))#aylara göre gruplar

plt.plot(data.groupby(["Month"]).agg({"Sales":"sum"}))
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.xticks(rotation=90,fontsize=14)
plt.show()

plt.bar(data.groupby(["Year"]).agg({"Sales":"sum"}).index,data.groupby(["Year"]).agg({"Sales":"sum"})["Sales"])
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.xticks(rotation=90,fontsize=14)
plt.show()




