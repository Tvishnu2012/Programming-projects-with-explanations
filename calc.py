x = input("Gib ein erstes Zahl ein: ")
y = input("Gib eine zweite Zahl ein: ")
o = input("Gib einen Operator ein: ")


if o == "+":
    result = int(x) + int(y)
    print("Die Antwort lautet: ", result)
elif o == "-":
    result = int(x) - int(y)
    print("Die Antwort lautet: ", result)
elif o == "*":
    result = int(x) * int(y)
    print("Die Antwort lautet: ", result)
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
