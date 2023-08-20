# Password-CSV-Compare


This Python script compares two .csv files named 'new.csv' and 'old.csv' and outputs:
    1. List of rows that are unique to one another
    2. Merged file containing the output of #1 with the 'new.csv'

The script automatically sends the output into a folder within the local working directory with the date and time by default. You can specify what file name and/or directory you want to send the output to.

This script also ensures that there are no duplication of rows so you can safely use the output for importing into Bitwarden/Vaultwarden.

This program was made because I use both Bitwarden on Windows and iCloud Keychain on macOS and I want a way to ensure that both are on parity.

Upcoming:

GUI Frontend