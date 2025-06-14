import pandas as pd

data = {
    "Name": ["ram", "shyam", "monu", 'avi', 'akash', 'adi', 'sonu', 'raj'],
    "Age": [34, 20, 17, 28, 26, 25, 19, 22],
    "City": ['nanded', 'kandhar', 'loha', 'ambulga', 'mumbai', 'USA', 'uk', 'pune'],
    "Salary": [10000, 20000, 15000, 18000, 25000, 30000, 12000, 22000],
        "performance": [100, 98, 95, 97, 99, 96, 94, 93]
    }

df = pd.DataFrame(data)
#display the DataFrame
print('Sample DataFrame:')
print(df)
print("Names(single column returnseries)")
name = df['Name']
print(name)

#selecting multiple columns
subset = df[["Name", "Age"]]
print("/nSubset with name and salary")
print(subset)


