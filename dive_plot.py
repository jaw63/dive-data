import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load data from SQL database

# Connect to the database
conn = sqlite3.connect('dives_old.db')

# Create a cursor object
cursor = conn.cursor()

# Get data
cursor.execute("SELECT * FROM dive_log_records LIMIT 0")
headers = [description[0] for description in cursor.description]

df = pd.read_sql_query("SELECT * FROM dive_log_records", conn)

# format data
df['currentTime'] = df['currentTime']/(1000*60)
groups = df.groupby('diveLogId')

# Filter data for a specific dive
dive_id = 2231504401645269763
dive_data = df[df['diveLogId'] == dive_id]

# Create a figure with four subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Create Dive Profile graph
for name, group in groups:
    axs[0,0].plot(group['currentTime'], group['currentDepth'], label=name)

axs[0, 0].set_title(f"Dive Profile for All Dives")
axs[0, 0].set_xlabel("Time (min)")
axs[0, 0].set_ylabel("Depth")
axs[0, 0].invert_yaxis()


# Create max depths bar graph
max_depths = df.groupby('diveLogId')['currentDepth'].max().reset_index(drop=True)
axs[0, 1].bar(max_depths.index+1, max_depths.values)
axs[0, 1].set_xlabel('Dive #')
axs[0, 1].set_ylabel('Max Depth (ft)')
axs[0, 1].set_title('Max Depth by Dive')


# Create avg temperature graph
avg_temp = df.groupby('diveLogId')['waterTemp'].mean().reset_index(drop=True)
axs[1, 0].bar(avg_temp.index+1, avg_temp.values)
axs[1, 0].set_xlabel('Dive #')
axs[1, 0].set_ylabel('Avg Temp (ft)')
axs[1, 0].set_title('Avg Temp by Dive')
axs[1, 0].set_ylim(75,101)


# Cylinder pressure graph
for name, group in groups:
    axs[1,1].plot(group['currentTime'], group['aiSensor0_PressurePSI'], label=name)

axs[1,1].set_xlabel('Time (min)')
axs[1,1].set_ylabel('Cylinder Pressure (PSI)')
axs[1,1].set_ylim(0,3300) 

axs[1,1].set_title('Cylinder Pressure Over Time for All Dives')

# Adjust layout
plt.tight_layout()

# Display the figure
plt.show()
