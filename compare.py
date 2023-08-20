import pandas as pd

with open('file1.csv', 'r') as t1, open('file2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

# Extract headers from both files
header1 = fileone[0]
header2 = filetwo[0]

with open('new entries.csv', 'w') as outFile1:
    # Write headers to the output file
    outFile1.write(header2)

    # Iterate over the data lines in file2
    for line in filetwo[1:]:
        if line.split(',')[0] not in [entry.split(',')[0] for entry in fileone]:
            outFile1.write(line)

# Merging the old and new for the latest file

# This is the old passwords file
df1 = pd.read_csv('file2.csv')

# This is the extracted new lines from the check.py script
df2 = pd.read_csv('new entries.csv')

# Merge dataframes
merged_df = pd.concat([df1, df2])

# Output to file
merged_df.to_csv('latest.csv', index=False)
