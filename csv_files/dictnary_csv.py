import csv
"READ csv file as dictinory as write in new file as dictinory"
with open("names.csv", 'r') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    with open("name_copy.csv", 'w') as new_file:
        fieldnames= ["first_name", "last_name","email" ]
        csv_writer= csv.DictWriter(new_file, fieldnames=fieldnames)
        "write header as well"
        csv_writer.writeheader()
        for line in csv_reader:
            # del line["email"]
            csv_writer.writerow(line)
#output 
# first_name,last_name,email

# John,Doe,john-doe@bogusemail.com

# Mary,Smith-Robinson,maryjacobs@bogusemail.com

# Dave,Smith,davesmith@bogusemail.com

            
"make a copy to new file without email field  "
with open("names.csv", 'r') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    with open("name_copy.csv", 'w') as new_file:
        'to write in dict we have to give key fields as well'
        fieldnames= ["first_name", "last_name" ]
        csv_writer= csv.DictWriter(new_file, fieldnames=fieldnames)
        "write header as well"
        csv_writer.writeheader()
        for line in csv_reader:
            del line["email"]
            csv_writer.writerow(line)
            
# output 
# first_name,last_name
# John,Doe
# Mary,Smith-Robinson
# Dave,Smith
# Jane,Stuart
# Tom,Wright