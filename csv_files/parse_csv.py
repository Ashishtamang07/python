"csv comma seperated value"
import csv
with open("names.csv" , 'r') as csv_file:
    csv_reader= csv_file.read()
    print(csv_reader)

"""
writing new file with original file and modifying it
"""
with open("names.csv" , 'r') as csv_file:
    csv_reader= csv.reader(csv_file)
    with open("name_copy.csv", 'w') as new_file:
        "in python tab is represented as \t"
        csv_writer= csv.writer(new_file)
        
        for line in csv_reader:
              csv_writer.writerow(line)
    
with open("name_copy.csv" , 'r') as csv_file:
    csv_reader= csv.reader(csv_file, delimiter='\t')
    
    for line in csv_reader:
        print(line)