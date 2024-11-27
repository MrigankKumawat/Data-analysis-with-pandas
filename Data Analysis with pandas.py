### Data Analysis with Pandas

import pandas as pd 
df=pd.read_csv('C:\\Users\\pc\\Downloads\\Detergent-sales-data.csv')

print(df.head())                            ## Used to inspect first few rows  
print("\n")

average=df['Sales'].mean()                  ## Used to calculate average sales
print("Average Sales:",average)
print("\n")

total=df['Sales'].sum()                     ## Used to calculate total revenue
print("Total Revenue:",total)
print("\n")

describe=df["Sales"].describe()
print(describe)
print("\n")

mini=df['Sales'].min()                      ## Used to calculate minimum sales
print("Minimum Sales:",mini)
print("\n")

maxi=df['Sales'].max()                      ## Used to calculate maximum sales
print("Maximum Sales:",maxi)
print("\n")




