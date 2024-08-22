import mysql.connector

# Define cur and conn as global variables
cur = None
conn = None

def database():
    global cur, conn  # Declare cur and conn as global variables
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            port=3306
        )
        if conn.is_connected():
            print("Database is connected mysql!!")
        cur = conn.cursor()
        cur.execute("create database if not exists medicines")
        cur.execute("use medicines")
        cur.execute("create table if not exists medicines (drug_id Int Primary key, drug_name varchar(255), price FLOAT, expiry date)")

        # Commit the changes to the database
        conn.commit()
        print("Database and table created successfully")

    except Exception as e:
        print("Error", e)

def insert_to_database(drug_id, drug_name, price, expiry):
    try:
        # SQL query with placeholders
        sql = 'INSERT INTO medicines (drug_id, drug_name, price, expiry) VALUES (%s, %s, %s, %s)'

        # Data to be inserted into the table
        data = (drug_id, drug_name, price, expiry)

        # Execute the query with the data
        cur.execute(sql, data)

        # Commit the changes to the database
        conn.commit()
        print("Data inserted successfully")
        print(f"{cur.rowcount} rows are inserted")

    except Exception as e:
        print("Error", e)

def update_to_database(drug_id, drug_name, price, expiry):
    try:
        # SQL query with placeholders
        sql = 'UPDATE medicines SET drug_name=%s, price=%s, expiry=%s WHERE drug_id=%s'

        # Data to be updated in the table
        data = (drug_name, price, expiry, drug_id)

        # Execute the query with the data
        cur.execute(sql, data)

        # Commit the changes to the database
        conn.commit()
        print("Data updated successfully")
        print(f"{cur.rowcount} rows are updated")

    except Exception as e:
        print("Error", e)

def delete_to_database(drug_id):
    try:
        # SQL query with placeholders
        sql = 'DELETE FROM medicines WHERE drug_id=%s'

        # Data (drug_id) to be deleted from the table
        data = (drug_id,)

        # Execute the query with the data
        cur.execute(sql, data)

        # Commit the changes to the database
        conn.commit()
        print("Data deleted successfully")
        print(f"{cur.rowcount} rows are deleted")

    except Exception as e:
        print("Error", e)

def display_database():
    try:
        # SQL query to fetch all records
        sql = 'SELECT * FROM medicines'

        # Execute the query
        cur.execute(sql)

        # Fetch all records from the cursor
        records = cur.fetchall()

        # Print the fetched records
        for row in records:
            print(row)

    except Exception as e:
        print("Error", e)

def search_database(drug_id):
    try:
        # SQL query with placeholders
        sql = 'SELECT * FROM medicines WHERE drug_id=%s'

        # Data (drug_id) to be searched in the table
        data = (drug_id,)

        # Execute the query with the data
        cur.execute(sql, data)

        # Fetch the matching record from the cursor
        record = cur.fetchone()

        # Print the fetched record
        print(record)

    except Exception as e:
        print("Error", e)

# Call the database function to set up the database and table
database()

#  Inserting a new record
insert_to_database(1, 'pst', 100, '2025-02-24')
insert_to_database(2, 'pst', 100, '2025-02-24')

#  Updating the record with drug_id=1
update_to_database(1, 'paracetomol', 200, '2025-02-24')

#  Deleting the record with drug_id=1
delete_to_database(2)

#  Display all records
display_database()

#  Search for a specific record with drug_id=1
search_database(1)

cur.close()
if conn.is_connected():
    conn.close()
    print("MySQL connection is closed")