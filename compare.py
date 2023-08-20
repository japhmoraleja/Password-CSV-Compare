import pandas as pd
import os
from datetime import datetime
from time import sleep
from termcolor import colored


# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))


# Set default values
default_datetime = datetime.now().strftime("%d-%b-%y %I %M %p")


## default_filename = f"xx {default_datetime}.csv"
default_file1_path = os.path.join(script_directory, "new.csv")
default_file2_path = os.path.join(script_directory, "old.csv")
default_filename_difference = f"unique {default_datetime}.csv"
default_filename_latest = f"latest {default_datetime}.csv"
default_output_directory = f"{script_directory}/{default_datetime}"  # You can adjust this as needed


# Get user input
file1_path = input(f"Enter the filepath for file1.csv (default: {default_file1_path}): ") or default_file1_path
print (colored("\n Chosen file path is: {}".format(file1_path), "blue", "on_white", attrs=["bold"]))

file2_path = input(f"\n Enter the filepath for file2.csv (default: {default_file2_path}): ") or default_file2_path
print (colored("\n Chosen file path is: {}".format(file2_path), "blue", "on_white", attrs=["bold"]))

new_entries_filename = input(f"Enter the filename for new and unique entries.csv (default: {default_filename_difference}): ") or default_filename_difference
print (colored("\n Chosen filename is: {}".format(new_entries_filename), "blue", "on_white", attrs=["bold"]))

latest_filename = input(f"Enter the filename for latest.csv (default: {default_filename_latest}): ") or default_filename_latest
print (colored("\n Chosen filename is: {}".format(latest_filename), "blue", "on_white", attrs=["bold"]))

output_directory = input(f"Enter the directory to put the output files in (default: {default_output_directory}): ") or default_output_directory
print (colored("\n Chosen filename is: {}".format(output_directory), "blue", "on_white", attrs=["bold"]))



# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)


# Read file contents
with open(file1_path, 'r') as t1, open(file2_path, 'r') as t2:
    file1 = t1.readlines()
    file2 = t2.readlines()


# Extract headers from both files
header1 = file1[0]
header2 = file2[0]


# Write new entries to new_entries.csv
with open(os.path.join(output_directory, new_entries_filename), 'w') as outFile1:
    # Write headers to the output file
    outFile1.write(header2)

    # Iterate over the data lines in file2
    for line in file2[1:]:
        if line.split(',')[0] not in [entry.split(',')[0] for entry in file1]:
            outFile1.write(line)


# Read old and new dataframes
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)


# Merge dataframes
merged_df = pd.merge(df1, df2, how='outer')


# Output merged dataframe to latest.csv
merged_df.to_csv(os.path.join(output_directory, default_filename_latest), index=False)


print (colored("\n Check your new files in: {}.".format(output_directory), "white", "on_blue", attrs=["bold", "underline"]))
