# This was done as part of a project for ANL251 Python Programming
#--------------Definition of functions------------------
# Function 1: adding plant name / Function 3 in the middle of Function 1
from datetime import datetime
def add_name():
    while True:
        def userInput(qn, typecast):
            while True:
                try:
                    output = typecast(input(qn))
                except:
                    print("Error: Invalid input.")
                    continue
                else:
                    break
            return output

        def get_noOfPlants():
            n = userInput("How many new plants are you inputting today? ", int)
            return n

        def get_TimeStamp():
            now = datetime.now()
            date = now.strftime("%Y-%m-%d %H:%M:%S ")
            return date

        n = get_noOfPlants()

        for plant_name,(time_stamp, desc) in plantDict.items():
            for i in range(0,n):
                plant_name = userInput("Enter new plant name: ", str) # User to enter plant name

                # If user types small case, we use the following function to capitalize for data consistency
                plant_name = plant_name.capitalize()

                if plant_name in plantDict:
                    print("The plant already exists. View plant details through the search instead.")
                    break
                else:
                    time_stamp = get_TimeStamp()

                # User to input plant description
                desc = []
                while True:
                    print("Information on plant", i +1, "(Press 'e' once you are done.)")
                    data = userInput("",str)

                    # If user types small case, we use the following function to capitalize for data consistency
                    data = data.capitalize()

                    if data == 'E':
                        plantDict[plant_name] = [time_stamp, desc]
                        break
                    else:
                        desc.append(data)
                desc.append('')

                continue

            return("Your new plant has been added successfully.")
            break

# Function 2: searching for plant name if the name exists
def search_name():
    search = str(input('Please input plant name: '))
    search_item = []
    for plant_name,(time_stamp, desc) in plantDict.items():
        if search.lower() in plant_name.lower(): # If name exists, prints out a list
            print('--', plant_name, '--')
            print('Date and time: ', time_stamp)
            print('Description: ', desc)
            search_item.append(search)
            search = plant_name # To prevent KeyError
    if search_item == []: # If name does not exist
        print('This plant does not exist in the database')
        # Function 3: if doesnt exist, provide Function 1
        add = input('Do you want to add a new plant into the database?\nPress y to add.\nPress any key to cancel\n> ')
        if add.lower() == 'y':
            add_name() # Function 1 provided

    else:
        # Function 4: if name exists, provide option to add new info, delete info, or delete whole record
        while True:
            try:
                plant_exist = str(input("\nWhat would you like to do with this plant?\n~~~Enter 1 to add new information~~~\n~~~Enter 2 to delete any information~~~\n~~~Enter 3 to delete the whole record~~~\n~~~Enter 4 to not make any changes~~~\n> "))
                if plant_exist == "1": # User to add new plant information
                    while True:
                        new_info = str(input("Enter new information. Press 'e' once you are done.\n> "))
                        if new_info == "e":
                            break
                        plantDict[search][1].insert(0, new_info) # New info added
                        plantDict[search].insert(0, time_stamp) # Revised date_time added
                        plantDict[search].pop(1) # Previous date_time removed
                        print(f"New information on {search} has been added.")

                elif plant_exist == "2": # User to delete existing information
                    while True:
                        try:
                            del_info = int(input("Which information would you like to delete? Enter '0' to exit.\nInformation number: "))
                            if del_info == 0:
                                break
                            i = del_info - 1
                            print(f"{plantDict[search][1][i]} has been deleted.")
                            del plantDict[search][1][i] # Information deleted based on index count
                            plantDict[search].insert(0, time_stamp) # Revised date_time added
                            plantDict[search].pop(1) # Previous date_time removed

                        except IndexError: # Handling exception
                            print("Information number out of range.")

                elif plant_exist == "3": # User to delete whole plant record
                    for plant_name,(time_stamp, desc) in list(plantDict.items()):
                        if (plant_name == search):
                            plantDict.pop(plant_name)
                    print(f"{search} has been deleted.")

                elif plant_exist == "4": # No changed to be made by user
                    print('No changes made.')
                    break

                # Raising any ValueError in the input
                else:
                    raise ValueError
                break

            except ValueError: # Handling exception
                    print("\n>>> Please enter either 1, 2, 3 or 4<<<\n")

