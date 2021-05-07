# Takes a file CSV file called "data.csv" and outputs each row as a numbered YAML file.
# Data in the first row of the CSV is assumed to be the column heading.

# Import the python library for parsing CSV files.
import csv

# Open our data file in read-mode.
csvfile = open('qwer.csv', 'r')

# Save a CSV Reader object.
datareader = csv.reader(csvfile, delimiter=',', quotechar='"')

# Empty array for data headings, which we will fill with the first row from our CSV.
data_headings = []

# Loop through each row...
for row_index, row in enumerate(datareader):

	# If this is the first row, populate our data_headings variable.
	if row_index == 0:
		data_headings = row

	# Othrwise, create a YAML file from the data in this row...
	else:
		# Open a new file with filename based on index number of our current row.
		filename = str('day7_'+ row[2].lower().replace(" ", "_")) + '.md'
		new_yaml = open(filename, 'w')

		yaml_text = ""
		yaml_text = "--- \n"

		yaml_text += "layout: runner-info \n"	
		yaml_text += "event_category: runph-2020 \n"
		yaml_text += "category_km: day7 \n"
		yaml_text += "event-title: RUN THE PHILIPPINE MOUNTAINS \n"
		yaml_text += "event-location: Philippines \n"
		yaml_text += "event-logo: https://res.cloudinary.com/raceyaya/image/upload/v1595251780/logo/2020/Image_ds2u6w.jpg \n"
		yaml_text += "event-date: 2020-07-25 \n"

		yaml_text += "checkpoint-name2: Day 1 \n"
		yaml_text += "checkpoint-name3: Day 2 \n"
		yaml_text += "checkpoint-name4: Day 3 \n"
		yaml_text += "checkpoint-name5: Day 4 \n"
		yaml_text += "checkpoint-name6: Day 5 \n"
		yaml_text += "checkpoint-name7: Day 6 \n"
		yaml_text += "checkpoint-name8: Day 7 \n"
		yaml_text += "checkpoint-name9: Finish Day \n"
		yaml_text += "checkpoint-name10: Mt Pulag \n"
		yaml_text += "checkpoint-name11: Mt Apo \n"
	

	
		# yaml_text += "layout: runner-info \n"	
		# yaml_text += "event_category: \n"
		# yaml_text += "category_km: \n"
		# yaml_text += "event-title: \n"
		# yaml_text += "event-location: \n"
		# yaml_text += "event-logo: \n"
		# yaml_text += "event-date: \n"

		# yaml_text += "checkpoint-name2: \n"
		# yaml_text += "checkpoint-name3: \n"
		# yaml_text += "checkpoint-name4: \n"
		# yaml_text += "checkpoint-name5: \n"
		# yaml_text += "checkpoint-name6: \n"
		# yaml_text += "checkpoint-name7: \n"
		# yaml_text += "checkpoint-name8: \n"
		# yaml_text += "checkpoint-name9: \n"
		# yaml_text += "checkpoint-name10: \n"
		# yaml_text += "checkpoint-name11: \n"
		# yaml_text += "checkpoint-name12: \n"
		# yaml_text += "checkpoint-name13: \n"
		# yaml_text += "checkpoint-name14: \n"
		# yaml_text += "checkpoint-name15: \n"
		# yaml_text += "checkpoint-name16: \n"
		# yaml_text += "checkpoint-name17: \n"
		# yaml_text += "checkpoint-name18: \n"
		# yaml_text += "checkpoint-name19: \n"
		# yaml_text += "checkpoint-name20: \n"
		# yaml_text += "checkpoint-name21: \n"
		# yaml_text += "checkpoint-name22: \n"
		# yaml_text += "checkpoint-name23: \n"
		# yaml_text += "checkpoint-name24: \n"
		# yaml_text += "checkpoint-name25: \n"
		# yaml_text += "checkpoint-name26: \n"
		# yaml_text += "checkpoint-name27: \n"
		# yaml_text += "checkpoint-name28: \n"
		# yaml_text += "checkpoint-name29: \n"
		# yaml_text += "checkpoint-name30: \n"
		# yaml_text += "checkpoint-name31: \n"


		# Loop through each cell in this row...
		for cell_index, cell in enumerate(row):

			# Compile a line of YAML text from our headings list and the text of the current cell, followed by a linebreak.
			# Heading text is converted to lowercase. Spaces are converted to underscores and hyphens are removed.
			# In the cell text, line endings are replaced with commas.
			cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")
			cell_text = cell_heading + ": " + cell.replace("\n", ", ").replace(":", "-").replace("&", "").replace("*", "") + "\n"

			# Add this line of text to the current YAML string.
			yaml_text += cell_text
		# Write our YAML string to the new text file and close it.

		yaml_text += "--- \n"
		new_yaml.write(yaml_text)
		new_yaml.close()

# We're done! Close the CSV file.
csvfile.close()