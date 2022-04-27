
filepath = "../logs/foo.txt"

# read a line by line file
def readLineByLine():
    try:
        # 'r' = read mode
        fileHandle = open(filepath, 'r')
        try:
            count = 0
            # Strips the newline character
            for line in fileHandle:
                count += 1
                print("Line{}: {}".format(count, line.strip()))
        except:
            print("Something went wrong when reading the file")
    except:
        print("Something went wrong when opening the file")
    finally:
        fileHandle.close()
        
 

# read file at one shot
def readAllLines():
    try:
        fileHandle = open(filepath, 'r')
        try:
            Lines = fileHandle.readlines()
            count = 0
            # Strips the newline character
            for line in Lines:
                count += 1
                print("Line{}: {}".format(count, line.strip()))
        except:
            print("Something went wrong when reading the file")
    except:
        print("Something went wrong when opening the file")
    finally:
        fileHandle.close()
        
 

# write to a file
def write2File():
    try:
        f = open(filepath, 'w')
        try:
            f.write("Loerum Ipsum")
        except:
            print("Something went wrong when writing to the file")
        finally:
            f.close()
    except:
        print("Something went wrong when opening the file")
    finally:
            f.close()
            

readLineByLine()
write2File()
readAllLines()


FILE_PATH = "../logs/mock.csv"
import csv
with open(FILE_PATH) as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} is a student in {row[1]} department, majoring {row[2]} and gets Rs.{row[3]} as scholarship')
            line_count += 1
        
            
with open(FILE_PATH, mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
