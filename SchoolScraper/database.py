import pandas as pd
import mysql.connector
from mysql.connector import Error
import numpy as np  # Import NumPy to handle NaN values

# Database Config (Modify as needed)
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "sidsis@10"
DB_NAME = "schools_db"

# Connect to MySQL and Insert Data
def store_data_in_db():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        # Drop table if it exists to recreate it properly
        cursor.execute("DROP TABLE IF EXISTS schools")

        # Create Table
        create_table_query = """
        CREATE TABLE schools (
            id INT AUTO_INCREMENT PRIMARY KEY,
            program_type TEXT,
            program TEXT,
            site_name TEXT,
            borough TEXT,
            agency TEXT,
            contact_number TEXT,
            grade_level TEXT,
            location TEXT,
            postcode TEXT,
            latitude FLOAT,
            longitude FLOAT
        )
        """
        cursor.execute(create_table_query)
        print("✅ Table 'schools' created successfully!")

        # Read the cleaned CSV
        df = pd.read_csv("cleaned_schools.csv")

        # Replace NaN values with None (to be interpreted as NULL in MySQL)
        df = df.replace({np.nan: None})

        # Insert data into MySQL
        insert_query = """
        INSERT INTO schools (program_type, program, site_name, borough, agency, contact_number, 
                             grade_level, location, postcode, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for _, row in df.iterrows():
            values = (
                row['PROGRAM TYPE'], row['PROGRAM'], row['SITE NAME'], row['BOROUGH / COMMUNITY'],
                row['AGENCY'], row['Contact Number'], row['Grade Level / Age Group '],
                row['Location 1'], row['Postcode'], row['Latitude'], row['Longitude']
            )
            cursor.execute(insert_query, values)

        # Commit and close connection
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Data successfully stored in MySQL!")

    except Error as e:
        print(f"❌ Error: {e}")

# Run the function
if __name__ == "__main__":
    store_data_in_db()
