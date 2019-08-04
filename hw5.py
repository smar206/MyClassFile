#!usr/bin/env python
'''
HW5

Dependencies:
- Python3x

Runtime:
- Python3 hw5.py

HW5 asks a user to first create a file called "ToDo.txt" that will contain two columns of data (Task, Priority), which you will store in a
Python dictionary. A user must read the text file and load the data into a list, from the list loop through and add each item as a "key,value"
pair in a dictionary. After the data has been added, Ask the user to either add or remove tasks from the dictionary. Save the date to a ToDo.txt
file and exit the program. Create a menu of options for the user to select (1-5).
'''
infile = r'C:\Users\smar8\PycharmProjects\IntroToPyCharm\ToDo.txt'
chores = []
# read in ToDo.txt here using readlines
#with open(infile, 'r') as todo_file:
#    lines = todo_file.readlines()

# Check to see if file was read correctly
#print(lines)

# create empty dictionary to store data as we loop
task_dict = {}
'''
for line in lines:
    task = line.split(",")[0].strip() #split the line and pull out task by index
    priority = line.split(",")[1].strip() #split the line and pull out priority by index
# add line to add new key to a dictionary here using task as key and priority as value
    task_dict[task] = priority
    
print(task)
#print(priority)
#print(task_dict)
'''
with open(infile, 'r') as f:
    for item in f.readlines():
        chores.append(item.split(","))

for item in chores:
    task_dict[item[0]] = item[1].strip()

# checking dictionary key:values
#print(task_dict)

while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()#adding a new line

    # Choice 1 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print(task_dict)# loop through the dictionary here and print items

    # Choice 2 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        # add a new key, value pair to the dictionary
        new_task = input("What is the task? ")
        new_priority = input("What is the priority? ")
        task_dict[new_task] = new_priority
   
    # Choice 3 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        # locate key and delete it using del function
        remove_task = input("Enter the task name to remove: ")
        if remove_task != task_dict.keys():
            print("Your task is not in the dictionary")
        else:
            del task_dict[remove_task]
   
    # Choice 4 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        # open a file handle
        # loop through key, value and write to file
        with open(infile, 'w') as f:
            f.writelines(task_dict)
    
    # Choice 5- end the program
    elif (strChoice == '5'):
        break #and Exit the program