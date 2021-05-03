import pandas as pd

happiness = pd.read_csv("pertemuan11\\world-happiness-report-2021.csv")

# print data
print(happiness)
print()

# print top 5 rows of the data
print(happiness.head())
print()

# print top 5 from bottom of the data
print(happiness.tail())
print()

# print 10 random rows from the data
print(happiness.sample(10))
print()

# print the colums of the data
print(happiness.columns)
print()

# print specified column of the data
print(happiness['Country name'])
print()

# print two or more specified columns of the data
print(happiness[['Country name', 'Freedom to make life choices']])
print()

# print specified column and specified row
print(happiness['Country name'][1])
print()

# print data that statisfy the given condition
condition = (happiness['Freedom to make life choices'] > 0.8)
print(happiness[condition])
print()

# store the data to numpy array
print(happiness.to_numpy())
print()
