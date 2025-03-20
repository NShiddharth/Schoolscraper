import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sidsis@10",
    database="schools_db"
)

# Query to get the number of schools per borough
query = "SELECT borough, COUNT(*) as total_schools FROM schools GROUP BY borough ORDER BY total_schools DESC;"
df = pd.read_sql(query, conn)

# Close the database connection
conn.close()

# Plot the data
plt.figure(figsize=(10, 5))
plt.bar(df["borough"], df["total_schools"], color="skyblue")
plt.xlabel("Borough")
plt.ylabel("Total Schools")
plt.title("Number of Schools per Borough")
plt.xticks(rotation=45)
plt.show()
