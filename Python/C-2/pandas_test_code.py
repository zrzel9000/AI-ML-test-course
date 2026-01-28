import pandas as pd

dict = {'Name': ['Tejasv', 'Rahul', 'Priyal', 'Anjali', 'a', 'b', 'c'],
        'Age': [20, 19, 21, 19, 21, 24, 30],
        'Branch': ['ece', 'CSE', 'BCH', 'BME', 'CSE', 'cse', 'cse']
}


# TASK  -  2

df = pd.DataFrame(dict)
df['Branch'] = df['Branch'].str.upper()
print(df)



print('\n',df[df["Branch"] == "ECE"])

print('\n',df[(df['Branch'] == 'CSE') & (df['Age'] > 19)])


# TASK  -  3


sorted_df = df.sort_values(by=['Age'])
print('\n', sorted_df[['Name', 'Age']])

print('\n', df.describe())