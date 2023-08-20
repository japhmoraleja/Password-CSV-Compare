import pandas as pd
import os
from datetime import datetime

# Get default values and user input
default_directory = os.getcwd()
default_datetime = datetime.now().strftime("%d-%b-%y %I:%M %p")
default_filename_difference = f"difference {default_datetime}.csv"
default_filename_latest = f"latest {default_datetime}.csv"

file1_path = input(f"Enter the filepath for file1.csv (default: {default_directory}): ") or default_directory
file2_path = input(f"Enter the filepath for file2.csv (default: {default_directory}): ") or default_directory
new_entries_filename = input(f"Enter the filename for new entries.csv (default: {default_filename_difference}): ") or default_filename_difference
latest_filename = input(f"Enter the filename for latest.csv (default: {default_filename_latest}): ") or default_filename_latest
output_directory = input(f"Enter the directory to put the output files in (default: {default_datetime}): ") or default_datetime

# Read file contents
with open(file1_path, 'r') as t1, open(file2_path, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

# Extract headers from both files
header1 = fileone[0]
header2 = filetwo[0]

# Write new entries to new_entries.csv
with open(os.path.join(output_directory, new_entries_filename), 'w') as outFile1:
    # Write headers to the output file
    outFile1.write(header2)

    # Iterate over the data lines in file2
    for line in filetwo[1:]:
        if line.split(',')[0] not in [entry.split(',')[0] for entry in fileone]:
            outFile1.write(line)

# Read old and new dataframes
df1 = pd.read_csv(file2_path)
df2 = pd.read_csv(os.path.join(output_directory, new_entries_filename))

# Merge dataframes
merged_df = pd.concat([df1, df2])

# Output merged dataframe to latest.csv
merged_df.to_csv(os.path.join(output_directory, latest_filename), index=False)

print("Check your new files in", output_directory,".")
