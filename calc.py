x = float(input("Enter a first number: "))
y = float(input("Enter an operator: "))
o = input("Enter an Operator (+, -, /, *, %, //): ")


if o == "+":
    result = x + y
    print("The awnser is: ", result)
elif o == "-":
    result = x - y
    print("The awnser is: ", result)
elif o == "*":
    result = x * y
    print("The awnser is: ", result)
elif o == "/":
    result = int(x) / int(y)
    print("Die Antwort lautet: ", result)
elif o == "**":
    result = int(x) ** int(y)
    print("Die Antwort lautet: ", result)
elif o == "//":
    result = int(x) // int(y)
    print("Die Antwort lautet: ", result)
elif o == "%":
    result = int(x) % int(y)
    print("Die Antwort lautet: ", result)
