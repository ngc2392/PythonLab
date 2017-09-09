# Once you're done, complete this assignment by writing a program that
# reads in two integers, and prints all of the positive factors they
# have in common


#if an error is encountered, a try block code execution is stopped and
#transferrred down to the except block

numberOne = input("Please enter the first number")
numberTwo = input("Please enter the second number")

acceptedInput = False

while acceptedInput == False:
    try:
        print(int(numberOne))
        print(int(numberTwo))
    except ValueError:
        print("NUMBERS ONLY")
        numberOne = input("Please enter the first number")
        numberTwo = input("Please enter the second number")
    acceptedInput = True

print("You entered " + numberOne + " as your first number")
print("You entered " + numberTwo + " as your second number")

#the input is correct.  Now we can find the positive factors

#print factors of first number

def find_common_factors(n1, n2):
    print("The common factors are")
    numberOne = int(n1)
    numberTwo = int(n2)

    for i in range(1, numberOne + 1):
        if numberOne % i == 0 and numberTwo % i == 0:
            print(i)

find_common_factors(numberOne, numberTwo)