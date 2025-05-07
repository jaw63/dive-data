import sqlite3

# Connect to the database
conn = sqlite3.connect('dives\dives may 2025.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT statement to fetch the column names
cursor.execute("SELECT * FROM dive_log_records LIMIT 0")
headers = [description[0] for description in cursor.description]

# Execute a SELECT statement to fetch the first few rows
cursor.execute("SELECT * FROM dive_log_records LIMIT 5")
# cursor.execute("select divelogid,round(max(currentdepth),2) as max_depth_ft,round(avg(currentdepth),2) as avg_depth_ft,max(aiSensor0_PressurePSI) as max_PSI,min(aiSensor0_PressurePSI) as min_PSI,max(aiSensor0_PressurePSI)-min(aiSensor0_PressurePSI) as consumed_PSI,(max(currenttime)-min(currenttime))/1000/60 as time_minutes from dive_log_records group by 1")
rows = cursor.fetchall()

# Print the headers
print(headers)

# Print the rows
for row in rows:
    print(row)

# Close the connection
conn.close()