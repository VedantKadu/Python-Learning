import pandas as pd

# Read the original CSV file
original_df = pd.read_csv("material_data.csv")

# Group by 'Set Point (C)' and create a new DataFrame
grouped_df = original_df.groupby("Set Point (C)")

# Create a new DataFrame to store the results
new_df = pd.DataFrame()

# Iterate over groups and extract values into separate columns
for group_name, group_data in grouped_df:
    new_df[group_name] = group_data["impedance imaginary"].reset_index(drop=True)

# Transpose the new DataFrame
new_df = new_df.T

# Write the new DataFrame to a new CSV file
new_df.to_csv("output_file.csv", index_label="Set Point (C)")
