import pandas as pd


#Data Transformation
'''#Sample dataset
data = {
    'StudentID': [1, 2, 3, 4, 5],
    'Math': [85, 90, 75, 80, 95],
    'Science': [70, 75, 80, 85, 90],
    'English': [80, 85, 90, 95, 100]
}

# Create a DataFrame
df = pd.DataFrame(data)

print(df)

# Add a new column for average score
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=0)

# Print the transformed DataFrame
print(df)'''


#Data Cleaning
'''# Sample dataset with missing values and inconsistencies
data = {
    'StudentID': [1, 2, 3, 4, 5],
    'Math': [85, 90, None, 80, 95],  # Missing value for student 3
    'Science': [70, 75, 80, -85, 90],  # Negative score for student 4
    'English': [80, None, 90, 95, 100]  # Missing value for student 2
}

# Create a DataFrame
df = pd.DataFrame(data)

# Check for missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Replace negative scores with NaN
df['Science'] = df['Science'].apply(lambda x: None if x < 0 else x)

# Fill missing values with the mean
df.fillna(df.mean(), inplace=True)

# Check missing values after filling
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print(df)'''


#Data Integration
'''#Sample datasets
data1 = {
    'StudentID': [1, 2, 3, 4, 5],
    'Math': [85, 90, 75, 80, 95],
    'Science': [70, 75, 80, 85, 90]
}

data2 = {
    'StudentID': [1, 2, 3, 4, 5],
    'English': [80, 85, 90, 95, 100],
    'History': [75, 70, 85, 80, 95]
}

# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge the datasets on 'StudentID'
merged_df = pd.merge(df1, df2, on='StudentID')

# Print the merged dataset
print(merged_df)'''


#Error Correcting
'''# Sample dataset with errors
data = {
    'StudentID': [1, 2, 3, 4, 5],
    'Math': [85, 90, 75, 180, 95],  # Erroneous score for student 4
    'Science': [70, 75, 80, 85, 90],
    'English': [80, 85, 90, 95, 100]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Check for errors
print("Data before error correction:")
print(df)

# Correct errors (assuming any score above 100 is erroneous)
df.loc[df['Math'] > 100, 'Math'] = 100

# Check after correction
print("\nData after error correction:")
print(df)'''




