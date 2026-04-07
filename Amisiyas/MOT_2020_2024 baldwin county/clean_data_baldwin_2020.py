import pandas as pd

# Dataset loading, viewing, and cleaning for 2020, Baldwin County, Alabama

df = pd.read_csv("Amisiyas/MOT_2020_2024 baldwin county/mot_baldwin_2020.csv")

df["Label (Grouping)"] = df["Label (Grouping)"].str.strip() # Removing whitespace

print(df.shape) # Shape before cleaning

# Dropping columns
df = df.drop([
    'Baldwin County, Alabama!!Total!!Margin of Error',
    'Baldwin County, Alabama!!Car, truck, or van -- drove alone!!Margin of Error',
    'Baldwin County, Alabama!!Car, truck, or van -- carpooled!!Margin of Error',
    'Baldwin County, Alabama!!Public transportation (excluding taxicab)!!Margin of Error'
], axis=1)

# Renaming columns
df = df.rename(columns={
    'Baldwin County, Alabama!!Total!!Estimate': 'Total Pop, % Total Pop',
    'Baldwin County, Alabama!!Car, truck, or van -- drove alone!!Estimate': 'Drove Alone',
    'Baldwin County, Alabama!!Car, truck, or van -- carpooled!!Estimate': 'Carpooled',
    'Baldwin County, Alabama!!Public transportation (excluding taxicab)!!Estimate': 'Public Transportation'
})

# Dropping specific rows
df = df.iloc[:112]
df = df.drop(df.index[81:92])
df = df[df["Label (Grouping)"] != "Mean travel time to work (minutes)"]

print(df.head(10))
print(df.tail(10))