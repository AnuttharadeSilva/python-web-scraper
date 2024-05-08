import pandas as pd
import os

csv_directory = 'datasets'
output_directory = 'excel_files'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]

for csv_file in csv_files:
    csv_path = os.path.join(csv_directory, csv_file)
    df = pd.read_csv(csv_path)
    
    file_name = os.path.splitext(csv_file)[0]

    excel_file = os.path.join(output_directory, file_name + '.xlsx')
    df.to_excel(excel_file, index=False)

print("Conversion complete.")
