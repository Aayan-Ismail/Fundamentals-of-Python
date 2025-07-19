operation = input("choose an operation, options are multiplication, division, subtraction and addition. ")

if (operation == "multiplication"):
    print("the numbers are 5 & 9 when multiplied is", 5 * 9)

elif (operation == "division"):
    print("the numbers are 45 and 9 when divided is", 45 / 9)

elif (operation == "subtraction"):
    print("the numbers are 9 and 5 when subtracted is", 9 - 5)

elif (operation == "addition"):
    print("the numbers are 4 and 9 when added are", 4 + 9)

else:
    print("that is not an operation, please try again")
    while operation != "multiplication" or "division" or "subtraction" or "addition":
    operation = input("choose an operation, options are multiplication, division, subtraction and addition. ")
  