'''
Viz of Price of USB Thumbs
'''
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
capacity = [2,4,8,16,32,64,128,256,512,1024,2000]
price_2019 = [2.0,2.0,3.0,5.0,7.0,10.0,18.0,40.0,100.0,200.0,400.0]
price_2021 = [2,2.5,2.8,3.2,4.4,6.5,15.0,29.0,60.0,42.0,54.0]
price_2023 = [2.2,2.2,2.5,2.5,4.0,4.4,5.5,15.25,23.0,26.0,28.0]

price_dict = {'capacity':capacity,'price_2019':price_2019,'price_2021':price_2021,'price_2023':price_2023}

data = pd.DataFrame(price_dict)

print(data)
ci = 80
sns.regplot(x=data.capacity,y=data.price_2019,label='2019', ci = ci)
sns.regplot(x=data.capacity,y=data.price_2021,label='2021', ci = ci)
sns.regplot(x=data.capacity,y=data.price_2023,label='2023', ci = ci)
plt.xlabel("Capacity in GB")
plt.ylabel('USD')
plt.title('USB 3.0 Typical Thumbdrive Prices')
plt.show()