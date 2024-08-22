



import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the date range
start_date = datetime(2024, 7, 1)
date_range = [start_date + timedelta(days=i) for i in range(30)]

# Define instructors, vehicles, and learners
instructors = ["Pavan", "Divya", "Boby", "Aishu", "David"]
vehicles = ["Honda Civic", "I10", "Tata Neno", "Alto", "Wagon R"]
learners = ["Lavanya", "Raju", "Cherry", "Dasu", "maggiee", "loki", "jagan", "gagan", "lisa", "Jack","Alice", "Dhrvu","Eve", "Frank", "Grace"]

# Assign three learners per instructor
learner_groups = {
    "Pavan": ["Lavanya", "Raju", "Cherry"],
    "Divya": ["Dasu", "maggiee", "loki"],
    "Boby": ["jagan", "gagan", "lisa"],
    "Aishu": ["Jack", "Alice", "Dhrvu"],
    "David": ["Eve", "Frank", "Grace"]
}

# Generate data for 30 days
data = []
for date in date_range:
    for instructor, vehicle in zip(instructors, vehicles):
        for learner in learner_groups[instructor]:
            km_travel = np.random.randint(20, 100)
            avg_speed = np.random.uniform(40, 80)
            fuel_used = np.random.uniform(3, 10)
            leave = np.random.choice([1, 0], p=[0.1, 0.9])
            ac_issues = np.random.choice([1, 0], p=[0.05, 0.95])
            engine_heating = np.random.choice([1, 0], p=[0.05, 0.95])
            leakage = np.random.choice([1, 0], p=[0.03, 0.97])
            data.append([date.strftime("%Y-%m-%d"), instructor, learner, vehicle, km_travel, round(avg_speed, 2), round(fuel_used, 2), leave, ac_issues, engine_heating, leakage])

# Create dataframe
columns = ["Date", "Instructor Name", "Learner Name", "Vehicle Name", "KM Travel", "Average Speed", "Fuel Used", "Instructor Leave", "A/C Issues", "Engine Start Heating", "Leakage"]
df = pd.DataFrame(data, columns=columns)

# Save to Excel
output_path = 'DrivingSchoolData_30Days.xlsx'
df.to_excel(output_path, index=False)

output_path
