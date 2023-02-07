import pandas as pd


# How to make data frames using pandas library

XYZ_Web = {
    "Day": [1, 2, 3, 4, 5, 6],
    "Visitors": [1000, 200, 310, 405, 602, 701],
    "Bounce_Rate": [20, 10, 30, 15, 3, 20]
}

df = pd.DataFrame(XYZ_Web)
print("Data Frame", end='\n\n')

print(df)

print("-----------------------------")


# Now I will perform operations on pandas dataframe

# 1- Slicing
print("Slicing", end='\n\n')
print(df.head(2))  # slicing the starting 2 rows
print(df.tail(2))  # slicing the last 2 rows

print("-----------------------------")

# 2- Merging
df1 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int-rate": [2, 1, 2, 3],
                   "IND_GDP": [50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int-rate": [2, 1, 2, 3],
                   "IND_GDP": [50, 45, 45, 67]}, index=[2005, 2006, 2007, 2008])

merge = pd.merge(df1, df2)  # Merges df1 and df2 into 1 dataframe
print("Merging", end='\n\n')
print(merge)


print("-----------------------------")
# # Rq: If you want only 1 column to be common
# #merge = pd.merge(df1, df2, on = "HPI")
# # print(merge)


# 3- Joining
df3 = pd.DataFrame({"Int-rate": [2, 1, 2, 3],
                   "IND_GDP": [50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])
df4 = pd.DataFrame({"Low_Tier_HPI": [50, 45, 67, 34], "Unemployment": [
                   1, 3, 5, 6]}, index=[2001, 2003, 2004, 2004])

joined = df3.join(df4)
print("Joining", end='\n\n')
print(joined)


print("-----------------------------")
# # Rq: The main difference between join vs merge is that join() is used to combine 2 dataframes on the index not on columns


# 4- Changing the index and column headers
df = pd.DataFrame({"Day": [1, 2, 3, 4], "Visitors": [
                  200, 100, 230, 300], "Bounce_Rate": [20, 45, 60, 10]})

df.set_index("Day", inplace=True)  # changing the index of the table for "Day"
# changing column header from "Visitors" to "Users"
df = df.rename(columns={"Visitors": "Users"})
print("Changing the index and column headers", end='\n\n')
print(df)


print("-----------------------------")

# 5- Concatination
concat = pd.concat([df1, df2])
print("Concatination", end='\n\n')
print(concat)


# 6- Data Munging

# Data Munging means that you can actually convert a particular format of data into a different format.
# So if you have a data which is in CSV file, you can convert it to an HTML.

country = pd.read_csv(
    r'C:\Users\peter\Documents\Courses\AI\play\Social_Network_Ads - Copy.csv', index_col=0)
# Rq: "index_col = 0" is to make sure that I have no index present in that particular dataframe
country.to_html('edu.html')

print("-----------------------------")


# Aggregation

XYZ_File = {
    "Day": [1, 2, 3, 4, 5, 6],
    "Visitors": [1000, 200, 310, 405, 602, 701],
    "Bounce_Rate": [20, 10, 30, 15, 3, 20]
}

df = pd.DataFrame(XYZ_File)

print("Aggregation", end='\n\n')
print(df.aggregate({
    "Day": ['max'],
    "Visitors": ['max', 'min'],
    "Bounce_Rate": ['min']

}))

print("-----------------------------")

# Querying
print("Querying", end='\n\n')
print("Bounce_Rate > 10")
print(df.query('Bounce_Rate > 10'), end='\n\n')
print("Visitors > 400")
print(df.query('Visitors > 400'))
