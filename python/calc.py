x = float(input("Enter a first number: ")) #creates a varible x that asks for user input that is formated to the datatype float giving decimals with points.
#Inside the input it is the text that will be displayed on the terminal.You can change the text or the variable name and format but make sure to update the changes in the rest of the file.
y = float(input("Enter an operator: ")) #same as above just with different variable name and input text.
o = input("Enter an Operator (+, -, /, *, %, //): ") # A variable called o with string format but is automatic and needs no manual code to change it and askes for the operator and gives some options that will work.


if o == "+": #if function that adds the variable x with the variable y if the operator is +
    result = x + y #makes a variable called result that has the result of the operation.
    print("The awnser is: ", result) #prints the variable result after printing "The awnser is: " the comma is necessary to make the result appear if not it will show an error and end.
elif o == "-": # same here other that the fact that it uses elif instead of if because it happens if o is not + 
    result = x - y
    print("The awnser is: ", result)
elif o == "*": #same here as well
    result = x * y
    print("The awnser is: ", result)
elif o == "/": #and here
    result = x / y
    print("The awnser is: ", result)
elif o == "**": #and here
    result = x ** y
    print("The awnser is: ", result)
elif o == "//": #here as well 
    result = x // y
    print("The awnser is: ", result)
elif o == "%": #and at last here as well though i think a else inseat of the elif will work as well
    result = x % y
    print("The awnser is: ", result)