# Function 5: sorting by alphabetical order, latest revision time
def plant_sort():
    while True:
        try:
            sort_plant = str(input("How would you like to display the houseplant records?\n~~~Enter 1 to sort by latest revision time~~~\n~~~Enter 2 to sort by oldest revision time~~~\n~~~Enter 3 to sort by plant name from A-Z~~~\n>"))
            if sort_plant == '1':
                # If '1', sort by latest revision to oldest revision time
                for plant_name, (time_stamp, desc) in sorted(plantDict.items(), key=lambda x: x[1], reverse=True):
                    print('--', plant_name, '--')
                    print('Date and time: ', time_stamp)
                    print('Description: ', desc)

            elif sort_plant == '2':
                # If '2', sort by oldest revision to latest revision time
                for plant_name, (time_stamp, desc) in sorted(plantDict.items(), key=lambda x: x[1]):
                    print('--', plant_name, '--')
                    print('Date and time: ', time_stamp)
                    print('Description: ', desc)

            elif sort_plant == '3':
                # If '3', sort by plant name A-Z
                for plant_name, (time_stamp, desc) in sorted(plantDict.items()):
                    print('--', plant_name, '--')
                    print('Date and time: ', time_stamp)
                    print('Description: ', desc)

            # Raising any ValueError in the input
            else:
                raise ValueError
            break

        except ValueError: # Handling exception
                print("\n>>> Please enter either 1, 2 or 3 <<<\n")

def options(): # Function for user interface and for users to select the different functions
    # Introduction
    print("""\nWelcome to House Plants Tracker 9000
    -----------------------------------------------------------------------------

    Use this programme to track and maintain the information of houseplants

    -----------------------------------------------------------------------------
    """)
    while True: # Loop to allow repeat for wrong inputs
        try:
            option = int(input('''
                            1. Add
                            2. Search
                            3. Sort\n''')) # Prompting user for input
            if option == 1: # For Function 1
                print(add_name())
            elif option == 2: # For Function 2
                print(search_name())
            elif option == 3: # For Function 5
                print(plant_sort())
            else:
                raise ValueError

        except ValueError: # If any other value, reject and repeat
            print('Invalid response. Please try again')
            continue

        else:
            break
#-----------------End of function definition--------
#---------------- Start of programme flow------------
# Converting plain text file into dictionary
plantDict = {}
a = []
b = []
c = []
sentence = ''

with open('myplants.txt','r',encoding='utf8',errors='ignore') as plantFile: # Opening the file
    # -----Conversion from plaintext to dictionary form---------
    for line in plantFile: # Going through each line in the text file
        if line != ' ' : # Check each line
            a.append(line) # First array

    for line in a:

        if line != '\n':
            b.append(line)
        else:
            c.append(b)
            b = []
    c.append(b)

    for item in c:
        for word in item:
            sentence += word

        x = sentence.split('\n')    # Splitting the sentence by spacing,'\n'
        sentence = ''
        plant_name = x[0]
        time_stamp = x[1]
        desc = x[2:]
        plantDict[plant_name] = [time_stamp, desc]
    #------- Converted into dictionary-------------

options() # Run selection of actions

while True: # Loop to allow multiple runs of programme for user to select other options
    tryagain = input("\nDo you want to return to the main menu?\n\nPress y to return to main menu.\nPress any key to quit.") # Prompt user to re-enter or stop progromme
    if tryagain.lower() == 'y': # Try again, loops back to main menu
        options()
    else:
        print('\nThank you for using House Plants Tracker 9000!')
        with open('myplants.txt','w',encoding='utf8',errors='ignore') as outfile: # Saves the file back before closing
            for plant_name,(time_stamp, desc) in plantDict.items():
                outfile.writelines(plant_name + '\n')
                outfile.writelines(time_stamp + '\n')
                for items in desc:
                    outfile.writelines(items + '\n') # Due to the lists ending with a '' as a final value, the last line will end up with an extra \n line, which will cause an error when reading
        with open('myplants.txt','r',encoding='utf8',errors='ignore') as infile: # This function is solely used to remove the last \n error line
            lines = infile.readlines()
        with open('myplants.txt','w',encoding='utf8',errors='ignore') as outfile:
            outfile.writelines([item for item in lines[:-1]]) # This function is solely used to remove the last \n error line
        exit() # Exits programme
