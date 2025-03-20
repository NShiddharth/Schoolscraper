import pandas as pd
import os

# Define file path (FIXED)
csv_file = r"C:\Users\Shidd\Downloads\schools.csv"

# Check if the file exists
if not os.path.exists(csv_file):
    print(f"Error: File '{csv_file}' not found. Please download and place it in the project directory.")
    exit()

# Load CSV into DataFrame
df = pd.read_csv(csv_file)

# Display basic info
print("✅ Dataset Loaded Successfully!")
print("Total rows:", len(df))
print("Columns:", df.columns.tolist())

# Preview first few rows
print(df.head())

# Save cleaned data (optional)
df.to_csv("cleaned_schools.csv", index=False)
print("✅ Cleaned data saved as 'cleaned_schools.csv'.")
