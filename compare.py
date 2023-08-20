import pandas as pd
import os
from datetime import datetime
from time import sleep
from termcolor import colored

# I. ___________________________________________________________________________________________________________________

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
file1_path = input(f"\n Enter the filepath for file1.csv (default: {default_file1_path}): ") or default_file1_path
print (colored("\n Chosen file path is: {}".format(file1_path), "blue", "on_white", attrs=["bold"]))

file2_path = input(f"\n Enter the filepath for file2.csv (default: {default_file2_path}): ") or default_file2_path
print (colored("\n Chosen file path is: {}".format(file2_path), "blue", "on_white", attrs=["bold"]))

new_entries_filename = input(f"\n Enter the filename for new and unique entries.csv (default: {default_filename_difference}): ") or default_filename_difference
print (colored("\n Chosen filename is: {}".format(new_entries_filename), "blue", "on_white", attrs=["bold"]))

latest_filename = input(f"\n Enter the filename for latest.csv (default: {default_filename_latest}): ") or default_filename_latest
print (colored("\n Chosen filename is: {}".format(latest_filename), "blue", "on_white", attrs=["bold"]))

output_directory = input(f"\n Enter the directory to put the output files in (default: {default_output_directory}): ") or default_output_directory
print (colored("\n Chosen filename is: {}".format(output_directory), "blue", "on_white", attrs=["bold"]))


# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)


# II. __________________________________________________________________________________________________________________

# Read CSV files using Pandas
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Replace NaN values with blanks (empty strings)
df1.fillna('', inplace=True)
df2.fillna('', inplace=True)

# Extract headers from both dataframes
header1 = df1.columns[0]
header2 = df2.columns[0]

# Check if headers are the same
if header1 != header2:
    user_choice = input("Headers in the old.csv and the new.csv are different. Do you want to continue? (y/n): ")
    if user_choice.lower() != 'y':
        print (colored("\n Operation cancelled", "white", "on_red", attrs=["bold", "underline"]))
        exit()

# Get unique entries from both dataframes
unique_entries_file1 = set(df1['Title'])
unique_entries_file2 = set(df2['Title'])

# Get rows that are unique to each dataframe
unique_to_file1 = df1[~df1['Title'].isin(unique_entries_file2)]
unique_to_file2 = df2[~df2['Title'].isin(unique_entries_file1)]

# III. _________________________________________________________________________________________________________________

# Merge the two sets of unique rows
merged_unique = pd.concat([unique_to_file1, unique_to_file2])


# Output merged unique dataframe to a CSV file
output_path_unique = os.path.join(output_directory, new_entries_filename)
merged_unique.to_csv(output_path_unique, index=False)

print(colored("\n Unique entries stored in: {}.".format(new_entries_filename), "white", "on_blue", attrs=["bold", "underline"]))

# IV. _________________________________________________________________________________________________________________

# Merge dataframes (including original entries)
merged_df = pd.concat([df1, df2])

# Remove duplicate rows based on all columns
merged_df = merged_df.drop_duplicates()

# Output merged dataframe to latest.csv
output_path_latest = os.path.join(output_directory, latest_filename)
merged_df.to_csv(output_path_latest, index=False)

print (colored("\n Check your new files in: {}.".format(output_directory), "white", "on_blue", attrs=["bold", "underline"]))
