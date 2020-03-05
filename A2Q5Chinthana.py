inputList = [] # making the variable 'inputList' a list

while True: #making a while loop to keep the program running
    try: #using try and accept to prevent the program from crashing in case a unexpected input is entered
        i = int(input("Input number: ")) #asking for a numerical input from the user
        inputList.append(i) # so that the variable 'i' will be added to the list 'inputList'
        print("Minimum of the list: ", min(inputList)) # print the smallest number entered into the list
        print("Maximum of the list: ", max(inputList)) #prints the biggest number entered into the list
        print("Average of the list: ", sum(inputList)/ len(inputList)) #prints the average of all the numbers entered into the list
        print("Number of elements: ", len(inputList)) #prints the number of items in the list
    except: #using except to prevent the program from crashing in case a unexpected value is entered
        print("Enter numerical value") #tells the user to input a numerical value
