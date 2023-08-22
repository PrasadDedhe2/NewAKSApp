for i in range(1,3):
	print(i)

import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='sfabdjkfsdjfsafj',
    database='mydatabase'
)

# Create a cursor object
cursor = conn.cursor()

# Execute SQL queries using the cursor
cursor.execute("SELECT * FROM users")

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()

