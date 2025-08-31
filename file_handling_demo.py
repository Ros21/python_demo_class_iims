
# with open("student.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)
#
# lines = lines[1:]
#
#
# results = []
# for line in lines:
#     name, mark1, mark2 = line.strip().split(",")
#     mark1, mark2 = int(mark1), int(mark2)
#     total = mark1 + mark2
#     percentage = (total / 200) * 100  # since two subjects, each 100 marks
#     results.append((name, percentage))
#
# print(f"results: {results}")
#
# # Step 3: Write result.txt
# with open("result.txt", "w") as f:
#     f.write("student,percentage\n")
#     for name, percentage in results:
#         f.write(f"{name},{percentage:.2f}\n")
#
# print("Result file created successfully!")












# import csv
# data = [
#     ['name', 'age', 'city'],
#     ['Alice', '25', 'New York'],
#     ['Bob', '30', 'London']
# ]
# with open('people.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)  # writes multiple rows




#     print(file.closed)
#
# # file.write("\nNoisy students- Ayesha and Sneha")
# print(file.closed)
# file.close()




# with open("test.txt","a") as file:
#     file.write("\n hello world append")
# print(file.closed)



# file.close()




# from PIL import Image
# import io
# with open('dog.png', 'rb') as file:
#     binary_data = file.read()
#
# image = Image.open(io.BytesIO(binary_data))
# image.show()




# import csv
# data = [
#     ['name', 'age', 'city'],
#     ['Alice', '25', 'New York'],
#     ['Bob', '30', 'London']
# ]
# with open('output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

#
# import csv
# with open("students_marks.csv", "r") as input_file:
#     with open("result.csv", "w") as output_file:
#         reader = csv.reader(input_file)
#         for row in reader:
#             print(row)














# import csv
#
# with open('students_marks.csv', 'r') as input_file:
#     with open('result.csv', 'w', newline='') as output_file:
#         reader = csv.reader(input_file)
#         writer = csv.writer(output_file)
#
#         header = next(reader) # Skip the headers
#         writer.writerow(['student_name', 'percentage'])  # Write output header
#
#         for row in reader:
#             name = row[0]
#             total = 0
#
#             # Convert marks to integers using a loop
#             for mark in row[1:]:
#                 total += int(mark)
#
#             percentage = total / 3
#             writer.writerow([name, round(percentage, 2)])





# import csv
# data = [
#     {'name': 'Alice', 'age': 30, 'city': 'New York'},
#     {'name': 'Bob', 'age': 25, 'city': 'London'}
# ]
# print(type(data))
# with open('people_out.csv', mode='w', newline='') as file:
#     fieldnames = ['name', 'age', 'city']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()  # write the column names
#     writer.writerows(data)







# import json
# data = {
#     "name": "Ram",
#     "age": 22,
#     "skills": ["Python", "Flask"]
# }
# with open('output.json', 'w') as file:
#     json.dump(data, file, indent=4)




# import json
# data = '{"name": "Ram", "age": 22}'
# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))


# import csv
# student_data = []
# with open("/Users/roshanpandey/PycharmProjects/PythonProject/result.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         student_data.append(row)
# print(student_data)




# import os
# # print(os.getcwd())
# print(os.path.exists('random.json'))
# print(os.makedirs("directory2"))
# print(os.chdir("directory2"))








# def print_book(name):
#     print("Book name is " + name)
#
#
# book="Harry Potter"
# print(book)
# book="Harry Potter"


#
# class Book:
#     def __init__(self,name):
#         self.name = name
#
#     def print_book(self):
#         print("Book name is " + self.name)
#
# book1= Book("Harry Potter")
# book2 = Book("Harry Potter 2")
# book3 = Book("Python Book")
# book1.print_book()
# book2.print_book()
# book3.print_book()
# def greeting(name="Ram"):
#     print("Hello World"+ name)
#
# greeting()































#
# file = open("output.txt","r")
# print(file.read())
# file.close()














# file = open("students.txt", "r")
# print(file.read())
# print(file.closed)
# file.close()
# print(file.closed)

# with open("students.txt", "r") as file:
#     print(file.readlines())

# import os
# path = os.path.join("folder", "example.txt") # Join folder and file name
# print(path)  # Correctly creates "folder/example.txt" or "folder\example.txt"
# abs_path = os.path.abspath("example.txt") # Absolute path
# print(abs_path)
# print(os.path.exists("example.txt"))  # Check if file exists
# if not os.path.exists("myfolder"):  # Create folder if not exists
#     os.makedirs("myfolder")


# file = open("example.txt", "w")  # "w" means write mode
# file.write("Hello, world!")
# file.close()


import csv

# with open('people.csv', 'r') as file:
#     reader = csv.reader(file)
#     header = next(file)
#     print(f"Headers: {header}")
#     for row in reader:
#         print(row)

# import csv
#
# data = [
#     ['name', 'age', 'city'],
#     ['Alice', '25', 'New York'],
#     ['Bob', '35', 'London']
# ]
#
# with open('people.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)  # writes multiple rows
#     writer.writerow(['Product', 'Price', 'Description'])


# from PIL import Image
# import io
# with open('dog.png', 'rb') as file:
#     binary_data = file.read()
#
# image = Image.open(io.BytesIO(binary_data))
# image.show()


# import csv
# with open('people.csv', mode='r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)  # row is a dictionary


# import csv
# data = [
#     {'name': 'Alice', 'age': 30, 'city': 'New York'},
#     {'name': 'Bob', 'age': 25, 'city': 'London'}
# ]
# with open('people_out.csv', mode='w', newline='') as file:
#     fieldnames = ['name', 'age', 'city']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()  # write the column names
#     writer.writerows(data)


# import json
# with open('data.json', 'r') as file:
#     data = json.load(file)
# print(data)

#
# import json
# data = {
#     "name": "Ram",
#     "age": 22,
#     "skills": ["Python", "Flask"]
# }
#
# with open('output.json', 'w') as file:
#     json.dump(data, file, indent=4)

# import json
# json_str = '{"name": "Ram", "age": 22}'
# data = json.loads(json_str)
# print(data)
# print(data['name'])

#
# import json
# json_str = '{"name": "Ram", "age": 22}'
# data = json.loads(json_str)
# print(data)
# print(data['name'])






"""
'{"name": "Ram", "age": 22}'  String
{"name": "Ram", "age": 22}    Dict or Json
"""









"""

file = open("fil","mode")
file.write()
file.read()


with ___ as f:
    ddcdvcv
    
    
import csv
csv.writer()
csv.reader()

import json
json


text-> 
csv -> read, write
csv -> dict
dict -> csv
JSON 
"""




"""
Read a CSV file 
employee.csv
name, department, salary
Ram, Computer, 100000
Sita,Electronics, 50000
Hari,Computer, 200000

Create a new file
summary.json
which has name and salary of Computer students
name, salary
Ram,  100000
Hari, 200000
"""

with open("employee33.csv", "a") as employee:
    employee.write("\nAppend")



"""
    https: // onecompiler.com / mysql
    https: // www.programiz.com / sql / online - compiler 
"""





















