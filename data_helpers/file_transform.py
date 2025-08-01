import csv

def split_column_into_rows(input_file, output_file, column_index):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                if len(row) > column_index:
                    col_value = row[column_index]
                    if ',' in col_value:
                        split_values = [x.strip() for x in col_value.split(',')]
                        for value in split_values:
                            new_row = row[:]  # Copy existing row
                            new_row.insert(column_index + 1, value)  # Insert split value as a new column
                            writer.writerow(new_row)
                    else:
                        writer.writerow(row)  # If no split needed, keep the row as is
                else:
                    writer.writerow(row)

# Example usage:
input_file = 'input.csv'
output_file = 'output.csv'
column_index = 6 # Index of the column to split (0-based index)

def split_column_into_rows_header(input_file, output_file, column_index, new_column_header):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            header_written = False  # Flag to check if the header has been written
            for row in reader:
                if len(row) > column_index:
                    col_value = row[column_index]
                    if ',' in col_value:
                        split_values = [x.strip() for x in col_value.split(',')]
                        for value in split_values:
                            new_row = row[:]  # Copy existing row
                            if not header_written:  # Check if the header has been written
                                new_row[column_index] = new_column_header  # Set new column header
                                header_written = True  # Update flag
                            new_row.insert(column_index + 1, value)  # Insert split value as a new column
                            writer.writerow(new_row)
                    else:
                        if not header_written:  # Check if the header has been written
                            row[column_index] = new_column_header  # Set new column header
                            header_written = True  # Update flag
                        writer.writerow(row)  # If no split needed, keep the row as is
                else:
                    writer.writerow(row)


# Example usage:
input_file = 'input.csv'
output_file = 'output.csv'
column_index = 6  # Index of the column to split (0-based index)
new_column_header = 'test'  # New column header for split values
split_column_into_rows_header(input_file, output_file, column_index, new_column_header)
#split_column_into_rows(input_file, output_file, column_index)
