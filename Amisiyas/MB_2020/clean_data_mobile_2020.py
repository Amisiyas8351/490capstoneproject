import pandas as pd

# Dataset loading, viewing, and cleaning for 2020, Mobile County, Alabama

df = pd.read_csv("Amisiyas/MB_2020/mot_mobile_2020.csv")

pd.set_option('display.max_rows', None) # Set option to display all rows

df["Label (Grouping)"] = df["Label (Grouping)"].str.strip() # Removing whitespace

print(df.shape) # Shape before cleaning

# Dropping columns
df = df.drop([
    'Mobile County, Alabama!!Total!!Margin of Error',
    'Mobile County, Alabama!!Car, truck, or van -- drove alone!!Margin of Error',
    'Mobile County, Alabama!!Car, truck, or van -- carpooled!!Margin of Error',
    'Mobile County, Alabama!!Public transportation (excluding taxicab)!!Margin of Error'
], axis=1)

# Renaming columns
df = df.rename(columns={
    'Mobile County, Alabama!!Total!!Estimate': 'Total',
    'Mobile County, Alabama!!Car, truck, or van -- drove alone!!Estimate': 'Drove Alone',
    'Mobile County, Alabama!!Car, truck, or van -- carpooled!!Estimate': 'Carpooled',
    'Mobile County, Alabama!!Public transportation (excluding taxicab)!!Estimate': 'Public Trans',
    'Label (Grouping)': 'Label'
})

# Dropping specific rows
df = df.iloc[:112]
df = df.drop(df.index[81:92])
df = df[df["Label"] != "Mean travel time to work (minutes)"]

# Setting 'Label' column as the index
df = df.set_index("Label")

# Drop rows with missing values
df = df.dropna()

# Renaming index values for better clarity
df = df.rename(index = {"16 to 19 years": "Workers aged 16-19", "20 to 24 years": "Workers aged 20-24", "25 to 44 years": "Workers aged 25-44",
                       "45 to 54 years": "Workers aged 45-54", "55 to 59 years": "Workers aged 55-59", "60 and over": "Workers over 60"})

# Dropping more rows
df = df.drop(df.index[69:79]) # Didnt contain data on entire baldwin county population
df = df.drop(df.index[69:76]) # Didn't contain data on entire baldwin county population
df = df.drop(["One race", "Foreign born", "Speak language other than English", "Workers 16 years and over", 
              "Workers 16 years and over with earnings", "Median earnings (dollars)", 
              "Workers 16 years and over for whom poverty status is determined", 
              "Worked in state of residence", "Median age (years)"]) # Dropping rows that included totals/summaries of the data

# Checking datatypes, removing symbols, converting to numeric & whole numbers
df["Total"] = df["Total"].str.replace('%', '').astype(float)
df["Drove Alone"] = df["Drove Alone"].str.replace('%', '').astype(float)
df["Carpooled"] = df["Carpooled"].str.replace('%', '').astype(float)
df["Public Trans"] = df["Public Trans"].str.replace('%', '').astype(float)

df["Total"] = ((df["Total"] / 100) * 173223).round(0).astype(int)
df["Drove Alone"] = ((df["Drove Alone"] / 100) * 148366).round(0).astype(int)
df["Carpooled"] = ((df["Carpooled"] / 100) * 11994).round(0).astype(int)
df["Public Trans"] = ((df["Public Trans"] / 100) * 896).round(0).astype(int)

print(df) #print all rows and columns of the cleaned dataframe