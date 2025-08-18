import pandas as pd
import matplotlib.pyplot as plt
data={'Fruits':['Apple','banana','Mango','Orange','Grapes','Pineapple'],'Sales':[120,90,150,110,80,60]}
df=pd.DataFrame(data)
df.to_csv('fruit_sales.csv', index=False)
df = pd.read_csv('fruit_sales.csv')
plt.bar(df['Fruits'],df['Sales'],color='Green')
plt.title("fruit Sales - Barchart")
plt.xlabel('fruits')
plt.ylabel('Sales')
plt.show()

plt.scatter(df['Fruits'],df['Sales'],color='red', s=100)
plt.title("fruit Sales - Scatter Plot")
plt.xlabel('fruits')
plt.ylabel('Sales')
plt.show()