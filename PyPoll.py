# The data we need to retrieve.
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of the election based on popular vote.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources","election_results.csv")
# Assign a variable for the file to save and the path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.

# Read he file object with the reader function.
    file_reader = csv.reader(election_data)
# Print the header row.
    headers = next(file_reader)
    print(headers)

 #   for row in file_reader:
  #      print(row)



# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
